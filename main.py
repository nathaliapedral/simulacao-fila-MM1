from event import Event
from customer import Customer
from statistics import Statistics
from utils import Utils
import numpy as np
import scipy.stats as stats
from math import sqrt
import sys

np.random.seed(42) #Semente inicial

#Variaveis globais
events_list = []
customers_list = []
wait_queue = []
n_rounds = 3200
statistics = []
k_samples = 1
estimated_mean = 0
estimated_variance = 0
estimated_covariance = 0

#Passando a disciplina e rho por argumentos
discipline = sys.argv[1] if len(sys.argv) > 1 else 'FCFS'
rho = sys.argv[2] if len(sys.argv) > 2 else '0.9' 


#Definindo a primeira chegada no sistema
first_customer = Customer(0, 0, 0)
customers_list.append(first_customer)

first_arrival = Event('CH', 0, 0)
events_list.append(first_arrival)

print ''
print 'Rho utilizado:', rho
print 'Disciplina de atendimento:', discipline
print ''

#Loop responsavel por rodar a fase transiente
for current_round in xrange(0, n_rounds):
	statistics.append(Statistics())
	while statistics[current_round].sample_index < k_samples:
		current_event = events_list.pop(0)
		if (current_event.event_type == "CH"):		
			current_event.queue_arrival(customers_list, events_list, wait_queue, current_round)
		elif (current_event.event_type == "ES"):
			current_event.service_entry(customers_list, events_list, wait_queue)
		elif (current_event.event_type == "SS"):
			current_event.service_exit(customers_list, events_list, wait_queue, statistics, current_round)
	statistics[current_round].mean_calculator()
	
	estimated_mean_acumulator = 0
	for x in statistics:
		estimated_mean_acumulator += x.mean_queue_wait
	estimated_mean = estimated_mean_acumulator / len(statistics)

	if len(statistics) > 1:
		estimated_variance_acumulator = 0
		for x in statistics:
			estimated_variance_acumulator += (x.mean_queue_wait - estimated_mean)**2
		estimated_variance = estimated_variance_acumulator / (len(statistics) - 1)

	if len(statistics) > 2:
		estimated_covariance_acumulator = 0
		for x in xrange(0, len(statistics)-1):
			estimated_covariance_acumulator += (statistics[x].mean_queue_wait - estimated_mean) * (statistics[x+1].mean_queue_wait - estimated_mean)
		estimated_covariance = estimated_variance_acumulator / (len(statistics) - 2)
		if ((estimated_covariance / estimated_variance)-1 <= 0.1):
			break
		k_samples = k_samples * 2

#Loop responsavel por rodar a simulacao
statistics = []
k_samples = 100
for current_round in xrange(0, n_rounds):
	statistics.append(Statistics())
	while statistics[current_round].sample_index < k_samples:
		current_event = events_list.pop(0)
		if (current_event.event_type == "CH"):		
			current_event.queue_arrival(customers_list, events_list, wait_queue, current_round)
		elif (current_event.event_type == "ES"):
			current_event.service_entry(customers_list, events_list, wait_queue)
		elif (current_event.event_type == "SS"):
			current_event.service_exit(customers_list, events_list, wait_queue, statistics, current_round)
	statistics[current_round].mean_calculator()
	statistics[current_round].nq_calculator()
	
#============================Calculo da média, variancia e IC de Nq==================================
estimated_nq_acumulator = 0
for x in statistics:
	estimated_nq_acumulator += x.mean_nq

estimated_nq_real = estimated_nq_acumulator / n_rounds		

print 'Nq medio:', estimated_nq_real

estimated_variance_nq_acumulator = 0
for x in statistics:
	estimated_variance_nq_acumulator += (x.mean_nq - estimated_nq_real)**2

estimated_variance_nq = estimated_variance_nq_acumulator / (n_rounds - 1) 
print 'Variancia Nq:',estimated_variance_nq

inf_nq, sup_nq, precision_nq = Utils.mean_queue_wait_confidence_interval(sqrt(estimated_variance_nq), estimated_nq_real, n_rounds)

print 'IC media nq:', inf_nq, sup_nq
print 'precisao media nq:', precision_nq


inf_var_nq, sup_var_nq, precision_var_nq = Utils.variance_queue_wait_confidence_interval(estimated_variance_nq, n_rounds, 1)

print 'IC Variancia nq:', inf_var_nq, sup_var_nq
print 'precisao variancia nq:', precision_var_nq

#===================================================================================================


#============================Calculo da média, variancia e IC de W==================================
estimated_mean_acumulator = 0
for x in statistics:
	estimated_mean_acumulator += x.mean_queue_wait

estimated_mean_real = estimated_mean_acumulator / n_rounds
print 'Media W:',estimated_mean_real


estimated_variance_w_acumulator = 0
for x in statistics:
	estimated_variance_w_acumulator += (x.mean_queue_wait - estimated_mean_real)**2

estimated_variance_w = estimated_variance_w_acumulator / (n_rounds - 1) 
print 'Variancia W:',estimated_variance_w

inf_w, sup_w, precision_w = Utils.mean_queue_wait_confidence_interval(sqrt(estimated_variance_w), estimated_mean_real, n_rounds)
print 'IC da media de W: ',inf_w, sup_w, precision_w
print 'precisao IC da media de W:', precision_w

inf_var_w, sup_var_w, precision_var_w = Utils.variance_queue_wait_confidence_interval(estimated_variance_w, n_rounds, 1)
print 'IC da variancia de W: ',inf_var_w, sup_var_w, precision_var_w
print 'precisao IC da media de W:', precision_var_w

#====================================================================================================

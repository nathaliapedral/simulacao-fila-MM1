from event import Event
from customer import Customer
from statistics import Statistics
from utils import Utils
import numpy as np
import scipy.stats as stats
from math import sqrt
import sys

np.random.seed(42)
events_list = []
customers_list = []
wait_queue = []
n_rounds = 3200
n = 1
statistics = []
k_samples = 1
estimated_mean = 0
estimated_variance = 0
estimated_covariance = 0


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

print 'IC nq:', inf_nq, sup_nq
print 'precisao nq:', precision_nq


'''sum = 0
for x in statistics[0].samples_queue_time:
	sum += (x - statistics[0].mean_queue_wait)**2

estimated_mean_real = statistics[0].mean_queue_wait
estimated_variance = sum / (k_samples - 1)
'''
estimated_mean_acumulator = 0
for x in statistics:
	estimated_mean_acumulator += x.mean_queue_wait

estimated_mean_real = estimated_mean_acumulator / n_rounds
print 'Media W:',estimated_mean_real
print 'rho:',estimated_nq_real / estimated_mean_real

inf_var_nq, sup_var_nq, precision_var_nq = Utils.variance_queue_wait_confidence_interval(estimated_variance_nq, n_rounds, 1)

print 'IC Variancia nq:', inf_var_nq, sup_var_nq
print 'precisao variancia nq:', precision_var_nq

'''
for x in statistics:
	estimated_variance_acumulator += (x.mean_queue_wait - estimated_mean_real)**2

estimated_variance = estimated_variance_acumulator / (n_rounds - 1) 



print 'media da FCFS', estimated_mean_real
print 'variancia da FCFS', estimated_variance_real
'''
'''
standard_deviation = sqrt(estimated_variance_real)

mean_infe_limit, mean_sup_limit, t_precision = Utils.mean_queue_wait_confidence_interval(standard_deviation, estimated_mean_real, n_rounds)
infe_limit, sup_limit, chi_precision = Utils.variance_queue_wait_confidence_interval(estimated_variance_real, n_rounds, k_samples)

tam_ic_mean = (2*1.96*standard_deviation) / sqrt(n_rounds)

#print 'desvio padrao', standard_deviation
print 'media estimada do tempo de espera na fila',  estimated_mean_real
print 'IC da media da  t-student: ',mean_infe_limit, mean_sup_limit 
print 'Precisao da media usando t-student: ', t_precision
print 'Tamanho do IC usando os limites', mean_sup_limit - mean_infe_limit
print 'Tamanho do IC da media', tam_ic_mean
print '10 per cent da media', estimated_mean_real * 0.1
print '============='
print 'variancia estimada do tempo de espera na fila',  k_samples * estimated_variance_real
print 'IC da variancia bolado: ', infe_limit, sup_limit   
print 'Precisao da variancia usando chi: ', chi_precision 
print 'Tamanho do IC usando os limites', sup_limit - infe_limit
#print 'Tamanho do IC da variancia', tam_ic_mean
print '10 per cent da media', estimated_variance_real * 0.1
'''
#for x in events_list:
	#print x.time, x.event_type, x.customer_index
#print ''
#print '=================================================================='
#print ''

#for x in customers_list:
#	print 'Customer ',customers_list.index(x),':'
#	print 'Chegou no tempo ', x.arrival_time,'s'
#	print 'Entrou em servico no tempo ' , x.entry_server_time,'s'
#	print 'Saiu de servico no tempo ', x.exit_server_time,'s'
#	print 'Tempo em servico: ', x.exit_server_time - x.entry_server_time,'s'
#	print 'Tempo na fila de espera: ', x.entry_server_time - x.arrival_time,'s'
#	print 'Tempo total no sistema: ',x.exit_server_time - x.arrival_time,'s'
#	print '-------------\\-------------\\-------------\\-------------\\-----'

#mean_service_time = Statistics()

#print 'Teste tempo medio de servico: ', mean_service_time.mean_service_time(customers_list)
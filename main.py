from event import Event
from customer import Customer
from statistics import Statistics
from utils import Utils
import numpy as np
import scipy.stats as stats
from math import sqrt

#Variaveis globais
np.random.seed(777)
events_list = []
customers_list = []
wait_queue = []
n_rounds = 1
n = 1
statistics = []
k_samples = 10000
estimated_mean = 0
estimated_variance = 0

#Definindo a primeira chegada no sistema
first_customer = Customer(0, 0, 0)
customers_list.append(first_customer)

first_arrival = Event('CH', 0, 0)
events_list.append(first_arrival)


#Loop responsavel por rodar a simulacao
for current_round in xrange(0, n_rounds):
	statistics.append(Statistics())
	while statistics[current_round].sample_index < k_samples:
		current_event = events_list.pop(0)
		#print current_event.time, current_event.event_type, current_event.customer_index
		if (current_event.event_type == "CH"):		
			current_event.queue_arrival(customers_list, events_list, wait_queue, current_round)
		elif (current_event.event_type == "ES"):
			current_event.service_entry(customers_list, events_list, wait_queue)
		elif (current_event.event_type == "SS"):
			current_event.service_exit(customers_list, events_list, wait_queue, statistics, current_round)
	statistics[current_round].mean_calculator()

sum = 0
for x in statistics[0].samples_queue_time:
	sum += (x - statistics[0].mean_queue_wait)**2

estimated_mean_real = statistics[0].mean_queue_wait
estimated_variance = sum / (k_samples - 1)

#for x in statistics:
#	estimated_mean += x.mean_queue_wait

#estimated_mean_real = estimated_mean / n_rounds

#for x in statistics:
	#estimated_variance += (x.mean_queue_wait - estimated_mean_real)**2

#standard_deviation = estimated_variance / (n_rounds - 1)

mean_infe_limit, mean_sup_limit, t_precision = Utils.mean_queue_wait_confidence_interval(sqrt(estimated_variance), estimated_mean_real, k_samples)
#infe_limit, sup_limit, chi_precision = Utils.variance_queue_wait_confidence_interval(estimated_variance / (n_rounds - 1), n_rounds)

print 'media estimada do tempo de espera na fila',  estimated_mean_real
print 'IC da media da  t-student: ',mean_infe_limit, mean_sup_limit 
print 'Precisao da media usando t-student: ', t_precision
print 'conta doida', mean_sup_limit - estimated_mean_real
print '5 per cent da media', estimated_mean_real * 0.05
#print 'variancia estimada do tempo de espera na fila',  estimated_variance / (n_rounds - 1)
#print 'IC da variancia bolado: ', infe_limit, sup_limit   
#print 'Precisao da variancia usando chi: ', chi_precision 


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
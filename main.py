from event import Event
from customer import Customer
from statistics import Statistics
from utils import Utils
import numpy as np

np.random.seed(777)
events_list = []
customers_list = []
wait_queue = []
statistics = Statistics()

first_customer = Customer(0)
customers_list.append(first_customer)

first_arrival = Event('CH', 0, 0)
events_list.append(first_arrival)

while statistics.sample_index < 90:
	current_event = events_list.pop(0)
	#print current_event.time, current_event.event_type, current_event.customer_index
	if (current_event.event_type == "CH"):		
		current_event.queue_arrival(customers_list, events_list, wait_queue)
	elif (current_event.event_type == "ES"):
		current_event.service_entry(customers_list, events_list, wait_queue)
	elif (current_event.event_type == "SS"):
		current_event.service_exit(customers_list, events_list, wait_queue, statistics)
print "VAMO VE", statistics.sample_index
print 'media do tempo de servico', statistics.mean_service_time/statistics.sample_index
print 'media do tempo na fila', statistics.mean_queue_time/statistics.sample_index
print 'media do tempo de espera no sistema', statistics.mean_system_time/statistics.sample_index 

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
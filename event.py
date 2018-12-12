from customer import *
from utils import *
import sys

busy_server = False
customer_id = 0
discipline = sys.argv[1] if len(sys.argv) > 1 else 'FCFS' 

class Event:

    '''
    Atributos de cada Evento:
    - event_type: Define o tipo do evento 
        -- Chegada no sistema (CH) 
        -- Entrada em servico (ES) 
        -- Saida de servico (SS)
    
    - time: Define o tempo de inicio do evento
    - customer_index: Define o indice do fregues a qual o evento se refere
    '''

    def __init__(self, event_type, time, customer_index): 
        self.event_type = event_type
        self.time = time
        self.customer_index = customer_index

    def queue_arrival(self, customers_list, events_list, wait_queue, current_round):
        global customer_id
        arrival_time = self.time + Utils.generate_arrival_time(0.4)
        customer_id += 1
        customers_list.append(Customer(customer_id, arrival_time, current_round))
        Utils.append_event(Event('CH', arrival_time, customer_id), events_list)
        if (len(wait_queue) == 0 and not busy_server):
            Utils.append_event(Event('ES', self.time, self.customer_index), events_list)
        else:
            wait_queue.append(self.customer_index)

    def service_entry(self, customers_list, events_list, wait_queue):
        global busy_server
        if (len(wait_queue) > 0):
            next_in_queue = 0 if discipline == 'FCFS' else len(wait_queue)-1
            wait_queue.pop(next_in_queue)
        service_time = self.time + Utils.generate_service_time()
        Utils.append_event(Event('SS', service_time , self.customer_index), events_list)
        busy_server = True
        customers_list[Utils.find_customer(customers_list, self.customer_index)].entry_server_time = self.time

    def service_exit(self, customers_list, events_list, wait_queue, statistics, current_round):
        global busy_server
        if (len(wait_queue) > 0):
            next_in_queue = 0 if discipline == 'FCFS' else len(wait_queue)-1
            Utils.append_event(Event('ES', self.time, wait_queue[next_in_queue]), events_list)
        busy_server = False
        aux_customer_id = Utils.find_customer(customers_list, self.customer_index)
        customers_list[aux_customer_id].exit_server_time = self.time
        statistics[current_round].statistics_acumulator(customers_list[aux_customer_id])
        customers_list.pop(aux_customer_id)
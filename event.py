from customer import *
from utils import *

busy_server = False
customer_id = 0

class Event:

    # Atributos:
    #
    # event_type - Define  o tipo do evento 
    # ---- Chegada (CH) ----
    # ---- Entrada em servico (ES) ----
    # ---- Saida de servico (SS) ----
    #
    # time - Define o tempo de inicio do evento
    #
    # customer_index - Define o indice do individuo a qual o evento se refere

    def __init__(self, event_type, time, customer_index): 
        self.event_type = event_type
        self.time = time
        self.customer_index = customer_index

    def queue_arrival(self, customers_list, events_list, wait_queue, current_round):
        global customer_id
        arrival_time = self.time + Utils.generate_arrival_time(0.9)
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
            wait_queue.pop(0)
        service_time = self.time + Utils.generate_service_time()
        Utils.append_event(Event('SS', service_time , self.customer_index), events_list)
        busy_server = True
        customers_list[Utils.find_customer(customers_list, self.customer_index)].entry_server_time = self.time

    def service_exit(self, customers_list, events_list, wait_queue, statistics, current_round):
        global busy_server
        if (len(wait_queue) > 0):
            Utils.append_event(Event('ES', self.time, wait_queue[0]), events_list)
        busy_server = False
        aux_customer_id = Utils.find_customer(customers_list, self.customer_index)
        customers_list[aux_customer_id].exit_server_time = self.time
        statistics[current_round].statistics_acumulator(customers_list[aux_customer_id])
        customers_list.pop(aux_customer_id)
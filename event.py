from customer import *
from utils import *

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

    def queue_arrival(self, customers_list, events_list, wait_queue):   
        customers_list.append(Customer())
        Utils.append_event(Event('CH', self.time + Utils.generate_arrival_time(), len(customers_list) - 1), events_list)
        if (len(wait_queue) == 0):
            Utils.append_event(Event('ES', self.time, self.customer_index), events_list)
        else:
            wait_queue.append(self.customer_index)

    def service_entry(self, events_list, wait_queue):
        service_time = self.time + Utils.generate_service_time()
        Utils.append_event(Event('SS',service_time , self.customer_index), events_list)
        if (len(wait_queue) > 0):
            Utils.append_event(Event('ES', service_time, wait_queue.pop(0)), events_list)

    def service_exit(self, events_list, wait_queue):
        wait_queue.pop(0)



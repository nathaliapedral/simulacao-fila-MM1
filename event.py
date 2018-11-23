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

    def queue_arrival(self, customers_list, events_list):   
        customers_list.append(Customer())
        Utils.append_event(Event('CH', 1, len(customers_list) - 1), events_list)

    def service_entry(self, events_list):
        Utils.append_event(Event('SS', 1, self.customer_index))

    def service_exit(self, events_list, wait_queue):
        if (len(wait_queue) > 0):
            Utils.append_event(Event('ES', 1, wait_queue.pop(0)), events_list)



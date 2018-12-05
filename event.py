from customer import *
from utils import *

busy_server = False  

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
        print "chegamais"
        print busy_server
        if (len(wait_queue) == 0 and not busy_server):
            Utils.append_event(Event('ES', self.time, self.customer_index), events_list)
        else:
            wait_queue.append(self.customer_index)

    def service_entry(self, events_list, wait_queue):
        global busy_server
        if (len(wait_queue) > 0):
            wait_queue.pop(0)
        service_time = self.time + Utils.generate_service_time()
        Utils.append_event(Event('SS',service_time , self.customer_index), events_list)
        busy_server = True
        print "entraS"
        print busy_server
        

    def service_exit(self, events_list, wait_queue):
        global busy_server
        if (len(wait_queue) > 0):
            Utils.append_event(Event('ES', self.time, wait_queue[0]), events_list)
        busy_server = False
        print "saiS"
        print busy_server

import numpy as np

class Utils:
	
    @staticmethod
    def append_event(event, events_list):
        for x in range(0, len(events_list)):
            if (events_list[x].time > event.time):
                events_list.insert(x, event)
                return
        events_list.append(event)

    @staticmethod
    def generate_arrival_time(lambda_):
        u0 = np.random.rand()
        t0 = np.log(u0) / (-lambda_)
        return t0

    @staticmethod
    def generate_service_time():    	
    	global t, n
        u0 = np.random.rand()
        x0 = np.log(u0) / -1 # A taxa de servico e 1 pois foi dado na descricao do trabalho 
        return x0
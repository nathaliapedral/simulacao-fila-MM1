import numpy as np
from scipy.stats import chi2
from scipy.stats import t

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
        u0 = np.random.rand()
        x0 = np.log(u0) / -1 # A taxa de servico e 1 pois foi dado na descricao do trabalho 
        return x0

    @staticmethod
    def find_customer(customers_list, id):
        for x in xrange(0, len(customers_list)):
            if (customers_list[x].id == id):
                return x
        return None

    @staticmethod
    def variance_queue_wait_confidence_interval(estimated_variance, n_rounds):
        superior_limit = ((n_rounds - 1) * estimated_variance) / chi2.ppf(q = 0.025, df = n_rounds-1)
        inferior_limit = ((n_rounds - 1) * estimated_variance) / chi2.ppf(q = 0.975, df = n_rounds-1)
        return inferior_limit , superior_limit, chi2.ppf(q = 0.975, df = n_rounds-1), chi2.ppf(q = 0.025, df = n_rounds-1)

    def mean_queue_wait_confidence_interval(standard_deviation, estimated_mean, n_rounds):
        superior_limit = estimated_mean + (t.ppf(q = 0.975, df = n_rounds-1) * (standard_deviation/sqrt(n_rounds))) 
        inferior_limit = estimated_mean - (t.ppf(q = 0.975, df = n_rounds-1) * (standard_deviation/sqrt(n_rounds)))
        
        
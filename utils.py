from random import randint

class Utils:
	
    @staticmethod
    def append_event(event, events_list):
        for x in range(0, len(events_list)):
            if (events_list[x].time > event.time):
                events_list.insert(x, event)
                return
        events_list.append(event)

    @staticmethod
    def generate_arrival_time():
        #return randint(0, 9)
        return 3

    @staticmethod
    def generate_service_time():
        #return randint(0, 9)
        return 1

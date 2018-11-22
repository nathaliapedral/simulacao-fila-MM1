from event import Event
from custumer import Custumer

events_list = []
custumers_list = []

first_custumer = Custumer()
custumers_list.append(first_custumer)

first_arrival = Event('CH', 1, len(custumers_list)-1)
events_list.append(first_arrival)

for x in xrange(0, 9):
	events_list[x].queue_arrival(custumers_list, events_list)

print len(events_list)
	
	
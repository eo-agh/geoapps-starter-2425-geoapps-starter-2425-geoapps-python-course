from .incident import Incident
from datetime import datetime


class IncidentQueue:
    def __init__(self):
        self.__queue = []

    def __getitem__(self, position):
        return self.__queue[position]

    def __setitem__(self, position, value):
        self.__queue[position] = value

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.__queue):
            result = self.__queue[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

    def __contains__(self, incident):
        return incident in self.__queue

    def __repr__(self):
        return f"IncidentQueue({self.__queue!r})"

    def __str__(self):
        if len(self):
            return "\n".join([f"{' ' * (4 * idx)}{incident}" for idx, incident in enumerate(self.__queue)])
        else:
            return "Empty queue"

    def __add__(self, other):
        if isinstance(other, Incident):
            new__queue = IncidentQueue()
            new__queue.__queue = self.__queue[:] 
            new__queue += other
            return new__queue
        else:
            return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Incident):
            new__queue = IncidentQueue()
            new__queue += other
            new__queue.__queue += self.__queue
            return new__queue
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Incident):
            self.__queue.append(other)
        return self

    def __call__(self, id):
        for incident in self.__queue:
            if incident.id == id:
                return incident
            pass
        raise ValueError("No incident found with the given ID")

    def __lt__(self, other):
        return len(self.__queue) < len(other.__queue)

    def __gt__(self, other):
        return len(self.__queue) > len(other.__queue)

    def __bool__(self):
        return bool(self.__queue)

    def __len__(self):
        return len(self.__queue)

    def sort_incidents(self):
        time = datetime.now()
        zhigh = IncidentQueue()
        zmedium = IncidentQueue()
        zlow = IncidentQueue()
        for x in self.__queue:
            if x.status != "pending":
                continue
            if x.priority == "high":
                zhigh += x
            elif x.priority == "medium":
                zmedium += x
            elif x.priority == "low":
                zlow += x
                
        for w in range(len(zhigh)):
            for x in range(len(zhigh)-1):
                time1 = time - zhigh.__queue[x].timestamp
                zhigh.__queue[x].time_since_report = time1
                time2 = time - zhigh.__queue[x+1].timestamp
                if time1 > time2:
                    zhigh.__queue[x], zhigh.__queue[x+1] = zhigh.__queue[x+1], zhigh.__queue[x]
            
        for w in range(len(zmedium)):
            for x in range(len(zmedium)-1):
                time1 = time - zmedium.__queue[x].timestamp
                zmedium.__queue[x].time_since_report = time1
                time2 = time - zmedium.__queue[x+1].timestamp
                if time1 > time2:
                    zmedium.__queue[x], zmedium.__queue[x+1] = zmedium.__queue[x+1], zmedium.__queue[x]    
        
        for w in range(len(zlow)):
            for x in range(len(zlow)-1):
                time1 = time - zlow.__queue[x].timestamp
                zlow.__queue[x].time_since_report = time1
                time2 = time - zlow.__queue[x+1].timestamp
                if time1 > time2:
                    zlow.__queue[x], zlow.__queue[x+1] = zlow.__queue[x+1], zlow.__queue[x]
        
        new__queue = IncidentQueue()
        new__queue.__queue = zhigh.__queue[:]
        new__queue.__queue += zmedium.__queue[:]
        new__queue.__queue += zlow.__queue[:]

        return new__queue
                               
                     

if __name__ == "__main__":
    queue = IncidentQueue()
    incident1 = Incident("Power outage in sector 4", "low", (50.923145, 18.917486), "Amy King")
    incident2 = Incident("Fire alarm in building 21", "high", (50.923145, 19.017486), "Phill Poe")
    incident4 = Incident("Fire alarm in building 129", "medium", (50.023145, 18.907486), "Mindy Lote")


    print(f"---------- wyświetlanie za pomocą __str__ ----------")
    print(queue)

    print(f"---------- dodanie za pomocą __iadd__ ----------")
    queue += incident1
    queue += incident2
    print(queue)
    print(f"---------- dodanie za pomocą __add__ ----------")
    queue = queue + incident4
    print(queue)

    print(f"---------- dostęp za pomocą __getitem__ ----------")
    print(queue[0])
    print(f"---------- sprawdzenie za pomocą __contains__ ----------")
    print(incident1 in queue)

    print(f"---------- iteracja za pomocą __iter__ i __next__ ----------")
    for incident in queue:
        print(incident)

    print(f"---------- dodawanie prawostronne za pomocą __radd__ ----------")
  
    new_incident = Incident("Test incident", "low", (50.00983746, 19.891731), "Victor Grahm")
    queue = new_incident + queue

    print(f"---------- test za pomocą __bool__ ----------")
    if queue:
        print("Queue is not empty.")

    print(f"---------- długość kolejki za pomocą __len__ ----------")
    print(len(queue))

    print(f"---------- wyszukiwanie za pomocą __call__ ----------")
    print(queue(1))
    
    print(f"---------- wyświetlanie za pomocą __str__ ----------")
    print(queue)
    
    print()
    
    print(f"---------- wyświetlanie za pomocą __str__ po sortowaniu ----------")
    print(queue.sort_incidents())
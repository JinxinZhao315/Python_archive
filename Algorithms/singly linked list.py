class Plane:
    def __init__(self,airline,flightno):
        self.airline = airline
        self.flightno = flightno
        self.behind = None


class Runway:
    def __init__(self,head):
        self.head = None

    def join(self, plane):
        if self.head == None:
            self.head = plane
        else:
            tracker = self.head
            while True:
                if not tracker.behind == None:
                    tracker = tracker.behind
                else:
                    tracker.behind = plane
                    break
                        
    

    def find(self, position):
        if position>0:
            tracker = self.head
            counter = position
            while counter > 0:
                if tracker == None:
                    print('plane not found at', position)
                    return
                elif counter == 1:
                    print('plane founf at',position,'is',airline, flightno)
                tracker = tracker.behind
                counter -= 1
                
                
            

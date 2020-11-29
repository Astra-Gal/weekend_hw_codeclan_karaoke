class Room:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.guests = []
        self.playlist = []

    
    def check_capacity(self):
        return len(self.guests)

    def check_in_guest(self, guest):
        if len(self.guests) < self.capacity:
            self.guests.append(guest)
        else:
            return "Sorry! Over Capacity"

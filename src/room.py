class Room:

    def __init__(self, name, capacity, entry_fee):
        self.name = name
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.guests = []
        self.playlist = []

    
    def check_capacity(self):
        return len(self.guests)

    def check_in_guest(self, guest):
        if len(self.guests) < self.capacity:
            self.guests.append(guest)
        else:
            return "Sorry! Over Capacity"

    def guest_is_old_enough(self, guest):
        return guest.age >= 18

    def playlist_length(self):
        return len(self.playlist)

    def add_song_to_playlist(self, song):
        self.playlist.append(song)

    def add_song_to_play_next(self, song):
        self.playlist[:0] = [song]

    def can_afford_entry(self, guest):
        return guest.wallet >= self.entry_fee

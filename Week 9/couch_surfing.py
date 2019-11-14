class Member:
    def __init__(self):
        #want to seperate occasions where you were a host from when you were a guest for a couch stay
        self.host_stays = []
        self.guest_stays = []

    #for a stay, add it to the host list, ie. this member provided the couch this time
    def add_host_stay(self, guest, nights):
        self.host_stays.append(Stay(self, guest, nights))
    #ie. this member rented the couch this time
    def add_guest_stay(self, guest, nights):
        self.guest_stays.append(Stay(guest, self, nights))

    #member rating average of their rating as a host and as a renter of couches
    def get_average_rating(self):
        total = 0
        for s in self.host_stays:
            total += s.review_of_host.rating

        for s in self.guest_stays:
            total += s.review_of_guest.rating

        return total/(len(self.host_stays) + len(self.guest_stays))

class Stay:
    def __init__(self, host, guest, nights):
        self.host = host
        self.guest = guest
        self.review_of_guest = None
        self.review_of_host = None
        self.nights = nights

    #reviewing the stay
    def review_as_guest(self, description, rating):
        self.review_of_host = Review(self.guest, self.host, description, rating)
    #reviewing the guest who stayed
    def review_as_host(self, description, rating):
        self.review_of_guest = Review(self.host, self.guest, description, rating)

class Review:
    def __init__(self, reviewer, reviewee, description, rating):
        self.reviewer = reviewer
        self.reviewee = reviewee
        self.description = description
        self.rating = rating

    def exceptional(self):
        return self.rating >= self.reviewer.get_average_rating()

    def dubious(self):
        return self.rating - self.reviewee.get_average_rating() > 2

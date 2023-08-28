class Restaurant:
    
    def __init__(self, name):
        self.name = name
        self.reviews = []
        
    def add_review(self, rating):
        self.reviews.append(rating)
        
    def average_star_rating(self):
        if len(self.reviews) == 0:
            return 0  # Return 0 if there are no reviews
        total_rating = sum(self.reviews)
        average_rating = total_rating / len(self.reviews)
        return average_rating
    
    def get_name(self):
        return self.name
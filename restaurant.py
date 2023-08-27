class Restaurant:
    
    def __init__(self, name):
        self.name = name
        self.reviews = []
        
    def add_review(self, rating):
        self.reviews.append(rating)
class Review:
    
    all_reviews = []
    
    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        Review.all_reviews.append(self)
class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []
        Customer.all_customers.append(self)

class Customer:
    all_customers = []
    
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []
        Customer.all_customers.append(self)
        
    def set_given_name(self, given_name):
        self.given_name = given_name
        
    def set_family_name(self, family_name):
        self.family_name = family_name
        
    def get_given_name(self):
        return self.given_name
    
    def get_family_name(self):
        return self.family_name
    
    def full_name(self):
        return f"{self.given_name} {self.family_name}"
    @classmethod
    def all(cls):
        return cls.all_customers
    
    def add_review(self,restaurant,rating):
        review  = Review(self,restaurant,rating)
        self.reviews.append(review)
        restaurant.add_review(review)
        
    def num_reviews(self):
        return len(self.reviews)
    
    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        return None
    
    @classmethod
    def find_all_by_given_name(cls,name):
        customers = []
        for customer in cls.all_customers:
         if customer.given_name()==name:
            customers.append = customers
            return customers


customer1 = Customer("mary", "John") 
# print(Customer)          
    

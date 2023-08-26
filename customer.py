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
    

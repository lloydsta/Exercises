# 9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
#   Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and
# print the value again.
#   Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any number
# you like that could represent how many customers were served in, say, a
# day of business.

# NOTE: Using import and inheritence is not actually part of the exercise

# Import the Restaurant class from Exercise 9-1
from ematthes_9_1_9_3 import Restaurant

# Use Inheritance
class Restaurant_9_4(Restaurant):
    """Inherited from the Restaurant class defined in Excersise 9-1."""
    def __init__(self, restaurant_name, cuisine_type):

        """Initialize attributes of the parent class."""
        super().__init__(restaurant_name, cuisine_type)

        # 9-4 new attribute: number served
        self.number_served = 0

    # 9-4 new method: show number served
    def show_number_served(self):
        print('The restaurant has served ' + str(self.number_served) + ' people')

    # 9-4 new method: set number served
    def set_number_served(self, served):
        '''Allows you to set the number of people served'''
        self.number_served = served

    # 9-4 new method: increment number served
    def increment_number_served(self, increment):
        '''Allows you to increment the number of people served in one day'''
        self.number_served += increment


# Create a new restaurant instance
restaurant = Restaurant_9_4('Apollo 69', 'Space food')

# Test to see if child class/instance got properly created (not part of question)
restaurant.describe_restaurant()

# Show initial number of people served, which should be 0
restaurant.show_number_served()

# Change number of people served to 5
restaurant.number_served = 5

# Reprint number of people served
restaurant.show_number_served()

# Explicitly set the number of people served to 50
restaurant.set_number_served(50)

# Increment the previous number by 100
restaurant.increment_number_served(100)

# Reprint number of people served (should be 150)
restaurant.show_number_served()

print('\n')



# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 166). Write a method called increment_
# login_attempts() that increments the value of login_attempts by 1. Write
# another method called reset_login_attempts() that resets the value of login_
# attempts to 0.
#   Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.

# Import the User class from Exercise 9-3
from ematthes_9_1_9_3 import User

# Use Inheritance
class User_9_5(User):
    """Inherited from the User class defined in Excersise 9-3."""
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)

        # 9-5 new attribute: login attempts
        self.login_attempts = 0

    # 9-5 new method: increment login attempts
    def increment_login_attempts(self):
        self.login_attempts += 1

    # 9-5 new method: reset login attempts
    def reset_login_attempts(self):
        self.login_attempts = 0

# Make an instance
user95 = User_9_5('Michael', 'Jordan', 20, 'Kansas')

# Increment login several times, then print
user95.increment_login_attempts()
user95.increment_login_attempts()
print(user95.login_attempts)

# Reset login attempts, then print
user95.reset_login_attempts()
print(user95.login_attempts)
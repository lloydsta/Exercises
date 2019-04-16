# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indicating
# that the restaurant is open.
#   Make an instance called restaurant from your class. Print the two attributes
# individually, and then call both methods.

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        '''Initialize the restaurant name and cuisine type'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

        # 9-4. Number Served (Continuation)
        self.number_served = 0

    def describe_restaurant(self):
        print('The name of the restaurant is ' + self.restaurant_name.title() + '.')
        print('The restaurant serves ' + self.cuisine_type + '.')

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is open.')

    # 9-4. Number Served (Continuation)
    def show_number_served(self):
        print('The restaurant has served ' + str(self.number_served) + ' people')

    # 9-4. Number Served (Continuation)
    def set_number_served(self, served):
        '''Allows you to set the number of people served'''
        self.number_served = served
    
    # 9-4. Number Served (Continuation)
    def increment_number_served(self, increment):
        '''Allows you to increment the number of people served in one day'''
        self.number_served += increment

restaurant = Restaurant('The Golden Saucer', 'Chinese')

restaurant.describe_restaurant()
restaurant.open_restaurant()
print('\n')

# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.

restaurant_dos = Restaurant('The Crying Bagel', 'Breakfast Food')
restaurant_tres = Restaurant('Oblong Gato', 'Cat Meat')

restaurant_dos.describe_restaurant()
print('\n')
restaurant_tres.describe_restaurant()


# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
#   Create several instances representing different users, and call both methods
# for each user.

class User():
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

        # 9-5. Login Attempts (Continuation)
        self.login_attempts = 0

    def describe_user(self):
        print("The user's first name is " + self.first_name + '.')
        print("The user's last name is " + self.last_name + '.')
        print("The user's age is " + str(self.age) + '.')
        print("The user's location is " + self.location + '.')

    def greet_user(self):
        print('Hello ' + self.first_name + ', this is a personalized message.')

    # 9-5. Login Attempts (Continuation)
    def increment_login_attempts(self):
        self.login_attempts += 1

    # 9-5. Login Attempts (Continuation)
    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User('John', 'Smith', 32, 'Mississippi')
user2 = User('Kathy', 'Griffin', 69, 'China')

user1.greet_user()
user1.describe_user()

print('\n')

user2.greet_user()
user2.describe_user()

print('\n')

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

# See 9-1 for new methods
restaurant.show_number_served()
restaurant.number_served = 5
restaurant.show_number_served()

print('\n')

restaurant.set_number_served(10)
restaurant.show_number_served()

print('\n')

restaurant.set_number_served(50)
restaurant.increment_number_served(100)
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

# See 9-3 for new methods
user95 = User('Michael', 'Jordan', 20, 'Kansas')
user95.increment_login_attempts()
user95.increment_login_attempts()
print(user95.login_attempts)
user95.reset_login_attempts()
print(user95.login_attempts)

# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indicating
# that the restaurant is open.
#   Make an instance called restaurant from your class. Print the two attributes
# individually, and then call both methods.

class Restaurant():
    """Defines a restaurant including its name and the type of food it serves."""
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('The name of the restaurant is ' + self.restaurant_name.title() + '.')
        print('The restaurant serves ' + self.cuisine_type + '.')

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is open.')


"""TRICK TO NOT RUN THIS CODE WHEN IMPORTED (subsequent exercises importing this module)"""
if __name__ == "__main__":
    # Make an instance called restaurant from your class.
    restaurant = Restaurant('The Golden Saucer', 'Chinese')

    # Call both methods.
    restaurant.describe_restaurant()
    restaurant.open_restaurant()
    print('\n')

# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.

"""TRICK TO NOT RUN THIS CODE WHEN IMPORTED (subsequent exercises importing this module)"""
if __name__ == "__main__":
    # Create three different instances 
    restaurant_dos = Restaurant('The Crying Bagel', 'Breakfast Food')
    restaurant_tres = Restaurant('Oblong Gato', 'Cat Meat')

    # Call describe restaurant method for each instance
    restaurant_dos.describe_restaurant()
    restaurant_tres.describe_restaurant()
    print('\n')


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

    def describe_user(self):
        print("The user's first name is " + self.first_name + '.')
        print("The user's last name is " + self.last_name + '.')
        print("The user's age is " + str(self.age) + '.')
        print("The user's location is " + self.location + '.')

    def greet_user(self):
        print('Hello ' + self.first_name + ', this is a personalized message.')


"""TRICK TO NOT RUN THIS CODE WHEN IMPORTED (subsequent exercises importing this module)"""
if __name__ == "__main__":
    # Create several instances representing different users
    user1 = User('John', 'Smith', 32, 'Mississippi')
    user2 = User('Kathy', 'Griffin', 69, 'China')

    # Call both methods for each user.
    user1.greet_user()
    user1.describe_user()

    user2.greet_user()
    user2.describe_user()
    print('\n')

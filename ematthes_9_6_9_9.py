# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote
# in Excercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
# the class will work; just pick the one you like better. Add an attribute called
# flavors that stores a list of ice cream flavors. Write a method that displays
# these flavors. Create an instance of IceCreamStand, and call this method.

# Import the class from 9-1
from ematthes_9_1_9_3 import Restaurant

# Use Inheritance
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)

        # New attribute that stores list of flavors
        self.flavors = ['Vanilla', 'Chocolate', 'Strawberry']
    
    # Method that displays flavors
    def show_flavors(self):
        print(self.flavors)


# Create an instance of IceCreamStand
coldstone = IceCreamStand('Coldstone', 'Ice cream')

# Call the method
coldstone.show_flavors()


# 9-7. Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
# or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator's set of
# privileges. Create an instance of Admin, and call your method.

# Import the class from 9-3
from ematthes_9_1_9_3 import User

# Use Inheritance
class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)

        # New attribute that stores a list of privileges
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    # Method that displays privileges
    def show_privileges(self):
        print(self.privileges)

# Create an instance of Admin
the_administrator = Admin('John', 'Smith', 30, 'Neverland')

# Call the method
the_administrator.show_privileges()


# 9-8. Privileges: Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use your
# method to show its privileges.

class Privileges():
    
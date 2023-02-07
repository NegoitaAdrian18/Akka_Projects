import establish_connection
from establish_connection import *

USER_INTERFACE = """

Choose one of these optinos:

1) Add a new person:
2) See all persons information: 
3) Update person details: 
4) Remove person information: 
5) Exit!

Enter your option: 
"""


class CreateDatabase:

    def menu(self):
        connection = establish_connection.CreateTable().connect()
        establish_connection.CreateTable().create_table(connection)

        while (user_input := input(USER_INTERFACE)) != "5":
            if user_input == "1":
                self.ui_add_informations_about_persons(connection)
            elif user_input == "2":
                self.ui_get_all_informations_about_a_person(connection)
            elif user_input == "3":
                self.ui_update_person_information(connection)
            elif user_input == "4":
                self.ui_remove_information_about_a_person(connection)
            else:
                print("Invalid input!")

    def ui_add_informations_about_persons(self, connection):
        first = input("First Name: ")
        second = input("Second Name: ")
        address = input("Address: ")
        phone = input("Phone Number: ")
        email = input("Email address: ")
        establish_connection.CreateTable().add_person_info(connection, first, second, address, phone, email)

    def ui_get_all_informations_about_a_person(self, connection):
        informations = establish_connection.CreateTable().get_all_person_info(connection)
        for info in informations:
            print(f"{info[0]} {info[1]} {info[2]} {info[3]} {info[4]}")


    def ui_update_person_information(self, connection):
        first = input("First Name: ")
        second = input("Second Name: ")
        phone = input("Enter the updated phone number: ")
        update = establish_connection.CreateTable().update_person_information(connection, first, second, phone)
        print(update)

    def ui_remove_information_about_a_person(self, connection):
        first = input("First Name: ")
        second = input("Second Name: ")
        remove = establish_connection.CreateTable().remove_information_about_a_person(connection, first, second)
        print(remove)


CreateDatabase().menu()

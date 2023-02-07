import sqlite3

CREATE_INFO_TABLE = """CREATE TABLE IF NOT EXISTS Person_details (
                            FirstName text,
                            SecondName text,
                            Address text,
                            PhoneNumber integer,
                            EmailAddress text
                            )"""

INSERT_PERSON_INFO = "INSERT INTO Person_details (FirstName, SecondName, Address, PhoneNumber, EmailAddress) VALUES (" \
                     "?, ?, " \
                     "?, ?, ?) "
GET_ALL_PERSON_INFO = "SELECT * FROM Person_details"
UPDATE_PERSON_INFORMATION = "UPDATE Person_details SET PhoneNumber = ?, WHERE FirstName = ? AND SecondName = ?"
REMOVE_INFORMATION_ABOUT_A_PERSON = "DELETE from Person_details WHERE FirstName = ? AND SecondName = ?"


class CreateTable:

    def connect(self):
        return sqlite3.connect('person_info.db')

    def create_table(self, connection):
        with connection:
            connection.execute(CREATE_INFO_TABLE)

    def add_person_info(self, connection, FirstName, SecondName, Address, PhoneNumber, EmailAddress):
        with connection:
            connection.execute(INSERT_PERSON_INFO, (FirstName, SecondName, Address, PhoneNumber, EmailAddress))

    def get_all_person_info(self, connection):
        with connection:
            return connection.execute(GET_ALL_PERSON_INFO).fetchall()

    def update_person_information(self, connection, PhoneNumber, FirstName, SecondName, ):
        with connection:
            return connection.execute(UPDATE_PERSON_INFORMATION, (PhoneNumber, FirstName, SecondName)).fetchall()

    def remove_information_about_a_person(self, connection, FirstName, SecondName):
        with connection:
            connection.execute(REMOVE_INFORMATION_ABOUT_A_PERSON, (FirstName, SecondName)).fetchone()

class Person:
    def __init__(self, firstName, lastName, email):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email

    def getName(self):
        return f"{self.firstName[0].upper()}{self.firstName[1:]} {self.lastName[0].upper()}{self.lastName[1:]}"

class Customer(Person):
    def __init__(self, firstName, lastName, email, number):
        Person.__init__(self, firstName, lastName, email)
        self.number = number

class Employee(Person):
    def __init__(self, firstName, lastName, email, ssn):
        Person.__init__(self, firstName, lastName, email)
        self.ssn = ssn

def main():
    print("Customer/Employee Data Entry")
    choice = "y"
    while choice == "y":
        print()
        user = str(input("Customer or employee? (c/e): "))
        print()
        if user.lower() != "c" and user.lower() != "e":
            print("Invalid input. Enter either 'c' or 'e'.")
        else:
            print("DATA ENTRY")
            firstName = str(input("First Name: "))
            lastName = str(input("Last Name: "))
            email = str(input("Email: "))
            if user.lower() == "c":
                number = str(input("Number: "))
                client = Customer(firstName, lastName, email, number)
            else:
                ssn = str(input("SSN: "))
                while len(ssn) != 11 or ssn[3] != "-" or ssn[6] != "-":
                    print("Invalid SSN. Please follow the format: xxx-xx-xxxx)")
                    ssn = str(input("SSN: "))
                client = Employee(firstName, lastName, email, ssn)
            if isinstance(client, Customer):
                print()
                print("Customer")
                print(f"Name:      {client.getName()}")
                print(f"Email:     {client.email}")
                print(f"Number:    {client.number}")
            if isinstance(client, Employee):
                print()
                print("Employee")
                print(f"Name:      {client.getName()}")
                print(f"Email:     {client.email}")
                print(f"Number:    {client.ssn}")
        print()
        choice = str(input("Continue? (y/n): "))
        while choice.lower() != "y" and choice.lower() != "n":
            print("Invalid input. Enter either 'y' or 'n'")
            choice = str(input("Continue? (y/n): "))
        if choice.lower() == "n":
            print()
            print("Bye!")


main()








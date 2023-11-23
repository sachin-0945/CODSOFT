# Initializing an empty dictionary to store contact information
contacts = {}

# Function to add a new contact
def add_contact():
    n=int(input('Enter the number of contacts you want to enter:'))
    for i in range(1,n+1):
        print(f'Enter person {i} detail:')
        name = input("Enter the contact's name: ")
        phone = input("Enter the contact's phone number: ")
        email = input("Enter the contact's email: ")
        address = input("Enter the contact's address: ")


        contacts[name] = {
             'phone': phone,
             'email': email,
             'address': address
        }
        print(f"{name} has been added to your contacts.")
        print()

# Function to view the contact list
def view_contact_list():
    if not contacts:
        print("Your contact list is empty.")
    else:
        print("Contact List:")
        print('-----------------------------------------')
        for name, ph in contacts.items():
            print(f"Name: {name} | Phone: {ph['phone']}")
        print('-----------------------------------------')

# Function to search for a contact by name or phone number
def search_contact():
    search_item = input("Enter a name or phone number to search for a contact: ")
    found = False
    for name, ph in contacts.items():
        if search_item in [name, ph['phone']]:
            print("Contact found : ")
            print('-----------------------------------------------------------------------------------')
            print(f"Name: {name}| Phone: {ph['phone']}| Email: {ph['email']}| Address: {ph['address']}")
            print('-----------------------------------------------------------------------------------')
            found = True
    if not found:
        print("Contact not found.")

# Function to update contact details
def update_contact():
    name = input("Enter the name of the contact you want to update: ")
    if name in contacts:
        print(f"Updating contact: {name}")
        phone = input("Enter the new phone number: ")
        email = input("Enter the new email: ")
        address = input("Enter the new address: ")
        
        contacts[name]['phone'] = phone
        contacts[name]['email'] = email
        contacts[name]['address'] = address
        print(f"{name}'s contact details have been updated.")
    else:
        print(f"Contact with name {name} does not exist.")

# Function to delete a contact
def delete_contact():
    if contacts=={}:
        print("No Contacts!")
    else:
        name = input("Enter the name of the contact you want to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"{name} has been deleted from your contacts.")
        else:
            print(f"Contact with name {name} does not exist.")

# User interface loop
while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")

    choice = input("Select an option (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact_list()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Goodbye! Have a nice day.")
        break
    else:
        print("Invalid option. Please choose a valid option (1-6).")

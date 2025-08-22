import json
import os

# File to store contacts
CONTACTS_FILE = 'contacts.json'

def load_contacts():
    """Load contacts from JSON file"""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    """Save contacts to JSON file"""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Add a new contact"""
    print("\nAdd New Contact")
    print("-" * 20)
    name = input("Name: ").strip().title()
    if not name:
        print("Error: Name cannot be empty!")
        return
        
    if name in contacts:
        print(f"A contact with name '{name}' already exists!")
        return
        
    phone = input("Phone: ").strip()
    email = input("Email: ").strip().lower()
    address = input("Address (optional): ").strip()
    
    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    save_contacts(contacts)
    print(f"\nContact '{name}' added successfully!")

def search_contacts(contacts):
    """Search contacts by name or phone"""
    if not contacts:
        print("No contacts found!")
        return
        
    search_term = input("\nEnter name or phone number to search: ").strip().lower()
    if not search_term:
        print("Search term cannot be empty!")
        return
    
    # Using list comprehension for searching
    results = [
        (name, info) 
        for name, info in contacts.items() 
        if (search_term in name.lower()) or (search_term in info['phone'])
    ]
    
    if not results:
        print("No matching contacts found!")
        return
        
    print(f"\nFound {len(results)} matching contact(s):")
    print("-" * 50)
    for name, info in results:
        print(f"Name: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        if info['address']:
            print(f"Address: {info['address']}")
        print("-" * 50)

def view_all_contacts(contacts):
    """Display all contacts"""
    if not contacts:
        print("No contacts found!")
        return
        
    print("\nAll Contacts")
    print("-" * 50)
    for name, info in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        if info['address']:
            print(f"Address: {info['address']}")
        print("-" * 50)

def delete_contact(contacts):
    """Delete a contact by name"""
    if not contacts:
        print("No contacts to delete!")
        return
        
    name = input("\nEnter name of contact to delete: ").strip().title()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found!")

def main():
    """Main function to run the contact book application"""
    contacts = load_contacts()
    
    while True:
        print("\nContact Book")
        print("-" * 20)
        print("1. Add Contact")
        print("2. Search Contacts")
        print("3. View All Contacts")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contacts(contacts)
        elif choice == '3':
            view_all_contacts(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("\nThank you for using Contact Book!")
            break
        else:
            print("\nInvalid choice! Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()

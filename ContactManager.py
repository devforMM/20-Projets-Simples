import json


def get_contact(contact_name,contacts):
    contacts_names=[contact["name"] for contact in contacts]
    postition=contacts_names.index(contact_name)
    return contacts_names.pop(postition)




class ContactManager:
    def __init__(self) -> None:
        self.contacts=[]

    def update_file(self,contacts):
        with open("contacts.json") as file:
            json.dump(contacts,file)
    


    
    def add_contact(self,contact_name,num_tel,adress):
        new_contact={
            "name":contact_name,
            "num tel":num_tel,
            "adress":adress
        }
        self.contacts.append(new_contact)
    def delete_contact(self,contact_name):
        get_contact(self,contact_name)

    def search_contact(self,contact_name):
        contact=get_contact(self.contacts,contact_name)
        self.contacts.append(contact)
        self.update_file(self.contacts)


    def update_contact(self,attribue,value,contact_name):
        contact=get_contact(contact_name,self.contacts)
        contact[attribue]=value
        self.contacts.__add__(contact)
        self.update_file(self.contacts)

    def show_contacts(self):
        for contact in self.contacts:
            print(f"Contact {contact.name}  Num Tel: {contact.num_tel}  adress: {contact.adress}")

Manager=ContactManager()


def system():
    print("welcome to the contact manager")
    while True:
        print("""
            Add contact
            Search contact
            Update contact
            Delete contact
            Show contacts
            Save contacts
            Load contacts
""")
        operation=input("Choose an operation:")
        if operation==1:
            contact_name=input("enter the name of the contact you want to add: ")
            num_tel=input("enter the phone number of the contact")
            adresse=input("enter the adress of the contact: ")
            Manager.add_contact(contact_name,num_tel,adresse)

        elif operation==2:
            contact_name=input("enter the contact name: ")
            Manager.search_contact(contact_name)

        elif operation==3:
            contact_name=input("enter the contact name: ")
            Manager.delete_contact(contact_name)

        elif operation==4:
            Manager.show_contacts()
        else:
            break
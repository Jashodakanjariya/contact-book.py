import json
contacts=[]
def save_contacts():
    with open("contacts.json","w") as file:
        json.dump(contacts,file)
def load_contacts():
    global contacts
    try:
        with open("contacts.json","r") as file:
            contacts=json.load(file)
    except FileNotFoundError:
        contacts=[]

load_contacts()

while True:

    print("------ Contact Book ------")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Update Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice=="1":
     print("Add contacts")
     name=input("enter name: ")
     phone=input("enter phone number: ")
     email=input("enter email: ")

     contact={
         "name":name,
         "phone":phone,
         "email":email

     }
     contacts.append(contact)
     save_contacts()
     print(contact)
     print("contact added sucessfully")

    elif choice=="2":
         if len(contacts)==0:
          print("no contact found")
         else:
            print("-----view contact------")
             
            for contact in contacts:
                print("name : ",contact["name"])
                print("phone : ",contact["phone"])
                print("email : ",contact["email"])
            print()
            
    elif choice=="3":

                 
                 
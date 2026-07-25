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
        search_name=input("enter  name :")
        found=False
        for contact in contacts:
         if contact["name"]==search_name:
            found=True
            print("contact founded")
            print("name :",contact["name"])
            print("phone :",contact["phone"])
            print("email :",contact["email"])
            break
        if found==False:
            print("contact not found")

    elif choice=="4":
        delete_contact=input("enter name to delete:")
        found=False
        for contact in contacts:
            if contact["name"]==delete_contact:
                found=True
                contacts.remove(contact)
                save_contacts()
                print("contact deleted successfully")
                break
            

    elif choice=="5":
        update_name=input("enter name to updatea")
        found=False
        for contact in contacts:
            if contact["name"]==update_name:
                found=True
                new=input("enter updated name :")
                contact["name"]=new
                save_contacts()
                print(update_name,"updated successfully")
                break
        if found==False:
          print("contact not founded")

    elif choice=="6":
        print("thank you")
        save_contacts()
        break
    
    else:
        print("invalid choice")
print("contact book version 2")

                 
                 
import json
students=[]
def save_students():
    with open("students.json","w") as file:
        json.dump(students,file)

def load_students():
    global students
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []
        
load_students()
while True:
    print("1.add ")
    print("2.view ")
    print("3.search ")
    print("4.delete")
    print("5.update")
    print("6.exit")
    
    choice = input("Enter your choice: ")
    

    if choice == "1":
        print("add student")
        name=input("enter name:")
        age=int(input("enter age:"))
        city=input("enter city:")

        student={
         "name":name,
         "age":age,
         "city":city
        }
        students.append(student)
        save_students()
        print(students)

    elif choice == "2":
        print("view student")
        print("-------student details--------")
        
        for student in students:
            print("name:",student["name"])
            print("age:",student["age"])
            print("city:",student["city"])
        print()

    elif choice == "3":
        print("search student")
        search_name=input("enter student name:")
        found=False
        for student in students:
            if student["name"]==search_name:
                found=True
                print("student found")
                print("name:",student["name"])
                print("age:",student["age"])
                print("city:",student["city"])
        if found==False:
         print("student not found")

        print()

    elif choice == "4":
        print("delete student")
        delete_name=input("enter student name to delete")
        found=False
        for student in students:
            if student ["name"]==delete_name:
                found=True
                students.remove(student)
                save_students()
                print("student deleted")
                break
        if found==False:
            print("student not found")

    elif choice == "5":
        print("update student")
        update_name= input("enter student name to update:")
        found=False
        for student in students:
            if student["name"]==update_name:
             found=True
             new=input("enter your city:")
             student["city"]=new
             new=input("enter your name")
             student["name"]=new
             new=int(input("enter age:"))
             student["age"]=new
             save_students()
             print(update_name," updated sucessfully")
             break
        if found==False:
            print("student not found")

    elif choice == "6":
        print("thank you")
        break
    else:
      print("invalid choice") 
import json
expenses=[]
def save_expenses():
   with open("expenses.json","w") as file:
      json.dump(expenses,file)
def load_expenses():
   global expenses
   try:
    with open("expenses.json","r") as file:
       expenses=json.load(file)
   except FileNotFoundError:
      expenses=[]
      
      
load_expenses()
while True:
  print("------- expense tracker--------")
  print("1.add expense")
  print("2.view expense")
  print("3.total expense")
  print("4.search expense")
  print("5.delete expense")
  print("6.update expense")
  print("7.exit")
  choice=input("enter your choice")

  if choice =="1":
    print("enter your expense")
    Category=input("enter category :")
    Amount=int(input("enter amount :"))
    Date=(input("enter date :"))
    expense={
      "Category":Category,
      "Amount":Amount,
      "Date":Date
    }
    expenses.append(expense)
    save_expenses()
    print(expenses)
    print("expense added sucessfully")


  elif choice=="2":
    if len(expenses) == 0:
        print("No expenses found.")

    else:
        print("------ Expense Details ------")
    
        for expense in expenses:
         print("Category :",expense["Category"])
         print("Amount :",expense["Amount"])
         print("Date :",expense["Date"]) 
        print()


  elif choice=="3":
     print("Total Amount")
     total=0
     for expense in expenses:
        total = total + expense["Amount"]
     print(total)

     
  elif choice=="4":
     print("search expense")
     search_category=input("enter category")
     found=False
     for expense in expenses:
      if expense["Category"]==search_category:
        found=True
        print("expense found")
        print("Category :",expense["Category"])
        print("Amount :",expense["Amount"])
        print("Date :",expense["Date"]) 
        break
     print()
     if found==False:
        print("not found")


  elif choice=="5":
     delete_category=input("enter category to delete")
     found=False
     for expense in expenses:
         if expense["Category"]==delete_category:
          found=True  
          expenses.remove(expense) 
          save_expenses()
          print("Expense Deleted") 
          break
     if found==False:
      print("expense not found")

  elif choice=="6":
     update_category=input("enter category to update")
     found=False
     for expense in expenses:
        if expense["Category"]==update_category:
           found=True
           new_amount=int(input("Enter new amount: "))
           expense["Amount"]=new_amount
           save_expenses()
           print(update_category," updated sucessfully")
           break
     if found==False:
        print("expense not found")


  elif choice=="7":
     print("Thank You ")
     save_expenses()
     break
  
  else:
     print("invalid choice")
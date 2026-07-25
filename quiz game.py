import json
questions=[]

def save_questions():
    with open("questions.json","w") as file:
        json.dump(questions,file)
def load_questions():
    global questions
    try:
     with open("questions.json","r") as file:
        questions=json.load(file)
    except FileNotFoundError:
       print("file not exist")
       questions=[]


questions=[
   {
   "question":"what is python",
  "options": {
    "A": "Programming Language",
    "B": "Browser",
    "C": "Database",
    "D": "OS"
    },
    "answer":"A"
},
{
   "question":"what is chrome",
   "options": {
    "A": "Programming Language",
    "B": "Browser",
    "C": "Database",
    "D": "OS"},
    "answer":"B"
}
]
score=0
for question in questions:
   print(question["question"])
   for key,values in question["options"].items():
      print(key,":",values)
   check=input("enter your answer : ").upper()
   if question["answer"]==check:
      print("Correct answer")
      score+=1
      print("Your Score Is :",score)
   else:
      print("Wrong answer")
      print("Correct answer:",question["answer"], "-",question["options"][question["answer"]])
      print("Your Score Is :",score)

print("\n------ Quiz Finished ------")
print("Final Score:", score, "/", len(questions))

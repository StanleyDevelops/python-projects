# Quizz App

list_of_quest = [
  {
    "question": "What is the capital of India?",
    "options": ["A. Mumbai", "B. Delhi", "C. Pune", "D. Chennai"],
    "answer": "B"
  },
  {
      "question": "Which is the pink city?",
      "options": ["A. Delhi", "B.Mumbai", "C.Jaipur", "D.Kolkata"],
      "answer": "B"
    },
   {
       "question": "Which city is Leading in Technology?",
       "options": ["A. Mumbhai", "B.Hyderbad", "C. Delhi", "4. Bangluru"],
       "answer": "D"
   },
   {"question": "Which is most Expensive city?",
    "options": ["A. Mumbai", "B.Delhi", "C. Kanpur", "D.Chennai"],
    "answer": "A"
    },
    {
        "question": "Which is famous for its beaches?",
        "options": ["A. Kocchi", "B. Goa", "C. Ahmedabad", "D.Chennai"],
        "answer": "B" 
    },
    {
        "question": "Which is the spiritual hub?",
        "options": ["A. Prayagraj", "B. Pune", "C. Varanasi", "D. Haridwar"],
        "answer": "C"
    },
    {
        "question": "Which is city of pearls?",
        "options": ["A. Hyderabad", "B. Chennai", "C: Lucknow", "D. Dehradun"],
        "answer": "A"
    },
    {
        "question": "Which is Considered Manchester of the East?",
        "options": ["A. Goa", "B. Ahmedabad", "C. Jaipur", "D. Punjab"],
        "answer": "B",
    },
    {
    "question": "Where is Dal lake?",
    "options": ["A. Mussoorie", "B. shrinagar", "C. Nainital", "D. Shimla" ],
    "answer": "B"
    },
    {
        "question": "Which city is known as Detroit of India?",
        "options": ["A. Delhi", "B. Mumbai", "C. Pune", "D. Chennai"],
        "answer": "D"
    }
]


high_score = -1
stay = True
while stay:
    print("===============The QUIZ of Cities==============")
    print("---------------MENU---------------")
    print("1. Start Quiz")
    print("2. View High Score")
    print("3. Quit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Wrong Input!")
        continue

    if choice == 1:
        score = 0
        for set_of_quest in list_of_quest:
                print(f"{set_of_quest["question"]}")
                print(f"{set_of_quest["options"]}")
                try:
                    user_answer = input("Enter you answer: ").lower().strip()
                except ValueError:
                    print("Please enter correct option!")
                    continue
                if user_answer == set_of_quest["answer"].lower():
                    print("Correct Answer. You are Genius!!")
                    score += 1
                else:
                    print("Wrong Answer!!")
            
        if score > high_score:
            high_score = score
        
        print("The Quiz Completed")
        print(f"Your Score is {score} of 10.")
        print(f"High score: {high_score}")

    elif choice == 2:
        print(f"The High score is: {high_score}")

    elif choice == 3:
        print("Happy Quiz..")
        print("Exiting...")
        stay = False


        



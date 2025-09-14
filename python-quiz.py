def quiz():
    
    print("Welcome To The QUIZ!!")
    
    playing = input("Do You Want to Play? (Yes/No):")
    if playing.lower() != "yes":
        print("Maybe next time!")
        return
        
    print("Okay! Let's Play :)")
    score = 0

    answer = input("1. Who Created the Python Programming Language? ")
    if answer.lower() == "guido van rossum":
        print("Correct")
        score += 1
    else:
        print("Incorrect Answer")

    answer = input("2. What is the output of print(2 ** 3)? ")
    if answer == "8":
        print("Correct")
        score += 1
    else:
        print("Incorrect Answer")

    answer = input("3. What keyword is used to define a function in Python? ")
    if answer.lower() == "def":
        print("Correct")
        score += 1
    else:
        print("Incorrect Answer")

    answer = input("4. What is the correct file extension for Python files? ")
    if answer.lower() == ".py":
        print("Correct")
        score += 1
    else:
        print("Incorrect Answer")

    answer = input("5. What data type is used to store text in Python? ")
    if answer.lower() == "str":
        print("Correct")
        score += 1
    else:
        print("Incorrect Answer")

    answer = input("6. What will be the output of: print(len('Python'))? ")
    if answer == "6":
        print("Correct")
        score += 1
    else:
        print("Incorrect Answer")

    answer = input("7. Which operator is used for floor division in Python? ")
    if answer == "//":
        print("Correct")
        score += 1
    else:
        print("Incorrect Answer")

    answer = input("8. What is the output of: print(type(42))? ")
    if answer.lower() == "<class 'int'>":
        print("Correct")
        score += 1
    else:
        print("Incorrect Answer")

    answer = input("9. Which of the following is a mutable data type in Python? (int, list, str, tuple) ")
    if answer.lower() == "list":
        print("Correct")
        score += 1
    else:
        print("Incorrect Answer")

    answer = input("10. What Keyword is used to define a class in Python? ")
    if answer.lower() == "class":
        print("Correct")
        score += 1
    else:
        print("Incorrect Answer")
        
    print(f"You got {score} out of 10 Questions Correct.")
    print(f"Your score: {(score / 10) * 100:.2f}%")

quiz()

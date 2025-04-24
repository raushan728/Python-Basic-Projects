def run_quiz(questions):
    score = 0

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        valid_inputs = [opt.split(".")[0].strip().lower() for opt in q["options"]]
        valid_values = [opt.split(".")[1].strip().lower() for opt in q["options"]]
        valid_answers = valid_inputs + valid_values

        while True:
            answer = input("Your answer: ").strip().lower()
            if answer in valid_answers:
                break
            else:
                print("❌ Invalid input. Please enter a valid option (e.g., 'b' or '8').")

        correct_answer = q["answer"].strip().lower()
        correct_value = None

        # Find correct value from options using letter
        for opt in q["options"]:
            if opt.lower().startswith(correct_answer + "."):
                correct_value = opt.split(".")[1].strip().lower()
                break

        if answer == correct_answer or answer == correct_value:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was: {correct_answer.upper()}")

    total = len(questions)
    print("\n🎯 You got", score, "out of", total, "correct.")
    print("📊 Your score:", (score / total) * 100, "%")



questions_list = [
    {
        "question": "Q1: What is the output of print(2 ** 3)?",
        "options": ["a. 6", "b. 8", "c. 9", "d. 5"],
        "answer": "b",
    },
    {
        "question": "Q2: Who developed Python?",
        "options": [
            "a. Dennis Ritchie",
            "b. James Gosling",
            "c. Guido van Rossum",
            "d. Bjarne Stroustrup",
        ],
        "answer": "c",
    },
    {
        "question": "Q3: What data type is used to store True or False?",
        "options": ["a. int", "b. str", "c. bool", "d. float"],
        "answer": "c",
    },
    {
        "question": "Q4: Which keyword is used for loops in Python?",
        "options": ["a. loop", "b. for", "c. iterate", "d. repeat"],
        "answer": "b",
    },
    {
        "question": "Q5: Which symbol is used for comments in Python?",
        "options": ["a. //", "b. <!-- -->", "c. #", "d. /* */"],
        "answer": "c",
    },
    {
        "question": "Q6: Which language is primarily used for Android app development?",
        "options": ["A. Python", "B. Kotlin", "C. Swift", "D. JavaScript"],
        "answer": "B",
    },
    {
        "question": "Q7: What is the square root of 81?",
        "options": ["A. 8", "B. 9", "C. 7", "D. 6"],
        "answer": "B",
    },
    {
        "question": "Q8: What does HTML stand for?",
        "options": [
            "A. Hyperlinks and Text Markup Language",
            "B. Home Tool Markup Language",
            "C. Hyper Text Markup Language",
            "D. Hyperlinking Text Markdown Language",
        ],
        "answer": "C",
    },
    {
        "question": "Q9: Which of the following is a Python data type?",
        "options": ["A. integer", "B. string", "C. list", "D. All of the above"],
        "answer": "D",
    },
    {
        "question": "Q10: What symbol is used to comment a single line in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. /* */"],
        "answer": "C",
    },
    {
        "question": "Q11: In Java, which keyword is used to inherit a class?",
        "options": ["A. extends", "B. implements", "C. inherit", "D. super"],
        "answer": "A",
    },
    {
        "question": "Q12: What does CSS stand for?",
        "options": [
            "A. Color Style Sheets",
            "B. Creative Style Sheets",
            "C. Cascading Style Sheets",
            "D. Computer Style Sheets",
        ],
        "answer": "C",
    },
    {
        "question": "Q13: What is the output of: print(2 ** 3) in Python?",
        "options": ["A. 6", "B. 8", "C. 9", "D. 5"],
        "answer": "B",
    },
    {
        "question": "Q14: What is the default port for HTTP?",
        "options": ["A. 443", "B. 21", "C. 80", "D. 22"],
        "answer": "C",
    },
    {
        "question": "Q15: Which of the following is used to define a function in Python?",
        "options": ["A. func", "B. function", "C. define", "D. def"],
        "answer": "D",
    },
    {
        "question": "Q16: What is the time complexity of binary search?",
        "options": ["A. O(n)", "B. O(log n)", "C. O(n log n)", "D. O(1)"],
        "answer": "B",
    },
    {
        "question": "Q17: Which language is primarily used for machine learning?",
        "options": ["A. C++", "B. HTML", "C. Python", "D. SQL"],
        "answer": "C",
    },
    {
        "question": "Q18: Which keyword is used to create a class in Python?",
        "options": ["A. def", "B. function", "C. class", "D. object"],
        "answer": "C",
    },
    {
        "question": "Q19: What does IDE stand for?",
        "options": [
            "A. Integrated Design Environment",
            "B. Internal Development Editor",
            "C. Integrated Development Environment",
            "D. Intelligent Development Engine",
        ],
        "answer": "C",
    },
    {
        "question": "Q20: In Python, which of the following is used to handle exceptions?",
        "options": ["A. try-except", "B. catch-finally", "C. do-while", "D. if-else"],
        "answer": "A",
    },
]

print("Welcome to the Python Quiz!")
run_quiz(questions_list)

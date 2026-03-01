# Quiz game with dictionaries
print("=== Quiz Game ===\n")

# Quiz questions (list of dictionaries)
questions = [
    {
        "question": "What is 5 + 3?",
        "answer": "8",
        "difficulty": "easy"
    },
    {
        "question": "What is the capital of France?",
        "answer": "paris",
        "difficulty": "easy"
    },
    {
        "question": "How many days in a week?",
        "answer": "7",
        "difficulty": "easy"
    },
    {
        "question": "what is the name of the user?",
        "answer": "Mr. Mohamed",
        "difficulty": "medium"
    },
    {
        "question": "What is 10 * 2?",
        "answer": "20",
        "difficulty": "easy"
    },
    {
        "question": "What color is the sky on a clear day?",
        "answer": "blue",
        "difficulty": "easy"
    },
    {
        "question": "What programming language are we learning?",
        "answer": "python",
        "difficulty": "medium"
    },
    {
        "question": "How many months are in a year?",
        "answer": "12",
        "difficulty": "medium"
    }
]

def run_quiz(quiz_questions):
    score = 0
    wrong_questions = []
    
    for i, q in enumerate(quiz_questions, 1):
        attempts = 0
        correct = False
        while attempts < 2:
            print(f"\nQuestion {i}: {q['question']}")
            user_answer = input("Your answer: ")
            attempts += 1
            
            if user_answer.lower() == q['answer'].lower():
                print("✓ Correct!")
                score += 1
                correct = True
                break
            else:
                print(f"✗ Wrong! Answer was: {q['answer']}")
           
        if attempts == 2 and not correct:
            wrong_questions.append(q)

    if wrong_questions:
        print("\nQuestions you got wrong:")
        for q in wrong_questions:
            print(" - ", q["question"])
    
    return score

# Run the quiz
final_score = run_quiz(questions)

print(f"\n--- Results ---")
print(f"Score: {final_score}/{len(questions)}")
percentage = (final_score / len(questions)) * 100
print(f"Percentage: {percentage:.1f}%")

if percentage >= 80:
    print("Grade: Excellent!")
elif percentage >= 60:
    print("Grade: Good")
else:
    print("Grade: Needs improvement")
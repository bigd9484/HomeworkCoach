

```python
# main.py

import os
import json
import openai

# Load your OpenAI API key from env
openai.api_key = os.getenv("OPENAI_API_KEY", "")

def load_assignments(path="school_portal.json"):
    """Load mock assignment data from a JSON file."""
    with open(path, "r") as f:
        return json.load(f)

def breakdown_steps(assignment):
    """
    Use an LLM to break an assignment into step-by-step instructions.
    Replace 'gpt-4' with your preferred model or Claude endpoint.
    """
    prompt = (
        f"Break down this assignment into clear, actionable steps:\n\n"
        f"Title: {assignment['title']}\n"
        f"Description: {assignment['description']}\n\n"
        "Steps:\n"
    )
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
    )
    # Extract the assistant's reply
    return response.choices[0].message.content.strip()

def quiz_student():
    """
    Simulate a simple math quiz. In a real build, swap in a local NIM model or
    more advanced logic. Here we ask a basic multiplication question.
    """
    import random
    a, b = random.randint(1, 12), random.randint(1, 12)
    answer = a * b
    guess = int(input(f"\nQuiz: What is {a} × {b}? "))
    if guess == answer:
        print("✅ Correct!")
    else:
        print(f"❌ Not quite. The answer is {answer}.")

def main():
    print("\n🎓 Welcome to HomeworkCoach!\n")
    assignments = load_assignments()
    # List available assignments
    for a in assignments:
        print(f"{a['id']}. [{a['subject']}] {a['title']}")
    choice = int(input("\nEnter assignment number to review: "))
    
    selected = next((a for a in assignments if a["id"] == choice), None)
    if not selected:
        print("❌ Invalid choice—exiting.")
        return

    print(f"\n🔍 Breaking down: {selected['title']}\n")
    steps = breakdown_steps(selected)
    print(steps)

    while True:
        cont = input("\nDo you want a quick math quiz? (y/n): ").strip().lower()
        if cont == "y":
            quiz_student()
        else:
            print("\n👍 All done! Happy studying.")
            break

if __name__ == "__main__":
    main()

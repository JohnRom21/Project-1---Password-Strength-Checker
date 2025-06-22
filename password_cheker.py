import re

def check_password_strength(password):
    score = 0
    feedback = []
    # Define QWERTY keyboard sequences
    letter_sequence = "qwertyuiopasdfghjklzxcvbnm"
    number_sequence = "1234567890"
    
    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    # Check uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")
    # Check lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")
    # Check numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")
    # Check special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$%^&*).")
    # Check for three or more consecutive identical characters
    if not re.search(r"(.)\1{2,}", password):
        score += 1
    else:
        feedback.append("Password should not contain three or more consecutive identical characters (e.g., 'aaa' or '111').")
    # Check for three or more raising/falling characters
    has_sequence = False
    lower_password = password.lower()
    for i in range(len(lower_password) - 2):
        substring = lower_password[i:i+3]
        # Check letters
        if all(c in letter_sequence for c in substring):
            forward = letter_sequence.find(substring[0]) < letter_sequence.find(substring[1]) < letter_sequence.find(substring[2])
            backward = letter_sequence.find(substring[0]) > letter_sequence.find(substring[1]) > letter_sequence.find(substring[2])
            if forward or backward:
                has_sequence = True
                break
        # Check numbers
        if all(c in number_sequence for c in substring):
            forward = number_sequence.find(substring[0]) < number_sequence.find(substring[1]) < number_sequence.find(substring[2])
            backward = number_sequence.find(substring[0]) > number_sequence.find(substring[1]) > number_sequence.find(substring[2])
            if forward or backward:
                has_sequence = True
                break
    if not has_sequence:
        score += 1
    else:
        feedback.append("Password should not contain three or more consecutive characters in keyboard order (e.g., 'qwe', '123', 'edc').")
    
    # Determine strength
    if score >= 7:
        return "Strong password!", feedback
    elif score >= 4:
        return "Moderate password.", feedback
    else:
        return "Weak password.", feedback

# Get user input and run until a strong password is provided or user quits
while True:
    password = input("Enter a password to check (or 'quit' to exit): ")
    if password.lower() == 'quit':
        print("Exiting password checker.")
        break
    strength, feedback = check_password_strength(password)
    print(f"Password Strength: {strength}")
    if feedback:
        print("Suggestions to improve:")
        for suggestion in feedback:
            print(f"- {suggestion}")
    if strength == "Strong password!":
        print("Password accepted!")
        break
    else:
        print("Password does not meet all requirements. Please try again or type 'quit' to exit.")
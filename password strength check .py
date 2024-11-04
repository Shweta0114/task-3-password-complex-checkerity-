import re

def assess_password_strength(password):
    score = 0

    # Check length
    if len(password) >= 12:
        score += 1

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1

    # Check for numbers
    if re.search(r"\d", password):
        score += 1

    # Check for special characters
    if re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", password):
        score += 1

    # Provide feedback based on the score
    if score == 5:
        return "Strong password!"
    elif score >= 3:
        return "Medium password. Consider adding more complexity."
    else:
        return "Weak password. Please try again."

# Test the function
password = input("Enter a password: ")
print(assess_password_strength(password))
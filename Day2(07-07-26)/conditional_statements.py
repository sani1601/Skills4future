score = 85

# if statement
if score > 70:
    print(f"Score ({score}): Good effort!")

# if-else statement
if score >= 90:
    print(f"Score ({score}): Excellent!")
else:
    print(f"Score ({score}): Keep practicing.")

# if-elif-else statement
grade = 'B'
if grade == 'A':
    print("Grade A: Outstanding!")
elif grade == 'B':
    print("Grade B: Very good!")
elif grade == 'C':
    print("Grade C: Pass.")
else:
    print("Grade: Needs improvement.")

# Nested if-else statement
attendance = 92
is_project_submitted = True

if attendance >= 90:
    if is_project_submitted:
        print(f"Attendance ({attendance}), Project Submitted: Eligible for final exam.")
    else:
        print(f"Attendance ({attendance}), Project Not Submitted: Submit project to be eligible.")
else:
    print(f"Attendance ({attendance}): Not eligible for final exam due to low attendance.")

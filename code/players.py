users = ['charles', 'ROB', 'mike', 'chris', 'adam']
new_users = ['jane', 'Rob', 'Mike', 'jenny', 'glerk']

users_lower = [user.lower() for user in users]

for new_user in new_users:
    if new_user.lower() in users_lower:
        print(f"{new_user} has already been chosen.")
    else:
        print(f"{new_user} is available.")

numbers = range(1, 11)
for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")


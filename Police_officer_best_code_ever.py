drivers_license = input("This is the police! Do you have your drivers license? ").lower()

if drivers_license == 'yes':
    print("Ok, you're good to go")
elif drivers_license == 'no':
    print("You're gonna have to come with us")
else:
    print("You're under arrest for not responding to police")

abuse_keyword = ["shit", "retard", "asshole", "stupid", "idiot"]

user_input = input("Enter a word: ").lower()

if user_input in abuse_keyword:
    print('You are under arrest for abusing a police officer')

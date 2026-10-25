drivers_liscense = input ("This is the police! Do you have your drivers license?")
if drivers_liscense == 'yes':
    print("Ok, you're good to go")

abuse_keyword = ["shit", "retard", "asshole"]

if drivers_liscense == 'no':
       print("You're gonna have to come with us")

if drivers_liscense != 'yes' and drivers_liscense != 'no':
        print("You're under arrest for not responding to police")


abuse_keyword = 'abuse'
user_input = input("Enter a word: ") 

if user_input == abuse_keyword:
    print('You are under arrest for abusing a police officer')

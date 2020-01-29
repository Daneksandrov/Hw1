db = {'Danya':'1234', 'Anya':'123'}
user_name = str(input('Enter your username: '))
user_pass = str(input('Enter your password: '))
for i in db.keys():
    if user_name == i:
        while True:
            if user_pass == db.get(i):
                print("Password for user: ", i, "is correct")
                break
            else:
                print("Password for user: ", i," is incorrect")
                print("Please try again...")
                user_pass = str(input('Enter your password: '))

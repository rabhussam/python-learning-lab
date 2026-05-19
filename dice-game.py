# The beauty of function is the fact that you can easily
# execute the whole code with a word ------ app(x, y, z) ------- the functions name is def app(x,y,z)

def app(username, email):
    print(f"Hello, {username}!")
    print(f"Can you confirm your email is {email}?")
    return

while True:
    usr = input('Enter your username: ')
    pas = input('Enter your password: ')
    ema = input('Enter your email: ')

    app (usr, ema)
    verify = input("Verify your info? (y/n): ").lower()
    if verify == 'y':
        print(f"Welcome back, {usr}!")
        break
    else:
        print("Lets try that again then!")


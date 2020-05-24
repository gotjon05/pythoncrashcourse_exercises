usernames = ['admin', 'guest', 'guest1', 'guest2']




for account in usernames:
    if account == 'admin':
        print("Hello Admin would you like to see a status report")
        break
    else:
        print("hello, thank you for logging in today")

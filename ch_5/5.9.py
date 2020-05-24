


usernames = []

if usernames:
    for account in usernames:
        if account == 'admin':
            print("Hello Admin would you like to see a status report")
            break
        else:
            print("hello, thank you for logging in today")
else:
    print("empty list")

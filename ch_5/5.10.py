current_users = ['jan_g', 'robert_galballs', 'John']
new_users = ['JOHN', 'robert_galballs', 'bob_jansen', 'larry_summers']

current_users_lower = [user.lower() for user in new_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(new_user + " username is taken")
    else:
        print("username " + new_user + " is available")


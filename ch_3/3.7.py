
guest = ['bob', 'fanny', 'larson', 'paul', 'boobie']
print("welcome "+ guest[0])
print("welcome "+ guest[1])
print("welcome "+ guest[2])
print("welcome "+ guest[3])
print("welcome "+ guest[4])


print(guest[1] + " cannot make it")

guest[1] = 'larry'
print("welcome "+ guest[0])
print("welcome "+ guest[1])
print("welcome "+ guest[2])
print("welcome "+ guest[3])
print("welcome "+ guest[4])


print("we found a bigger table")

guest.insert(0, 'robert')
guest.insert(2, 'jenkins')
guest.append('todd')

print("welcome "+ guest[0])
print("welcome "+ guest[1])
print("welcome "+ guest[2])
print("welcome "+ guest[3])
print("welcome "+ guest[4])
print("welcome "+ guest[5])
print("welcome "+ guest[6])
print("welcome "+ guest[7])

print("we can only invite two people for dinner")

dropped = guest.pop()
print("i am sorry " + dropped + " we cannot invite you to dinner at this time")
dropped = guest.pop()
print("i am sorry " + dropped + " we cannot invite you to dinner at this time")
dropped = guest.pop()
print("i am sorry " + dropped + " we cannot invite you to dinner at this time")
dropped = guest.pop()
print("i am sorry " + dropped + " we cannot invite you to dinner at this time")
dropped = guest.pop()
print("i am sorry " + dropped + " we cannot invite you to dinner at this time")
dropped = guest.pop()
print("i am sorry " + dropped + " we cannot invite you to dinner at this time")
print(guest[1] + " and " + guest[0] + " your still on the list")


del guest[1]
del guest[0]

print(guest)

















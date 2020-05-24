rivers = { 'nile': 'egypt', 'amazon':'brazil','nile':'egypt','delta':'USA'}

for key,value in sorted(rivers.items()):
    print(key + str(value))


for river in sorted(rivers.keys()):
    print(river)
for country in sorted(rivers.values()):
    print(country)

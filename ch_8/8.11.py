magicians = ['bob', 'stu the brave', 'elmer', 'larry the drunken clown', 'sad larry']

def show_magicians(magicians):
    print(magicians)


#any changes made to a list inside the functions body are permenant 
def make_great(magicians):
    i = 0;
    while i < len(magicians):
        #changes the str object pointed to by magicians and modifies
        magicians[i] = "The great " + magicians[i].title()
        i += 1


    #with_title = "The great " + magicians  -- tried to concatenate str to list
    #magician = magicians.pop
    #with_title = "The great " + magician
    #magicians.append(with_title)
    #return magicians

#passing function a copy of the list, not the orginal 
print(make_great(magicians[:]))

magic = show_magicians(magicians)
print(magic)



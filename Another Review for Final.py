place_holder = "The small brown fox jumps over the fence"
print(place_holder)
newlist = place_holder.split() # split method converts a string to a list. It is doing so by finding all the spaces
newstring = newlist[2:4]
newstring = ' '.join(newlist[2:4])
print(newstring)
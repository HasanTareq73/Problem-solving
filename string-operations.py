astring = "string operations"
print("single quotes are ' '")

print(len(astring))

print(astring.index("o"))

print(astring.index("t"))



print(astring.count("i"))



print (astring[6:11]) #start from 7no word to 11 no word.

print(astring[7:15:2]) #start from 8no word to 15 no word and skip 9,11,13,15no word 


print(astring[::-1]) #reverse word




print(astring.upper()) #uppercase
print(astring.lower()) #lowercase




print(astring.startswith("strings"))  ##if this sentence is start with this word then output is true otherwise false
print(astring.endswith("operations")) ## if this sentence is end with this word then output is true otherwise false



afewwords = astring.split(" ") # this splits the string into a bunch of strings grouped together in a list

print(afewwords)
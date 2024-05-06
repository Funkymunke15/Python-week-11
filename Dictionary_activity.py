# Davis Arita
# 11/9/22
# CS 131 Dictionary activity
# creating and using a dictionary

myDictionary = {}
print("The length of the dictionary is", len(myDictionary))
anotherDictionary = {"May": 2145523, "Cory": 3559912, "Sara": 4329898}

myDictionary["Alan"] = 4533344
myDictionary["Khoi"] = 334233

anotherDictionary["Ellen"] = 4349098

print("The length of the dictionary is", len(myDictionary))
print("The length of the dictionary is", len(anotherDictionary))

print("May's number is ", anotherDictionary["May"])

for key in anotherDictionary:
    print("key:", key)
    #print(key)
    print("value:", anotherDictionary[key])
    #print(anotherDictionary[key])

anotherDictionary.pop("Sara")
ellenNumber = anotherDictionary.pop("Ellen")

print("The popped number was: ", ellenNumber)

print("*" * 40)
print("My contacts:")
for key in sorted(anotherDictionary):
    print("%-10s %d" % (key, anotherDictionary[key]))

anotherDictionary["Cory"] = 5551234
print("Another way to iterate and print")
for item in anotherDictionary.items():
    print(item[0], item[1])

#Dictionaries are ordered collection of data item.They store multiple items in a single variable.
#They are enclosed within curly brackets.
dic={"Harry":"Human being","Spoon":"Object"}
print(dic["Harry"])
print(dic.keys())
print(dic.values())

for key in dic.keys():
    print(dic[key])

for key, value in dic.items():
    print(f"The value corresponding to the key {key} is {value}")
    

spam={'color':"red","price":"42"}
print("I have"+spam.get('price')+'price')
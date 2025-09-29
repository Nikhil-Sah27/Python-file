std1={"Nikhil":91,"Suyash":98,"Sujal":89,"Aadarsh":88}
std2={"Nishan":94,"Manish":85}
std1.update(std2)
print(std1)
# std2.clear()
# print(std2)
std1.pop("Nikhil")
print(std1)

std1.popitem() 

del std1["Nishan"]
print(std1)
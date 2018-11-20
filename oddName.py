"""My Name is KPhoo"""
name=input("Enter name: ")
while len(name) <1:
    print("Enter charater: ")
    name=input("enter name: ")
for i in range(0,len(name),2):
    print(name[i])
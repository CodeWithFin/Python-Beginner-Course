name = input("Write your name here : ")
if len(name) < 3:
    print("Name should be at least 3 characters long")
elif len(name) > 50 :
    print("name can be a maximum of 50 characters")
else:
    print("Name looks good")
weight = int(input("Weight: "))
weight_symbol = input("(L)bs or (K)g: ").lower()

if weight_symbol == "l":
    user_weight = weight * 0.45 
    print(f'You are {user_weight} Kilos')
elif weight_symbol == "k":
    user_weight = weight / 0.45 
    print(f'You are {user_weight} Pounds')

else:
    print("invalid input")



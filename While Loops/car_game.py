command = ""
while True:
    command = input("> ").lower()
    if command == 'start':
        print('the car has started ... ready to go! ')
        

    elif command =='stop':
        print('car stopped...')
    elif command == "help":
        print("""  
start - to start the car
stop - to stop the car
quit - to quit
    
              """)
    elif command =='quit':
        break
    else:
        print("Sorry, I don't understand this")
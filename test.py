userCommand = input("")
start = "Car started, ready to go!"
stop = 'Car stopped'


if(userCommand == 'help'):
    print("start - to start the car")
    print("stop - to stop the car")
    print("quit - to exit")
elif(userCommand == 'start'):
    print('Car started, ready to go!')
elif(userCommand == 'stop'):
    print('Car stopped')
elif(userCommand == 'quit'):
    pass
else:
    print("I don't understand that")

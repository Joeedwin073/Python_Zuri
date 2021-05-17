command = ''

while True:
    command = input("> ").lower()
    if command == 'start':
        print('Car started... Ready to go')
        command = input("> ").lower()
        if command == 'start':
            print('Car already started!')
        else:
                break
    elif command == 'stop':
        print('Car stopped')
        command = input("> ").lower()
        if command == 'stop':
            print('Car is off!')
        else:
                break
    elif command == 'help':
        print("""
start - start the car
stop - stop the car
quit - exit
    """)
    elif command == 'quit':
        break
    else:
        print("I don't understand that")
    
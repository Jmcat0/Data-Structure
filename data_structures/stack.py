undo_stack = []
redo_stack = []

text = ""

while True:
    choice = input(f"Your text is: {text} Enter command: type/undo/redo/quit")

    if choice == 'type':
        undo_stack.append(text)
        text = input('Enter text: ')
        print(undo_stack,redo_stack,'asdasdasd')
    elif choice == 'undo':
        if len(undo_stack) > 0:
            redo_stack.append(text)
            text = undo_stack.pop()
            print(undo_stack,redo_stack,'asdasdasd')
        else:
            print('Nothing to undo')
    elif choice == 'redo':
        if len(redo_stack) > 0:
            undo_stack.append(text)
            text = redo_stack.pop()
            print(undo_stack,redo_stack,'asdasdasd')
        else:
            print('Nothing to redo')
    elif choice == 'quit':
        break
    else:
        print('Please enter a valid command')

with open('mouse_log.txt', 'r') as fh:
    L = fh.readlines()
    new = []
    press = False
    for action in L[1:]:
        temp = action.split(',')
        # print(temp)
        if temp[3] == ' Pressed\n':
            press = True
        if press and temp[3] == ' Moved\n':
            temp[3] = ' Drag\n'
        if temp[3] == ' Released\n':
            press = False
        new.append(','.join(temp))
    with open('new_mouse_log.txt', 'w') as fh2:
        fh2.writelines(new)

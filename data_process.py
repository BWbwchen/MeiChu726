with open('mouse_log.txt', 'r') as fh:
    L = fh.readlines()
    # print(L)
    new = []
    press = False
    offset = float(L[1].split(',')[0])
    # print(offset)
    for action in L[1:]:
        temp = action.split(',')
        # print(temp[0])
        temp[0] = str(float(temp[0]) - offset)
        if temp[3] == ' Pressed\n':
            press = True
        if press and temp[3] == ' Moved\n':
            temp[3] = ' Drag\n'
        if temp[3] == ' Released\n':
            press = False
        new.append(','.join(temp))
    with open('new_mouse_log.txt', 'w') as fh2:
        fh2.writelines(new)

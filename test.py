from getkey import getkey, keys

while True:
    k = getkey(blocking=False)
    if len(k) > 0:
        if len(k) == 1:
            if keys.name(k) == "ESC":
                break
            print(k)
        else:
            print(keys.name(k))

def c_area(w = 0, h = 0):
    return w * h

def c_plus(x = 0, y = 0):
    return x + y

def c_checkgrade(n):
    for a in n:
        if type(a) == int:
            if a > 9:
                print(a, 'A')
            elif a >= 5:
                print(a, 'B')
            else:
                print(a, 'F')
        else:
            print(a, 'not acceptable')








def calculator(exp):
    exp = exp.replace(" ", "")

    # noinspection PyBroadException
    try:
        for e in exp:
            if e not in "1234567890+-x/().":
                exit()
    except:
        print("Error:is not acceptable ", e)
    # noinspection PyBroadException
    try:
        if exp[-1] == "+-/x.":
            exit()
    except:
        print("Error: invalid syntax.")

    a_list = []
    c = ""

    for i in exp:
        if i in '+-x/()':
            a_list.append(float(c))
            a_list.append(i)
            c = ''
        else:
            c += i
    a_list.append(float(c))

    a_list = [i for i in a_list if i != '']
    print(a_list)
    a_list = functioning_1(a_list)
    a_list = functioning_2(a_list)
    return a_list[0]


def functioning_1(a_list):
    b_list = []
    skip = False
    for i in range(len(a_list)):
        if a_list[i] == "x":
            result = b_list.pop() * a_list[i+1]
            b_list.append(result)
            skip = True

        elif a_list[i] == "/":
            result = b_list.pop() / a_list[i+1]
            b_list.append(result)
            skip = True

        elif not skip:
            b_list.append(a_list[i])
        else:
            skip = False
            pass
        print(b_list)
    return b_list

def functioning_2(a_list):
    b_list = []
    skip = False
    for i in range(len(a_list)):
        if a_list[i] == "+":
            result = b_list.pop() + a_list[i+1]
            b_list.append(result)
            skip = True

        elif a_list[i] == "-":
            result = b_list.pop() - a_list[i+1]
            b_list.append(result)
            skip = True

        elif not skip:
            b_list.append(a_list[i])
        else:
            skip = False
            pass
        print(b_list)
    return b_list

exp = "10+12x2-12/.2"

print(calculator(exp))

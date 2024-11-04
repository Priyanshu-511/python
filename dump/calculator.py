'''
already tried in c++ but this time i will doing it in python later on i will do it in java.
'''
n1 = int(input("Enter number: "))
while(True):
    opr = input("select any one of them '+'; '-'; '*';'/';'%';'=' ")
    num = int(input("Enter the next number: "))

    if opr == '+':
        res = n1+num
        n1 = res
        print(res)

    elif opr == '-':
        res = n1-num
        n1 = res
        print(res)

    elif opr == '*':
        res = n1*num
        n1 = res
        print(res)

    elif opr == '/':
        res = n1/num
        n1 = res
        print(res)

    elif opr == '%':
        res = n1%num
        n1 = res
        print(res)

    elif opr == '=':
        print(res)
        break

    else:
        print("invalid operator: ")
        break
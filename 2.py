def calcuaterbin(decimal):
    binary = []
    while decimal>0:
        w=str(decimal%2)
        binary.append(w)
        decimal//=2
    binary.reverse()
    return binary
decimal=int(input('enter a decimal number '))
print("".join(calcuaterbin(decimal)))




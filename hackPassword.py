truePassword = 12345
result = False
contador = 0
while not result:
    contador = contador + 1
    result = contador == truePassword
    if result == True:
        print("Access Granted: {}".format(contador))
    else:
        print("Access Denied")
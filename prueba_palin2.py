mystring = input("Inserte una palabra:")
for indice in range(0, len(mystring)):
    if mystring[indice] != mystring[-(indice+1)]:
        print(" no es ")





def is_palindrome(mystring):
    for indice in range(0, len(mystring)):
        print(mystring[indice] + " --> " + mystring[-(indice +1)])
        if mystring[indice] !=  mystring[-(indice+1)]:
            print("no es")
            return False
    return True
import random
import string

def lunghezza():
    lunghezza=int(input("Numero di caratteri: "))
    return lunghezza

def menu():
    print("Generatore di password")
    print()
    print("Scegli come vuoi generare la password:")
    scelta=int(input("1. solo numeri\n2. solo lettere (maiuscole)\n3. solo lettere (minuscole)\n4. solo lettere\n5. numeri e lettere\n6. completa (numeri lettere e simboli)\n"))
    return scelta

def genera_password(scelta, lunghezza):
    password=""
    if scelta==1:
        for i in range(lunghezza):
            password=password+random.choice(string.digits)
        return password
    elif scelta==2:
        for i in range(lunghezza):
            password=password+random.choice(string.ascii_uppercase)
        return password
    elif scelta==3:
        for i in range(lunghezza):
            password=password+random.choice(string.ascii_lowercase)
        return password
    elif scelta==4:
        for i in range(lunghezza):
            password=password+random.choice(string.ascii_letters)
        return password
    elif scelta==5:
        for i in range(lunghezza):
            if (random.randint(0,10)%2==0):
                password=password+random.choice(string.ascii_letters)
            else:
                password=password+random.choice(string.digits)
        return password
    elif scelta==6:
        for i in range(lunghezza):
            if (random.randint(0,10)%3==0):
                password=password+random.choice(string.ascii_letters)
            elif (random.randint(0,10)%3==1):
                password=password+random.choice(string.punctuation)
            else:
                password=password+random.choice(string.digits)
        return password

if __name__ == '__main__':
    scelta=menu()
    lunghezza=lunghezza()
    password=genera_password(scelta, lunghezza)

    print("La tua password generata è: "+ password)

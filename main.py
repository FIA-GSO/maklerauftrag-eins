def dingsfunktion0() -> int:
    print("Was sind die Dinger?")
    print("länge: ")
    dings1 = int(input())
    print("breite: ")
    dings2 = int(input())
    return dings1 * dings2

dingsArray0 = []

print("Hello World!")

while True:
    print("Gibt es noch unvermessene Räume? (y/n)")
    dings0 = input()

    if dings0 == 'n':
        break

    dings3 = dingsfunktion0()
    dingsArray0.append(dings3)

print(dingsArray0)


while True:
    new, delete, log, done

    new <raumname>: 
        wie viele Rechtecke im nächsten Raum?

        Seitenlängen eingeben

        kein weiterer Raum?
        -> Beenden + Ergebnisse ausgeben
    
    delete <raumname>:
        löscht den Raum
    
    log <raumname>: 
        gibt die werte der Rechtecke des Raumes aus
    
    log: 
        gibt die Räume und gesammtfläche aus
    
    done: 
        Gibt alle Werte der Wohnung aus. 


Wohnuuuuung = {
    "raum1": [(2, 3), (4, 5)],
    "raum2": [(2, 3)],
    "raum3": [(2, 3), (4, 5), (5, 6)],
    "raum4": [(2, 3), (4, 5)],
}

wohnung = {}

def isEmpty(word) -> boolean:
    return not word

def getUserinput() -> dict:
    userinput = input()
    if isEmpty(userinput):
        return getUserinput()
    userinput = userinput.split(' ', 1)
    return {
        "befehl": userinput[0], 
        "name": userinput[1] if isEmpty(userinput[1]) else ''
    }

def createNewRoom():
    


while True: 
    userinput = getUserinput()
    
    match userinput["befehl"]: 
        case "new":
            print(userinput)
        case "delete":
            print(userinput)
        case "log":
            print(userinput)
        case "done":
            print(userinput)
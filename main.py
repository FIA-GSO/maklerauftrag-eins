def dingsfunktion0():
    print("Was sind die Dinger?");
    print("länge: ");
    dings1 = int(input());
    print("breite: ");
    dings2 = int(input());
    return dings1 * dings2;







































































dingsArray0 = [];

print("Hello World!");







while True: 
    print("Gibt es noch unvermessene Räume? (y/n)");
    dings0 = input();

    if dings0 == 'n':
        break;

    dings3 = dingsfunktion0();
    dingsArray0.append(dings3);


print(dingsArray0);



"""implementation of the Maklerauftrag"""

class MaklerAuftrag():
    """maklerauftrag class"""
    def __init__(self):
        # struktur:
        # {
        # "raum1": [(2, 3), (4, 5)],
        # "raum2": [(2, 3)],
        # "raum3": [(2, 3), (4, 5), (5, 6)],
        # }
        self.wohnung = {}

    def calculate_room_area(self, name) -> float:
        """calculates area of a single room"""
        pairs = self.wohnung.get(name, [])
        return sum(a * b for a, b in pairs)

    def calculate_total_area(self) -> float:
        """calculates the total area"""
        return sum(self.calculate_room_area(name) for name in self.wohnung)

    def create_new_room(self, name):
        """creates new room"""

        if name in self.wohnung:
            print("Raum existiert schon")
            return

        self.wohnung[name] = []

        while True:
            values = input("> ").split()
            if not values:
                continue
            if values[0] == "done":
                break
            if len(values) > 2:
                print("Bitte zwei Werte Eingeben")
            try:
                self.wohnung[name].append((float(values[0]), float(values[1])))
            except (IndexError, ValueError):
                print("Wrong input")

        print(f"Neuen Raum erstellt: {name} {self.wohnung[name]}\n")

    def delete_room(self, name):
        """deletes room"""
        if name not in self.wohnung:
            print("Raum existiert nicht\n")
            return

        del self.wohnung[name]
        print(f"Raum gelöscht: {name}\n")

    def list_rooms(self):
        """lists all rooms"""
        if not self.wohnung:
            print("Keine Räume hizugefügt\n")
            return

        for name, pairs in self.wohnung.items():
            print(name + ": ")

            if not pairs:
                print("  Keine Werte hinzugefügt")
            else:
                for i, (a, b) in enumerate(pairs, 1):
                    print(f" {i}: {a} * {b} = {a*b}")
                print(f"Raum Fläche: {self.calculate_room_area(name)}\n")

        print(f"Gesamtfläche: {self.calculate_total_area()}\n")

    def run(self):
        """main method"""

        print("""Willkommen
              """)

        while True:
            userinput = input().split()
            if not userinput:
                continue

            if userinput[0] == "new":
                if len(userinput) == 2:
                    self.create_new_room(userinput[1])
            elif userinput[0] == "delete":
                if len(userinput) == 2:
                    self.delete_room(userinput[1])
            elif userinput[0] == "list":
                if len(userinput) == 1:
                    self.list_rooms()
            elif userinput[0] == "done":
                if len(userinput) == 1:
                    return

dings = MaklerAuftrag()
dings.run()

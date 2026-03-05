"""Implementation eines Maklerauftrags zur Berechnung von Wohnflächen."""

class MaklerAuftrag():
    """Klasse zur Verwaltung von Räumen und zur Berechnung der Wohnfläche."""
    def __init__(self):
        # struktur:
        # {
        # "raum1": [(2, 3), (4, 5)],
        # "raum2": [(2, 3)],
        # "raum3": [(2, 3), (4, 5), (5, 6)],
        # }
        self.wohnung = {}

    def calculate_room_area(self, name) -> float:
        """Berechnet die Fläche eines einzelnen Raumes."""
        pairs = self.wohnung.get(name, [])
        return sum(a * b for a, b in pairs)

    def calculate_total_area(self) -> float:
        """Berechnet die Gesamtfläche aller Räume."""
        return sum(self.calculate_room_area(name) for name in self.wohnung)

    def create_new_room(self, name):
        """Erstellt einen neuen Raum und erlaubt das Eingeben von Seitenpaaren."""

        print(f"""
Neuen Raum erstellen: {name}

Geben Sie Seitenpaare für Rechtecke ein, aus denen der Raum besteht.
Format: <länge> <breite>

Beispiele:
  3 4
  5 2.5

Jede Eingabe wird als Teilfläche gespeichert.
Geben Sie 'done' ein, um die Eingabe zu beenden.
""")

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
                continue
            try:
                self.wohnung[name].append((float(values[0]), float(values[1])))
            except (IndexError, ValueError):
                print("Wrong input")

        print(f"Neuen Raum erstellt: {name} {self.wohnung[name]}\n")

    def delete_room(self, name):
        """Löscht einen bestehenden Raum aus der Wohnung."""

        if name not in self.wohnung:
            print("Raum existiert nicht\n")
            return

        del self.wohnung[name]
        print(f"Raum gelöscht: {name}\n")

    def list_rooms(self):

        """Listet alle Räume mit ihren Flächen und Teilflächen auf."""
        if not self.wohnung:
            print("Keine Räume hizugefügt\n")
            return

        for name, pairs in self.wohnung.items():
            print(name + ": ")

            if not pairs:
                print("  Keine Werte hinzugefügt")
            else:
                for i, (a, b) in enumerate(pairs, 1):
                    print(f" {i}: {a}m * {b}m = {a*b}m²")
                print(f"Raum Fläche: {self.calculate_room_area(name)}m²\n")

        print(f"Gesamtfläche: {self.calculate_total_area()}m²\n")

    def run(self):
        """Startet das Kommandozeilen-Interface des Programms."""

        print("""
Maklerauftrag - Wohnflächenverwaltung

Verfügbare Befehle:
  new <raumname>     Erstellt einen neuen Raum. Danach können Seitenpaare
                     (z.B. "3 4") eingegeben werden. Mit "done" beenden.
  delete <raumname>  Löscht einen Raum.
  list               Zeigt alle Räume und deren Flächen.
  help               Zeigt diese Hilfe.
  done               Beendet das Programm.

Beim Hinzufügen eines Raumes können mehrere Rechtecke eingegeben werden,
deren Flächen zur Gesamtfläche des Raumes addiert werden.
""")

        while True:
            userinput = input().split()
            if not userinput:
                continue

            if userinput[0] == "new" and len(userinput) == 2:
                self.create_new_room(userinput[1])
            elif userinput[0] == "delete" and len(userinput) == 2:
                self.delete_room(userinput[1])
            elif userinput[0] == "list" and len(userinput) == 1:
                self.list_rooms()
            elif userinput[0] == "done" and len(userinput) == 1:
                return
            elif userinput[0] == "help" and len(userinput) == 1:
                print("""
Hilfe:

new <raumname>
    Erstellt einen neuen Raum. Danach können Maße eingegeben werden
    (z.B. "3 5"). Mit "done" wird die Eingabe beendet.

delete <raumname>
    Entfernt einen vorhandenen Raum.

list
    Zeigt alle Räume mit ihren Teilflächen und der Gesamtfläche.

done
    Beendet das Programm.
""")

if __name__ == "__main__":
    makler = MaklerAuftrag()
    makler.run()

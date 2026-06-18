
from datetime import datetime

from fahrzeug import Fahrzeug
from tarif import Tarif


class ParkingManager:

    def __init__(self):
        # Daten von einem Parkvorgang
        self.fahrzeug = None
        self.tarif = None
        self.parkdauer = None
        self.parkpreis = None

        # Die Tarife vom Parkhaus (Name -> Tarif-Objekt)
        self.tarife = {
            "STANDARD": Tarif("Standard", 2.00, 1.50),
            "KURZPARK": Tarif("Kurzpark", 1.00, 2.00),
            "LANGZEIT": Tarif("Langzeit", 5.00, 1.00),
        }

    # [1] Fahrzeug erfassen
    def fahrzeug_erfassen(self):
        kennzeichen = input("Kennzeichen: ").strip()
        if kennzeichen == "":
            print("Fehler: Das Kennzeichen darf nicht leer sein.")
            return

        fahrzeugtyp = input("Fahrzeugtyp (MOTORRAD, PKW, TRANSPORT): ").strip()
        try:
            Fahrzeug.preisfaktor(fahrzeugtyp)
        except ValueError as fehler:
            print(f"Fehler: {fehler}")
            return

        # neuen Parkvorgang starten, alten zuruecksetzen
        self.fahrzeug = Fahrzeug(kennzeichen, fahrzeugtyp.upper())
        self.tarif = None
        self.parkdauer = None
        self.parkpreis = None

        print(f"Fahrzeug gespeichert: {self.fahrzeug.kennzeichen} "
              f"({self.fahrzeug.fahrzeugtyp})")

    # [2] Tarife anzeigen
    def tarife_anzeigen(self):
        print("\n--- Tarife ---")
        for tarif in self.tarife.values():
            print(f"{tarif.name}: Grundpreis {tarif.grundpreis:.2f} EUR, "
                  f"pro Stunde {tarif.preis_pro_stunde:.2f} EUR")

    # [3] Parkpreis berechnen
    def parkpreis_berechnen(self):
        if self.fahrzeug is None:
            print("Fehler: Bitte zuerst ein Fahrzeug erfassen.")
            return

        # Tarif waehlen
        self.tarife_anzeigen()
        name = input("Tarif waehlen: ").strip().upper()
        if name not in self.tarife:
            print("Fehler: Diesen Tarif gibt es nicht.")
            return
        self.tarif = self.tarife[name]

        # Parkdauer eingeben und pruefen
        eingabe = input("Parkdauer in Stunden: ").strip()
        try:
            parkdauer = float(eingabe.replace(",", "."))
        except ValueError:
            print("Fehler: Bitte eine gueltige Zahl eingeben.")
            return

        if parkdauer < 0:
            print("Fehler: Die Parkdauer darf nicht negativ sein.")
            return
        if parkdauer == 0:
            print("Fehler: Die Parkdauer darf nicht 0 sein.")
            return
        if parkdauer > 72:
            print("Fehler: Die maximale Parkdauer betraegt 72 Stunden.")
            return

        self.parkdauer = parkdauer

        # Preisformel:
        # Endpreis = (Grundpreis + Preis_pro_Stunde * Parkdauer) * Fahrzeugfaktor
        faktor = Fahrzeug.preisfaktor(self.fahrzeug.fahrzeugtyp)
        self.parkpreis = (self.tarif.grundpreis +
                          self.tarif.preis_pro_stunde * parkdauer) * faktor

        print(f"Parkpreis: {self.parkpreis:.2f} EUR")

    # [4] Parkticket drucken
    def parkticket_drucken(self):
        if self.parkpreis is None:
            print("Fehler: Bitte zuerst den Parkpreis berechnen.")
            return

        zeit = datetime.now().strftime("%d.%m.%Y %H:%M")

        print("\n===== PARKTICKET =====")
        print(f"Kennzeichen: {self.fahrzeug.kennzeichen}")
        print(f"Fahrzeugtyp: {self.fahrzeug.fahrzeugtyp}")
        print(f"Tarif:       {self.tarif.name}")
        print(f"Parkdauer:   {self.parkdauer:g} Stunden")
        print(f"Parkpreis:   {self.parkpreis:.2f} EUR")
        print(f"Zeitstempel: {zeit}")
        print("======================")
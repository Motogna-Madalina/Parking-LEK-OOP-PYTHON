
class Fahrzeug:
    def __init__(self, kennzeichen, fahrzeugtyp):
        self.kennzeichen = kennzeichen
        self.fahrzeugtyp = fahrzeugtyp


    @staticmethod
    def preisfaktor(fahrzeugtyp):
        fest_faktoren = {
            "MOTORRAD": 0.7,
            "PKW": 1.0,
            "TRANSPORT": 1.5
        }

        if fahrzeugtyp.upper() not in fest_faktoren:
            raise ValueError(
<<<<<<< HEAD
                "Fahrzeugtyp ist nicht gefunden.\nBitte schreiben Sie: MOTORRAD, PKW oder TRANSPORT"
=======
                    "Unbekannter Fahrzeugtyp.\nBitte geben Sie einen der folgenden Fahrzeugtypen ein: MOTORRAD, PKW oder TRANSPORT."

>>>>>>> df5c8c0f9e8ad1d86fbe6e3263e6e83b132463e2
            )

        return fest_faktoren[fahrzeugtyp.upper()]
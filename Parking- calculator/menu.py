from parking_manager import ParkingManager


def start_program():

    manager = ParkingManager()

    while True:

        print("\n===== City Park =====")
        print("1 - Fahrzeug erfassen")
        print("2 - Tarife anzeigen")
        print("3 - Parkpreis berechnen")
<<<<<<< HEAD
        print("4 - Parkticket drucken")
=======
        print("5 - Parkticket drucken")
>>>>>>> df5c8c0f9e8ad1d86fbe6e3263e6e83b132463e2
        print("Q - Beenden")

        choice = input("Select: ").upper()

        if choice == "1":
            manager.fahrzeug_erfassen()

        elif choice == "2":
            manager.tarife_anzeigen()

        elif choice == "3":
            manager.parkpreis_berechnen()

<<<<<<< HEAD
        elif choice == "4":
            manager.parkticket_drucken()


=======
        elif choice == "5":
            manager.parkticket_drucken()

>>>>>>> df5c8c0f9e8ad1d86fbe6e3263e6e83b132463e2
        elif choice == "Q":
            print("Beenden.")
            break

        else:
            print("Invalid option.")
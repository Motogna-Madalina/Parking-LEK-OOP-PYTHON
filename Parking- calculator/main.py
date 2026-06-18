<<<<<<< HEAD
from menu import start_program

def main():
    start_program()

if __name__ == '__main__':

    main()
=======
from parking_manager import ParkingManager
from vehicle import Vehicle

def main():

    manager = ParkingManager()

    while True:

        print("\n===== City Park =====")
        print("1 - Enter Vehicle")
        print("2 - Select Parking Rate")
        print("3 - Record Parking Duration")
        print("4 - Calculate parking Price")
        print("5 - Show Parking Label")
        print("Q - Exit")

        choice = input("Select: ").upper()

        if choice == "1":
            manager.add_vehicle()

        elif choice == "2":
            manager.show_tariffs()

        elif choice == "3":
            manager.show_parking_duration()

        elif choice == "4":
            manager.calculate_parking_platz()

        elif choice == "5":
            manager.show_label()

        elif choice == "Q":
            print("Program closed.")
            break

        else:
            print("Invalid option.")

main()
>>>>>>> df5c8c0f9e8ad1d86fbe6e3263e6e83b132463e2

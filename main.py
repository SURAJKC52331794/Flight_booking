from flights import show_all_flights
from available_seats import show_available_seats
from book_seat import book_seat
from cancel_seat import cancel_seat
from view_bookings import view_all_bookings

def main_menu():
    while True:
        print("   Airplane Ticket Booking System    ")
        print("1. Show all flights")
        print("2. Show available seats")
        print("3. Book a seat")
        print("4. Cancel a seat")
        print("5. View all bookings")
        print("6. Exit program")
        
        choice = input("Enter your choice (1–6): ")

        if choice == '1':
            show_all_flights()
        elif choice == '2':
            show_available_seats()
        elif choice == '3':
            book_seat()
        elif choice == '4':
            cancel_seat()
        elif choice == '5':
            view_all_bookings()
        elif choice == '6':
            print(" Exiting program. Thank you!")
            break
        else:
            print(" Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()

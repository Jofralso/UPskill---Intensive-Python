class Theater:
    def __init__(self, num_rows, num_seats_per_row):
        self.num_rows = num_rows
        self.num_seats_per_row = num_seats_per_row
        self.seat_map = [[True] * num_seats_per_row for _ in range(num_rows)]

    def book_ticket(self, row, seat):
        if row < 1 or row > self.num_rows or seat < 1 or seat > self.num_seats_per_row:
            print("Invalid seat selection!")
        elif self.seat_map[row - 1][seat - 1]:
            self.seat_map[row - 1][seat - 1] = False
            print("Ticket booked successfully!")
        else:
            print("Seat already booked!")

    def display_seat_map(self):
        for i, row in enumerate(self.seat_map):
            print(f"Row {i + 1}: {' '.join(['O' if seat else 'X' for seat in row])}")
        print("\n")


theater = Theater(5, 6)
theater.display_seat_map()

theater.book_ticket(3, 4)  # Book a ticket for Row 3, Seat 4
theater.book_ticket(2, 5)  # Book a ticket for Row 2, Seat 5
theater.book_ticket(4, 3)  # Book a ticket for Row 4, Seat 3
theater.book_ticket(3, 4)  # Attempt to book the same seat again

theater.display_seat_map()
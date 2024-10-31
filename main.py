print("Homework 5-6")
class Ticket:
    def __init__(self, movie_title, seat_number, price):
        self.movie_title = movie_title
        self.seat_number = seat_number
        self.price = price

    def display_info(self):
        return f"Movie: {self.movie_title}, Seat: {self.seat_number}, Price: ${self.price:.2f}"

class StandardTicket(Ticket):
    def __init__(self, movie_title, seat_number, price, discount=0):
        super().__init__(movie_title, seat_number, price)
        self.discount = discount

    def display_info(self):
        discount_info = f"Discount: {self.discount}%" if self.discount > 0 else "No discount"
        return f"{super().display_info()}, {discount_info}"

class VIPticket(Ticket):
    def __init__(self, movie_title, seat_number, price, lounge_access=True, complimentary_drinks=1):
        super().__init__(movie_title, seat_number, price)
        self.lounge_access = lounge_access
        self.complimentary_drinks = complimentary_drinks

    def display_info(self):
        lounge_info = "Lounge Access: Yes" if self.lounge_access else "Lounge Access: No"
        drinks_info = f"Complimentary Drinks: {self.complimentary_drinks}"
        return f"{super().display_info()}, {lounge_info}, {drinks_info}"

class Cinema:
    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket):
        try:
            if not (1 <= ticket.seat_number <= 100):
                raise InvalidSeatNumberError(ticket.seat_number)
            self.tickets.append(ticket)
        except InvalidSeatNumberError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred while adding a ticket: {e}")

    def display_all_tickets(self):
        if not self.tickets:
            print("No tickets have been issued.")
        else:
            for ticket in self.tickets:
                print(ticket.display_info())

class InvalidSeatNumberError(Exception):
    def __init__(self, seat_number):
        super().__init__(f"Invalid seat number {seat_number}. Seat number must be between 1 and 100.")

cinema = Cinema()

ticket1 = StandardTicket("Avatar 2", 10, 12.5, discount=10)
ticket2 = StandardTicket("20 Days in Mariupol", 150, 10)
ticket3 = VIPticket("Spider-Man: No Way Home", 5, 20, lounge_access=True, complimentary_drinks=2)

cinema.add_ticket(ticket1)
cinema.add_ticket(ticket2)
cinema.add_ticket(ticket3)

cinema.display_all_tickets()

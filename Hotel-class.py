class Hotel:
    def __init__(self, name,  location, room):
        """Initialize  the hotel with a name, location, and number of rooms."""
        self.name = name
        self.location = location
        self.rooms = room
        self.booked_rooms = 0


    def book_room(self, number_of_rooms):
        # """Book a specified number of rooms,"""
         if number_of_rooms <= 0:
             print("Number of rooms to book mustbe positive.")
             return

         if self.booked_rooms + number_of_rooms > self.rooms:  # room - means available
             print("Not enough available rooms to book.") 
             return

         self.booked_rooms += number_of_rooms
         print(f"{number_of_rooms} room(s) successfilly booked.")

    # book info delet operation
    def checkout(self, number_of_rooms):
        #"""Check out a specified number of rooms."""
        if number_of_rooms <= 0:
             print("Number of rooms to checkout must be positive.")
             return

        if number_of_rooms > self.booked_rooms:
              print("Cannot checkout more rooms than booked.")
              return
         
        self.booked_rooms += number_of_rooms
        print(f"{number_of_rooms} room(s) successfully cheched out.")

    def get_availability(self):
        """Get the number of available rooms."""
        available_rooms = self.rooms - self.booked_rooms
        return available_rooms
    
    def __str__(self):
        """Return a  string reperesntation of the hotel."""
        return f"Hotel: {self.name}, location: {self.location}, Total Rooms: {self.rooms}, Booked Rooms: {self.booked_rooms}"
    
# creating an obect of the Hotel calss
my_hotel = Hotel("Seaside Resort", "california", 100
                   )
# Accessing attributes and methods
print(my_hotel) #Disply hotel detils

# Booking rooms
my_hotel.book_room(22)
print(f"Availble rooms:{my_hotel.get_availability()}")

# checking out rooms
my_hotel.checkout(4)
print(f"Available rooms:{my_hotel.get_availability()}")
          
              
                     
        
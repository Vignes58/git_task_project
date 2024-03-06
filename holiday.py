# Get user input for the destination of the holiday flight
holiday_flight = input("Please enter a destination between Germany, France, and Poland: ")

# Determine the flight cost based on the chosen destination
if holiday_flight == "Germany":
    flight_cost = 120
elif holiday_flight == "France":
    flight_cost = 80
elif holiday_flight == "Poland":
    flight_cost = 140
else:
    print("Please pick one of the valid destinations.")
    exit()

# Display the flight cost
print(f"Your flight to {holiday_flight} costs £{flight_cost}.")

# Get user input for the number of nights to stay
Nights = input("Please enter the number of nights you would like to stay; you can pick between 1, 2, and 3 nights: ")

# Determine the cost per night based on the chosen number of nights
if Nights == "1":
    Per_Night = 20
elif Nights == "2":
    Per_Night = 30
elif Nights == "3":
    Per_Night = 40
else:
    print("Please pick one of the valid numbers of nights.")
    exit()

# Display the cost of staying for the chosen number of nights
print(f"You will be staying {Nights} nights, and it will cost £{Per_Night} per night.")

# Get user input for the number of days to rent a car
Rental_days = input("Please enter the number of days you would like to rent a car for; pick a number from 1, 2, and 3:")

# Determine the rental cost based on the chosen number of days
if Rental_days == "1":
    Rental_cost = 15
elif Rental_days == "2":
    Rental_cost = 25
elif Rental_days == "3":
    Rental_cost = 35
else:
    print("Please enter a valid number of days you would like to rent a car for.")
    exit()

# Display the cost of renting a car for the chosen number of days
print(f"You have rented a car for {Rental_days} days, and it will cost £{Rental_cost}.")

# Calculate and display the total cost of the holiday
Total_cost = Rental_cost + Per_Night + flight_cost
print(f"Your total cost for the holiday will be £{Total_cost}.")






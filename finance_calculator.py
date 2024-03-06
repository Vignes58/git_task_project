import math

def calculate_interest(principal, interest_rate, years, interest_type):
    # Calculate interest based on the provided interest type
    if interest_type.lower() == 'simple':
        interest = principal * (1 + interest_rate * years)
    elif interest_type.lower() == 'compound':
        interest = principal * (1 + interest_rate) ** years
    else:
        # If an invalid interest type is provided, print an error message and return None
        print("Invalid interest type. Please enter 'simple' or 'compound'.")
        return None

    # Calculate and return the interest earned or amount to be paid on the loan
    return interest - principal

def main():
    # Get user's choice for either 'investment' or 'bond'
    user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

    if user_choice.lower() == 'investment':
        # For investment, get user inputs and calculate interest
        principal = float(input("Enter the amount of money that you are depositing: "))
        interest_rate = float(input("Enter the interest rate (as a percentage): ")) / 100.0
        years = int(input("Enter the number of years you plan on investing: "))
        interest_type = input("Enter 'simple' or 'compound' for interest type: ")

        result = calculate_interest(principal, interest_rate, years, interest_type)

        if result is not None:
            print(f"The amount of interest earned on your investment is: {result:.2f}")

    elif user_choice.lower() == 'bond':
        # For a home loan, get user inputs and calculate interest using simple interest
        principal = float(input("Enter the amount of the home loan: "))
        interest_rate = float(input("Enter the interest rate (as a percentage): ")) / 100.0
        years = int(input("Enter the number of years for the home loan: "))

        result = calculate_interest(principal, interest_rate, years, 'simple')

        if result is not None:
            print(f"The amount you'll have to pay on the home loan is: {result:.2f}")

    else:
        # If an invalid choice is entered, print an error message
        print("Invalid choice. Please enter either 'investment' or 'bond'.")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()

    
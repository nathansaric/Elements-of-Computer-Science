# NATHAN SARIC - 05/17/2019 

# This program calculates the monthly payment and the total interest paid
# over the entire term when given the principal amount, the length of the term,
# and the annual interest rate -- provided by the user.

# Global variables used as constants
MONTHS_PER_YEAR = 12

def main():
    # Obtain three required values from the user
    principal = float(input("Please enter the principal amount in dollars: $ "))
    term_years = float(input("Please enter the length of term in years: "))
    annual_interest_rate = float(input("Please enter the annual interest rate as a decimal: "))

    # Error check the users' inputs
    # Principal must lie between $1000 and $500000 inclusive
    if principal < 1000 or principal > 500000 :
        print("The principal amount entered is invalid!")
        return

    # Length of term, in years, must lie between 1 and 30 years inclusive
    if term_years < 1 or term_years > 30 :
        print("The length of term entered is invalid!")
        return

    # Annual interest rate must lie between 1% and 10% inclusive
    if annual_interest_rate < 0.01 or annual_interest_rate > 0.1 :
        print("The annual interest rate entered is invalid!")
        return

    # Calculate the monthly payment of the mortgage and the total interest paid over the entire term
    monthly_interest_rate = annual_interest_rate / MONTHS_PER_YEAR
    term_months = term_years * MONTHS_PER_YEAR

    monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** (term_months * -1))
    total_interest = term_months * monthly_payment - principal

    # Display the results to the user
    print("The monthly payment for your mortgage is ${0:.2f}".format(monthly_payment))
    print("The total interest paid over the entire term is ${0:.2f}".format(total_interest))

main()

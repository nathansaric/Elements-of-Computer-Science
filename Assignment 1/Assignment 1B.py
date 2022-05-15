# NATHAN SARIC - 05/17/2019 

# This program is a postage rate calculator which calculates the postage rate depending on the destination country,
# the size of the letter, and the weight of the letter -- supplied by the user.
# This program also checks the numeric inputs to make sure all values are legal and lie within the parameters of
# each respective variable.

# Global variables used as constants
STANDARD_CANADA = [1.05, 1.28]
NON_STANDARD_CANADA = [1.91]
OVERSIZE_CANADA = [3.13, 4.34, 4.98, 5.35]

STANDARD_USA = [1.29, 1.92]
NON_STANDARD_USA = [3.14]
OVERSIZE_USA = [5.45, 10.90]


def main():
    # Obtain three required values from the user
    country = str(input("Please enter the destination country - either 'Canada' or 'USA': "))
    letter_size = (input("Is the letter standard sized?\nPlease enter either 'Y' for yes, or 'N' for no: "))
    letter_weight = float(input("Please enter the weight of the letter in grams: "))

    # Check the legality of the destination country entered
    if country not in ['Canada','USA'] :
        print("The destination country entered is not supported by this calculator!")
        return
    
    # Check the legality of the weight of the letter entered
    if letter_weight <= 0 or letter_weight > 500 :
        print("The weight of the letter entered is invalid!")
        return

    # Determine if the size of the letter is standard or non-standard
    if letter_size == 'Y' and letter_weight > 50 :
        print("The weight of the letter entered is over 50 grams, therefore, non-standard / oversize postage rates will be applied.")
        
    # Determine the corresponding postage rate for the destination country
    if country == 'Canada' :
        if letter_weight > 0 and letter_weight <= 30 :
            postage_rate = STANDARD_CANADA[0]
        elif letter_weight > 30 and letter_weight <= 50 :
            postage_rate = STANDARD_CANADA[1]
        elif letter_weight > 50 and letter_weight <= 100 :
            postage_rate = NON_STANDARD_CANADA[0]
        elif letter_weight > 100 and letter_weight <= 200 :
            postage_rate = OVERSIZE_CANADA[0]
        elif letter_weight > 200 and letter_weight <= 300 :
            postage_rate = OVERSIZE_CANADA[1]
        elif letter_weight > 300 and letter_weight <= 400 :
            postage_rate = OVERSIZE_CANADA[2]
        elif letter_weight > 400 and letter_weight <= 500 :
            postage_rate = OVERSIZE_CANADA[3]

    else :
        if letter_weight > 0 and letter_weight <= 30 :
            postage_rate = STANDARD_USA[0]
        elif letter_weight > 30 and letter_weight <= 50 :
            postage_rate = STANDARD_USA[1]
        elif letter_weight > 50 and letter_weight <= 100 :
            postage_rate = NON_STANDARD_USA[0]
        elif letter_weight > 100 and letter_weight <= 200 :
            postage_rate = OVERSIZE_USA[0]
        elif letter_weight > 200 and letter_weight <= 300 \
                or letter_weight > 300 and letter_weight <= 400 \
                or letter_weight > 400 and letter_weight <= 500 :
            postage_rate = OVERSIZE_USA[1]

    # Display the results to the user
    print("The postage rate for the letter is ${0:.2f}".format(postage_rate))


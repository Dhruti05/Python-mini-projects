# Project 3: Decimal <-> Binary Converter
# Description: This program converts between decimal and binary formats based on user choice.

def decimal_to_binary(decimal_number):
    """
        Converts a decimal number to binary format.
    """
    return bin(decimal_number)[2:] #bin adds '0b' prefix, [2:] removes it 

def binary_to_decimal(binary_number):
    """
        Converts a binary string to decimal format
    """
    return int(str(binary_number), 2) #int(binary_string, base) converts binary -> decimal

def main():
    print(" Decimal <-> Binary Converter ")
    print("1. Decimal to Binary")
    print("2. Binary to Decimal")

    try:
        user_choice = int(input("Enter your choice (1 or 2):"))

        if user_choice == 1:
            #Decimal to Binary conversion
            dec = int(input("Enter a decimal number: "))
            binary_result = decimal_to_binary(dec)
            print(f"Binary equivalent: {binary_result}")

        elif user_choice == 2:
            #Binary to Decimal converter
            binary = int(input("Enter a binary number: "))
            decimal_result = binary_to_decimal(binary)
            print(f"Decimal equivalent: {decimal_result}")

        else:
            print("Invalid Choice!! Please enter 1 or 2")

    except ValueError:
        print("Error!! Please enter a valid numeric input")

#Run the program
if __name__ == "__main__":
    main()
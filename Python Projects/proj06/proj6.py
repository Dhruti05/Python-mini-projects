#Project 6: Number to words Converter
#Description: Converts a given number into its words representation.
#Example: 123 -> One Two Three

def number_to_words(num):
    """
    Convert a number (integer) into its word representation.
    Example: 123 -> 'One Two Three'
    """
    units = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

    #convert the following digit to corresponding words and join with space
    return ' '.join(units[int(digit)] for digit in str(num))

def main():
    try:
        user_input = int(input("Enter a number: "))
        print(f"Number in words: {number_to_words(user_input)}")
    except ValueError:
        print("Please enter a valid integer number!!")

if __name__ == "__main__":
    main()
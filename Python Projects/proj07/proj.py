#Project 7: Word Count Tool
# Description: This program counts the number of words in a given text entered by the user.

def count_words(text):
    """
    Function to count the number of words in a given string.
    A word is defined as a sequence of characters separated by spaces.
    """
    # Split the text into words using spaces as separators
    words = text.split()
    #return total length of words
    return len(words)

def main():
    """
    Main function to interact with the user.
    It takes input from the user and displays the word count.
    """
    # Ask the user to input text
    text = input("Enter some text: ")
    #count the words using count_words() function
    word_count = count_words(text)
    #display the result
    print(f"Word count: {word_count}")

if __name__ == "__main__":
    main()
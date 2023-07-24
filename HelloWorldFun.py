# DigitalKhalid's Fun Hello World Program

import time

def delay_print(text, delay=0.5):
    """
    Prints text with a delay between characters.
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    print("Welcome to DigitalKhalid's Fun Hello World Program!")
    print("Get ready for some fun!\n")

    # Print "Hello, World!" with a delay between characters
    delay_print("Hello, World!", delay=0.2)
    
    print("\nLet's make it more exciting!")
    print("How about printing each character on a new line?\n")

    # Print each character on a new line
    for char in "Hello, World!":
        print(char)
        time.sleep(0.1)
    
    print("\nWasn't that cool?")
    print("Now let's try some animation!\n")

    # Animation of "Hello, World!"
    for _ in range(3):
        for char in "Hello, World!":
            print(char, end='', flush=True)
            time.sleep(0.1)
            print('\b' + ' ' + '\b', end='', flush=True)
        time.sleep(0.5)
    
    print("\nThat was fun, right?")
    print("Now it's your turn to get creative with the 'Hello, World!' program!\n")
    print("Thank you for watching DigitalKhalid's Fun Hello World Program!")

if __name__ == '__main__':
    main()
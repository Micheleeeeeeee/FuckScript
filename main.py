import time
import os
from colorama import Fore, Style

string = 'Spam ' * 5000


def write(words, count):
    for i in range(count):
        for ele in words:
            with open(f'{ele}{i}.txt', 'w') as f:
                f.write(string)
                f.close()


def main():
    """
    Main method, run when script is run.
    :return: Integer, 0 or -1 depending on success.
    """
    print(f'{Fore.GREEN}Welcome to Fuck Script! {Fore.RESET}')

    run = input("Are you sure you would like to continue? (y=yes)")

    if run == 'y':
        run = True
    else:
        print(f'{Fore.RED}Exiting...{Fore.RESET}')
        return 0

    print(f'{Fore.GREEN}Continuing...{Fore.RESET}')

    word_count = 0
    words = []
    try:
        word_count = int(input("How many loops? "))
    except ValueError:
        word_count = 1
        print(f'{Fore.RED}Incorrect value specified, one thread.{Fore.RESET}')

    for i in range(word_count):
        words.append(f'python{i}')
    write(words, 500)

    """
    We did it! Return 0
    """
    return 0


if __name__ == '__main__':
    main()

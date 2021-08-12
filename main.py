"""
Just so you know, this script will attempt to create an EXTREMELY HIGH amount of files. 
Please only run this if you're ONE HUNDRED percent sure.

TODO: Multi-Threading
""" 

import time
import os
from threading import Thread
from colorama import Fore, Style

os.system('')

fuck_string = 'fuck string ' * 500
max_threads = 100
words = []

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
  print("Initialising...")
  time.sleep(1)
  print('Adding python[num] 100 times to words[]')
  for i in range(1, 101):
    words.append('python' + str(i))
  print(f'{Fore.GREEN}Successfully created list... {Style.RESET_ALL}')
  print(f'{Fore.RED}words: ' + str(words) + f'{Style.RESET_ALL}')

  print("Running in 5 seconds...")
  for i in range(6, 1):
    time.sleep(1)
    print(str(i) + "...")
  
 
def write(target_name):
  for i in range(1, 100000000):
    with open(target_name + str(i) + '.txt', 'w+') as f:
              f.write(fuck_string)
    if i == (100000000 / 2):
      print("50% done")
    elif i == (100000000 / 10):
      print("10% done")
    elif i == 5000:
      print("5000 done")
    elif i == 10000:
      print("10,000 done")
    elif i == 20000:
      print("20,000 done")
    elif i == 50000:
      print("50,000 done")
  
if __name__ == '__main__':
  main()
  

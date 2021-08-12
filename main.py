"""
Just so you know, this script will attempt to create an EXTREMELY HIGH amount of files. 
Please only run this if you're ONE HUNDRED percent sure.
"""

import time
import os

fuck_string = 'fuck string ' * 500

def main():
  print("Running in 5 seconds...")
  for i in range(6, 1):
    time.sleep(1)
    print(str(i) + "...")
  write()
 
def write():
  for i in range(1, 100000000):
    with open('owo' + str(i) + '.txt', 'w+') as f:
              f.write(fuck_string)
    if i == (100000000 / 2):
      print("50% done")
    elif i == (100000000 / 10):
      print("10% done")
    elif i == 5000:
      print("5000 done")
  
if __name__ == '__main__':
  main()
  

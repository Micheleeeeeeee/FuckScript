"""
Just so you know, this script will attempt to create an EXTREMELY HIGH amount of files. 
Please only run this if you're ONE HUNDRED percent sure.
"""

import time
import os

fuck_string = 'fuck string ' * 5000

def main():
  print("Running in 5 seconds...")
  for i in range(1, 6):
    time.sleep(1)
    print(str(i) + "...")
  os.popen("echo " + fuck_string + " >> owo.txt")  
  

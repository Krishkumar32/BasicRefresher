#✅ 1. input() — normal input
name = input("Enter your name: ")
print("You entered:", name)

#✅ 2. sys.stdin.readline() — fast input

import sys
x = sys.stdin.readline().strip()
print("You entered:", x)

#✅ 3. fileinput — read like Scanner
import fileinput
for line in fileinput.input():
    x = line.strip()
    print("You entered:", x)
    break


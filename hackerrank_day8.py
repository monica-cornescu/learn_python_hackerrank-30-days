'''
Task
Given names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
You will then be given an unknown number of names to query your phone book for.
For each queried, print the associated entry from your phone book on a new line in the form name=phoneNumber;
if an entry for is not found, print Not found instead.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())
phoneBook = {}

for i in range(n):
    readAgendaEntry = str(input())
    extractNameNumber = re.search(r"(.+?) +(\d{8})", readAgendaEntry)
    name = extractNameNumber.group(1)
    number = extractNameNumber.group(2)
    phoneBook[name] = number

phoneBookNames = phoneBook.keys()
query = str(input())
while query != "":
    if query in phoneBookNames:
        print("%s=%s" % (query, phoneBook[query]))
    else:
        print("Not found")

    query = str(input())
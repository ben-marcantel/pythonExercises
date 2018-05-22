import sys

MASTER_PASSWORD = 'yo'
password = input("Please enter password: ")
attempt_count = 1
while password != MASTER_PASSWORD:
    if attempt_count > 3:
        sys.exit("too manany attempts :( ")
    password = input("sorry bruh, try again: ")
    attempt_count +=1
print("Welome yo")
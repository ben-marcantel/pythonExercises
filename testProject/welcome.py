first_name = input("What is your first name?  ")
print("hello", first_name)
if first_name == "Craig":
    print(first_name, "is learning")
elif first_name == "ben":
    print("yooo dawg")
else:
    age = int(input("How old are you?"))
    if age<= 6 :
        print("wowo you're{} ".format(age))
    print("You should learn python")
print("Have a great day {}:".format(first_name))
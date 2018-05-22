SERVICE_CHARGE=2
TICKET_PRICE = 10

tickets_remaining = 100  

def calculate_price(num_of_tickets):
    
    return  (num_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:    
    print("There are {} tickets remaining".format(tickets_remaining))
    name = input("Please enter your name: ")
    number_of_tickets= input ("Welcome {}, please enter how many tickets you would like:".format(name))
    try:
        number_of_tickets = int(number_of_tickets)
        if number_of_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:      
        print("Whoops, you messed up {}!".format(err))
    else:    
        total_price = calculate_price(number_of_tickets)
        print("The total due is ${}, you better pay up".format(total_price))
        confirmation_prompt = input("Are you sure, y/n ?: ")
        if confirmation_prompt.lower() == "y":
            print("sold!!")
            tickets_remaining-=number_of_tickets
        else:
            print("Oh well, {}".format(name))
print(" all tickets are sold! :( ") 
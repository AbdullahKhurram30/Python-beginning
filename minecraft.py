name = input("What is your name?")
player = input("Do you play minecraft? Y for yes or N for no")
if player == "Y":
    diamonds_demand = int(input("How many diamonds do you want?"))
    if diamonds_demand > 5:
        print("System crashed..... Please try again later")
    else:
        print("congrats. you get", diamonds_demand, "diamonds")
elif player == "N":
    print("It is a good game try it")    
else:
    print("Follow the instructions!!!!")
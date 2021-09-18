def wash_car():
    type=input("Welcome in our wash car, choose between the Platinum or the Normal : ")
    if type == "Platinum":
        print("Wash with tri-color foam")
        print("Rinse twice")
        print("Dry with large blow dryer")
    elif type == "Normal":
        print("Wash with white foam")
        print("Rinse once")
        print("Air dry") 
    else:
        print("Oops! we don't have that option")
wash_car()

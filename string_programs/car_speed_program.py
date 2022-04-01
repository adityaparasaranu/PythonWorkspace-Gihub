print ("What is the \"Speed\" of your \"Vehicle\" ?")
speed = int (input())
while speed != 0 :
    if speed >= 1 and speed <= 60 :
        print ("Good you are following the \"Traffic Rules\" ")

    elif speed >60 and speed <=80 :
        print ("Oh ! It is \"Over Speed\". Please go slow. ")

    elif speed >80 and speed <400 :
        print ("Dager!! Red Alert!! Please stop your \"Vehicle\" ")

    elif speed >=400 :
        print ("What?? There is No such \"Speed!\" ")

    print ("  ")
    print("What is the \"Speed\" of your \"Vehicle\" ?")
    speed = int (input())

print ("Thank you 🙏. Your \"Vehicle\" is Ideal")


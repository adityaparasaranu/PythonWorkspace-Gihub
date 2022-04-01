name = input('Enter your good name Sir/Madam : ')

capital = name.upper()
remove_white_space = capital.strip()
if remove_white_space == 'ADITYA' :
    checking_hero = input("Hi Sir , You are a Hero right? ")
    remove_white_space_2 = checking_hero.strip()
    capital_2 = remove_white_space_2.upper()
    if capital_2 == 'YES' :
        print("Yes I know well. I am pleasure in meeting you sir.")
        quit()
elif remove_white_space == 'ARAVIND' :
    print ("You are a Hero's elder brother. You are lazy. So the program crashed")
    quit()
elif remove_white_space == 'ULAGANATHAN' :
    print ("You are a Hero's Father right. I am very happy in meeting you")
    quit()
else:
    print ("I don't know whom you are. So the program ended.")
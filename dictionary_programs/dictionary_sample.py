month = {'JANUARY' : 31 ,
         'FEBRUARY': 28 ,
         'MARCH' : 31 ,
         'APRIL': 30 ,
         'MAY' : 31 ,
         'JUNE' : 30 ,
         'JULY' : 31 ,
         'AUGUST': 31 ,
         'SEPTEMBER' : 30 ,
         'OCTOBER' : 31 ,
         'NOVEMBER' : 30 ,
         'DECEMBER' : 31}

month_input = input("Enter a month to find its days : ")

capital = month_input.upper()

checking = capital in month

if checking == True :
    value = month.get(capital)
    print('The month' , month_input , 'has' , value , 'days')

elif checking == False :
    remove_whitespace = month_input.strip()
    capital_2 = remove_whitespace.upper()
    checking_2 = capital_2 in month
    if checking_2 == True :
        value2 = month.get(capital_2)
        print ('The month' , remove_whitespace , 'has' , value2 , 'days')
    elif checking_2 == False :
        while checking_2 == False :
            input_2 = input("Please enter the month name properly : ")
            capital_2 = input_2.upper()
            checking_2 = capital_2 in month
            value_3 = month.get(capital_2)
            if checking_2 == True :
                print('The month' , input_2 , 'has' , value_3 , 'days')
                quit()
            else:
                remove_whitespace = input_2.strip()
                capital_2 = remove_whitespace.upper()
                checking_2 = capital_2 in month
                if checking_2 == True:
                    value2 = month.get(capital_2)
                    print('The month', remove_whitespace, 'has', value2, 'days')
                    quit()
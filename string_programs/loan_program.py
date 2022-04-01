print ("Do you want to know how much loan you can get from \"ARADI\" Bank ?")
print ("Enter your \"Name\" ")
name = input()
print ("Enter your \"Salary\" without \"Commas\" ")
salary = int (input())
print ("How much loan do you want? Enter the number without \"Commas\" ")
loan = int (input())
total = salary * 24
if loan  <=total :
    print (name , "the loan you asked can be given 👍")
else:
    print ("According to \"ARADI\" Bank rules a person can be given loan only below or equal to his \"2 Years Salary\"")
    print ("Sorry 😩" , name ,",the loan you asked cannot be given . You can only ask loan below" , total ,"or equal to" , total ,)
    print ("Thank" , name ,", for asking loan in our \"Bank\" 🙏")
class Calc :
    def addition(__self__, num1, num2) :
        print("The Addition of two is : ", num1 + num2)
    def subraction(__self__,num1, num2) :
        print("The Subraction of two is : ", num1 - num2)
    def multplication(__self__,num1, num2) :
        print("The Multiplication of two is : ", num1 * num2)
    def division(__self__,num1, num2) :
        print("The Division of two is : ", num1 / num2)

calc = Calc()

calc.addition(100 , 1)

num = int(input("Enter a number : "))

def finalOutput(num) :
    sum = 0
    for i in range (num + 1) :
        sum = sum + i
    print(sum)

finalOutput(num)
# def finalOutput(num):
#     if True :
#         sum = 0
#     print("num", num)
#     if num > 1:
#         finalOutput(num-1)
#         print("sum" , sum)
#     return sum
#
# print(finalOutput(num))

print ("Weight : ")
weight = int (input())
print ("Enter (K) if you have entered your weight in Kilogram and Enter (L) if you have entered your weight in Pound :")
ww = input()
if ww == "l" :
    print (weight * 453 , "g")
if ww == "L" :
    print (weight * 453 , "g")
elif ww == "k" :
    print (weight * 1000 , "g")
elif ww == "K" :
    print (weight * 1000 , "g")


x = "apple"  
y = "orange"  
z = "limon"
basket = x + " " + y + " " + z
#returns concatenated multiple strings
print(basket)

thebasket="apple orange limon"
#split a single string into words based on whitespace
print(thebasket.split())
#slicing a single string into words  
print(thebasket[0:5] +" "+thebasket[6:12] +" "+ thebasket[13:18])

the_basket="apple ,orange ,limon"
#split a single string into words based on (,)
print(the_basket.split(","))
#store the substring words in variables then displays them each in a new line 
a,b,c=the_basket.split(",")
print(a)
print(b)
print(c)

#store the substring words in variables then displays them using for loop
theBasket=the_basket.split(",")
for i in theBasket :
	print(i)

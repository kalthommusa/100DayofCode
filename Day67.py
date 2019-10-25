fletter=input("Enter your first letter of your name: ")
lletter=input("Enter your last letter of your name: ")
txt="Your name starts with the letter {} and ends with the letter {}"
print(txt.format(fletter, lletter))
#create an empty list 
lst=[]
#ask the user to enter a number of elemetns  
length=int(input("How many numbers you want to enter into your list: "))
print("OK, Enter the numbers: ")
#iterating till the range 
for i in range(0,length):
	num=int(input())
	#adding the element 
	lst.append(num)
print("Your list elements:",lst)

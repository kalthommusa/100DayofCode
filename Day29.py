x=["Successfully " , "passed" , "Day29"]
#prints each string in the list
for i in x:
	print(i)

#prints the charactere of the srting
for i in "Day29":
	print(i)

#exit the loop when i is "Day29"	
for i in x:
    if i == "Day29":
       break
    print(i)    

#skips "passed" and continue to the next
for i in x:
    if i == "passed":
        continue
    print(i) 


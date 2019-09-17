#while loop counter
i=1
"""
prints string $ i as long as i is less than 100
and prints a diffirint string when i is equal 100
"""
while i < 100:
	print("Day{}".format(i)+" "+"Keep learning, Happy coding")
	i+=1
	if i == 100:
		print("Congrats! you did it, {} Days Of Code".format(i))

#exit the loop when i is equal 28
while i < 100:
	print("Day{}".format(i)+" "+"Keep learning, Happy coding")
	if i == 28:
		print("break statement, the loop will stop now")
		break
	i+=1

#skips the current iteration and continue with the next when i is equal 28
while i < 100:
	print("Day{}".format(i)+" "+"Keep learning, Happy coding")
	i+=1
	if i == 100:
		print("Congrats! you did it, {} Days Of Code".format(i))
	if i == 28:
		print("continue statement")
		continue

#prints else statement when the condition is not true
while i < 100:
	print("Day{}".format(i)+" "+"Keep learning, Happy coding")
	i+=1
else:
	print("Congrats! you did it, {} Days Of Code".format(i))

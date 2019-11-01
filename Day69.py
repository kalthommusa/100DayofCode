import os

#open the file "demofile.txt" and read it
day69=open("demofile.txt","rt")
print(day69.read())
#Return the 6 first characters of the file
day69=open("demofile.txt","rt")
print(day69.read(6))
#Read one line of the file
day69=open("demofile.txt","rt")
print(day69.readline())
#Read two lines of the file
day69=open("demofile.txt","rt")
print(day69.readline())
print(day69.readline())
#Loop through the file line by line
day69=open("demofile.txt","rt")
for i in day69:
	print(i)
#Close the file when you are done with it
day69.close()

#Open the file "demofile2.txt" and append content to the file
day69=open("demofile2.txt","a")	
day69.write("Now the file has more content!")
day69.close()
#open the file "demofile.txt" and read it
day69=open("demofile2.txt","rt")
print(day69.read())

#Open the file "demofile3.txt" and overwrite the content
day69=open("demofile3.txt","w")	
day69.write("Woops! I have deleted the content.")
day69.close()
#open the file "demofile.txt" and read it
day69=open("demofile3.txt","rt")
print(day69.read())

#Create a new empty file called "myfile.txt"
day69=open("myfile.txt","x")
#Create a new file if it does not exist
day69=open("myfile2.txt","w")

#Remove the file "myfile.txt"
os.remove("myfile.txt")
day69=open("myfile.txt","rt")
print(day69.read())
#Check if file exists, then delete it
if os.path.exists("myfile2.txt"):
	os.remove("myfile2.txt")
else:
	print("The file does not exist")
day69=open("myfile2.txt","rt")
print(day69.read())

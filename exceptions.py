#Shea Wissler
#python exceptions let you deal with unexpected results
try:
	print(a) 		#this will throw an exception scince a is not defined
except:
	print("a is not defined!")

#there are specific errors to help with cases
try:
	print(a)	#this will thow an exception scince a is not defined
except NameError:
	print("a is still not defined!")
except:
	print:("Something else sent wrong.")

#this will break the program since a is not defined
print(a)
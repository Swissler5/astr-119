#Shea Wissler

import numpy as np			#imports numpy into the code and refers to it as np

def main():
	i = 0 				#i is a variable definted by an integer
	n = 10				#n is an example of another integer
	x = 119.0			#x is an example of a float

	#use numpy to declare arrays

	y = np.zeros(n,dtype=float)		#declares an array with 10 floating point numbers


	for i in range(n):				#array is inbetween [0, n-1]
		y[i] = 2.0 * float(i) +1	#set y[i] to change array by y = 2i + 1


	for y_element in y:			#prints items in array to the terminal
		print(y_element)


if __name__ == "__main__":		#run main function in terminal
	main()
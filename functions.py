#Shea Wissler
import numpy as np
import sys

#define a funtion
def expo(x):
	return np.exp(x)	#return np e^x function

#define a subroutine that doesn't give a value
def show_expo(n):
	for i in range(n):
		print(expo(float(i)))	#call the expo function

# define a main function
def main():
	n = 10		#gives n a default value

	#check if theres a command line argument provided in the terminal
	if (len(sys.argv)>1):
		n = int(sys.argv[1])  #use argument for n if provided in terminal

	show_expo(n) 	#call the show_expo subroutine

#run the function
if __name__ == "__main__":
	main()
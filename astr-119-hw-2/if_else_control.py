#Shea Wissler
#define a function
def flow_control(k):

	#define string based on k
	if(k==0):
		s = "Variable k = %d equals 0." % k

	elif(k==1):
		s = "Variable k = %d equals 1." % k

	else:
		s = "Variable k = %d does not equal 0 or 1." % k

	#print the variable
	print(s)

#define a main function
def main():

#declare an integer
	i = 0
	flow_control(i)

	#try flow_control for 1, 2
	i = 1
	flow_control(i)
	i = 2
	flow_control(i)

#run the program
if __name__ == "__main__":
	main()
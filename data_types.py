#Shea Wissler
import numpy as np

#integers
i = 10		#integer
print(type(i)) #print the data type of i

a_i = np.zeros(i,dtype=int) #declare an array of integers
print(type(a_i)) 		#returns ndarray
print(type(a_i[0])) 	#returns int64

#floats

x = 119.0 		#floating point number
print(type(x)) 	#print the data type of x

y = 1.19e2 	#scientific notation of float 119
print(type(y))

z = np.zeros(i,dtype=float)  #declare an array of floats
print(type(z))				##returns ndarray
print(type(z[0])) 			#returns int64
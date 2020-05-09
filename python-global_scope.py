# define a global variable "num"
num = 10
def increment_it():
	# to update it inside local scope, use global 
	global num
	num+=1
	return num
increment_it()



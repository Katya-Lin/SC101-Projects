"""
File: weather_master.py
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


def main():
	"""
	Enable the user to input the temperatures. If the user input -100, it will stop and show
	the highest, the lowest and average temperature. Eventually, it'll show the days that under 16 degrees.
	"""
	intro()
	Temperature()


def intro():
	print("stanCode \"Weather Master 4.0\"!")

def Temperature():
	input_list=[]  # create a list for input
	n=int(input("Next temperature(or-100 to quit)?"))
	input_list.append(n) # append the first input

	if n==(-100):
		print("No temperatures were entered")
	while n >(-100):
		n=int(input("Next temperature(or -100 to quit)?"))
		input_list.append(n)  # append the inputs

	input_list_new=input_list[0:(len(input_list)-1)] # the list which -100 is excluded

	print("Highest temperature:"+str(max(input_list_new)))  # highest temperature
	print("Lowest temperature:"+str(min(input_list_new)))   # lowest temperature

	sum=0
	time = 0
	for i in range(len(input_list_new)):
		sum+=input_list_new[i]      # average temperature
		if input_list_new[i]<16:    # find cold day(s)
			time+=1
	print("Average:"+str(sum/len(input_list_new)))
	print(str(time) + " cold day(s)")








###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()

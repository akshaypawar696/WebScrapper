import re
import sys
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt 

def main():
	city = []
	temp = []
	length = len(sys.argv)

	for i in range(1,length):
		cityName = sys.argv[i]
		city.append(cityName)
	#city.pop(0)
	#Here above for loop starts from 1 because sys.argv[0] contains the module name that is "temp.py"

	for i in city:
		cityTemp = findTemp(i)
		cityTemp = int(re.sub('[^1234567890 ]+', '',cityTemp))
		temp.append(cityTemp)

	print(city)
	print(temp)

	plt.plot(city, temp) 
	plt.xlabel('cities') 
	plt.ylabel('temperature') 
	plt.title('City-Temperature Graph') 	  
	plt.show() 

def findTemp(city):
	l = "https://www.google.com/search?q={}"
	q = "tempature of {} today"
	query = l.format(q.format(city))	
	r = requests.get(query)
	s = BeautifulSoup(r.text,"html.parser")
	return s.find("div",class_="iBp4i").text

if __name__=="__main__":
	if(len(sys.argv) == 1):
		print("Give city names through command line...")
		exit()
	if(sys.argv[1] == "h" or sys.argv[1] == "H"):
		print("This module returns graph of temperature of given cities...")
		exit()
	if(sys.argv[1] == "u" or sys.argv[1] == "U"):
		print("Give at list two city name through command line")
		exit()
	if(len(sys.argv) <= 2):
		print("Please enter at least two cities....")
		exit()
	main()







	

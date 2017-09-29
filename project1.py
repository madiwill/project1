import os
import filecmp

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.
	x = open(file)
	lst = []
	for key in x:
		s = {}
		key = key.rstrip()
		key = key.split(",")
		s["First"]=key[0]
		s["Last"]=key[1]
		s["Email"]=key[2]
		s["Class"]=key[3]
		s["DOB"]=key[4]
		lst.append(s.copy())
	return (lst)


#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	first_name = ""
	last_name = ""
	fullname = ""
	

	if col == "First":
		a = sorted(data, key=lambda x: x["First"], reverse= True)
		for name in a:
			first_name = name["First"]
			last_name = name["Last"]
			fullname = first_name + " " + last_name

	elif col == "Last":
		a = sorted(data, key=lambda x: x["Last"], reverse= True)
		for name in a:
			first_name = name["First"]
			last_name = name["Last"]
			fullname = first_name + " " + last_name

	elif col== "Email":
		a = sorted(data, key=lambda x: x["Email"], reverse= True)
		for name in a:
			first_name = name["First"]
			last_name = name["Last"]
			fullname = first_name + " " + last_name
	
	
	return fullname
	
#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
	tup = []
	Freshman, Sophomore, Junior, Senior = 0,0,0,0

	for row in data:
		if row["Class"] == "Freshman":
			Freshman += 1

		elif row["Class"] == "Sophomore":
			Sophomore += 1

		elif row["Class"] == "Junior":
			Junior += 1

		elif row["Class"] == "Senior":
			Senior += 1

	tup.append(("Freshman", Freshman))
	tup.append(("Sophomore", Sophomore))
	tup.append(("Junior", Junior))
	tup.append(("Senior", Senior))

	return sorted(tup, key=lambda x: x[1], reverse = True)

	

# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	list_day=[]
	count_day={}
	for z in a:
		if z['DOB'] == 'DOB':
			pass
		else:
			
			bday = z['DOB']
			day = bday.split('/')
			list_day.append(day[1])
	
	for x in list_day:
		if x in count_day:
			count_day[x] += 1
		else:
			count_day[x] = 1

	srt = sorted(count_day.items(), key = lambda x: x[1], reverse = True)

	return int(srt[0][0])



# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB
	
	list_age=[]
	
	for z in a:
		if z['DOB'] == 'DOB':
			pass
		else:
			bday = z['DOB']
			day = bday.split('/')
			year = (2017-int(day[2]))
			list_age.append(2017 - year)

	return sum(list_age)//len(list_age)



#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	outfile = open(fileName, 'w')

	if col == "First":
		b = sorted(a, key=lambda x: x["First"])
		for name in b:
			outfile.write(name['First'] + ',' + name['Last'] + ',' + name['Email'] + '\n')

	elif col == "Last":
		b = sorted(a, key=lambda x: x["Last"])
		for name in b:
			outfile.write(name['First'] + ',' + name['Last'] + ',' + name['Email'] + '\n')

	elif col == "Email":
		b = sorted(a, key=lambda x: x["Email"])
		for name in b:
			outfile.write(name['First'] + ',' + name['Last'] + ',' + name['Email'] + '\n')		
	outfile.close()
	

################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()


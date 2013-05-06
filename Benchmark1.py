"""
	This code tries to consider authors who have same name and affliation as the same one.
	
	Input: 
			Author.csv
	Output:
			Benchmark1.csv
				format: 
					Author ID, Duplicated Author ID
			
	Author: Yifan Li
	Version: 0.0.1

"""
import csv as csv

#Read the 'Author.csv' file
Author_object =csv.reader(open('C:\Users\Eagles2F\Desktop\DionyBuddy\data\dataRev2\Author.csv','rb'))
header = Author_object.next() #Skip the first line as it is a header
Author = [] #Creat a variable called 'Paper'
for row in Author_object: #Skip through each row in the csv file
    Author.append(row)#adding each row to the data variable
Author_length = len(Author)
print "The size of Author is %d"%Author_length


#Initialize the duplicated author.
Duplicated_Author = [[a] for a in range(Author_length)] # 247203 is the number of author in Author.csv
index = 0
for author in Author:
	Duplicated_Author[index][0] = int(author[0])
	index = index + 1
print "Initialization Succeeds!"

#Find the duplicated author pair for each author ID
dup_pair = []

for host in Author:
	for guest in Author:
		if	host[1] == guest[1] and host[2] == guest[2]:
			dup_pair.append(int(host[0]))
			dup_pair.append(int(guest[0]))
			
#Scan the dup_pair to make Duplicated_Author
dup_length = len(dup_pair)/2
print "The dup_length is %d"%dup_length

index = 0
for p in dup_pair:
	if index%2 == 0:
		for a in Duplicated_Author:
			if p == a[0]:
				a.append(dup_pair[index+1])
	index = index + 1
#Write the result into file
with open('C:\Users\Eagles2F\Desktop\DionyBuddy\data\dataRev2\Benchmark1.csv','wb') as csvfile:
	write_file_object = csv.writer(csvfile)
	for t in Duplicated_Author:
		write_file_object.writerow(t)

print "Succeed!"
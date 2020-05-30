#The data we need to retrieve

# 1.The  total number of votes cast
# 2.A comlete list of candidates who received votes
# 3.The percentage of votes each candidates won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular votes


#Here are the dependencies (in this case Comma Seperated Values(CSV) and Operating System(OS))
import csv
import os


#Assign a variable to load file from a path 

file_to_load = os.path.join("Resources\election_results.csv")

#Assign a variable to save the file to a path

file_to_save = os.path.join("\Users\Analysis", "election_analysis.txt")

#Open and read the election result file using with open () method

with open(file_to_load) as election_data:

#Now we can read the file with reader function

    file_reader = csv.reader(election_data)

#After reading the file we can print each row

headers = next(file_reader)
    print(headers)

#for row in file_reader:
#     print(row)




 

outfile.close()

import datetime 
import csv
import os

now = datetime.datetime.now()
print("The current time is ", now )


file_to_load = os.path.join('Resources','election_results.csv')
#Open file in read only mode
#Method 1 to read and open file
#election_data = open(file_to_load, 'r')

# save file to analysis
file_to_save = os.path.join('analysis','election_analysis.txt')
#election_data.close()

#Method 2 to read and write file
with open(file_to_load) as election_data:
    #print(election_data)
    
    file_reader = csv.reader(election_data)

#Method 1 for Opening text file and add text to it
#outfile = open(file_to_save,'w')
#outfile.write('Hello World')
#outfile.close()

#Method2  for opening text file and writing 
#with open(file_to_save,'w') as txt_file:
 #   txt_file.write('Arapahoe\nDenver\nJefferson')



#for header in file_reader:
    headers = next(file_reader)

    #print and read header from csv file
    print(headers)
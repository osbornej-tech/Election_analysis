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

#initailize a votes counter
total_votes = 0

candidate_options = []

#Create empty dictionary to add candidate info
candidate_votes = {}

#Method 2 to read and write file
with open(file_to_load) as election_data:
    #print(election_data)
    #read in CSV file
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
    #print(headers)

    #print rows of the Csv file 
    for row in file_reader:
        total_votes += 1
       
       #add candidate name starting from row two
        candidate_name = row[2]
        
        #add unique candidate names to list
        if candidate_name not in candidate_options:
        #add candidates to list
         candidate_options.append(candidate_name)
         
         #track candidate vote count
         candidate_votes[candidate_name] = 0

        # add a vote for each time the candidate name appear
        candidate_votes[candidate_name] += 1

#percentage of votes 
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes)/float(total_votes)*100

    winning_candidate =''
    winning_count = 0
    winning_percentage = 0

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
    
    # To do: print out the winning candidate, vote count and percentage to
    # terminal.
        print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')

        
winning_candidate_summary = (
    f'----------------------------\n'
    f'Winner: {winning_candidate}\n'
    f'Winning vote Count: {winning_count:,}\n'
    f'Winning Percentage: {winning_percentage:.1f}% \n'
    f'----------------------------\n'
)
print(winning_candidate_summary)
    # 

   # print(f'{candidate_name}: received {vote_percentage:.1f}% of the votes')



#print(candidate_options)
print(total_votes)
print(candidate_votes)

#first vote greater than zero


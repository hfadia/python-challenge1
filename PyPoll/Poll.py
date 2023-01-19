# Create the file object
file_name = 'election_data.csv'
file_object = open(file_name, 'r')

# create a raw data list with each line in the file
raw_data_list = [ ]
for each_line in file_object:
  raw_data_list.append(each_line)
file_object.close()

# strip off the first element which is a header
raw_data_list = raw_data_list[1:]

# calculate the total months = length of the list
total_votes = len(raw_data_list)

# split the data into date and amount 
# and create a new list with these two values
processed_data_list = [ ]
for each_line in raw_data_list:
  three_tokens = each_line.split(',')
  Ballot = three_tokens[0]
  County = three_tokens[1]
  Candidate = three_tokens[2]
  Ballot = int(Ballot)
  processed_data_list.append([Ballot, County, Candidate])

# Loop through the processed list
# and calculate the min, max and averages.

total = 0
max_amount = 0
min_amount = 2000000
for each_data_point in  processed_data_list:
  current_date = each_data_point[0]
  current_amount = each_data_point[1]
  total = total + each_data_point[1]

  # check for the max
  if (current_amount > max_amount):
    max_amount = current_amount
    max_date = current_date 

    # check for the min
  if (current_amount < min_amount):
    min_amount = current_amount
    min_date = current_date 



#========== final output comes from this section

print('Election Results')
print('----------------------------')

# 369711
print('Total Votes:', total_votes)

 
 
 #Charles Casper Stockham: 23.049% (85213)
  #Diana DeGette: 73.812% (272892)
  #Raymon Anthony Doane: 3.139% (11606)

print('Charles Casper Stockham:'+ str(total)) 
print('Diana DeGette:'+ str(total)) 
print('Raymon Anthony Doane:'+ str(total)) 





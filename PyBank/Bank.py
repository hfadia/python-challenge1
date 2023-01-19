# Create the file object
file_name = 'budget_data.csv'
file_object = open(file_name, 'r')

# create a raw data list with each line in the file
raw_data_list = [ ]
for each_line in file_object:
  raw_data_list.append(each_line)
file_object.close()

# strip off the first element which is a header
raw_data_list = raw_data_list[1:]

# calculate the total months = length of the list
total_months = len(raw_data_list)

# split the data into date and amount 
# and create a new list with these two values
processed_data_list = [ ]
for each_line in raw_data_list:
  date_amount_tokens = each_line.split(',')
  date = date_amount_tokens[0]
  amount = date_amount_tokens[1]
  amount = int(amount)
  processed_data_list.append([date, amount])

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


# average is the total divided by number of entries
average = total / total_months 


#========== final output comes from this section

print('Financial Analysis')
print('----------------------------')

# 86
print('Total Months:', total_months)

 # $22564198
print('Total: $' + str(total)) 

print('Average Change: $' + str(average))   #-8311.11


#  Aug-16 ($1862002)
print('Greatest Increase in Profits:' + str(max_date) + '($' + str(max_amount) + ')' ) 


# print('Greatest Decrease in Profits: Feb-14 ($-1825558)
print('Greatest Decrease in Profits:' + str(min_date) + '($' + str(min_amount) + ')' ) 


     

  
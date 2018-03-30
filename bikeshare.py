## TODO: import all necessary packages and functions
import pandas as pd
import numpy as np
import datetime
## Filenames
city_data = {	'chicago': 'chicago.csv',
				'new york': 'new_york_city.csv',
				'washington': 'washington.csv'	}

while True:
	city = (str(input('\nHello! Let\'s explore some US bikeshare data!\n'
    	 	     	'Would you like to see data for Chicago, New York, or Washington?\n'))).lower()
    if city not in ('chicago', "new york", 'washington'):
        print("Not a valid city. Let's try again!")
    else:
        break
    
while True:
    month = (str(input('\nPlease enter the specific month you want to explore the data!\n'
     		      	'January, February, March, April, May, June or "all".\n'))).lower()
    if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
        print("Not a valid month. Let's try again!")
    else:
        break

while True:
    day = (str(input('\nPlease enter the specific day you want to explore the data!\n'
            	'Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or "all".\n'))).lower()
    if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
        print("Not a valid day. Let's try again!")
    else:
        break    
        
# load data file into a dataframe
df = pd.read_csv(city_data[city])

# convert the Start Time column to datetime
df['Start Time'] = pd.to_datetime(df['Start Time'])

# extract month and day of week from Start Time to create new columns
df['month'] = df['Start Time'].dt.month
df['day_of_week'] = df['Start Time'].dt.weekday_name

# filter by month if applicable
if month != 'all':
# use the index of the months list to get the corresponding int
	months = ['january', 'february', 'march', 'april', 'may', 'june']
	month = months.index(month)+1

# filter by month to create the new dataframe
	df = df[df['month'] == month]

# filter by day of week if applicable
if day != 'all':
# filter by day of week to create the new dataframe
	df = df[df['day_of_week'] == day.title()]

 #Finding Most Common data in column 
def most_common(col_name):
  most_common_data = col_name.mode()[0]
  return most_common_data

#Print prompt
print ('\nCalculating...\n')
### 1. POPULAR TIME TO TRAVEL (i.e., occurs most often in the start time) ###
#most common month
if month == 'all':
  df['month'] = df['Start Time'].dt.strftime('%B')
  print ('Most Common Month:', most_common(df['month']))
#most common day of week
if day == 'all':
  df['day'] = df['Start Time'].dt.weekday_name
  print ('Most Common Month:', most_common(df['day']))

#most common hour of day
# extract hour from the Start Time column to create an hour column and find the most popular hour
df['hour'] = df['Start Time'].dt.strftime('%I %p')
print('Most Popular Start Hour:', most_common(df['hour']))

### 2. POPULAR STATIONS AND TRIP ###
#most common start station
print ('Most Common Start Station:', most_common(df['Start Station']))
#most common end station
print ('Most Common End Station:', most_common(df['End Station']))
#most common trip from start to end (i.e., most frequent combination of start station and end station)
dff = df.groupby(['Start Station','End Station']).size().reset_index().rename(columns={0:'count'})

print ('\n Most common trip from start to end:\n', dff.loc[dff['count'].argmax()], '\n')

### 3 TRIP DURATION ###
#total travel time
total_hours_travel = df['Trip Duration'].sum()/3600
print ('Total travel time (hrs):', int(total_hours_travel))
#average travel time
avg_travel = df['Trip Duration'].mean()/60
print ('Average travel time (mins):', int(avg_travel))
### 4 USER INFO ###
#counts of each user type
user_type = df.groupby(['User Type']).size().reset_index().rename(columns={0:'count'})
print ('\n',user_type)
#counts of each gender (only available for NYC and Chicago)
if city in ('chicago', "new york"):
  gender  = df.groupby(['Gender']).size().reset_index().rename(columns={0:'count'})
  
  
#earliest, most recent, most common year of birth (only available for NYC and Chicago)
  oldest = int(df['Birth Year'].min())
  youngest = int(df['Birth Year'].max())
  common = int(df['Birth Year'].mode()[0])
  print ('\n',gender)
  print ('\n Year of birth - Earliest: {}, most recent: {}, most common: {}\n'.format(oldest, youngest, common))


  
  
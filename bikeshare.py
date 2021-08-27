import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
              
MONTH_DATA = ['january', 'february', 'march',
             'april', 'may', 'june', 'all']

DAY_DATA = ['monday', 'tuesday', 'wednesday',
            'thursday', 'friday', 'saturday',
            'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for Chicago, New York City or Washington?\n').lower()
        if city not in CITY_DATA:
            print("\nplease enter a valid value\n")
            continue
        else:
            print('\nYour stats will be on: {}\n'.format(city))
            break
            
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month do you want to filter the data with? All, January, Feburary, March, April, May or June?\n').lower()
        if month in MONTH_DATA:
            print('\nYour stats will be on: {}\n'.format(month))
            break
        else:
            print ('Please check your answer. It should be between January and June, or  All.')
            
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day? All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday?\n").lower()
        if day in DAY_DATA:
            print('\nYour stats will be on: {}\n'.format(day))
            break
        else:
            print ('Please check your answer. It should be day of week, or  All.')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month = MONTH_DATA.index(month) +1
        df = df.loc[df['month'] == month]

    if day != 'all':
        df = df.loc[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month:', (common_month))

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day:', (common_day))

    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('Most common hour:', (common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('Most common start station:', (common_start))

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('Most common end station:', (common_end))

    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_combination = df['combination'].mode()[0]
    print('Most combination of start and end stations trip:', (common_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print('Total travel time:', (total_travel))

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('Mean travel time:', (mean_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types:', (user_types))

    # Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print('Counts of user gender:', (gender))
    else:
        print("There is no gender data for this city.")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()
        print('Earliest year:', int(earliest_year),'\n' 'Recent year:', int(most_recent_year),'\n' 'Most common year:', int(most_common_year))
    else:
        print('There is no birth year data for this city')
        
        print('\nThis took %s seconds.' % (time.time() - start_time))
        print('-'*40)
        
    # get input from user to show more rows or not
def display_raw_data(df):
   pd.set_option('display.max_columns',200)
   print(df.head()) 
   next = 0     
   while True:
        view_more = input('\nWould you like to see more data? Enter yes or no.\n').lower()
        if view_more == 'no':
           break
        elif view_more == 'yes':
           next = next + 5
           pd.set_option('display.max_columns',200)
           print(df.iloc[next:next+5])
        else:
           print('Please check your input, Should be yes or no.')
            
     # get input from user to restart or exit the program
def restart():
   while True:
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart == 'no':
            print ('Thankyou, Goodbye.')
            exit()
        elif restart == 'yes':     
            print ('Restarting...\n')
            main()
        else:
            print('Please check your input, Should be yes or no.')
            
      # main program      
def main():
   while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        restart()
            


if __name__ == "__main__":
	main()

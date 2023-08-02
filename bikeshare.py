import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    x=0
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while x==0:
        city=input("Please specify the city (chicago, new york city, washington) you want to see data for?")
        city=city.lower()
        if city=='chicago' or city=='new york city' or city=='washington':
            x=1
        else:
            print("Wrong Input. Please try again")

    # TO DO: get user input for month (all, january, february, ... , june)
    x=0
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while x==0:
        month=input("Please enter the month (all, january, february, ... , june) you want to see data for?")
        month=month.lower()
        if month=='all' or month=='january' or month=='february' or month=='march' or month=='april' or month=='may' or month=='june':
            x=1
        else:
            print("Wrong Input. Please try again")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    x=0
    while x==0:
        day=input("Please specify the week (all, monday, tuesday, ... sunday) you want to see data for?")
        day=day.lower()
        if day=='all' or day=='monday' or day=='tuesday' or day=='wednesday' or day=='thursday' or day=='friday' or day=='saturday' or day=='sunday':
            x=1
        else:
            print("Wrong Input. Please try again")

    print(f"\nYou have chosen to view data for city: {city.upper()}, month/s: {month.upper()} and day/s: {day.upper()}.")
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
    print("\nLoading data...")
    df = pd.read_csv(CITY_DATA[city])

    #Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #Filter by month if applicable
    if month != 'all':
        #Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        #Filter by month to create the new dataframe
        df = df[df['month'] == month]

    #Filter by day of week if applicable
    if day != 'all':
        #Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    #Returns the selected file as a dataframe (df) with relevant columns
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month=df['month'].mode()[0]

    print(f'\nMost Popular Month (1 = Jan,...,6 = Jun): {popular_month}')

    # TO DO: display the most common day of week
    popular_day=df['day_of_week'].mode()[0]

    print(f'\nMost Popular Day: {popular_day}')

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour=df['hour'].mode()[0]

    print(f'\nMost Popular hour: {popular_hour}')

    print(f'\nThis took %s seconds. {(time.time() - start_time)}seconds')
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    print(f'The most common used Start station was {start_station} and end station was {end_station}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()

    print(f'Total Travel Time comes to be {total_travel_time}')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print(f'Mean Travel Time comes to be {mean_travel_time}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()

    print(f'The count of types of users :\n\n{user_type_count}')

    # TO DO: Display counts of gender
    #Handling nulls/no gender found in some csv
    try:
        gender = df['Gender'].value_counts()
        print(f'\nThe count of users by gender:\n\n{gender}')
    except:
        print('\nThere is no Gender column in this file.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = int(df['Birth Year'].min())
        recent_year = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f'\nThe earliest year of birth: {earliest_year}\nThe most recent year of birth: {recent_year}\nThe most common year of birth: {common_year}')
    except:
        print('No birth year details found in this file.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):

    #Showing head(first 5 rows)
    response = ['yes','no']
    rawdata = ''
    counter=0

    while rawdata not in response:
        print('/nDo you wish to view the raw data(Yes or No)?')
        rawdata=input().lower()
        if rawdata=='yes':
            print(df.head())
        elif rawdata not in response:
            print('\n Please check input, need to be accepted values')

    while rawdata=='yes':
        print('\n Do you wish to see more raw data?')
        counter+=5
        rawdata=input().lower()
        if rawdata == "yes":
            print(df[counter:counter+5])
        elif rawdata != "yes":
            break

    print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()

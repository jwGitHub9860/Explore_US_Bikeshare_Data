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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ""
    while city != "chicago" and city != "new york city" and city != "washington":
        city = input("Please choose one of the following cities (chicago, new york city, washington): ")
        city = city.lower()

    # get user input for month (all, january, february, ... , june)
    month = ""
    while month != "all" and month != "january" and month != "february" and month != "march" and month != "april" and month != "may" and month != "june" and month != "july" and month != "august" and month != "september" and month != "october" and month != "november" and month != "december":
        month = input("Please choose one of the following months (all, january, february, ... , june): ")
        month = month.lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = ""
    while day != "all" and day != "monday" and day != "tuesday" and day != "wednesday" and day != "thursday" and day != "friday" and day != "saturday" and day != "sunday":
        day = input("Choose a day of the week (all, monday, tuesday, ... sunday): ")
        day = day.lower()

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
    df = pd.read_csv(CITY_DATA[city])  # load data file into a dataframe

    df['Start Time'] = pd.to_datetime(df['Start Time'])     # converts string to DateTime object (ex. String: 2001-12-24 12:38 ---> DateTime: 2001-12-24 12:38:00)

    df['month'] = df['Start Time'].dt.month  # creates new column containing months of 'Start Time'
    df['day'] = df['Start Time'].dt.weekday_name     # creates new column containing weekdays of 'Start Time'

    if month != "all":
        month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        month = month_list.index(month) + 1   # obtains number corresponding to month
        df = df[df['month'] == month]  # filters by month

    if day != "all":
        df = df[df['day'] == day.title()]  # filters by day

    # code for 'def time_stats(df)' function
    df['Start Hours'] = df['Start Time'].dt.hour     # creates new column holding "Start Hours"

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['month'].value_counts()
    most_common_month = df['month'].mode()[0]   # finds most common month
    print("Most Common Month:", most_common_month)

    # display the most common day of week
    df['day'].value_counts()
    most_common_day = df['day'].mode()[0]   # finds most common day of week
    print("Most Common Day of the Week:", most_common_day)

    # display the most common start hour
    df['Start Hours'].value_counts()
    most_common_start_hour = df['Start Hours'].mode()[0]   # finds most common start hour
    print("Most Common Start Hour:", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()



    # display most commonly used start station
    #common_start_section = pd.dat

    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

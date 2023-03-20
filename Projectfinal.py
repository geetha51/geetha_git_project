# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 22:30:01 2023

@author: sangi
"""

import time
import datetime
import pandas as pd
import numpy as np
from colorama import Fore
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
   
    print(Fore.RED + 'Welcome to the US bikeshare database!')
	
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city','washington']
    try:
        city = input (Fore.RED + 'What city would you like to explore? Chicago, New York City or Washington? ').lower()
        while (city not in cities):
            print(Fore.BLUE + 'You entered ',city,'. Please try again as this city if not among the provided options.')
            city = input(Fore.RED + 'Please choose a valid city: Chicago, New York City or Washington? ').lower()
        print(Fore.BLUE + 'You selected ',city,'. Thank you for your input.')
    except KeyError:
            print('Error Encountered')
	
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all','january','february','march','april','may','june']
    try:
        month = input(Fore.RED + 'What month would you like to look at? All, January, February, March, April, May or June? ').lower()
        while (month not in months):
            print(Fore.BLUE + 'You entered ',month,'. Please try again as the month is not among the provided options.')
            month = input(Fore.RED + 'Choose either a month from January to June, or choose All? ').lower()
        print(Fore.BLUE + 'You selected ',month,'. Thank you for your input.')
    except KeyError:
            print ('Error Encountered')
	
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)	
    days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    try:
        day = input (Fore.RED + 'What day of the week would you like to explore? All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday? ').lower()
        while (day not in days):
            print(Fore.BLUE + 'You entered',day,'. Please try again as the month is not among the provided options.')
            day = input(Fore.RED + 'Please choose a valid city: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All? ').lower()
        print(Fore.BLUE + 'You selected ',day,'. Thank you for your input.')
    except KeyError:
        print('Error Encountered')
    print(Fore.WHITE + '~'*40)
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
	
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['year']= df['Start Time'].dt.year
    df['month']= df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month)+1
        df=df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print(Fore.RED + '\nCalculating The Most Frequent Times of Travel\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print(Fore.BLUE + 'The most common month of travel: ', common_month)
    
 
    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    common_day_of_week = df['day_of_week'].mode()[0]
    print(Fore.BLUE + 'The most common day of week of travel: ',common_day_of_week)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(Fore.BLUE + 'The most common hour of travel: ',common_hour)
    print(Fore.BLUE + "\nThis took %s seconds." %round((time.time() - start_time),3))
    print(Fore.WHITE + '~'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print(Fore.RED + '\nCalculating The Most Popular Stations and Trip\n')
    start_time = time.time()
    common_start = df['Start Station'].mode()[0]
    print(Fore.BLUE + common_start)
	
    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print(Fore.BLUE + common_end)
	
    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + df['End Station']
    common_combination = df ['combination'].mode()[0]
    print(common_combination)
    print(Fore.BLUE + "\nThis took %s seconds." % round((time.time() - start_time),3))
    print(Fore.WHITE + '~'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print(Fore.RED + '\nCalculating Trip Duration\n')
    start_time = time.time()
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(Fore.BLUE + '\nTotal travel time: %s.'%str(datetime.timedelta(seconds = int(total_travel_time))))
	
    # TO DO: display mean travel time 
    average_travel_time = df['Trip Duration'].mean()
    print(Fore.BLUE + '\nThe average travel time: %s.'%str(datetime.timedelta(seconds = average_travel_time)))
    print(Fore.BLUE + "\nThis took %s seconds." % round((time.time() - start_time),3))
    print(Fore.WHITE + '~'*40)
def user_stats(df):
    """Displays statistics on bikeshare users."""
    print(Fore.RED + '\nCalculating User Stats\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print(Fore.BLUE + 'Number of users by type:{}/n',count_user_types)
    
    # TO DO: Display counts of gender
    try:
        count_gender = df['Gender'].value_counts()
        print(Fore.BLUE + 'Count of gender: ', count_gender)
    except KeyError:
        print(Fore.BLUE + 'No data is available for the selected city')    
    
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
        earliest_year = int(earliest_birth_year)
        print(Fore.BLUE + 'The earliest birth by year: ', earliest_year)
        most_recent_year = df['Birth Year'].max()
        recent_year = int(most_recent_year)
        print(Fore.BLUE + 'The most recent birth by year: ', recent_year)
        most_common_birth = df['Birth Year'].mode()[0]
        common_birth = int(most_common_birth)
        print(Fore.BLUE + 'The most common birth by year: ', common_birth)
    except KeyError:
        print(Fore.BLUE + 'Not available data')
    print(Fore.BLUE + "\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)
    
def view_chosen_data(df):
    viewer_choice = input(Fore.RED + '\nWould you like to view 5 individual rows of trip data? Enter Yes or No: \n').lower()
    choices = ['yes']
    view_steps = 0
    while (viewer_choice in choices):
        print( df.iloc[view_steps:view_steps+5])
        view_steps += 5
        viewer_choice = input(Fore.RED + 'Would you like to continue?: ').lower()
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_chosen_data(df)
        restart = input(Fore.RED + '\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()
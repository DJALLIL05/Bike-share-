import time
import pandas as pd
import numpy as np
import datetime

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
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # get user input for city (chicago, new york city, washington).
    while True :
        city = input('which city you want to explore chicago, new york city or washington: ').lower()
        if city not in CITY_DATA :
            print('please enter one of these three cities: chicago, new york city or washington\n')
        else :
            while True :
                print('you chose {} to explore'.format(city))
                proceed = input('if you want to change the city, type yes otherwise type no: ').lower()
                if proceed == 'yes' : break
                elif proceed == 'no' : break
                else : print('please enter yes or no ')
            if proceed == 'no' :break


    # get user input for month (all, january, february, ... , june)

    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = None
    while True :
        month_filter = input('\ndo you want to filter by month? enter yes or no: ').lower()
        if month_filter == 'yes' :
            month = input('available months are january, february, march, april, may and june enter the month you wish to filter by : ')
            if month not in months :
                print('please enter a month from january to june\n')
                month = None
            else : break
        if month_filter == 'no' : break
        if month_filter != 'yes' and month_filter != 'no' :
            print('please enter yes or no')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'monday', 'tuesday']
    day = None
    while True :
        day_filter = input('\ndo you want to filter by day? enter yes or no: ').lower()
        if day_filter == 'yes' :
            day = input('which day of the week you want to choose, please enter the full name of the day: ').lower()
            if day not in days :
                print('please enter a day of the week\n')
                day = None
            else : break
        if day_filter == 'no' : break
        if day_filter != 'yes' and day_filter != 'no' :
            print('please enter yes or no')


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != None:
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_idx = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month_idx]

    # filter by day of week if applicable
    if day != None:
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def display_raw_data (df) :
    start = 0
    while start != 5 :
        answer = input('would you like to see 5 lines of raw data: ').lower()
        if answer not in ['yes', 'no'] :
            print('please enter yes or no')
            continue
        elif answer == 'no' : break
        elif answer == 'yes' :
            display_data = answer
            print(df.iloc[start : start + 5])
            start += 5
        while display_data == 'yes' :
            answer = input('would you ike to see more 5 lines of raw data: ').lower()
            if answer not in ['yes', 'no'] :
                print('please enter yes or no')
                continue
            elif answer == 'yes' :
                print(df.iloc[start : start + 5])
                start += 5
            else : display_data = answer
        break


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if len(df['month'].unique()) == 1 :
        print('the most common month is:', df['month'].iloc[0])
    else :
        common_month = df['month'].mode()[0]
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        print('the most common month is:', months[common_month-1])

    # display the most common day of week
    if len(df['day_of_week'].unique()) == 1 :
        print('the most common day is:',df['day_of_week'].iloc[0])
    else :
        common_day = df['day_of_week'].mode()[0]
        print('the most common day is:',common_day)


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('the most common start hour is :',df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('the most commonly used start station is:',df['Start Station'].mode()[0])


    # display most commonly used end station
    print('the most commonly used end station is:',df['End Station'].mode()[0])


    # display most frequent combination of start station and end station trip
    df['start end combo'] = df['Start Station'] + ' and '+df['End Station']
    print('the most frequent combiation of start and end station trip is:',df['start end combo'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('the total travel time is:', datetime.timedelta(seconds = sum(df['Trip Duration'])))

    # display mean travel time
    print('the average travel time is:', datetime.timedelta(seconds = np.mean(df['Trip Duration'])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('the counts of users by type are as follows :')
    if len(df['User Type'].value_counts()) == 2 :
        print('\tSubscriber:',df['User Type'].value_counts()[0])
        print('\tCustomer:', df['User Type'].value_counts()[1])
    if len(df['User Type'].value_counts()) == 3 :
        print('\tSubscriber:',df['User Type'].value_counts()[0])
        print('\tCustomer:', df['User Type'].value_counts()[1])
        print('\tDependent:',df['User Type'].value_counts()[2])


    # Display counts of gender
    if 'Gender' not in df.columns :
        print('there are no information about the users gender')
    else :
        print('the counts of users by gender are as follows:')
        print('\tMale:',df['Gender'].value_counts()[0])
        print('\tFemale:',df['Gender'].value_counts()[1])


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df.columns :
        print('there are no information about users years of birth')
    else :
        print('some information about year of birth:')
        print('\tthe most recent year of birth:',df['Birth Year'].max())
        print('\tthe earliest year of birth:', df['Birth Year'].min())
        print('\tthe most commo year of birth:', df['Birth Year'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_raw_data (df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\n-----------------------------------------------')
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input("Please enter one of the following cities: Chicago, New York City, or Washington...  ").title()
        except KeyboardInterrupt:
            print("\nSorry, an error occurred.\n")
            continue
        if city not in ('Chicago', 'New York City', 'Washington'):
            print("Sorry, that's not an appropriate choice.\n")
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("\nOk!  Now enter one of the first six months of the year: Jan, Feb, Mar, Apr, May, Jun.  Otherwise, enter 'all' to access data from all six months...  ").title()
        except KeyboardInterrupt:
            print("\nSorry, an error occurred.\n")
            continue
        if month not in ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'All'):
            print("Oops.  Would you please re-enter?  Remember to use this format: Jan, Feb, Mar, Apr, May, Jun.  Or 'all' for data from all months.\n")
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("\nGreat.  Now enter a day of the week: Monday, Tuesday, etc.  Otherwise, enter 'all' to access data from the entire week...  ").title()
        except KeyboardInterrupt:
            print("\nSorry, an error occurred.\n")
            continue
        if day not in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All'):
            print("Sorry, could you try that again?  Remember to use the full day name.  Or use 'all' for the entire week.\n")
        else:
            break

    print('-'*40)
    return city, month, day


#Time based stats
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

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    df['End Time'] = pd.to_datetime(df['End Time'])

    df['month'] = df['End Time'].dt.month
    df['day_of_week'] = df['End Time'].dt.weekday_name
    df['hour'] = df['End Time'].dt.hour

    if month != 'All':
        month = Months.index(month) + 1
        df = df[ df['month'] == month ]

    if day != 'All':
        df = df[ df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print ('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    # display the most common day of week
    # display the most common start hour

    most_common_month = df['month'].value_counts().idxmax()
    print ('The most common month is :', most_common_month)

    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print ('The most common day of week is :', most_common_day_of_week)

    most_common_start_hour = df['hour'].value_counts().idxmax()
    print ('The most common start hour is :', most_common_start_hour)

    print ("\nThis took %s seconds." % (time.time() - start_time))
    print ('-'*40)

#Station base stats
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most commonly used starting station for bikeshares was " + popular_start_station + ".\n")

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The most commonly used ending station for bikeshares was " + popular_end_station + ".\n")

    # TO DO: display most frequent combination of start station and end station trip
   
    popular_station_combo = df['Station Combo'].mode()[0]
    print("The most commonly used combination of starting and ending stations was " + popular_station_combo + ".\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#Trip stats
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print ('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    # display mean travel time

    total_travel_time = df['Trip Duration'].sum()
    print ("Travel time sum:", total_travel_time)

    mean_travel_time = df['Trip Duration'].mean()
    print ("Your mean travel time:", mean_travel_time)

    print ("\nThis took %s seconds." % (time.time() - start_time))
    print ('-'*40)

#User stats
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print ('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    # Display counts of gender
    # Display earliest, most recent, and most common year of birth

    print ('Counts of user types:\n')
    user_counts = df['User Type'].value_counts()
    for index, user_count in enumerate(user_counts):
        print ('{}:{}'.format(user_counts.index[index], user_count))

    print ()

    if 'Gender' in df.columns:
        user_stats_gender(df)

    if 'Birth Year' in df.columns:
        user_stats_birth(df)

    print ("\nThis took %s seconds." % (time.time() - start_time))
    print ('-'*40)

def user_stats_gender(df):
    print ('Counts of gender is:\n')
    gender_counts = df['Gender'].value_counts()
    for index, gender_count in enumerate(gender_counts):
        print('{}:{}'.format(gender_counts.index[index], gender_count))

    print()

def user_birth_year(df):

    birth_year = df['Birth Year']

    earliest_year = birth_year.min()
    print ('The oldest person is born in:', earliest_year)

    recent_year = birth_year.max()
    print ('The youngsest person is born in:', recent_year)

    most_common_year = birth_year.value_counts().idxmax()
    print ('The most common birth year is:', most_common_year)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

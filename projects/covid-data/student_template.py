import sys
import numpy as np
from numpy.core.fromnumeric import argmax


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date, county, state, cases, deaths) information
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data



def first_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """

    Q1RockDate = 0
    Q1HarrDate = 0

    for (date, county, state, cases, deaths) in data:
        if state == "Virginia" and county == "Rockingham":
                Q1RockDate = date
                break
    print("The first positive case in Rockingham occurred on:",Q1RockDate)
    for (date, county, state, cases, deaths) in data:
            if state == "Virginia" and county == "Harrisonburg city":
                Q1HarrDate = date
                break
    print("The first positive case in Harrisonburg city occurred on:",Q1HarrDate)
    return Q1RockDate, Q1HarrDate


def second_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """

    # your code here
    Q2RockDate = 0
    Q2HarrDate = 0

    Q2RockSet = np.array(["date","county","state","cases","deaths"])
    Q2HarrSet = np.array(["date","county","state","cases","deaths"])

    """
    Create two dummy values to hold the final answers.
    Create two numpy arrays with the same format as 'data'
    These arrays will hold the covid data for just rockingham and harrisonburg.
    """

    for (date, county, state, cases, deaths) in data:
        if state == "Virginia" and county == "Rockingham":  #If the state and county match, put the data in the rockingham array
            val1=np.array([date,county,state,cases,deaths])
            Q2RockSet = np.vstack((Q2RockSet, val1))
        if state == "Virginia" and county == "Harrisonburg city": #If the state and county match, put the data in the harrisonburg array
            val2=np.array([date,county,state,cases,deaths])
            Q2HarrSet = np.vstack((Q2HarrSet, val2))

    for (date, county, state, cases, deaths) in Q2RockSet:
            if cases == max(cases): # If the cases on any entry in the set is equal to the maximum of the cases column, set the date of that row equal to the answer.
                Q2RockDate = date
    print("The most cases in Rockingham County occurred on :",Q2RockDate)
    for (date, county, state, cases, deaths) in Q2HarrSet:
        if cases == max(cases): # If the cases on any entry in the set is equal to the maximum of the cases column, set the date of that row equal to the answer.
            Q2HarrDate = date
    print("The most cases in Harrisonburg city occurred on :",Q2HarrDate)

    return Q2RockDate, Q2HarrDate

def third_question(data):
    # Write code to address the following question:Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.

    Q3RockDates = 0
    Q3HarrDates = 0

    Q3Rock7DayTable = np.array(["dates", "deaths"])
    Q3Harr7DayTable = np.array(["dates", "deaths"])

    Q3RockSet = np.array(["date", "county", "state", "cases", "deaths"])
    Q3HarrSet = np.array(["date", "county", "state", "cases", "deaths"])

    """
    Create two dummy values to hold the final answers.
    Create two numpy arrays with the same format as 'data'
    These arrays will hold the covid data for just rockingham and harrisonburg.
    """
    for (date, county, state, cases, deaths) in data:
        if state == "Virginia" and county == "Rockingham":  #If the state and county match, put the data in the rockingham array
            val1=np.array([date,county,state,cases,deaths])
            Q3RockSet = np.vstack((Q3RockSet, val1))
        if state == "Virginia" and county == "Harrisonburg city": #If the state and county match, put the data in the harrisonburg array
            val2=np.array([date,county,state,cases,deaths])
            Q3HarrSet = np.vstack((Q3HarrSet, val2))

    """
    I was unable to deduce how to find the worst seven day period.
    The closest I could get was to find the seven day period around the worst day in each location.
    """

    for (date, county, state, cases, deaths) in Q3RockSet:
        if deaths == max(deaths):
            med_date = date.split("-")
            year = int(med_date[0])
            month = int(med_date[1])
            low_date = int(med_date[2]) - 3
            high_date = int(med_date[2]) + 3
    print("The worst seven day period for deaths in Rockingham county was :",year,month,low_date," to",year,month,high_date)

    for (date, county, state, cases, deaths) in Q3HarrSet:
        if deaths == max(deaths):
            med_date = date.split("-")
            year = int(med_date[0])
            month = int(med_date[1])
            low_date = int(med_date[2]) - 3
            high_date = int(med_date[2]) + 3
    print("The worst seven day period for deaths in Harrisonburg city was :",year,month,low_date," to",year,month,high_date) #This date is incorrect, I was unable to account for differing days in each month.


    return Q3RockDates, Q3HarrDates

if __name__ == "__main__":
    data = parse_nyt_data('us-counties.csv')

    #for (date, county, state, cases, deaths) in data:
        # print('On ', date, ' in ', county, ' ', state, ' there were ', cases, ' cases and ', deaths, ' deaths')


    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    first_question(data)


    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    second_question(data)

    # write code to address the following question:Use print() to display your responses.
    # What was the worst seven day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    third_question(data)



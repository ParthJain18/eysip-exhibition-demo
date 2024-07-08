import pandas as pd

def get_average_time(data: pd.DataFrame) -> dict:
    """
    * Function Name:    get_average_time
    * Input:            data: pd.DataFrame
    * Output:           dict
    * Logic:            This function returns the average time spent on each page by the users.
    """

    average_time = {}

    data['dwell_time'] = data['timestamp'] - data['timestamp'].shift()
    data['dwell_time'] = data['dwell_time'].shift(-1)
    data.fillna(0)

    print(data)

    # First total the dwell time for each user on each page
    new_data = data.groupby(['user_id', 'activity'])['dwell_time'].sum().reset_index()

    # Then note the time spent on each page as a list
    for i, row in new_data.iterrows():
        if row['activity'] not in average_time.keys():
            average_time[row['activity']] = [row['dwell_time']]
        else:
            average_time[row['activity']].append(row['dwell_time'])
    
    # Calculate the average time spent on each page by dividing the total time by total values
    for key, value in average_time.items():
        average_time[key] = round(sum(value) / len(data['user_id'].unique()))
    
    return average_time

if __name__ == '__main__':
    data = pd.read_csv(r"process_model/dummy.csv")
    average_time = get_average_time(data)
    pd.DataFrame(average_time.items(), columns=['Page', 'Average Time Spent']).to_csv(r'average_time.csv', index=False)
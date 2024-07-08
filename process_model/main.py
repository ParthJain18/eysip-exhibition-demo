import pandas as pd
import graphviz
from process_model.average_time import get_average_time

# data = pd.read_csv(r"path-to-csv-file")
output_file_name = 'ocr_result'

def create_process_model(data: pd.DataFrame):
        
    # Function to replace colons in a string with dashes
    def replace_colon(s):
        return s.replace(':', ' -')

    # data['timestamp'] = pd.to_datetime(data['timestamp'])

    # Sort the data by 'user_id' and 'timestamp'
    data = data.sort_values(by=['user_id', 'timestamp'])
    data['activity'] = data['activity'].apply(replace_colon)

    # Calculate the average time for each activity
    average_time_dict = get_average_time(data)

    # Create a dictionary to store user sequences
    user_sequences = {}

    # Group the data by 'user_id' and store the sequences in the dictionary
    for user_id, group in data.groupby('user_id'):
        user_sequences[user_id] = list(group['activity'])

    # Create a dictionary to store transition counts
    transitions = {}

    # Iterate over each sequence and count the transitions
    for sequence in user_sequences.values():
        for i in range(len(sequence) - 1):
            element = (sequence[i], sequence[i + 1])
            if element not in transitions.keys():
                transitions[element] = 1
            else:
                transitions[element] += 1

    # Create a graphviz Digraph object
    dot = graphviz.Digraph(format='png')
    dot.attr(dpi='1200', fontname="Helvetica")

    # Add nodes for each unique activity
    for activity in data['activity'].apply(replace_colon).unique():
        label = f'<{activity}<BR/><BR/><FONT POINT-SIZE="8">Avg time (in seconds) = {average_time_dict[activity]}</FONT>>'
        dot.node(activity, label=label, shape='box', style='rounded', penwidth='0.4', margin='0.2')

    # Add edges for each transition with labels indicating transition counts
    for start, end in transitions.keys():
        dot.edge(start, end, label=f' {transitions[(start, end)]}', penwidth=f'{0.5 * transitions[(start, end)]}')

    # Render the process model diagram as a PNG file
    dot.render(output_file_name, view=True, cleanup=True, format='png', directory='process_model', engine='dot')

    print(f"Process model diagram saved as '{output_file_name}.png'")


if __name__ == '__main__':
    data = pd.read_csv('process_model/dummy.csv')
    create_process_model(data)
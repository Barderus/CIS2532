import numpy as np
def array_formatter(arr):
    string = "["
    for row in arr:
        string += "["
        for elem in row:
            string += f"{elem} "  # Format each element with 3 decimal places
        string = string[:-1] + "]\n"  # Remove trailing space and add closing bracket and newline
    return string[:-1] + "]"  # Remove trailing newline and add closing bracket

# Example usage:
arr = np.array([[1, 2, 3, 4, 5],
                [6, 7 , 8, 9, 10]])
print(array_formatter(arr))




def format_dataframe(dataframe):
    formatted_str = ""

    # Print column names
    for column in dataframe.columns:
        formatted_str += f"{column:15}"  # Adjust width as needed
    formatted_str += "\n"

    # Print data rows
    for index, row in dataframe.iterrows():
        for column in dataframe.columns:
            formatted_str += f"{row[column] :15}"  # Adjust width as needed
        formatted_str += "\n"

    return formatted_str


# Example usage:
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

formatted_df = format_dataframe(df)
print(formatted_df)

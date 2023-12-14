import pandas as pd


def count_vowels_in_dataframe_column(file_path, column_name):
    """
    Counts the number of vowels in a specified column of a CSV file using pandas.

    :param file_path: Path to the CSV file.
    :param column_name: Name of the column to analyze.
    :return: A pandas Series with the number of vowels in the specified column.
    """
    df = pd.read_csv(file_path)

    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in the CSV file.")

    vowels = "aeiouAEIOU"
    count_vowels = lambda x: sum(1 for char in str(x) if char in vowels)

    return df[column_name].apply(count_vowels)


# Path to the uploaded CSV file
file_path = './titles.csv'

# Assuming we want to count vowels in the first column
# Here we use the column name, which is assumed to be the header of the first column
vowel_counts = count_vowels_in_dataframe_column(file_path,
                                                'Title')  # Replace 'Title' with actual column name if different
vowel_counts.head(10)  # Display the first 10 rows for brevity



def concatCategoryColumns():
    '''
    This function concatenates two columns ('category' and 'new_category') from the DataFrame, applies some preprocessing steps to create a new category column, 
    concatenates this new category with another column ('details'), and writes the modified DataFrame to a new CSV file. Additionally, it loads a dictionary 
    containing category mappings using joblib.
    '''
    # import library
    import pandas as pd
    import numpy as np
    from joblib import load

    # Read file csv
    df = pd.read_csv('/opt/airflow/data/product_data.csv')
    dict_cat= load('dict_cat.joblib')

    # Define conditions for mapping categories using the loaded dictionary
    condlist = [
        df['category'].isin(dict_cat['deplist_bath_body']),
        df['category'].isin(dict_cat['deplist_fragrance']),
        df['category'].isin(dict_cat['deplist_gifts']),
        df['category'].isin(dict_cat['deplist_hair']),
        df['category'].isin(dict_cat['deplist_makeup']),
        df['category'].isin(dict_cat['deplist_mini']),
        df['category'].isin(dict_cat['deplist_others']),
        df['category'].isin(dict_cat['deplist_skincare']),
        df['category'].isin(dict_cat['deplist_tools_brushes'])
    ]

    # Define corresponding choices for the new category column
    choicelist = ['bath_body', 'fragrance', 'gifts', 'hair', 'makeup', 'mini', 'others', 'skincare', 'tools_brushes']
    # Apply the conditions to create the new category column
    df['new_category'] = np.select(condlist, choicelist)

    # Concatenate the original category and the new category to create a new column
    df['cat'] = df['category']+' '+df['new_category']

    # Initialize an empty list to store unique concatenated strings
    list_unique = []

    # Loop through each concatenated string
    for word in df['cat']:
        # Split the string into individual words
        words = word.split()

        # Create a set to remove duplicates
        unique_words = set(words)

        # Join the unique words back into a string
        result_string = ' '.join(unique_words)

        # Append the unique string to the list
        list_unique.append(result_string)

    # Assign the list of unique strings as the new 'cat' column     
    df['cat'] = list_unique

    # Concatenate 'details' and 'cat' columns to create a new 'details_category' column
    df['details_category'] = df['details']+' '+df['cat']

    # Write the modified DataFrame to a new CSV file
    df.to_csv('/opt/airflow/data/text_processing.csv', index=False)


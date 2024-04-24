def textProcessing(text):
    '''
    This function preprocesses the given text by removing noise, converting to lowercase, removing stopwords, and lemmatizing. 
    '''
    # Import necessary libraries
    import re
    import nltk

    # Download required NLTK resources
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('wordnet')

    # Import NLTK modules for text preprocessing
    from nltk.stem import WordNetLemmatizer
    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords

    # Define additional stopwords to be added to the default English stopwords list
    additional_stopwords = ['know', 'need', 'contains', 's', 'u s', 'u', 'jcpenny store', 'inside jcpenny', 'help', 'formula', 'formulated','oz', 'ml', 'contains oz', 'category others', 'please visit', 'inside jcpenny', 'jcpenny store', 'help', 'provide']
    
    # Retrieve the default English stopwords list and add additional stopwords
    stpwrd = list(set(stopwords.words('english')))
    for i in additional_stopwords:
        stpwrd.append(i)

    # Initialize WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()

    # Remove new line
    text = re.sub("\n" , " ", text)

    # Convert text to lowercase
    text = text.lower()

    # Remove symbols and numbers
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    # Remove extra whitespaces
    text = re.sub("\s\s+" , " ", text)

    # Strip leading and trailing whitespaces
    text = text.strip()

    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove stopwords
    text = ' '.join([word for word in tokens if word not in stpwrd])

    # Lemmatize the text
    text = lemmatizer.lemmatize(text)

    return text

def dataCleaning():
    '''
    This function loads a CSV file, performs data cleaning tasks like dropping missing values, renaming columns, dropping duplicates, 
    and applies text preprocessing to a specific column, then saves the cleaned data back to a CSV file.
    '''

    # Import necessary libraries   
    import pandas as pd

    # Read csv file
    df = pd.read_csv('/opt/airflow/data/text_processing.csv')

    # Drop missing values
    df = df.dropna()

    # Convert column names to lowercase
    df.columns = df.columns.str.lower()

    # Replace column names space with underscore (_) 
    df.columns = df.columns.str.replace(' ', '_')

    # Convert all object columns to lowercase
    df.columns = [x.lower() for x in df.columns]

    # Drop duplicates
    df = df.drop_duplicates()

    #  Calling text processing
    df['processing_details_category'] = df['details_category'].apply(lambda x: textProcessing(x))

    # Save data to csv
    df.to_csv('/opt/airflow/data/text_processing.csv', index=False)


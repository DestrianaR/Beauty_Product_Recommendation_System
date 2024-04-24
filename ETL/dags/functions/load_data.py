
def loadData():
    '''
    This function creates a table in a PostgreSQL database if it doesn't exist already, then loads data from 
    a CSV file into that table. It uses psycopg2 for database connection and pandas for data manipulation.
    '''

    # Import the pandas library for data manipulation
    import pandas as pd
    # Import the psycopg2 library for connecting to the PostgreSQL database
    import psycopg2 as db

    # Define the connection string with the necessary parameters (dbname, host, user, password, port)
    conn_string="dbname='airflow' host='postgres' user='airflow' password='airflow' port='5432'"
    # Establish a connection to the PostgreSQL database using psycopg2 and the specified connection string
    conn=db.connect(conn_string)
    # Create a cursor object to execute SQL queries
    cur = conn.cursor()

    # SQL query to create a table if it doesn't exist already, with specified column names and data types
    sql = '''
        CREATE TABLE IF NOT EXISTS text_processing (
            text_id SERIAL,
            product_id INT,
            text_processing VARCHAR,
            PRIMARY KEY(text_id),
            CONSTRAINT fk_products
            FOREIGN KEY(product_id)
            REFERENCES products(product_id)

        )
    '''
    # Execute the SQL query to create the table
    cur.execute(sql)
    # Commit the transaction to save the changes
    conn.commit()

    # Read data from the CSV file containing cleaned data
    df= pd.read_csv('/opt/airflow/data/text_processing.csv')
    # Iterate over each row in the DataFrame and insert it into the database table
    for index, row in df.iterrows():
        # SQL query to insert a row into the table with placeholders for values
        insert_query = "INSERT INTO text_processing (product_id, text_processing) VALUES (%s, %s);"
        # Get the values from the current row and convert them into a list
        values = list(row)
        # Execute the SQL query with the values to insert the row into the table
        cur.execute(insert_query, values)

    # Commit the transaction to save the changes
    conn.commit()
    # Close the database connection
    conn.close()   
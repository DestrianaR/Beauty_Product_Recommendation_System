def getData():
    '''
    This function connects to a PostgreSQL database, retrieves data from a specific table, converts it into a pandas DataFrame, 
    and then saves this DataFrame into a CSV file.
    '''

    # Import the pandas library for data manipulation
    import pandas as pd
    # Import the psycopg2 library for connecting to the PostgreSQL database
    import psycopg2 as db

    # Define the connection string with the necessary parameters (dbname, host, user, password, port)
    conn_string="dbname='airflow' host='postgres' user='airflow' password='airflow' port='5432'"

    # Establish a connection to the PostgreSQL database using psycopg2 and the specified connection string
    conn=db.connect(conn_string)

    # Read data from the 'table_final_project' table in the database using the established connection and store it in a pandas DataFrame
    df=pd.read_sql('select * from products', conn)

    # Save the pandas DataFrame to a CSV file at the specified location '/opt/airflow/data/sephora_website_dataset.csv' without including the index when saving
    df.to_csv('/opt/airflow/data/product_data.csv', index=False)
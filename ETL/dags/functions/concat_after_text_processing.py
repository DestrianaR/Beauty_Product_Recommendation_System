def concatTextProcessingAndBrand():
    # import library
    import pandas as pd

    # Read csv file
    df = pd.read_csv('/opt/airflow/data/text_processing.csv')

    # Concat brand column to'preprocessing_details_category'
    df['text_processing'] = df['brand']+' '+df['processing_details_category']

    # Select columns
    df = df[['product_id', 'text_processing']]

    # Save data to csv
    df.to_csv('/opt/airflow/data/text_processing.csv',index=False)
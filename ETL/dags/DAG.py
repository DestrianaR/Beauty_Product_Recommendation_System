import datetime as dt

from airflow.models import DAG
from airflow.operators.python import PythonOperator

from functions.get_data import getData
from functions.concat_before_text_processing import concatCategoryColumns
from functions.concat_after_text_processing import concatTextProcessingAndBrand
from functions.data_cleaning_text_processing import dataCleaning
from functions.load_data import loadData

default_args = {
    'owner': 'destri',
    'start_date': dt.datetime(2024, 4, 24, 12, 30, 0) -  dt.timedelta(hours=7),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1),
}

with DAG('ETL',
         default_args=default_args,
         schedule_interval = '30 6 * * *' # Shedule every day in 6:30
         ) as dag:

    get_data_from_database = PythonOperator(task_id='Get_Data_From_Database',
                                 python_callable=getData)
    
    concat_before_text_processing = PythonOperator(task_id='Concat_Before_Text_Processing',
                                 python_callable=concatCategoryColumns)

    cleaning_data = PythonOperator(task_id='Cleaning_Data',
                                 python_callable=dataCleaning)
    
    concat_after_text_processing = PythonOperator(task_id='Concat_After_Text_Processing',
                                 python_callable=concatTextProcessingAndBrand)
    
    post_data_to_database = PythonOperator(task_id='Post_Data_To_Database',
                                 python_callable=loadData)


get_data_from_database >> concat_before_text_processing >> cleaning_data >> concat_after_text_processing >> post_data_to_database
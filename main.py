import os
import pandas as pd
from flask import Flask, render_template
from google.cloud import bigquery

project_id  = 'nitya-final-project'
dataset_id  = 'austincrimedata'
table_train = 'austincrimedatatrain'
table_predict  = 'austincrimedatapredict'


app = Flask(__name__)

def model_train():

    query_train = f'''
        CREATE MODEL `{project_id}.{dataset_id}.model2` 
OPTIONS (model_type = 'Logistic_reg', input_label_cols = ['primary_type'])
AS 
SELECT * from `austincrimedata.austincrimedatatrain`;
        '''
    client = bigquery.Client(project = project_id)
    query_job = client.query(query_train)
    query_job.result()
    
    return "Model training finished"

@app.route('/',, methods=['POST'])
def model_test():
     query_test = f'''
         SELECT *
          FROM ML.PREDICT(MODEL `{project_id}.{dataset_id}.model2`,
          (
          SELECT * from `austincrimedata.austincrimedatatrain`
          )
          )
         '''
     client = bigquery.Client(project = project_id)
     query_job = client.query(query_test)
     query_job.result()
     df = query_job.to_dataframe()
     result = df.to_html()
     print(result)
    
     return "Model prediction finished"



if __name__ == "__main__":
    app.run(host = '127.0.0.1', debug = True, port=int(os.environ.get("PORT", 8080)))

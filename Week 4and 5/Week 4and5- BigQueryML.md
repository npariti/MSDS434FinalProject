# MSDS 434 Project Week 4 and 5 BigQuery ML 
- A sql query was developed to train and predict the logistic regression model based on the dataset

## Training the model 
1. Run the query below within a BigQuery SQL editor in order to execute the function and train a BigQuery ML based model based on the dataset/table stored in BigQuery. 
```
CREATE OR REPLACE MODEL `{project_id}.{dataset_id}.model2` 
OPTIONS (model_type = 'Logistic_reg', input_label_cols = ['primary_type'])
AS 
SELECT * from `austincrimedata.austincrimedatatrain`;
```
2. The model took approximately 15 minutes to train. Overall metrics were fairly effective: 
    - Accuracy: 0.9267
    - Recall: 0.7598 
    - Precision: 0.8326
3. The model was saved within the schema as 'model2'

## Predict the model 
- The model prediction was done on the 2016 Austin data
```
SELECT *
          FROM ML.PREDICT(MODEL `{project_id}.{dataset_id}.model2`,
          (
          SELECT * from `austincrimedata.austincrimedatatrain`
          )
          )
```
- It was deployed by incorporating it in the main.py script. The results were routed to the Flask app and deployed and posted using the index.html template 

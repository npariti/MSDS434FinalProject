from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """
    Demo version of the Austin Crime Prediction app.
    
    Originally, this app queried a BigQuery ML Logistic Regression model
    named 'model2' to generate crime predictions. Since the model is no
    longer available, this demo uses sample data to simulate predictions.
    """

    environment = "Local (mocked)"

    # -----------------------------
    # Original BigQuery query (commented out)
    # -----------------------------
    # from google.cloud import bigquery
    # PROJECT_ID = "nitya-final-project"
    # DATASET_ID = "austincrimedata"
    # MODEL_NAME = "model2"
    #
    # query = f"""
    #     SELECT *
    #     FROM ML.PREDICT(
    #         MODEL `{PROJECT_ID}.{DATASET_ID}.{MODEL_NAME}`,
    #         (SELECT * FROM `{PROJECT_ID}.{DATASET_ID}.austincrimedatatrain`)
    #     )
    # """
    # client = bigquery.Client(project=PROJECT_ID)
    # query_job = client.query(query)
    # results_df = query_job.to_dataframe()

    # -----------------------------
    # Mocked data for demo
    # -----------------------------
    sample_data = {
        "incident_number": [1, 2, 3],
        "primary_type": ["THEFT", "ASSAULT", "ROBBERY"],
        "predicted_type": ["THEFT", "ASSAULT", "ROBBERY"],
        "prediction_confidence": [0.85, 0.9, 0.75]
    }
    results_df = pd.DataFrame(sample_data)

    return render_template(
        "index.html",
        page_type="Crime Prediction Results",
        environment=environment,
        tables=[results_df.to_html(classes="table table-striped")]
    )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

# MSDS434 Project Week 7 Creation of Multiple Environments 
- There was a staging and production environment created for deployment in the us-east1 region
- The following commands were run: 
  - To create the enviornment: gcloud composer environments create staging --location us-east1
  - To activate the environment: gcloud config configurations activate staging 
  - To deploy the app: gcloud app deploy app.yaml 

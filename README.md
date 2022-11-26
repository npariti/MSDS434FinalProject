# MSDS434FinalProject
- This directory contains the necessary files to deploy the final project app
- This app uses a simple html template to display a front end that will list the predictions from the Logistic Regression model created to predict the crime types in austin 
- A development and a production environment were created with Google Cloud Composer to deploy the application
- A VM instance was created to do load tests with ApacheBench 
- To deploy the following instructions can be followed: 
  - Clone the git repository: git clone https://github.com/npariti/MSDS434FinalProject.git
  - Change the directory to MSDS434FinalProject: cd MSDS434FinalProject
  - Deploy the app: gcloud app deploy app.yaml

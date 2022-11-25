# MSDS 434 Final Project- Nitya Pariti 

This is a document for all the coursework and all associated files that lead up to the creation fo the final project for MSDS 434, Winter 2022. 
Work is still in progress and as new items are added, this repository will be updated as necessary until the project has been completed and submitted for grading. 

# Description
- This project was designed to meet the requiremnts outlined the course objectives for MSDS 434 
- The overall idea was to implement a ML model that would predict the crime types in Austin. The final front end would display these predictiosn 
- Google Cloud Platform would be utilized as a means of serving the application to end users. 
  - This would include ingesting adn storing the data, using BigQueryML or AutoML to train and serve a Logistic Regression Model, and using AppEngine to deploy a publicly accessible interface that users can access 
-At this time, the interface will display the predictions in a table 
- Local development has been done to establish the necessary items that will be required to complete the process: 
  - Python and SQL were used to clean the data 
  - BigQueryML was used to create a Logistic Regression model 
  - Python to serve a Flask based web interface to accept user input and serve the saved TF model to generate predictions 
 - A Google Cloud Project called 'nitya-final-project' has been created, and development has begun within it 

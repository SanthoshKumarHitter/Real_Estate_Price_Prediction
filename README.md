# Real Estate Price Prediction using Machine Learning
  
     This project aims to predict real estate prices using a machine learning model, specifically a Linear Regression algorithm. The goal is to provide accurate predictions of property prices based on various features 
     such as the age of the house, distance to the nearest MRT station, number of convenience stores nearby, latitude, and longitude. Accurate price predictions can help buyers, sellers, investors, and real estate 
     professionals make informed decisions about real estate transactions.

     
 ## Table of Contents
 
     1. Installation
     2. Data Features
     3. Tools and Libraries
     4. Usage
     5. Steps Involved
     6. File Structure
     7. Contributing
     8. Credits
     9. License
     10. Contact Information
     11. Result

   ### 1) Installation:-

       1. Using Google Colab
          Open Google Colab in your browser.
          
          Mount your Google Drive.
          
          Navigate to the desired directory in your Google Drive where you want to clone the repository.
          
          Clone the repository. 
         
       2. Install required packages.
     
       3. Download and extract the dataset.
       
          Upload the dataset ZIP file to your Google Drive.
          
          Extract the dataset in your project directory.

           ** Deployment:-**

             To run the web application locally, follow these steps:

             Open VS Code Editor and write the web application Code Using Streamlit.

             To Run the Streamlit application,
           
                streamlit run app.py
             
                Open your web browser and navigate to http://localhost:8501 to use the application.


   ### 2) Data Features:-
   
         House Age: Age of the house in years.
      
         Distance to the nearest MRT station: Distance from the property to the nearest MRT station in meters.
      
         Number of convenience stores: Number of convenience stores within a certain radius of the property.
      
         Latitude: Geographical latitude of the property.
      
         Longitude: Geographical longitude of the property.
      
         House Price of Unit Area: Actual price of the house per unit area (target variable).

   ### 3) Tools and Libraries:-
    
          Google Colab: For training the machine learning model and performing data analysis.
       
          VS Code: For developing the Streamlit application and coding the project.
       
          Python Libraries: Including pandas, scikit-learn, joblib, matplotlib, and seaborn for data manipulation, modeling and visualization.


   ### 4) Usage:-

          Home Buyers and Sellers: To estimate property prices based on specific features, helping in making informed buying or selling decisions.
          
          Real Estate Investors: To analyze potential investments and predict future property values based on current market trends.
          
          Real Estate Professionals: To assist clients with accurate pricing strategies and market evaluations.
          
          Data Scientists and Analysts: To explore machine learning applications in real estate and improve predictive modeling skills.


       
   ### 5) Steps Involved:-
     
          1. Data Preprocessing
              Load the dataset.
              Handle missing values (if any).
              Perform exploratory data analysis (EDA).
              Visualize the data to understand the relationships between features and the target variable.
          
          2. Model Building
              Split the data into training and testing sets.
              Train a Linear Regression model using the training data.
              Evaluate the model based on its predictions on the test data.
          
          3. Model Deployment
              Save the trained model using Joblib.
              Create an interactive web application using Streamlit to input new data and predict real estate prices.

     
   ### 6) File Structure:-

               ├── data
               │   ├── Real_Estate.csv
               ├── Deploy Application
               │   ├── app.py
               │   ├── model.pkl
               ├── notebooks
               │   ├── Real_Estate_Price_Prediction.ipynb
               ├── README.md


   ### 7) Result:-

          
           ![Real estate](https://github.com/user-attachments/assets/7f960c68-34d4-4dec-ba98-5eb828dbbad2)

       
   ### 8) Contributing:-


              Contributions are welcome! Please follow these steps:-

                     Fork the repository.
                     Create a new branch (git checkout -b feature-branch).
                     Make your changes and commit them (git commit -m 'Add new feature').
                     Push to the branch (git push origin feature-branch).
                     Open a Pull Request.
                     
     
   ### 9) Credits:-
       
              Statso for the original problem statement.
     
   ### 10) License:-

              This project is licensed under the MIT License - see the LICENSE file for details.
              
   ### 11) Contact Information:-

               MailId:- santhuhitter1515@gmail.com

   

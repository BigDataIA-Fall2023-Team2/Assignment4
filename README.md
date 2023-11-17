# Assignment4

### Project Descrition 

In this application, the user will ask a question related to data stored in data warehouse in english language. The application will convert the english statement into SQL query and will get exectued against the snowflake databases. The results will be then displayed on the application.

### Application and Documentation Link

App link - 

### Project Resources

Google Codelab link - 

Project Demo - 

Proof of Concept - https://docs.google.com/document/d/1N0K34Oohp1onvOfS91-UuH7-uUOE0VP_1edQ5f1bfcY/edit

### Tech Stack
Python | Streamlit | Snowflake | Langchain | OPENAI

### Architecture diagram ###

![image](https://github.com/BigDataIA-Fall2023-Team2/Assignment4/assets/131703516/3590949a-c9eb-486f-9ce6-3d475b41fd98)


### Project Flow

The user will ask a question related to the data in snowflake. The question which is in simple english language will be processed into an SQL query. Then the sql query is then sent to snowflake database for exection whose results are then shared into the application. 

1) Firstly, we get our data from market place and load it into the snowflake datawarehouse. Below are the datasets that we are using for this project. The data is added to individual schemas :
  Consumer data : Consumer Info
  App usage : App Usage
  NFL post sponsership : NFL post sponsership

2) Now to load the data from the individual schemas we run 3 different scripts. 
  Consumer data : .sql
  App usage : .sql
  NFL post sponsership : .sql

  The script copy the data and runs the required functions to transform the data and store it in analytics schema. 

3) We run a stored procedure to get and transform the data using aggregate functions to create a combined view and store them in analytics schema.

Proof of Concept (https://docs.google.com/document/d/1N0K34Oohp1onvOfS91-UuH7-uUOE0VP_1edQ5f1bfcY/edit) will explain more about the data transformation and data quality checks that are done. 

### Repository Structure


### Contributions

| Name                            | Contribution                                                                 |  
| ------------------------------- | -----------------------------------------------------------------------------|
| Shardul Chavan                  | Langchain and Streamlit integration                                          | 
| Chinmay Gandi                   | Snowflake - SQL process, UDF Function                                        | 
| Dhawal Negi                     | Snowflake - SQL process, UDF Function, Stored Procedure                      |                                                  

### Additional Notes
WE ATTEST THAT WE HAVEN’T USED ANY OTHER STUDENTS’ WORK IN OUR ASSIGNMENT AND ABIDE BY THE POLICIES LISTED IN THE STUDENT HANDBOOK. 


Instructions:
- To run the program use the command python ETL_OLAP.py
- Ensure that the data set 'Car_Sales_Data_Set.csv' is located within the same folder as the program. 

Description:
ETL_OLAP.py first creates a new sorted csv file in the current directory, and then prints options for the user to select. Twelve options are printed, corresponding to 12 different data frames which can be generated. 
Enter a number 1-12 to select a certain data frame.

For example, if the user selects 3, the following is printed:
 Time_Year
2017    34392
2018    38278
Name: Sales_Units, dtype: int64

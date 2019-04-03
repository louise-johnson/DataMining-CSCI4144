How to use ETL_OLAP.py:
To run the program on the bluenose server, use
python ETL_OLAP.py

ETL_OLAP.py first creates a new sorted csv file in the current directory, and then prints options for the user to select. Twelve options are printed, corresponding to 12 different data frames which can be generated. 
Simply enter a number 1-12 to select a certain data frame.

For example, if the user selects 3, the following is printed:
 Time_Year
2017    34392
2018    38278
Name: Sales_Units, dtype: int64

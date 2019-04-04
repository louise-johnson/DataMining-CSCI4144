Instructions:
- To run the program, use the command python BUC.py
- Ensure that the data set 'Product_Sales_Data_Set.csv' is located within the same directory as the python script

Description:
BUC.py generates iceberg cubes given a user defined minimum support count. 
The result of the iceberg cube computation is stored and accessible in Iceburg-Cube-Results.txt
In this dataset, the minimum support count represents the minimum number of sales_units the user wishes to see. 
For example, if the user enters 27 as the minimum support, then iceberg cubes are generated so long as the sales_units are
greater than or equal to 27. This example produces the output:

Item	   Sales_Units
Camera	 93
Computer 97
Phone	   96
Printer	 92

Item	    Location	Sales_Units
Computer	New York	29

Item	    Location	Year	Sales_Units

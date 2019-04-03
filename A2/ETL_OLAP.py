import pandas as pd
# Read in the data
df_old = pd.read_csv('Car_Sales_Data_Set.csv', sep=',')

# Create a new, sorted csv file
df_old.drop(columns='Record_ID', axis=1, inplace=True)
df_old = df_old.sort_values(['Country', 'Time_Year', 'Time_Quarter'])
df_old.insert(0, 'Record_ID', list(range(1,101)))
df_old.to_csv('Car_Sales_Data_Set_Sorted.csv', index=False)

# Print options to the user
print("\nThere are 12 tuples to choose from:")
options = "(1)  - () \n" \
          "(2)  - (Country)\n" \
          "(3)  - (Time_Year)\n" \
          "(4)  - (Time_Quarter - Time_Year)\n" \
          "(5)  - (Car_Manufacturer)\n" \
          "(6)  - (Country, Time_Year)\n" \
          "(7)  - (Country, Time_Quarter - Time_Year)\n" \
          "(8)  - (Country, Car_Manufacturer)\n" \
          "(9)  - (Time_Year, Car_Manufacturer)\n" \
          "(10) - (Time_Quarter - Time_Year, Car_Manufacturer)\n" \
          "(11) - (Country, Time_Year, Car_Manufacturer)\n" \
          "(12) - (Country, Time_Quarter - Time_Year, Car_Manufacturer)\n"
print(options)
userSel = input("Enter a number 1 - 12: ")
print("")
# Listen for option selected from user and print corresponding data
df = pd.read_csv('Car_Sales_Data_Set_Sorted.csv', sep=',')
if (int(userSel) == 1):
   print(df)
elif (int(userSel) == 2):
    print(df.groupby(['Country'])['Sales_Units'].sum())
elif (int(userSel) == 3):
   print(df.groupby(['Time_Year'])['Sales_Units'].sum())
elif (int(userSel) == 4):
   print(df.groupby(['Time_Year', 'Time_Quarter'])['Sales_Units'].sum())
elif (int(userSel) == 5):
   print(df.groupby(['Car_Manufacturer'])['Sales_Units'].sum())
elif (int(userSel) == 6):
   print(df.groupby(['Country', 'Time_Year']) \
   ['Sales_Units'].sum())
elif (int(userSel) == 7):
   print(df.groupby(['Country', 'Time_Year', 'Time_Quarter']) \
   ['Sales_Units'].sum())
elif (int(userSel) == 8):
   print(df.groupby(['Country', 'Car_Manufacturer']) \
   ['Sales_Units'].sum())
elif (int(userSel) == 9):
   print(df.groupby(['Time_Year', 'Car_Manufacturer']) \
   ['Sales_Units'].sum())
elif (int(userSel) == 10):
    print(df.groupby(['Time_Year','Time_Quarter', 'Car_Manufacturer']) \
          ['Sales_Units'].sum())
elif (int(userSel) == 11):
   print(df.groupby(['Country', 'Time_Year', 'Car_Manufacturer']) \
   ['Sales_Units'].sum())
elif (int(userSel) == 12):
   print(df.groupby(['Country', 'Time_Year', 'Time_Quarter', \
                          'Car_Manufacturer'])['Sales_Units'].sum())
else:
    print("Invalid input. Please enter a number 1-12.")
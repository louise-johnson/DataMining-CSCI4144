import pandas as pd
import numpy as np
import os

#load in data
df = pd.read_csv('Product_Sales_Data_Set.csv', sep=',')

min_sup = float(input("\nEnter a minimum support: "))
print("")
   
# Creates a dictionary of dimensions.
# The dimensions are: Item, Location, Year, Supplier
# The measure is Salues_Units
dim_dic = {}
key_order = ('Item', 'Location', 'Year', 'Supplier')
for i in key_order:
    # exclude the measure from this dictionary
    if (i == 'Sales_Units'):
        continue
    dim_dic[(i)] = len(df[i].unique())
    
# Creates a dictionary of a dimension's unique values in a slice
def dic(dim, dfslice):
    dic = {}
    for i in set(dfslice[dim]):
        ind = np.where(dfslice[dim] == i)[0]
        ddd = dfslice.iloc[ind, :]
        dic[(i)] = np.sum(ddd.Sales_Units)
    return dic

# slices a dimension
def agg(dim, dfslice):
    local_dict = dic(dim, dfslice)
    newDF = pd.DataFrame()

    for i in set(local_dict.keys()):
        if (local_dict[i] > min_sup):
            newTuples = dfslice.loc[dfslice[dim] == i]
            newDF = newDF.append(newTuples)
            
    return newDF

# Remove the old file, if it exists
try:
    os.remove("Iceburg-Cube-Results.txt")
except:
    print()

# Expand on Item
dim = 'Item'
dim_list = [dim]
new_df = agg(dim, df)
outputRec = new_df.groupby(dim_list)['Sales_Units'].sum()
outputRec.to_csv('Iceburg-Cube-Results.txt', header=True, index=True, sep='\t', mode='a')

# Expand on location
dim = 'Location'
output_df = pd.DataFrame()
for i in set(new_df['Item']):
    candidate_tuples = agg(dim, new_df.loc[new_df['Item'] == i])
    output_df = output_df.append(candidate_tuples)

dim_list.append(dim)
if not output_df.empty:
    outputRec = output_df.groupby(dim_list)['Sales_Units'].sum()
    outputRec.to_csv('Iceburg-Cube-Results.txt', header=True, index=True, sep='\t', mode='a')

    # Expand on year
    dim = 'Year'
    itemlocyr_df = pd.DataFrame()
    for i in set(output_df['Item']):
        #slice the df and increment the dimension, do BUC on this
        sliced = output_df.loc[output_df['Item'] == i]
        for j in set(sliced['Location']):
            new_slice = sliced.loc[sliced['Location'] == j]
            candidate_tuples = agg(dim, new_slice)
            itemlocyr_df = itemlocyr_df.append(candidate_tuples)

    dim_list.append(dim)
    if not itemlocyr_df.empty:
        outputRec = itemlocyr_df.groupby(dim_list)['Sales_Units'].sum()
        outputRec.to_csv('Iceburg-Cube-Results.txt', header=True, index=True, sep='\t', mode='a')
    else:
        with open("Iceburg-Cube-Results.txt", 'a') as f:
            for i in dim_list:
                f.write(i)
                f.write('\t')
else:
    with open("Iceburg-Cube-Results.txt", 'a') as f:
        for i in dim_list:
            f.write(i)
            f.write('\t')
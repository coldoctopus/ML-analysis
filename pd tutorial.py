import pandas as pd
#dataframe: a table has colummn and its row value, edit row name by index
table = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]}, index = ['test A','test B'])

#series: a colummn with row value
score = pd.Series([384,345,523,600,193], index =['A','B',"C",'D','E'])

#read from files
#create csv file with notepad, with excel (file name).csv then select csv
#use index as first: index_col=0
#phase_result = pd.read_csv("D:\legacy code\games.csv", index_col=0)

#.head(): print first 5 lines
#.shape: get size of file
#.to_csv(" "): to dave DataFrame to a csv

print(table)
#print(phase_result.head())
#print(phase_result.shape)


#to access a property: csv_name.property or csv_name['property']
#to a specific value ['property'][index]
#locate with integer .iloc[index] / use [:no] like python to access various rows / [-no:] for backward .iloc[index,columns] index & columns can be a list
#.loc: index = name of indicies (prefer list): print(phase_result.loc[:,["age"]]) .loc[row,col] can be a list
#diff: .iloc use number & .loc use name
#print(phase_result.loc[:,["age"]])

#manupilate index: se_index("index")
#conditional select: data.property == value / .loc thì thêm vào [] / 2 or more use & / or: use |
#.property.isin(['value',...]): get row with specific value
#.isnull() , .notnull()
index = [1,3,5,6]
#frame = phase_result.iloc[index]
#frame = phase_result.loc[101:105,"address"] #since index = student id at upper code
#print(frame)

#assign data: fixed or interable value
#combine info: ... + " " +...

'''
    .descibe() : give brief info about frame (max,min,count,etc)
    .mean() : mean value of given Series
    .unique() : unique value
    .value_counts() : count values [value_counts(normalize=True) : with %]
    .map(): give a single Series value and convert to aa new Series with calculated function
    .apply(): same as map but whole DataFrame .apply("function", args =[...]) exclude if property is located
    Example move to chess db.py
'''
'''
    .idxmax(): return max value by col / by row .idxmax(axis = "columns")
'''

#sorting
'''
    .sort_values(by='property',ascending = True/False) default is True
    .sort_values(by=['propertyA','propertyB',...],ascending = [True/False,...) can do multiple condition. Xét từ trái sang. Ascending tương ứng với condition
'''

#group
'''
    use filter and .loc get a group
    .groupby() get all group with a column
    .get_group() get a specific group after .groupby
    .agg([list of func...]) do multiple function with a group
'''

#missing data & dtype
'''
    .dtype returns type of data in series
    .astype(type) changes type of data
    with NaN: use .fillna('things to fill')
    to replace: use .replace('thing to replace','what to replace')
'''

#rename & combine
'''
    .concat([list of DataFrame]) combine data frames
    .set_index('name id') set the id
'''
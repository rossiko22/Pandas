import pandas as pd
import numpy as np

#Reading csv
df = pd.read_csv("csv_example_1.csv", delimiter=";")

#Csv specifications
print(df.info()) # summary of dataframe
print(df.describe()) # basic statistics

#Here we can change value on whole Identifier column
df['Identifier'] = 1

#Here we can drop column with creating a copy
new_df = df.drop(columns="Identifier")

#Here we can drop an column directly on the dataframe
#So we use inplace when we want to make direct change to dataframe without making copies
df.drop(columns="Identifier", inplace=True)


df_1 = pd.DataFrame({
    'A' : [0, 0, np.nan],
    'B' : [0, 1, np.nan]
})

#Here we update directly with inplace
df_1.fillna(2, inplace=True)

#Here we update with copy without inplace
new_df_1 = df_1.fillna(2)

print(new_df_1)


#Filtering csv
#We use bitwise (&-and , |-or) here between the two , because they are like elements , two dataframes
#And inside we can use logical operators , this is short , if you want to know more search
#And we must put them in () because they are like elements and must be separated
filtered_df = df[(df['First name'] == 'Rachel') | (df['One-time password'] == "12se74")]
print(filtered_df)

#Filtering csv using an list based on some column
#We need to create df[] and inside filter 
#If we want to assign directly we can use df = df[] and filter then
names_to_filter = ['Rachel', 'Laura', 'Craig', 'Marko']
filtered_df_1 = df[df['First name'].isin(names_to_filter)]
print(filtered_df_1)


#Adding an column into csv
age = [1, 2, 3, 4]
#Add the age and fill the rest with the missing getting from len(df) - len(age)
#but 0 must be as list placed in []
df["Age"] = age + [0] * (len(df) - len(age))
print(df)

#If we know the lenght we can add
df['new_col'] = [1, 2, 3, 4, 5]
print(df)

#Filtering with substring
#Here we can use string functions ?? learn about string functions
filtered_df_2 = df[df['First name'].str.startswith("Rac")]
print(filtered_df_2)

#Filtering with query() that has syntax like SQL
filtered_df_3 = df.query('Age > 1 and new_col > 1')
print(filtered_df_3)

#Adding an list and filling the rest with none(null values)
year = ["2003", "2002", "2001"]
year_column_filter = year + [None] * (len(df) - len(year))
df['Year'] = year_column_filter
print(df)

#filtering looking for none or null
null_df = df[df['Year'].isnull()]
print(null_df)

not_null_df = df[df['Year'].notnull()]
print(not_null_df)
#Here we create an dict where keys are columns and values are rows
create_csv = {
    "Username" : ["Marko", "Maric"],
    "Password" : ["123", "123"]
}

#Filtering using loc(label based indexing) and iloc(positional indexing)
#Filtering and also grepping the columns that i want to print based on the result
#With loc i can filter and make an boolean like == 'Rachel' in it but with iloc i cant
#I must furst filter and then use iloc to specify index of columns
loc_df = df.loc[df['First name'] == 'Rachel', ['First name', 'One-time password']]
print(loc_df)

#Here we create simple filter
iloc_df = df[df['First name'] == 'Laura']
print(iloc_df)

#From the 0 row based on the iloc_df data frame 
#Give me the value at column 5
iloc_df_filtered = iloc_df.iloc[0, 5]
print(iloc_df_filtered)






#Here we create dataframe from that object , e.g dataframe
df_create_csv = pd.DataFrame(create_csv)

#Here we convert the dataframe to csv, and index when created , [0, 1, 2, 3, 4] on the side are removed
#With sep we specify the delimiter that we want to use Username;Password
df_create_csv.to_csv("csv_example_2.csv", index=False, sep=";")

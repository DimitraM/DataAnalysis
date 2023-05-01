import pandas as pd
df = pd.read_csv("adult.data.csv",index_col="race")
print("\nResults of analysic in adult.data.csv file\n")
print('What is the average age of men? : ')
average_age_men = df.loc[df['sex']=='Male']['age'].mean()
print(average_age_men, "%\n")

print("What is the percentage of people who have a Bachelor's degree ? :" )

percentage_bachelors = (df.loc[df['education']=='Bachelors']['education'].count() / df['education'].count())*100
print(percentage_bachelors, "%\n")


# What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
# What percentage of people without advanced education make more than 50K?

# with `Bachelors`, `Masters`, or `Doctorate`

higher_education = df.loc[df['education'].isin(['Bachelor','Masters','Doctorate'])]['salary'] == '>50K'

higher_education = ((higher_education.where(higher_education==True).count()) / (higher_education.count()))*100

print('Percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) that make more than 50K:', higher_education ,"%\n")

#without `Bachelors`, `Masters`, or `Doctorate`
lower_education = df.loc[~df['education'].isin(['Bachelor','Masters','Doctorate'])]['salary'] == '>50K'
lower_education = ((lower_education.where(lower_education==True).count()) / (lower_education.count()))*100

print('Percentage of people without advanced education that make more than 50K \n' , lower_education , "%\n")

# What is the minimum number of hours a person works per week (hours-per-week feature)?
print("What is the minimum number of hours a person works per week (hours-per-week feature)?")
min_work_hours = df['hours-per-week'].min()
print(min_work_hours, "\n")

print("What percentage of the people who work the minimum number of hours per week have a salary of >50K?")
# What percentage of the people who work the minimum number of hours per week have a salary of >50K?
num_min_workers =df.loc[df['hours-per-week']== min_work_hours]['salary'].count()

rich_percentage = df.loc[df['hours-per-week']== min_work_hours]['salary'] == '>50'

if num_min_workers == rich_percentage.count():
    # no rich peaple with salary >50K
    # value_counts has only False and is equal to num_min_workers

    # print('No rich peaple with salary >50K')
    # print(rich_percentage.value_counts())
    rich_percentage = 0.0
else:
    rich_percentage = (rich_percentage.where(rich_percentage == True).count()/rich_percentage.count())*100

print(rich_percentage,"%\n")

print("What country has the highest percentage of people that earn >50K?")
# What country has the highest percentage of people that earn >50K?
highest_earning_country_df = df.loc[df['salary'] == '>50K']['native-country'].value_counts().to_dict()

highest_earning_country = max(highest_earning_country_df,key=highest_earning_country_df.get)    

# print(highest_earning_country)
#from the dictionary i made that has for every country a summary of rich people
# i got the max value(value of United States) devided by the summary of every worker in US.
highest_earning_country_percentage = ((max(highest_earning_country_df.values()))/(df.loc[df['native-country']=='United-States']['salary'].count()))*100

print(highest_earning_country_percentage, "%\n")


print("Identify the most popular occupation for those who earn >50K in India.")
pop_occupation_india = df.loc[df['salary']=='>50K'][['native-country','occupation']]
pop_occupation_india = pop_occupation_india.loc[pop_occupation_india['native-country']=='India']
pop_occupation_india = pop_occupation_india.value_counts().to_dict()

top_IN_occupation = max(pop_occupation_india,key=pop_occupation_india.get)

print(top_IN_occupation, "%\n")
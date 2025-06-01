# Project1 = Analyzing Indian Premier League (IPL) Data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = {
    'season': [2023, 2023, 2023, 2022, 2022, 2022, 2021, 2021, 2021],
    'team1': ['MI', 'CSK', 'RCB', 'MI', 'KKR', 'CSK', 'DC', 'RCB', 'MI'],
    'team2': ['CSK', 'RCB', 'MI', 'KKR', 'CSK', 'MI', 'MI', 'CSK', 'KKR'],
    'winner': ['MI', 'CSK', 'MI', 'MI', 'KKR', 'CSK', 'DC', 'RCB', 'MI'],
    'city': ['Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Chennai', 'Mumbai', 'Delhi', 'Bangalore', 'Kolkata'],
    'player_of_match': ['Rohit Sharma', 'MS Dhoni', 'Virat Kohli', 'Jasprit Bumrah', 'Andre Russell', 'Ravindra Jadeja', 'Rishabh Pant', 'AB de Villiers', 'Kieron Pollard'],
    'runs_scored': [160, 180, 175, 150, 200, 190, 170, 185, 165],
}

ipl_df = pd.DataFrame(data)

# 1. Basic Data Exploration
print(ipl_df.head())
print(ipl_df.info())

# 2. Team Performance
team_wins = ipl_df['winner'].value_counts()
print("\nTeam Wins: \n", team_wins)

# 3. Player of the Match Analysis
player_of_match_counts = ipl_df['player_of_match'].value_counts()
print("\nPlayer of the Match Counts:\n", player_of_match_counts)

# 4. Runs Scored Analysis
average_runs_per_match = ipl_df['runs_scored'].mean()
print("\nAverage Runs Scored per Match: ", average_runs_per_match)
# 1. Bar Chart of Team Wins
plt.figure(figsize=(10, 6))
sns.countplot(x='winner', data=ipl_df)
plt.title('Number of wins by Team')
plt.xlabel('Team')
plt.ylabel('Number of Wins')
plt.show()
# 2. Histogram of Runs Scored
plt.figure(figsize=(8, 5))
plt.hist(ipl_df['runs_scored'], bins=8)
plt.title('Distribution of Runs Scored per Match')
plt.xlabel('Runs Scored')
plt.ylabel('Frequency')
plt.show()
     
#    season team1 team2 winner       city player_of_match  runs_scored
# 0    2023    MI   CSK     MI     Mumbai    Rohit Sharma          160
# 1    2023   CSK   RCB    CSK    Chennai        MS Dhoni          180
# 2    2023   RCB    MI     MI  Bangalore     Virat Kohli          175
# 3    2022    MI   KKR     MI    Kolkata  Jasprit Bumrah          150
# 4    2022   KKR   CSK    KKR    Chennai   Andre Russell          200
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 9 entries, 0 to 8
# Data columns (total 7 columns):
#  #   Column           Non-Null Count  Dtype 
# ---  ------           --------------  ----- 
#  0   season           9 non-null      int64 
#  1   team1            9 non-null      object
#  2   team2            9 non-null      object
#  3   winner           9 non-null      object
#  4   city             9 non-null      object
#  5   player_of_match  9 non-null      object
#  6   runs_scored      9 non-null      int64 
# dtypes: int64(2), object(5)
# memory usage: 636.0+ bytes
# None

# Team Wins: 
#  winner
# MI     4
# CSK    2
# KKR    1
# DC     1
# RCB    1
# Name: count, dtype: int64

# Player of the Match Counts:
#  player_of_match
# Rohit Sharma       1
# MS Dhoni           1
# Virat Kohli        1
# Jasprit Bumrah     1
# Andre Russell      1
# Ravindra Jadeja    1
# Rishabh Pant       1
# AB de Villiers     1
# Kieron Pollard     1
# Name: count, dtype: int64

# Average Runs Scored per Match:  175.0


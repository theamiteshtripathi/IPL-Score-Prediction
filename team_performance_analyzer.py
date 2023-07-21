# -*- coding: utf-8 -*-
"""team_performance_analyzer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rb1-8WkWTSls4TE_-Yeb5tgBj0xB9pja
"""

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('ipl.csv')

"""**Data Preprocessing**: We'll remove any rows that are not relevant or could distort our analysis. Given that we're analyzing overall team performance, we'll remove rows corresponding to matches that have less than 5 overs of data, as these could skew our analysis."""

# Data Preprocessing
df = df[df['overs']>=5.0]

"""**Feature Engineering:** We'll compute some basic metrics such as total runs scored by each team, total wickets taken by each team, total matches played by each team, and total matches won by each team. We'll also compute derived metrics like the average runs per match and the win ratio for each team."""

# Total runs scored by each team
total_runs = df.groupby('bat_team')['runs'].sum()

# Total wickets taken by each team
total_wickets = df.groupby('bowl_team')['wickets'].sum()

# Total matches played by each team
total_matches = df.groupby('bat_team')['mid'].nunique()

# Construct a DataFrame with these metrics
team_performance = pd.DataFrame({
    'Total Runs': total_runs,
    'Total Wickets': total_wickets,
    'Total Matches': total_matches
})

# Compute derived metrics
team_performance['Average Runs per Match'] = team_performance['Total Runs'] / team_performance['Total Matches']

# Set up the matplotlib figure
f, axes = plt.subplots(3, 1, figsize=(10, 15))

# Total Runs Scored by Each Team
sns.barplot(x=team_performance['Total Runs'], y=team_performance.index, ax=axes[0])
axes[0].set_title('Total Runs Scored by Each Team')

# Total Wickets Taken by Each Team
sns.barplot(x=team_performance['Total Wickets'], y=team_performance.index, ax=axes[1])
axes[1].set_title('Total Wickets Taken by Each Team')

# Average Runs per Match
sns.barplot(x=team_performance['Average Runs per Match'], y=team_performance.index, ax=axes[2])
axes[2].set_title('Average Runs per Match')

plt.tight_layout()
plt.show()


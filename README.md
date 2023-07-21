# IPL First Innings Score Prediction, Team Performance and Player Performance Analysis 🏏
Welcome to our IPL First Innings Score Prediction and Performance Analysis project! This project uses Machine Learning algorithms and Data Analysis techniques on IPL (Indian Premier League) datasets to predict the first innings score, analyze team performances, and analyze player performances.


![IPL Banner](./static/ipl_banner.jpg)



## Data 📊
The data used in this project is IPL (Indian Premier League) match data from 2008 to 2017. The dataset includes variables such as the teams playing, the venue, overs, runs, wickets, and more. It is stored in `ipl.csv`.

## Score Prediction Model 🎯
The score prediction model is a Linear Regression model that predicts the first innings score based on the current match stats. The model is trained on data from matches up to 2016 and tested on data from matches in 2017 and later. The trained model is saved as a pickle file (`innings-score-lr-model.pkl`).

## Team Performance Analysis 📈
The team performance analysis includes metrics like the total runs scored by each team, total wickets taken, average runs per match, and more. The analysis is performed in `team_performance_analyzer.py`, and visualizations are created using Matplotlib and Seaborn.

## Player Performance Analysis 📊
The player performance analysis includes metrics like total runs scored by each player, total wickets taken by each player, strike rate, bowling average, and more. The analysis is performed in `player_performance_analyzer.py`, and visualizations are created using Matplotlib and Seaborn.

## Web Application 💻
The project includes a Flask web application that allows users to enter the current match stats and get a prediction for the first innings score. The web application uses the trained model to make predictions. It is designed to be deployed on Heroku.

## Setup and Installation ⚙️
To run the project locally:

1. Clone the repository: `git clone https://github.com/theamiteshtripathi/ipl-score-prediction.git`
2. Navigate into the project directory: `cd ipl-score-prediction`
3. Install the required packages: `pip install -r requirements.txt`
4. Run the prediction file: `python "Innings Score Prediction - IPL.py"`
5. Run the app: `python app.py`

Then, open a web browser and navigate to `localhost:5000` to view the app.

## Future Work 🔮
- Improve the score prediction model by using more advanced models and feature engineering.
- Predict the match outcome (i.e., which team will win) in addition to the first innings score.
- Use real-time data to make predictions during live matches.
- Improve the web application by providing a detailed analysis of the prediction, showing important features, providing visualizations, etc.

## Acknowledgements 🙏
References: https://github.com/anujvyas/IPL-First-Innings-Score-Prediction-Deployment






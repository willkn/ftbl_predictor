# Set up the ML algorithm in here
# Continue to tune until < 10% accuracy
import pandas as pd
from sklearn import linear_model
import csv


def predictValue(name):
    df = pd.read_csv("players.csv")

    X = df[['overall', 'age', 'potential', 'international_reputation',
            'league_level', 'release_clause_eur', 'club_contract_valid_until']]
    y = df['value_eur']

    regr = linear_model.LinearRegression()
    regr.fit(X, y)

    playerValues = []
    playersLocal = []
    players = csv.reader(open('PlayerStats/players_22.csv'), delimiter=',')
    for row in players:
        playersLocal.append(row)

    for row in playersLocal:
        if(row[2] == name):
            playerValues = [row[5], row[9], row[6],
                            row[30], row[16], row[34], row[21]]
            break

    predictedValue = regr.predict([playerValues])
    return int(predictedValue)

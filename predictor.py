# Set up the ML algorithm in here
# Continue to tune until < 10% accuracy
import pandas as pd
from sklearn import linear_model
import csv

df = pd.read_csv("players.csv")
# def init():
#     playersLocal = []
#     attributes = ['sofifa_id', 'player_url', 'short_name', 'long_name', 'player_positions', 'overall', 'potential', 'value_eur', 'wage_eur', 'age', 'dob', 'height_cm', 'weight_kg', 'club_team_id', 'club_name', 'league_name', 'league_level', 'club_position', 'club_jersey_number', 'club_loaned_from', 'club_joined', 'club_contract_valid_until', 'nationality_id', 'nationality_name', 'nation_team_id', 'nation_position', 'nation_jersey_number', 'preferred_foot', 'weak_foot', 'skill_moves', 'international_reputation', 'work_rate', 'body_type', 'real_face', 'release_clause_eur', 'player_tags', 'player_traits', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic', 'attacking_crossing', 'attacking_finishing', 'attacking_heading_accuracy', 'attacking_short_passing', 'attacking_volleys', 'skill_dribbling', 'skill_curve', 'skill_fk_accuracy', 'skill_long_passing',
#                 'skill_ball_control', 'movement_acceleration', 'movement_sprint_speed', 'movement_agility', 'movement_reactions', 'movement_balance', 'power_shot_power', 'power_jumping', 'power_stamina', 'power_strength', 'power_long_shots', 'mentality_aggression', 'mentality_interceptions', 'mentality_positioning', 'mentality_vision', 'mentality_penalties', 'mentality_composure', 'defending_marking_awareness', 'defending_standing_tackle', 'defending_sliding_tackle', 'goalkeeping_diving', 'goalkeeping_handling', 'goalkeeping_kicking', 'goalkeeping_positioning', 'goalkeeping_reflexes', 'goalkeeping_speed', 'ls', 'st', 'rs', 'lw', 'lf', 'cf', 'rf', 'rw', 'lam', 'cam', 'ram', 'lm', 'lcm', 'cm', 'rcm', 'rm', 'lwb', 'ldm', 'cdm', 'rdm', 'rwb', 'lb', 'lcb', 'cb', 'rcb', 'rb', 'gk', 'player_face_url', 'club_logo_url', 'club_flag_url', 'nation_logo_url', 'nation_flag_url']

#     numbers = []
#     numbers.append(attributes.index('short_name'))
#     numbers.append(attributes.index('overall'))
#     numbers.append(attributes.index('age'))
#     numbers.append(attributes.index('potential'))
#     numbers.append(attributes.index('value_eur'))

#     players = csv.reader(open('PlayerStats/players_22.csv'), delimiter=',')
#     for row in players:
#         playersLocal.append(row)

#     for row in playersLocal:
#         tempValues = []
#         for number in numbers:
#             tempValues.append(row[number])

#         playerScope = ",".join(tempValues)

# A player name should be inputted into the preict function.


def predictValue(name):
    X = df[['overall', 'age', 'potential']]
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
            playerValues = [row[5], row[9], row[6]]
            break

    predictedValue = regr.predict([playerValues])
    return int(predictedValue)

import csv

import settings
from search import attributes


def similarPlayers():
    stats = ['pace', 'shooting', 'passing',
             'dribbling', 'defending', 'physic']

    playersLocal = []  # Changes from csv reader object to a python list
    for row in (csv.reader(open('PlayerStats/players_22.csv'), delimiter=',')):
        if (type(row[0]) != str):
            playersLocal.append(row)

    '''
    Probably a faster way to do this search, given its a psuedo-sorted list.
    Only perform the search between +- 10 overall of the player? Unlikely to miss potential matches 
    but cuts down a significant portion of the db. Helps meet the lightweight stakeholder requirement.  
    '''
    similar = []
    # Let valueRange be set manually by the user. Default should be 5.
    valueRange = 5
    for row in playersLocal:
        x = 0
        tempPlayer = dict(zip(attributes, row))
        for z in range(1, 6):
            if (tempPlayer.get('player_positions') != 'GK'): # This means the feature doesn't work for GK's currently.
                if ((int(float(settings.currentPlayerOutline[z]) - valueRange)) <= (int(float(tempPlayer.get(stats[z - 1])))) <= (int(float(settings.currentPlayerOutline[z]) + valueRange))):
                    x += 1

        if(x > 4):
            similar.append(tempPlayer.get('short_name'))

    print(similar)

    '''
    Could predict what players youth players are likely to be similar to in the future.
    Do the same thing with the range but add x points onto the values where x is determined by their potential,
    the higher the potential the higher x is.    

    Could also sort by similarity.  
    '''
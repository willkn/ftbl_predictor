import csv

import settings
from search import attributes


def similarPlayers():
    stats = ['pace', 'shooting', 'passing',
             'dribbling', 'defending', 'physic']


    playersLocal = []  # Changes from csv reader object to a python list
    for row in (csv.reader(open('PlayerStats/players_22.csv'), delimiter=',')):
        playersLocal.append(row)

    '''
    Probably a faster way to do this search, given its a psuedo-sorted list.
    Only perform the search between +- 10 overall of the player? Unlikely to miss potential matches 
    but cuts down a significant portion of the db.  
    '''
    similar = []
    valueRange = 5 # Let this be set manually by the user. Default should be 5.
    for row in playersLocal:
        x = 0
        tempPlayer = dict(zip(attributes, row))
        print(tempPlayer.get('short_name'))
        for z in range(1, 6):
            if (tempPlayer.get('player_positions') != 'GK'):
                print(stats[z], tempPlayer.get(stats[z]))

                if ((int(settings.currentPlayerOutline[z]) - valueRange) <= (int(tempPlayer.get(stats[z - 1]))) <= (int(settings.currentPlayerOutline[z]) + valueRange)):
                    print('testing!')
                    x += 1

        if(x > 4):
            similar.append(tempPlayer.get('short_name'))

    print(similar)

import csv
import settings

attributes = ['sofifa_id', 'player_url', 'short_name', 'long_name', 'player_positions', 'overall', 'potential', 'value_eur', 'wage_eur', 'age', 'dob', 'height_cm', 'weight_kg', 'club_team_id', 'club_name', 'league_name', 'league_level', 'club_position', 'club_jersey_number', 'club_loaned_from', 'club_joined', 'club_contract_valid_until', 'nationality_id', 'nationality_name', 'nation_team_id', 'nation_position', 'nation_jersey_number', 'preferred_foot', 'weak_foot', 'skill_moves', 'international_reputation', 'work_rate', 'body_type', 'real_face', 'release_clause_eur', 'player_tags', 'player_traits', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic', 'attacking_crossing', 'attacking_finishing', 'attacking_heading_accuracy', 'attacking_short_passing', 'attacking_volleys', 'skill_dribbling', 'skill_curve', 'skill_fk_accuracy', 'skill_long_passing',
              'skill_ball_control', 'movement_acceleration', 'movement_sprint_speed', 'movement_agility', 'movement_reactions', 'movement_balance', 'power_shot_power', 'power_jumping', 'power_stamina', 'power_strength', 'power_long_shots', 'mentality_aggression', 'mentality_interceptions', 'mentality_positioning', 'mentality_vision', 'mentality_penalties', 'mentality_composure', 'defending_marking_awareness', 'defending_standing_tackle', 'defending_sliding_tackle', 'goalkeeping_diving', 'goalkeeping_handling', 'goalkeeping_kicking', 'goalkeeping_positioning', 'goalkeeping_reflexes', 'goalkeeping_speed', 'ls', 'st', 'rs', 'lw', 'lf', 'cf', 'rf', 'rw', 'lam', 'cam', 'ram', 'lm', 'lcm', 'cm', 'rcm', 'rm', 'lwb', 'ldm', 'cdm', 'rdm', 'rwb', 'lb', 'lcb', 'cb', 'rcb', 'rb', 'gk', 'player_face_url', 'club_logo_url', 'club_flag_url', 'nation_logo_url', 'nation_flag_url']


def build():
    choice = int(
        input('To search for a player enter 1 or to search by attribute enter 2:\n'))

    if(choice == 1):
        print('Search for a player:')
        searchTerm = input().lower()
        return searchTerm

    elif(choice == 2):
        print(attributes)
        chosenAttribute = input(
            'Enter a filter from the above list:\n').lower()
        chosenValue = input('Enter a value to for your attribute:\n')
        searchTerm = {chosenAttribute: chosenValue}
        return searchTerm


# Create a key-value dictionary to make traversing the output easier
def executeQuery(queryResult):
    i = 0
    playersLocal = []
    players = csv.reader(open('PlayerStats/players_22.csv'), delimiter=',')
    for row in players:
        playersLocal.append(row)

    if (type(queryResult) == str):
        for row in playersLocal:
            # if (enchant.utils.levenshtein(query, row[3]))
            if(queryResult == (row[2]).lower()):
                settings.currentPlayer = dict(zip(attributes, row))
                print(settings.currentPlayer)
                break # If there is more than one of this player returned in the search, return the highest rated. 
    else:  # This code may need to be updated to be able to support multiple filters.
        x = list(queryResult.values())

        for item in queryResult:
            for row in playersLocal:
                if (row[attributes.index(item)] == x[0]):
                    settings.currentPlayer = dict(zip(attributes, row))

def query(searchTerm):  # Returns a query that is ready to be inputted into the search function
    if(type(searchTerm) != str):
        return (searchTerm)
    else:
        if(len(searchTerm) != 0):
            return (searchTerm)


def search():
    executeQuery(query(build()))
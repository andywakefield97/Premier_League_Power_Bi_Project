import pandas as pandas

dataset = pandas.DataFrame(dataset)

def player_image_adder (row):
    if row['Player'] == 'Sergio Aguero':
        return 'https://resources.premierleague.com/premierleague/photos/players/250x250/p37572.png'
    if row['Player'] == 'Sadio Mane':
        return 'https://resources.premierleague.com/premierleague/photos/players/250x250/p110979.png'
    if row['Player'] == 'Harry Kane':
        return 'https://resources.premierleague.com/premierleague/photos/players/250x250/p78830.png'
    if row['Player'] == 'Paul Pogba':
        return 'https://resources.premierleague.com/premierleague/photos/players/250x250/p74208.png'
    if row['Player'] == 'Pierre Emerick Aubameyang':
        return 'https://resources.premierleague.com/premierleague/photos/players/250x250/p54694.png'
    if row['Player'] == 'Mo Salah':
        return 'https://resources.premierleague.com/premierleague/photos/players/250x250/p118748.png'
    if row['Player'] == 'Eden Hazard':
        return 'https://resources.premierleague.com/premierleague/photos/players/250x250/p42786.png'
    if row['Player'] == 'Raheem Sterling':
        return 'https://resources.premierleague.com/premierleague/photos/players/250x250/p103955.png'
    if row['Player'] == 'Jamie Vardy':
        return 'https://resources.premierleague.com/premierleague/photos/players/250x250/p101668.png'
    if row['Player'] == 'Callum Wilson':
        return 'https://resources.premierleague.com/premierleague/photos/players/250x250/p75115.png'
    return 'N/A'

dataset['player_image'] = dataset.apply(lambda row: player_image_adder(row), axis = 1)

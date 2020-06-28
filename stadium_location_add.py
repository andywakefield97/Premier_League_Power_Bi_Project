import pandas as pandas


dataset = pandas.read_csv('D://england-premier-league-matches-2018-to-2019-stats.csv')

dataset = pandas.DataFrame(dataset)

def latitude_location_identifier (row):
    if row['stadium_name'] == 'Anfield':
        return '53.4308358'
    if row['stadium_name'] == 'Cardiff City Stadium':
        return '51.47284635'
    if row['stadium_name'] == 'Craven Cottage':
        return '51.474954'
    if row['stadium_name'] == 'Etihad Stadium':
        return '53.48309105'
    if row['stadium_name'] == 'Emirates Stadium':
        return '51.55504035'
    if row['stadium_name'] == 'Goodison Park':
        return '53.4387191'
    if row['stadium_name'] == 'King Power Stadium':
        return '52.62039695'
    if row['stadium_name'] == 'London Stadium':
        return '51.5386807'
    if row['stadium_name'] == 'Molineux Stadium':
        return '52.590281'
    if row['stadium_name'] == 'Old Trafford':
        return '53.46310955'
    if row['stadium_name'] == 'Selhurst Park':
        return '51.39824295'
    if row['stadium_name'] == "St. James' Park (Newcastle upon Tyne)":
        return '54.9754693'
    if row['stadium_name'] == "St. Mary's Stadium":
        return '50.90582665'
    if row['stadium_name'] == 'Stamford Bridge':
        return '51.4816865'
    if row['stadium_name'] == 'The American Express Community Stadium':
        return '50.86154985'
    if row['stadium_name'] == "The John Smith's Stadium":
        return '53.65434935'
    if row['stadium_name'] == 'Tottenham Hotspur Stadium':
        return '51.6041916'
    if row['stadium_name'] == 'Turf Moor':
        return '53.7881472'
    if row['stadium_name'] == 'Vicarage Road Stadium':
        return '51.64975455'
    if row['stadium_name'] == 'Vitality Stadium':
        return '50.73518145'
    if row['stadium_name'] == 'Wembley Stadium':
        return '51.55598385'
    return 'N/A'


def longitude_location_identifier (row):
    if row['stadium_name'] == 'Anfield':
        return '-2.96090954'
    if row['stadium_name'] == 'Cardiff City Stadium':
        return '-3.20287484'
    if row['stadium_name'] == 'Craven Cottage':
        return '-0.22168378'
    if row['stadium_name'] == 'Etihad Stadium':
        return '-2.200252'
    if row['stadium_name'] == 'Emirates Stadium':
        return '-0.10839967'
    if row['stadium_name'] == 'Goodison Park':
        return '-2.96645399'
    if row['stadium_name'] == 'King Power Stadium':
        return '-1.14233521'
    if row['stadium_name'] == 'London Stadium':
        return '-0.01787252'
    if row['stadium_name'] == 'Molineux Stadium':
        return '-2.13040078'
    if row['stadium_name'] == 'Old Trafford':
        return '-2.29138649'
    if row['stadium_name'] == 'Selhurst Park':
        return '-0.08525506'
    if row['stadium_name'] == "St. James' Park (Newcastle upon Tyne)":
        return '-1.62187367'
    if row['stadium_name'] == "St. Mary's Stadium":
        return '-1.39088167'
    if row['stadium_name'] == 'Stamford Bridge':
        return '-0.19196366'
    if row['stadium_name'] == 'The American Express Community Stadium':
        return '-0.08486805'
    if row['stadium_name'] == "The John Smith's Stadium":
        return '-1.76829988'
    if row['stadium_name'] == 'Tottenham Hotspur Stadium':
        return '-0.06623491'
    if row['stadium_name'] == 'Turf Moor':
        return '-2.2296491'
    if row['stadium_name'] == 'Vicarage Road Stadium':
        return '-0.401348'
    if row['stadium_name'] == 'Vitality Stadium':
        return '-1.83832795'
    if row['stadium_name'] == 'Wembley Stadium':
        return '-0.27957892'
    return 'N/A'

def badge_image_add (row):
    if row['stadium_name'] == 'Anfield':
        return 'https://upload.wikimedia.org/wikipedia/en/thumb/0/0c/Liverpool_FC.svg/791px-Liverpool_FC.svg.png'
    if row['stadium_name'] == 'Cardiff City Stadium':
        return 'https://upload.wikimedia.org/wikipedia/en/thumb/3/3c/Cardiff_City_crest.svg/983px-Cardiff_City_crest.svg.png'
    if row['stadium_name'] == 'Craven Cottage':
        return 'https://upload.wikimedia.org/wikipedia/en/thumb/e/eb/Fulham_FC_%28shield%29.svg/769px-Fulham_FC_%28shield%29.svg.png'
    if row['stadium_name'] == 'Etihad Stadium':
        return 'https://upload.wikimedia.org/wikipedia/en/thumb/e/eb/Manchester_City_FC_badge.svg/1024px-Manchester_City_FC_badge.svg.png'
    if row['stadium_name'] == 'Emirates Stadium':
        return 'https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Arsenal_FC.svg/872px-Arsenal_FC.svg.png'
    if row['stadium_name'] == 'Goodison Park':
        return 'https://upload.wikimedia.org/wikipedia/en/thumb/7/7c/Everton_FC_logo.svg/1002px-Everton_FC_logo.svg.png'
    if row['stadium_name'] == 'King Power Stadium':
        return 'https://upload.wikimedia.org/wikipedia/en/thumb/2/2d/Leicester_City_crest.svg/1024px-Leicester_City_crest.svg.png'
    if row['stadium_name'] == 'London Stadium':
        return 'https://upload.wikimedia.org/wikipedia/en/thumb/c/c2/West_Ham_United_FC_logo.svg/920px-West_Ham_United_FC_logo.svg.png'
    if row['stadium_name'] == 'Molineux Stadium':
        return 'https://upload.wikimedia.org/wikipedia/en/thumb/f/fc/Wolverhampton_Wanderers.svg/1024px-Wolverhampton_Wanderers.svg.png'
    if row['stadium_name'] == 'Old Trafford':
        return 'https://upload.wikimedia.org/wikipedia/en/thumb/7/7a/Manchester_United_FC_crest.svg/1010px-Manchester_United_FC_crest.svg.png'
    if row['stadium_name'] == 'Selhurst Park':
        return 'https://upload.wikimedia.org/wikipedia/en/thumb/0/0c/Crystal_Palace_FC_logo.svg/821px-Crystal_Palace_FC_logo.svg.png'
    if row['stadium_name'] == "St. James' Park (Newcastle upon Tyne)":
        return 'https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Newcastle_United_Logo.svg/1017px-Newcastle_United_Logo.svg.png'
    if row['stadium_name'] == "St. Mary's Stadium":
        return 'https://upload.wikimedia.org/wikipedia/en/thumb/c/c9/FC_Southampton.svg/897px-FC_Southampton.svg.png'
    if row['stadium_name'] == 'Stamford Bridge':
        return 'https://upload.wikimedia.org/wikipedia/en/thumb/c/cc/Chelsea_FC.svg/1024px-Chelsea_FC.svg.png'
    if row['stadium_name'] == 'The American Express Community Stadium':
        return 'https://upload.wikimedia.org/wikipedia/en/thumb/f/fd/Brighton_%26_Hove_Albion_logo.svg/1024px-Brighton_%26_Hove_Albion_logo.svg.png'
    if row['stadium_name'] == "The John Smith's Stadium":
        return 'https://upload.wikimedia.org/wikipedia/en/7/7d/Huddersfield_Town_A.F.C._logo.png'
    if row['stadium_name'] == 'Tottenham Hotspur Stadium':
        return 'https://upload.wikimedia.org/wikipedia/en/thumb/b/b4/Tottenham_Hotspur.svg/499px-Tottenham_Hotspur.svg.png'
    if row['stadium_name'] == 'Turf Moor':
        return 'https://upload.wikimedia.org/wikipedia/en/thumb/6/62/Burnley_F.C._Logo.svg/876px-Burnley_F.C._Logo.svg.png'
    if row['stadium_name'] == 'Vicarage Road Stadium':
        return 'https://upload.wikimedia.org/wikipedia/en/thumb/e/e2/Watford.svg/917px-Watford.svg.png'
    if row['stadium_name'] == 'Vitality Stadium':
        return 'https://upload.wikimedia.org/wikipedia/en/thumb/e/e5/AFC_Bournemouth_%282013%29.svg/781px-AFC_Bournemouth_%282013%29.svg.png'
    if row['stadium_name'] == 'Wembley Stadium':
        return 'https://upload.wikimedia.org/wikipedia/en/thumb/b/b4/Tottenham_Hotspur.svg/499px-Tottenham_Hotspur.svg.png'
    return 'N/A'



dataset['Latitude'] = dataset.apply(lambda row: latitude_location_identifier(row), axis = 1)
dataset['Longitude'] = dataset.apply(lambda row: longitude_location_identifier(row), axis = 1)
dataset['Image'] = dataset.apply(lambda row: badge_image_add(row), axis = 1)

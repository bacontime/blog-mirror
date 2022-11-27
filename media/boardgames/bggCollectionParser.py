'''
This script parses the collection.csv,
which is exported from bgg,
and converts it to an html or markdown table 
with trimmed down information.
'''
#%%
import csv

gameDataMap = dict()

langMap = {
    "No necessary in-game text": "0",
    "Some necessary text - easily memorized or small crib sheet": "1",
    "Moderate in-game text - needs crib sheet or paste ups": "2",
    "Extensive use of text - massive conversion needed to be playable": "3",
    "Unplayable in another language": "4",
    "": "?",
}

with open("collection.csv", encoding="utf8") as f:
    #for line in f.readlines():
    csv_reader = csv.reader(f, delimiter=',')
    next(csv_reader) #skips first row
    for row in csv_reader:
        name, myrating, avgrating, weight, bggrecplayers, bgglanguagedependence = row[0], row[2], row[21], row[22], row[33], row[36]
        #print([(i,x) for i,x in enumerate(row)])
        players = bggrecplayers.split(',')
        weight = weight[:3]
        minplayer,maxplayer = players[0], players[-1]
        wordiness = langMap[bgglanguagedependence]
        if myrating == "0":
            myrating = ""
        gameDataMap[name] = [name, myrating, minplayer,maxplayer, weight, wordiness]



# TODO: include info on whether game is homemade, customized, etc.
# player count, language dependency, age?


#%% Define function for creating markdown row
def printMDRow(gamename):
    game = gameDataMap[gamename]
    #print(game)
    assert len(game) == 6
    print('| ' + ' | '.join(game) + ' |')
    #print(r'<tr><td>' + r'</td><td>'.join(game) + r'</td><td>')



tableHeader = r'''<table class="js-sort-table">
<thead>
<tr><td>Name</td><td>Rating</td><td>minP</td><td>maxP</td><td>weight</td><td>wordy</td></tr>
</thead><tbody>
'''
tableFooter = r"</tbody></table>"


tableHeader = "| Name | rating | minP | maxP | weight | wordy |\n|:--|:-:|:-:|:-:|:-:|:-:|"
tableFooter = "{: .js-sort-table }"



# %%
shelfList = [
    'Watson & Holmes',
    'Castles of Mad King Ludwig',
    'Blueprints',
    'Mysterium',
    'The Quest for El Dorado',
    'Zendo',
    'Cthulhu Wars',
    'Jaipur',
    'Kingdomino',
    'Raptor',
    'My Little Scythe',
    'Okey Dokey',
    'Photosynthesis',
    'Dancing Eggs',
    'KeyForge: Call of the Archons',
    'Agricola',
    'Machi Koro Legacy',
    'Mahjong',
    'Hive Pocket',
    'TAJ',
    'Codenames: Pictures',
    'Codenames: Duet',
    'Tsuro',
    'Mage Knight Board Game',
    'Scoville',
    'Sherlock Holmes Consulting Detective: Jack the Ripper & West End Adventures',
    'Disney Villainous: Perfectly Wretched',
    'Charterstone',
    'Hanamikoji',
    'Planet',
    'Funkoverse Strategy Game',
    'Attack on Titan: The Last Stand',
    'Coup',
    'Pandemic: Iberia',
    'Adventure Time Card Wars: Finn vs. Jake',
    'The Castles of Burgundy',
    'Porta Nigra',
    'Biblios',
    'Sushi Go Party!',
    'Tales & Games: The Hare & the Tortoise',
    'Santorini',
    'Bob Ross: Art of Chill Game',
    'Azul',
    'ICECOOL',
    'Caverna: Cave vs Cave',
    'Welcome to the Dungeon',
    'Magic: The Gathering – Heroes of Dominaria Board Game',
    'Lord of the Rings: The Confrontation',
    'String Railway',
    'Trains: Rising Sun',
    'Catacombs (Third Edition)',
]

otherInHouseList = [
    'Portal: The Uncooperative Cake Acquisition Game',
    'Jungle Speed',
    'ZÈRTZ',
    'Loony Quest',
    'Jenga',
    'Deep Sea Adventure',
    'Love Letter',
    'BANG! The Dice Game',
    'Epic Card Game',
    'Spot it!',
    'Epic Card Game',
    'Mint Works',
    'Portal: The Uncooperative Cake Acquisition Game',
    'Go',
]


excludedGames = [ # games not to be converted to markdown
    #'Mahjong Rummy',
    'Hive',
    'Homeworlds',
]


#%% print the games in my apartment
print(tableHeader)
for game in shelfList:
    printMDRow(game)
for game in otherInHouseList:
    printMDRow(game)
print(tableFooter)


#%% Print other games in collection

print(tableHeader)
otherGames = set(gameDataMap.keys()) - set(shelfList) - set(otherInHouseList) - set(excludedGames)
for game in otherGames:
    printMDRow(game)
print(tableFooter)

# %%

# ---
# jupyter:
#   jupytext:
#     formats: ipynb,md,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# <img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 15px; height: 80px">
#
# # Project 1
#
# ### Building "Pokemon Stay"
#
# ---
# You are an analyst at a "scrappy" online gaming company that specializes in remakes of last year's fads.
#
# Your boss, who runs the product development team, is convinced that Pokemon Go's fatal flaw was that you had to actually move around outside. She has design mock-ups for a new game called Pokemon Stay: in this version players still need to move, but just from website to website. Pokemon gyms are now popular online destinations, and catching Pokemon in the "wild" simply requires browsing the internet for hours in the comfort of your home.
#
# She wants you to program a prototype version of the game, and analyze the planned content to help the team calibrate the design.

# #### Package imports
#
# The pprint package below is the only package imported here, and it's not even strictly required to do any of the project. Printing python variables and objects with pprint can help to format them in a "prettier" way.

from pprint import pprint

# <img src="http://imgur.com/l5NasQj.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
#
# ## 1. Defining a player
#
# ---
#
# The player variables are:
#
#     player_id : id code unique to each player (integer)
#     player_name : entered name of the player (string)
#     time_played : number of time played the game in minutes (float)
#     player_pokemon: the player's captured pokemon (dictionary)
#     gyms_visited: ids of the gyms that a player has visited (list)
#     
# Create the components for a player object by defining each of these variables. The dictionary and list variables should just be defined as empty; you can use any (correctly typed) values for the others.

## Creating Variables for player 1234
player_id = 1234
player_name = 'Arthur Ketchum'
time_played = 45.6
player_pokemon = {}
gyms_visited = []

# <img src="http://imgur.com/l5NasQj.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
#
# ## 2. Defining "gym" locations
#
# ---
#
# As the sole programmer, Pokemon Stay will have to start small. To begin, there will be 10 different gym location websites on the internet. The gym locations are:
#
#     1. 'reddit.com'
#     2. 'amazon.com'
#     3. 'twitter.com'
#     4. 'linkedin.com'
#     5. 'ebay.com'
#     6. 'netflix.com'
#     7. 'amazon.com'
#     8. 'stackoverflow.com'
#     9. 'github.com'
#     10. 'quora.com'
#
# 1. Set up a list of all the gym locations. This will be a list of strings.
# 2. Append two of these locations to your player's list of visited gyms.
# 3. Print the list.

# Creating list of pokemon_gyms for Pokemon Stay
pokemon_gyms = ['reddit.com','amazon.com','twitter.com','linkedin.com','ebay.com','netflix.com','amazon.com',
        'stackoverflow.com','github.com','quora.com']

## Add linkedin.com and stackoverflow.com to list of gyms visited by 
## player 1234
gyms_visited.extend([pokemon_gyms[3],pokemon_gyms[7]])

## Confirm poke_gyms and appending was successful
print('pokemon_gyms \n',pokemon_gyms)
print('\ngyms_visited \n',gyms_visited)

# <img src="http://imgur.com/l5NasQj.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
#
# ## 3. Create a pokedex
#
# ---
#
# We also need to create some pokemon to catch. Each pokemon will be defined by these variables:
#
#     pokemon_id : unique identifier for each pokemon (integer)
#     name : the name of the pokemon (string)
#     type : the category of pokemon (string)
#     hp : base hitpoints (integer)
#     attack : base attack (integer)
#     defense : base defense (integer)
#     special_attack : base special attack (integer)
#     special_defense : base sepecial defense (integer)
#     speed : base speed (integer)
#
# We are only going to create 3 different pokemon with these `pokemon_id` and `pokemon_name` values:
#
#     1 : 'charmander'
#     2 : 'squirtle'
#     3 : 'bulbasaur'
#
# Create a dictionary that will contain the pokemon. The keys of the dictionary will be the `pokemon_id` and the values will themselves dictionaries that contain the other pokemon variables. The structure of the pokedex dictionary will start like so:
#      
#      {
#          1: {
#                  'name':'charmander',
#                  'type':'fire',
#                  ...
#                  
# The `type` of charmander, squirtle, and bulbasaur should be `'fire'`, `'water'`, and `'poison'` respectively. The other values are up to you, make them anything you like!
#
# Print (or pretty print) the pokedex dictionary with the 3 pokemon.

## Creating pokedex as instructed.
pokedex = {1 :{
                'name': 'charmander',
                'type': 'fire',
                'hp': 39,
                'attack': 52,
                'defense': 43,
                'special_attack': 60,
                'special_defense': 50,
                'speed': 65},
           2 :{'name': 'squirtle',
               'type': 'water',
               'hp': 44,
               'attack':48,
               'defense':65,
               'special_attack':50,
               'special_defense':64,
               'speed': 43},
           3 : {'name': 'bulbasaur',
                'type': 'poison',
                'hp': 46,
                'attack': 49,
                'defense': 49,
                'special_attack': 65,
                'special_defense': 65,
                'speed': 45}}

# Confirmation
pprint(pokedex)

# <img src="http://imgur.com/l5NasQj.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
#
# ## 4. Create a data structure for players
#
# ---
#
# ### 4.1 
#
# In order to maintain a database of multiple players, create a dictionary that keeps track of players indexed by `player_id`. 
#
# The keys of the dictionary will be `player_id` and values will be dictionaries containing each player's variables (from question 1). 
#
# Construct the `players` dictionary and insert the player that you defined in question 1, then print `players`.

# Creating player dictionary database
players = {}

## Adding player 1234 into players database using variables created 
## in question 1
players[player_id] = {'player_name': player_name,
                 'time_played': time_played,
                 'player_pokemon': player_pokemon,
                 'gyms_visited': gyms_visited}

# Confirmation
pprint(players)

# ---
#
# ### 4.2
#
# Create a new player with `player_id = 2` in the `players` dictionary. Leave the `'player_pokemon'` dictionary empty. Append `'alcatraz'` and `'pacific_beach'` to the `'gyms_visited'` list for player 2.
#
# The `'player_name'` and `'time_played'` values are up to you, but must be a string and float, respectively.
#
# Remember, the player_id is the key for the player in the players dictionary.
#
# Print the `players` dictionary with the new player inserted.

## Adding player 2 to database
players[2] = {'player_name': "Gideon Oak",
             'time_played' : 86.2,
             'player_pokemon' : {},
             'gyms_visited': []}

## Appending alcatraz and pacific_beach to player 2's visited gyms
players[2]['gyms_visited'] = ['alcatraz','pacific_beach']

# Confirming
pprint(players)

# <img src="http://imgur.com/l5NasQj.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
#
# ## 5. Add captured pokemon for each player
#
# ---
#
# The `'player_pokemon'` keyed dictionaries for each player keep track of which of the pokemon each player has.
#
# The keys of the `'player_pokemon'` dictionaries are the pokemon ids that correspond to the ids in the `pokedex` dictionary you created earlier. The values are integers specifying the stats for the pokemon.
#
# Give player 1 a squirtle. Give player 2 charmander and a bulbasaur.
#
# Print the players dictionary after adding the pokemon for each player.
#

## Giving player 1(1234) squirtle
players[1234]['player_pokemon'].update({2 : pokedex[2]})

## Giving player 2 charmander and bulbasaur
players[2]['player_pokemon'].update({1 : pokedex[1], 3 : pokedex[3]})

#Confirm
pprint(players)

#
#
# ## 6. What gyms have players visited?
#
# ---
# <img src="http://imgur.com/l5NasQj.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
# ### 6.1
#
# Write a for-loop that:
#
# 1. Iterates through the `pokemon_gyms` list of gym locations you defined before.
# 2. For each gym, iterate through each player in the `players` dictionary with a second, internal for-loop.
# 3. If the player has visited the gym, print out "[player] has visited [gym location].", filling in [player] and [gym location] with the current player's name and current gym location.

## For every gym in the list:pokemon_gyms, check if that gym is in 
## The list of gyms visited for each player.
## Print gym if true
for gym in pokemon_gyms:
    for player,stats in players.items():
        if gym in stats['gyms_visited']:
            print(f"{player} has visited {gym}")

# <img src="http://imgur.com/xDpSobf.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
# ### 6.2
#
# How many times did that loop run? If you have N gyms and also N players, how many times would it run as a function of N?
#
# Can you think of a more efficient way to accomplish the same thing? 
#
# (You can write your answer as Markdown text.)



# <img src="http://imgur.com/l5NasQj.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
#
# ## 7. Calculate player "power".
#
# ---
#
# Define a function that will calculate a player's "power". Player power is defined as the sum of the base statistics all of their pokemon.
#
# Your function will:
#
# 1. Accept the `players` dictionary, `pokedex` dictionary, and a player_id as arguments.
# 2. For the specified player_id, look up that player's pokemon and their level(s).
# 3. Find and aggregate the attack and defense values for each of the player's pokemon from the `pokedex` dictionary.
# 4. Print "[player name]'s power is [player power].", where the player power is the sum of the base statistics for all of their pokemon.
# 5. Return the player's power value.
#
# Print out the pokemon power for each of your players.

def player_power(id,players=players,pokedex=pokedex):
    power = 0
    pokemon = [pokemon_id for pokemon_id in players[id]['player_pokemon']]
# Create power variable
# Creates list of pokemon owned by id
    
    for pokemon_id in pokemon:
        pokemon = players[id]['player_pokemon'][pokemon_id]
        power += pokemon['attack'] + pokemon['defense']  + pokemon['special_defense'] + pokemon['special_defense'] + pokemon['hp'] + pokemon['speed']
# For each pokemon owned by id. Add their base stats to the power variable 
## Inner 'pokemon' varaible created for less typing.
    
    print(f"{players[id]['player_name']}'s power is {power}")
#           Print the out the player's name and their power number


#Confirm
player_power(1234)

#Confirm
player_power(2)

# <img src="http://imgur.com/l5NasQj.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
#
# ## 8. Load a pokedex file containing all the pokemon
#
# ---
#
# ### 8.1
#
# While you were putting together the prototype code, your colleagues were preparing a dataset of Pokemon and their attributes. (This was a rush job, so they may have picked some crazy values for some...)
#
# The code below loads information from a comma separated value (csv) file. You need to parse this string into a more useable format. The format of the string is:
#
# - Rows are separated by newline characters: \n
# - Columns are separated by commas: ,
# - All cells in the csv are double quoted. Ex: "PokedexNumber" is the first cell of the first row.
#
#
# Using for-loops, create a list of lists where each list within the overall list is a row of the csv/matrix, and each element in that list is a cell in that row. Additional criteria:
#
# 1. Quotes are removed from each cell item.
# 2. Numeric column values are converted to floats.
# 3. There are some cells that are empty and have no information. For these cells put a -1 value in place.
#
# Your end result is effectively a matrix. Each list in the outer list is a row, and the *j*th elements of list together form the *j*th column, which represents a data attribute. The first three lists in your pokedex list should look like this:
#
#     ['PokedexNumber', 'Name', 'Type', 'Total', 'HP', 'Attack', 'Defense', 'SpecialAttack', 'SpecialDefense', 'Speed']
#     [1.0, 'Bulbasaur', 'GrassPoison', 318.0, 45.0, 49.0, 49.0, 65.0, 65.0, 45.0]
#     [2.0, 'Ivysaur', 'GrassPoison', 405.0, 60.0, 62.0, 63.0, 80.0, 80.0, 60.0]

# Load csv into variable:raw_pd
with open('pokedex_basic.csv', 'r') as f:
    raw_pd = f.readlines()

# +
clean_pd = []
# new variable for cleaned pokedex

for row in raw_pd:
    new_row = []
#     create an empty list
    
    row_fixed = row[:-1].split(',')
#     remove \n in -1 and split row by ,'s 
    
    for cell in row_fixed:
        if cell in (None, ""):
            cell_pd.append(-1)
#             Add -1 if cell is empty
        else:
            try:
                new_row.append(float(cell.replace('"','')))
#                 Recognises number strings, convert to float, and add to new_row 
            except:
                new_row.append(cell.replace('"',''))
#                 Else add the string to new_row. Float() on string with no numbers creates an error.
    clean_pd.append(new_row)
#     add cleaned 'new_row' to 'clean_pd' list

# -

#Confirm
clean_pd

# <img src="http://imgur.com/xDpSobf.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
#
# ### 8.2 Parse the raw pokedex with list comprehensions
#
# ---
#
# Perform the same parsing as above, but **using only a single list comprehension** instead of for loops. You may have nested list comprehensions within the main list comprehension! The output should be exactly the same.

lc_clean_pd = [[-1 if cell in (None,"") 
                ## Checks empty cells
                else float(cell.replace('"','')) if cell.replace('"','').isdigit() == True 
                ## Converts number_strings using .isdigit()
                else cell.replace('"','') 
                ## Add strings, removing ""'s
                for cell in row[:-1].split(',')]
#                [:-1] removes \n
               for row in raw_pd]

lc_clean_pd

# <img src="http://imgur.com/l5NasQj.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
#
# ## 9. Write a function to generate the full pokedex
#
# ---
#
# Write a function that recreates the pokedex you made before, but with the data read in from the full pokemon file. The `PokedexNumber` should be used as the `pokemon_id` key values for the dictionary of pokemon.
#
# Your function should:
#
# 1. Take the parsed pokedex information you created above as an argument.
# 2. Return a dictionary in the same format as your original pokedex you created before containing the information from the parsed full pokedex file.
#
# To test the function, print out the pokemon with id = 100.

# +
LARGE_POKEDEX = {}
## Create a new dictionary

for a_row in lc_clean_pd[1:]:

    poke_id = a_row[0]
    while poke_id in LARGE_POKEDEX.keys():
        poke_id += 0.1
# This section ensures pokemon's with the same id in the csv are added to this dictionary with a unique key
# It assigns the id to a variable and will keep adding 0.1 to the variable if the variable already exists in 
# Pokemon dictionary.
    
    LARGE_POKEDEX[poke_id] = {'name': a_row[1],
                                'type': a_row[2],
                                'total': a_row[3],
                                'hp': a_row[4],
                                'attack': a_row[5],
                                'defense': a_row[6],
                                'special_attack': a_row[7],
                                'special_defense': a_row[8],
                              'speed': a_row[9]} 
#     Add the relavent stats dictinary using a unique poke_id 
# -

#Confirm
LARGE_POKEDEX

LARGE_POKEDEX.keys()
# Confirms adding 0.1 is sufficent for duplicate pervention.

# <img src="http://i.imgur.com/GCAf1UX.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
#
# ## 10. Write a function to generate a "filtered" pokedex
# ---
# Your function should:
# 1. Take the parsed pokedex information you created above as an argument.
# 1. Take a dictionary as a parameter with keys matching the features of the Pokedex, filtering by exact match for string type values, and/or filter continuous variables specified value that is greater than or equal to the dictionary key parameter.
# 1. Return multiple elements from the Pokedex
#
# Example:
#
# ```python
#
# # Only filter based on parameters passed
# filter_options = {
#     'Attack':   25,
#     'Defense':  30,
#     'Type':     'Electric'
# }
#
# # Return records with attack >= 24, defense >= 30, and type == "Electric"
# # Also anticipate that other paramters can also be passed such as "SpecialAttack", "Speed", etc.
# filtered_pokedex(pokedex_data, filter=filter_options)
#
# # Example output:
# # [{'Attack': 30.0,
# #  'Defense': 50.0,
# #  'HP': 40.0,
# #  'Name': 'Voltorb',
# #  'SpecialAttack': 55.0,
# #  'SpecialDefense': 55.0,
# #  'Speed': 100.0,
# #  'Total': 330.0,
# #  'Type': 'Electric'},
# #  {'Attack': 30.0,
# #  'Defense': 33.0,
# #  'HP': 32.0,
# #  'Name': 'Pikachu',
# #  'SpecialAttack': 55.0,
# #  'SpecialDefense': 55.0,
# #  'Speed': 100.0,
# #  'Total': 330.0,
# #  'Type': 'Electric'},
# #  ... etc
# #  ]
#
# ```
#
#

# +
## My original code didn't take in the filter_option dictionary parameter.
## I decided to write the code to take in both parameters and dictionary.

# +
def LARGE_POKEDEX_FILTER(attack=0,defense=0,hp=0,name='',specialattack=0,specialdefense=0,speed=0,pokemon_type='',total=0,
                        filter_options={}):
    
    filter_option = {'name':'',
                     'attack':0,
                     'defense':0,
                    'special_attack':0,
                    'special_defense':0,
                    'hp':0,
                    'total':0,
                    'type':'',
                    'speed':0}
#     Create an empty dictionary containing default values for each stat.
#     If the person doesn't input all the keys of the filter, the function will not be able to do a comparison
#     with a non exsisting key (Error). 

# The rest of the function will call keys from each keys from this default dictionary.
    
    if filter_options != {}:
        for key,value in filter_options.items():
            filter_option[key.lower()] = value 
#     If the person does input in a dictionary. The inputed dictionary keys will update the keys in the default 
#     default dictionary. Incorrect key input will not effect the function. .lower() prevents lower/upper case issues

# Rest of the function performs filtering 
    
    filtered_dictionary = {}
#     This dictionary will contain the results of each filtering operation and the final output.    

    if '' != (name or filter_option['name']):
        filtered_dictionary = {i:LARGE_POKEDEX[i] for i,values in LARGE_POKEDEX.items() if values['name'].lower() == (name.lower() or filter_options['name'].lower())}
    else:
        filtered_dictionary = LARGE_POKEDEX
#     If a name is given by the person. Update the filtered dictionary with items from the LARGE_POKEDEX dictionary
#     ELSE: let filtered_dictionary be the entire LARGE_POKEDEX
        
 
    if '' != (pokemon_type or filter_option['type']):
            filtered_dictionary = {i:filtered_dictionary[i] for i,values in filtered_dictionary.items() if values['type'].lower() == (pokemon_type.lower() or filter_options['type'].lower())}
    else:
        pass
#     Do the same if the person gives a type. .lower() stops case issues.
#     Pass this function if no type is given.

# Filter by name and then type and then numbers are the most efficent ways of writing the code.
# Attempting to combine name and type functions isn't functional. Function won't be robust if person inputs both
# A name and a type.

    filtered_dictionary = {i:filtered_dictionary[i] for i,values in filtered_dictionary.items() if values['speed'] >= max([speed,filter_option['speed']])}
    filtered_dictionary = {i:filtered_dictionary[i] for i,values in filtered_dictionary.items() if values['special_defense'] >= max(specialdefense,filter_option['special_defense'])}
    filtered_dictionary = {i:filtered_dictionary[i] for i,values in filtered_dictionary.items() if values['special_attack'] >= max(specialattack,filter_option['special_attack'])}
    filtered_dictionary = {i:filtered_dictionary[i] for i,values in filtered_dictionary.items() if values['hp'] >= max(hp,filter_option['hp'])}
    filtered_dictionary = {i:filtered_dictionary[i] for i,values in filtered_dictionary.items() if values['defense'] >= max(defense,filter_option['defense'])}
    filtered_dictionary = {i:filtered_dictionary[i] for i,values in filtered_dictionary.items() if values['attack'] >= max(attack,filter_option['attack'])}
    filtered_dictionary = {i:filtered_dictionary[i] for i,values in filtered_dictionary.items() if values['total'] >= max(total,filter_option['total'])}
#     For each numerical pokemon stat. Update filtered_dictionary with items are are larger or equal to the max of 
#     Either the parameter or the default_dictionary.
#     If the person doesn't input a number, all is good because the function contains default values in the function
#     and the dictionary (=0)
    

    
    return filtered_dictionary
#     Prints the final result
# -

# # Tests

LARGE_POKEDEX_FILTER(filter_options={'speed':133}, pokemon_type='electric', attack=40,speed=120)

LARGE_POKEDEX_FILTER(filter_options={'speed':120}, pokemon_type='electric', attack=40,speed=133)

LARGE_POKEDEX_FILTER(filter_options={'name':'MewtwoMega Mewtwo X','speed':0},)

LARGE_POKEDEX_FILTER(speed=90,total=750)

LARGE_POKEDEX_FILTER(filter_options={'speed':135},speed=90,total=750)

LARGE_POKEDEX_FILTER(filter_options={'speed': 90,'total':750},speed=135)


# ## 9. Descriptive statistics on the prototype pokedex
#
# <img src="http://imgur.com/l5NasQj.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
# ### 9.1
#
# What is the population mean and standard deviation of the "Total" attribute for all characters in the Pokedex?
#
#

import pandas as pd
# Pandas makes it easier. Creating tables called dataframes

# +
df = pd.DataFrame(data=lc_clean_pd,columns = lc_clean_pd[0])
# Create a dataframe using the cleaned csv. 

df_v2 = df[1:]
# Removes the first row of the table, containing the header titles.

df_v2.set_index('PokedexNumber', inplace=True)
# Sets the index for each row to be the pokedexNumber column.
# -

# Check and confirm
df_v2.head()

print(f" The mean is {df_v2['Total'].mean()}")
print(f" The standard deviation is {df_v2['Total'].std()}")

# <img src="http://imgur.com/l5NasQj.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
# ### 9.2
#
# The game is no fun if the characters are wildly unbalanced! Are any characters "overpowered", which we'll define as having a "Total" more than three standard deviations from the population mean?

import numpy as np
import scipy.stats as stats

## Create varaibles representing the 3 standard deviation threshold
std3 = df_v2['Total'].mean() + (df_v2['Total'].std())*3
std3_neg = df_v2['Total'].mean() - (df_v2['Total'].std())*3
print(std3,std3_neg)

# Outputs a dataframe showing pokemon who's total lies outside of the 3-std range.
df_v2[(df_v2["Total"] > std3) | (df_v2['Total'] < std3_neg)]

# <img src="http://imgur.com/xDpSobf.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
#
# ## 10. Calibrate the frequency of Pokemon
#
# The design team wants you to make the powerful Pokemon rare, and the weaklings more common. How would you set the probability $p_i$ of finding Pokemon *i* each time a player visits a gym?
#
# Write a function that takes in a Pokedex number and returns a value $p_i$ for that character.
#
# Hint: there are many ways you could do this. What do _you_ think makes sense? Start with simplifying assumptions: for example, you could assume that the probabilities of encountering any two Pokemon on one visit to a gym are independent of each other.

# +
## Frequency assignment formula:
# (max(Total) - total + (min(Total)/2) / max(Total)

# Frequency is then inversely proportional (kinda) to total stat.
# min(Total)/2 prevents the lower level pokemon having a prob of 1
# -

## Assigning total_max and min variables
total_max = df_v2['Total'].max()
total_min = df_v2['Total'].min()

## Creating a new frequency column
df_v2['Frequency'] = df_v2['Total'].apply(lambda num: (total_max-num+(total_min/2))/total_max)
# Note: Write comment for this

## Index has duplication, fix with keys from LARGE_POKEDEX.
df_v2['PokdexNumber_fixed'] = LARGE_POKEDEX.keys()

## Set the new index to this 
df_v2.reset_index()


def get_probability(PokedexNumber=None,name=None):
    if type(PokedexNumber) == str:
        name = PokedexNumber
    else:
        pass
    
    if name != None:
        return df_v2[df_v2['Name'] == name]['Frequency']
    elif PokedexNumber != None:
        return df_v2[df_v2['PokdexNumber_fixed'] == PokedexNumber]['Frequency']


# ## Tests

get_probability(3.1)

get_probability(name='Ivysaur')

get_probability('Ivysaur')

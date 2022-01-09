# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light,md
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

# +
# Code to read in pokedex info
raw_pd = ''
pokedex_file = 'pokedex_basic.csv'
with open(pokedex_file, 'r') as f:
    raw_pd = f.read()
    
# the pokedex string is assigned to the raw_pd variable
# -



# <img src="http://imgur.com/xDpSobf.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
#
# ### 8.2 Parse the raw pokedex with list comprehensions
#
# ---
#
# Perform the same parsing as above, but **using only a single list comprehension** instead of for loops. You may have nested list comprehensions within the main list comprehension! The output should be exactly the same.



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



#
# ## 9. Descriptive statistics on the prototype pokedex
#
# <img src="http://imgur.com/l5NasQj.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
# ### 9.1
#
# What is the population mean and standard deviation of the "Total" attribute for all characters in the Pokedex?
#
#



# <img src="http://imgur.com/l5NasQj.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
# ### 9.2
#
# The game is no fun if the characters are wildly unbalanced! Are any characters "overpowered", which we'll define as having a "Total" more than three standard deviations from the population mean?



# <img src="http://imgur.com/xDpSobf.png" style="float: left; margin: 25px 15px 0px 0px; height: 25px">
#
# ## 10. Calibrate the frequency of Pokemon
#
# The design team wants you to make the powerful Pokemon rare, and the weaklings more common. How would you set the probability $p_i$ of finding Pokemon *i* each time a player visits a gym?
#
# Write a function that takes in a Pokedex number and returns a value $p_i$ for that character.
#
# Hint: there are many ways you could do this. What do _you_ think makes sense? Start with simplifying assumptions: for example, you could assume that the probabilities of encountering any two Pokemon on one visit to a gym are independent of each other.



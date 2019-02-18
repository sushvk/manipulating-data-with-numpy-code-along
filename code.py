# --------------
import numpy as np
# Not every data format will be in csv there are other file formats also.
# This exercise will help you deal with other file formats and how toa read it.
data_ipl =np.genfromtxt(path,delimiter =',',dtype='str',skip_header=True)
#data_ipl[1:5,:]
matches = data_ipl[:,0]
print(len(set(matches)))

# How many matches were held in total we need to know so that we can analyze further statistics keeping that in mind.
team_1 = set(data_ipl[:,3])
team_2 = set(data_ipl[:,4])
print(team_1)
print(team_2)
all_teams =team_1.union(team_2)
print("the set of all the team palyed ",all_teams)

# this exercise deals with you getting to know that which are all those six teams that played in the tournament.
extras_data = data_ipl[:,17]
extras_data_int = extras_data.astype(int)
print(extras_data_int)
is_extra= extras_data_int[extras_data_int>0]
filtered_data = extras_data_int[is_extra]
print("the total extras are ",sum(extras_data_int))
print("the toral number of extras in all matches",len(filtered_data))

# An exercise to make you familiar with indexing and slicing up within data.


# Get the array of all delivery numbers when a given player got out. Also mention the wicket type.
given_batsman = 'ST Jayasuriya'
is_out =data_ipl[:,-3] == given_batsman
output_data  =data_ipl[:,[11,-2]]
print(output_data[is_out])

# this exercise will help you get the statistics on one particular team
toss_winner_data =data_ipl[:,5]
given_team = 'Mumbai Indians'
toss_winner_given_team =toss_winner_data == given_team
print(toss_winner_given_team)
filtered_match_number =data_ipl[toss_winner_given_team,0]
print('the num of matches',given_batsman,'won the toss is',len(set(filtered_match_number)))

# An exercise to know who is the most aggresive player or maybe the scoring player 
runs_data =data_ipl[:,-7].astype(int)
runs_data_mask=runs_data ==6
sixer_batsman =(data_ipl[runs_data_mask,-10])
from collections import Counter
sixer_counter  =Counter(sixer_batsman)
print(sixer_counter)
print(max(sixer_counter,key=sixer_counter.get))







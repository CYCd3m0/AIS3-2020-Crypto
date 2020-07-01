data = '&$ !# $# @% { %$ #! $& %# &% &% @@ $# %# !& $& !& !@ _ $& @% $$ _ @$ !# !! @% _ #! @@ !& _ $# && #@ !% %$ ## !# &% @$ _ $& &$ &% %& && #@ _ !@ %$ %& %! $$ &# !# !! &% @% ## $% !% !& @! #& && %& !% %$ %# %$ @% ## %@ @@ $% ## !& #% %! %@ &@ %! &@ %$ $# ## %# !$ &% @% !% !& $& &% %# %@ #$ !# && !& #! %! ## #$ @! #% !! $! $& @& %% @@ && #& @% @! @# #@ @@ @& !@ %@ !# !# $# $! !@ &$ $@ !! @! &# @$ &! &# $! @@ &@ !% #% #! &@ &$ @@ &$ &! !& #! !# ## %$ !# !# %$ &! !# @# ## @@ $! $$ %# %$ @% @& $! &! !$ $# #$ $& #@ %@ @$ !% %& %! @% #% $! !! #$ &# ## &# && $& !! !% $! @& !% &@ !& $! @# !@ !& @$ $% #& #$ %@ %% %% &! $# !# $& #@ &! !# @! !@ @@ @@ ## !@ $@ !& $# %& %% !# !! $& !$ $% !! @$ @& !& &@ #$ && @% $& $& !% &! && &@ &% @$ &% &$ &@ $$ }'
data = data.replace('!', '0').replace('@', '1').replace('#', '2').replace('$', '3').replace('%', '4').replace('&', '5')
data = data.split()

table = [
    ['V', 'F', 'Y', 'J', '6', '1'],
    ['5', '0', 'M', '2', '9', 'L'],
    ['I', 'W', 'H', 'S', '4', 'Q'],
    ['K', 'G', 'B', 'X', 'T', 'A'],
    ['E', '3', 'C', '7', 'P', 'N'],
    ['U', 'Z', '8', 'R', 'D', 'O']
]

flag = ''
for i in data :
    if i == '_' :
        flag += '_'
    elif i == '{' :
        flag += '{'
    elif i == '}' :
        flag += '}'
    else :
        flag += table[int(i[1])][int(i[0])]
print(flag)

# flag = AIS3{TYR4NN0S4URU5_R3X_GIV3_Y0U_SOMETHING_RANDOM_5TD6XQIVN3H7EUF8ODET4T3H907HUC69L6LTSH4KN3EURN49BIOUY6HBFCVJRZP0O83FWM0Z59IISJ5A2VFQG1QJ0LECYLA0A1UYIHTIIT1IWH0JX4T3ZJ1KSBRM9GED63CJVBQHQORVEJZELUJW5UG78B9PP1SIRM1IF500H52USDPIVRK7VGZULBO3RRE1OLNGNALX}
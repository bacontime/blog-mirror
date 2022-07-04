# How many hexagonal isomorphic keyboard arrangements are there?
# Well, an infinite number.
# But how many up to rotation, translation, reflection and octave shifts?
# 6 directions, each encoded by shift, counted in semitones
#   uniquely determined with any two of these shifts
#   WLOG, assume shifts are (a,b), where b>=a and both numbers are positive
#   modular nature of musical notes means a,b in {0,1,2,3,4,5,6}
# Therefore only 28 distinct isomorphic layouts

# How many of these 28 layouts cover all 12 notes?
# If either a or b in {1,5}, all notes are covered. 
#   This covers 6+2 + 6+2 - 3 = 13 unique possibilities
# If a+b in {1,5,7,11}, all notes are covered. 
#   Not counting the above, this only covers 2 additional possibilities ((2,3) and (3,4))
# Therefore there are 15 distinct isomorphic keyboards that cover all 12 notes.

# This code is to double check my counts.

#%% There are 2
values = [0,1,2,3,4,5,6]
validPairs = set()
for a in values:
    for b in values:
        if b>=a:
            validPairs.add((a,b))


print(len(validPairs), "distinct pairs")

# %%
def enumeratepairs(a,b):
    pairset = set()
    for i in range(12):
        for j in range(12):
            reachableValue = (i*a+j*b) % 12
            pairset.add(reachableValue)
    return pairset

incompletePairs = set()
for a,b in validPairs:
    reachableSet = enumeratepairs(a,b)
    if len(reachableSet) != 12:
        print((a,b),  len(reachableSet))
        incompletePairs.add((a,b))

print(len(incompletePairs), "distinct pairs that don't cover all 12 notes")
print(len(validPairs)-len(incompletePairs), "distinct pairs that DO cover all 12 notes")
# %%

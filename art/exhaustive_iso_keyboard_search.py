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
values = list(range(0,13))
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



#If octave shifts aren't treated as equivalent, but we restrict a,b shift to less than an octave, 
#28 distinct pairs that don't cover all 12 notes
#50 distinct pairs that DO cover all 12 notes

# If we restrict all 6 shifts to no more than an octave. IE range(13) = {0...12}
# ~~21~~ 25 distinct pairs that don't cover all 12 notes
# ~~28~~ 24 distinct pairs that DO cover all 12 notes
# See below. This is the most meaningful count I think.

# If further restrict to avoid cases where adjacent hex is identical, range(1,13)={1...12}
# 12 distinct pairs that don't cover all 12 notes
# 24 distinct pairs that DO cover all 12 notes

validOctaveRangePairs = {
    (0, 1), 
    #(0, 5), (0, 7), (0, 11), 
    (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), 
    (2, 3), (2, 5), (2, 7), (2, 9), 
    (3, 4), (3, 5), (3, 7), (3, 8), 
    (4, 5), (4, 7), 
    #(5, 5), 
    (5, 6), (5, 7)
}


# %%










#%%
# Conduct a more exhaustive search
# This treats notes as equivalent under octave shifts

distinctPairs = set()
distinctRings = set()
allRingVariants = set()
def recordRingVariants(ring):
    '''
    Takes a tuple representing one variant of a isomorphic hex layout.
    Adds its reflections and rotations to the set tracking such variants.
    '''
    assert len(ring) == 6
    for i in range(6):
        allRingVariants.add(ring[i:]+ring[:i])
        allRingVariants.add(tuple(reversed(ring[i:]+ring[:i])))
def generateRing(alpha,beta):
    ring = (alpha%12,
        (alpha+beta)%12,
        beta%12,
        (-alpha)%12,
        (-alpha-beta)%12,
        (-beta)%12,
    )
    return ring



#for alpha in range(12):
#    for beta in range(12):
# Here's something equivalent that visits small pairs sooner:
for total in range(24):
    for beta in range(min(total+1,12)):
        print(total,beta)
        alpha = (total-beta)%12
        ring = generateRing(alpha,beta)
        if ring not in allRingVariants:
            print((alpha,beta))
            recordRingVariants(ring)
            distinctRings.add(ring)
            distinctPairs.add((alpha,beta))

print(len(distinctPairs))

#{(0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (5, 0), (5, 1), (5, 2), (6, 0)}

# %%
# Re-evaluate set of distinct pairs 

def enumeratepairs(a,b):
    pairset = set()
    for i in range(12):
        for j in range(12):
            reachableValue = (i*a+j*b) % 12
            pairset.add(reachableValue)
    return pairset

incompletePairs = set()
for a,b in distinctPairs:
    reachableSet = enumeratepairs(a,b)
    if len(reachableSet) != 12:
        print((a,b),  len(reachableSet))
        incompletePairs.add((a,b))

print(len(incompletePairs), "distinct pairs that don't cover all 12 notes")
print(len(distinctPairs)-len(incompletePairs), "distinct pairs that DO cover all 12 notes")

# 9 distinct pairs that don't cover all 12 notes
# 10 distinct pairs that DO cover all 12 notes
# {(1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (4, 1), (4, 3), (5, 0), (5, 1), (5, 2)}

validModuloPairs = {
    (1, 0), (1, 1), 
    (2, 1), 
    (3, 1), (3, 2), 
    (4, 1), (4, 3), 
    (5, 0), (5, 1), (5, 2)
}

# %%















#%% REDO 2022 11 05
# I am not satisfied with the above results.

# Firstly enumerate all the alpha beta pairs
# Rule 1: Alpha in [0,11]
# Rule 2: Beta in [0, A]
# Rule 3: Alpha plus Beta sums to no more than 12.

preliminarySet = set()

for A in range(12+1):
    for B in range(A+1):
        if A+B <= 12:
            mytuple = (A,B)
            preliminarySet.add(mytuple)
            print(mytuple)

print(len(preliminarySet))


#%% Now restrict to only those which cover the octave.
# This means that they must be coprime under mod 12 or contain 1.
def enumeratepairs(a,b):
    pairset = set()
    for i in range(12):
        for j in range(12):
            reachableValue = (i*a+j*b) % 12
            pairset.add(reachableValue)
    return pairset

incompletePairs = set()
for a,b in preliminarySet:
    reachableSet = enumeratepairs(a,b)
    if len(reachableSet) != 12:
        #print((a,b),  len(reachableSet))
        incompletePairs.add((a,b))
    else:
        print((a,b))

specialCases = {(5,0),(7,0),(11,0),(5,5)}

print(len(incompletePairs), "distinct pairs that don't cover all 12 notes")
print("4 special cases")
fullOctaveSet = preliminarySet-incompletePairs-specialCases
print(len(fullOctaveSet), "distinct pairs that DO cover all 12 notes")

#%% Now, among these 24 pairs, many are equivalent under the modulo 12 symmetrry
# Eg 54 53 and 43 are the same.

ringDict = dict() # Keep track of which rings map to which pairs

def calcRingAroundC(A,B):
    ring = [A,B, A+B, -A-B, -A, -B]
    ringMod12 = [x % 12 for x in ring]
    ringTuple = tuple(sorted(ringMod12))
    print(ringTuple)
    if ringTuple in ringDict:
        ringDict[ringTuple].append((A,B))
    else:
        ringDict[ringTuple] = [(A,B)]

for A,B in fullOctaveSet:
    calcRingAroundC(A,B)

ringDict





# %%

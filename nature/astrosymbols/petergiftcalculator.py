#%%
import math

#rad_eq is equatorial radius in km
#rad_plr is polar radius in km
#rad_mean is mean radius in km
#distance is mean orbital distance from sun in AU
planets = {
        'Sun': {
            'rad_mean': 695_700,
            'rad_eq': 695_700,
            'rad_plr': 695_700,
            'distance': 0,
            'perihelion': 0,
            'aphelion': 0,
        },
        'Mercury': {
            'rad_mean': 2440,
            'rad_eq': 2440,
            'rad_plr': 2440,
            'distance': .387,
            'perihelion': .3075,
            'aphelion': .4667,
        },
        'Venus': {
            'rad_mean': 6052,
            'rad_eq': 6052,
            'rad_plr': 6052,
            'distance': .7233,
            'perihelion': 0.718,
            'aphelion': 0.728,
        },
        'Earth': {
            'rad_mean': 6371,
            'rad_eq': 6378,
            'rad_plr': 6356,
            'distance': 1,
            'aphelion': 1.0167,
            'perihelion': 0.983269,
        },
        'Moon': {
            'rad_mean': 1737,
            'rad_eq': 1738,
            'rad_plr': 1736,
            'distance': 1,
            'aphelion': 1.0167,
            'perihelion': 0.983269,
        },
        'Mars': {
            'rad_mean': 3390,
            'rad_eq': 3396,
            'rad_plr': 3376,
            'distance': 1.524,
            'perihelion':  1.666,
            'aphelion': 1.382,
        },
        'Ceres': {
            'rad_mean': 480,
            'rad_eq': 480,
            'rad_plr': 480,
            'distance': 2.766,
            'perihelion': 2.55,
            'aphelion': 2.98,
        },
        'Jupiter': {
            'rad_mean': 69_911,
            'rad_eq': 71_492,
            'rad_plr': 66_854,
            'distance': 5.2033,
            'perihelion': 4.9501,
            'aphelion': 5.4588,
        },
        'Saturn': {
            'rad_mean': 58_232,
            'rad_eq': 60_268,
            'rad_plr': 54_364,
            'distance': 9.537,
            'perihelion': 9.0412,
            'aphelion': 10.1238,
        },
        'Uranus': {
            'rad_mean': 25_362,
            'rad_eq': 25_559,
            'rad_plr': 24_973,
            'distance': 19.19,
            'perihelion': 18.2861,
            'aphelion': 20.0965,
        },
        'Neptune': {
            'rad_mean': 24_622,
            'rad_eq': 24_764,
            'rad_plr': 	24_341,
            'distance': 30.07,
            'perihelion': 29.81,
            'aphelion': 30.33,
        },
        'Pluto': {
            'rad_mean': 1188,
            'rad_eq': 1188,
            'rad_plr': 	1188,
            'distance': 39.482,
            'perihelion': 29.658 ,
            'aphelion': 49.305,
        },
    }



# %% Determine scales on board in cm. The board is a bit less than 61 cm.

print("RADIUS")
# Choose planet scaling factor so that Mercury is 2 mm in diameter. 1mm in radius.
# RADIUSMULT = 1/planets['Mercury']['rad_eq'] / 10 #NVM. This makes planets too big.
# Choose to make Earth 3mm exactly.
RADIUSMULT = .15/planets['Earth']['rad_eq'] 
#RADIUSMULT = 1.5/planets['Saturn']['rad_eq'] 

for name,data in planets.items():
    data['rad_board'] = data['rad_eq']*RADIUSMULT
    txt = " radius {r:.2f} diameter {d:.2f} cm"
    print(name + txt.format(r = data['rad_board'], d = data['rad_board']*2))

print("\nORBITS")
# Now we need to figure out what the orbit scale needs to be to prevent venus earth overlap.
EVGap = planets['Earth']['distance'] - planets['Venus']['distance']
EVBulge = planets['Earth']['rad_board'] + planets['Venus']['rad_board']
ORBITMULT = 1.4
for name,data in planets.items():
    data['dist_board'] = data['distance']*ORBITMULT
    print(name, data['dist_board'])

#ALSO CONVERT APHELION AND PERIHELION TO BOARD SCALE
MinAU = 149597870700 
for name,data in planets.items():
    data['ap_board'] = data['aphelion']*ORBITMULT
    data['peri_board'] = data['perihelion']*ORBITMULT


#Can use .15, 1.1 or .175,1.3
#.15, 1.4 allows room for saturns rings
# Setting the radius of saturn to 1.5cm with ORBITMULT=1.4 also works well.
# Okay, I've settled on .15, 1.4

print("\nDISTANCE ON BOARD")
#Finally, check to see where the planets range on the board.
SUNDIST = planets['Sun']['rad_board']
for name,data in planets.items():
    data['dist_board_max'] = SUNDIST + data['dist_board'] + data['rad_board']
    data['dist_board_min'] = SUNDIST + data['dist_board'] - data['rad_board']
    txt = " from {close:.2f} to {far:.2f} cm"
    print(name + txt.format(close = data['dist_board_min'], far = data['dist_board_max']))



print("EVGap",planets['Earth']['dist_board_min'] - planets['Venus']['dist_board_max'])


# 

# %% Display the lengths on board
# The sun has a radius of 0.0046 AU, so 
# negligible whether I'm scaling according to surface from sun vs distance from sun.


for name,data in planets.items():
    txt = "close: {close:.2f}, mean {mean:.2f}, far {far:.2f}"
    r = data['rad_board']
    mean = data['dist_board']
    close = mean - r
    far = mean + r
    print(name,txt.format(close=close,mean=mean,far=far))



# %% Check ring overlap
#Saturn rings should have radius of 3.848 for .175,1.125 version
#Saturn rings should have radius of 3.298 for .15,1.1 version
RINGRAD = 2.32716954068*planets['Saturn']['rad_board']
satmin = planets['Saturn']['dist_board'] - RINGRAD
jupmax = planets['Jupiter']['dist_board'] + planets['Jupiter']['rad_board']
print("JUPSATGAP",RINGRAD, satmin - jupmax)
# %%



#%% Saturn Details https://nssdc.gsfc.nasa.gov/planetary/factsheet/satringfact.html
SATRAD = planets['Saturn']['rad_board']
print("C start",1.239*SATRAD)
print("C end",1.526*SATRAD)
print("B start",1.526*SATRAD)
print("B end",1.950*SATRAD)
print("A start",2.030*SATRAD)
print("Encke",2.214*SATRAD)
print("A end",2.270*SATRAD)
print("F",2.320*SATRAD)

# %%

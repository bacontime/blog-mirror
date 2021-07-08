import math

radkm = {'Ceres': 473,
         'Pluto': 1188,
         'Haumea': 816,
         'Makemake': 715,
         'Eris': 1163,
         'Mercury': 2440,
         'Venus': 6051,
         'Earth': 6378,
         'Mars': 3396,
         'Jupiter': 71492,
         'Saturn': 60268,
         'Uranus': 25559,
         'Neptune': 24764,
         'Sun': 695508,
         'Moon': 1737,
         'Sedna': 497,
         'Gonggong': 615,
         'Quaoar': 560.5,
         'Io': 1815,
         'Europa': 1569,
         'Ganymede': 2634,
         'Callisto': 2410,
         'Mimas': 198,
         'Enceladus': 252,
         'Tethys': 533,
         'Dione': 562,
         'Rhea': 764,
         'Titan': 2576,
         'Iapetus': 736,
         'Miranda': 236,
         'Ariel': 579,
         'Umbriel': 585,
         'Titania': 789,
         'Oberon': 761,
         'Triton': 1353,
         'Charon': 603,
         'Dysnomia': 350,}

distanceAU = {'Ceres': 2.766,
         'Pluto': 39.482,
         'Haumea': 43.335,
         'Makemake': 45.792,
         'Eris': 67.668,
         'Mercury': .387,
         'Venus': .7233,
         'Earth': 1,
         'Mars': 1.524,
         'Jupiter': 5.2033,
         'Saturn': 9.537,
         'Uranus': 19.19,
         'Neptune': 30.07,
         'Sun': 0,
         'Moon': 1737,
         'Sedna': 497,
         'Gonggong': 615,
         'Quaoar': 615,}

#The calculated ellipsoid shape of Haumea, 1,960×1,518×996 km
#Some argue salacia is too smol.

symbol = {'Ceres': '⚳',
         'Pluto': '♇',
         'Haumea': '',
         'Makemake': '',
         'Eris': '⯰',
         'Mercury': '☿',
         'Venus': '♀',
         'Earth': '⊕',
         'Mars': '♂',
         'Jupiter': '♃',
         'Saturn': '♄',
         'Uranus': '⛢',
         'Neptune': '♆',
         'Sun': '☉',
         'Moon': '☾',}

namesake = {'Ceres': '',
         'Pluto': '',
         'Haumea': '',
         'Makemake': '',
         'Eris': '',
         'Mercury': '',
         'Venus': '',
         'Earth': '',
         'Mars': '',
         'Jupiter': '',
         'Saturn': '',
         'Uranus': '',
         'Neptune': '',
         'Sun': '',
         'Moon': '',}

placeholder = {'Ceres': '',
         'Pluto': '',
         'Haumea': '',
         'Makemake': '',
         'Eris': '',
         'Mercury': '',
         'Venus': '',
         'Earth': '',
         'Mars': '',
         'Jupiter': '',
         'Saturn': '',
         'Uranus': '',
         'Neptune': '',
         'Sun': '',
         'Moon': '',}







for planet in radkm:
    #print(planet,math.log(radkm[planet]/100))
    print(planet,radkm[planet]**(1/2))


for planet in radkm:
    #print(planet,math.log(radkm[planet]/100))
    print(planet,radkm[planet]/250)

for planet in distanceAU:
    #print(planet,math.log(radkm[planet]/100))
    print("Dist",planet,distanceAU[planet]*100)

#%% Scale the features of saturn's rings
#data from https://nssdc.gsfc.nasa.gov/planetary/factsheet/satringfact.html
# and from https://en.wikipedia.org/wiki/Rings_of_Saturn
# format is (distance from saturn center to inside of feature, '' to outside of feature)

SATRAD_KM = 60_268
SATRAD_SCALED = 2

dist_km = {
    'A': (122_340, 136_780),
    'B': (91_975, 117_507),
    'C': (74_658, 91_975),
    'D': (66_900, 74_510),
    'Maxwell': (87_491, 87_761),
    'Encke': (133_410, 133_735),
    }

dist_scaled = dict()
for structure, (inner, outer) in dist_km.items():
    scaled_inner = round(SATRAD_SCALED*inner/SATRAD_KM,3)
    scaled_outer = round(SATRAD_SCALED*outer/SATRAD_KM,3)
    dist_scaled[structure] = (scaled_inner,scaled_outer)


dist_scaled == {
    'A': (4.06, 4.539),
    'B': (3.052, 3.899),
    'C': (2.478, 3.052),
    'D': (2.22, 2.473),
    'Maxwell': (2.903, 2.912),
    'Encke': (4.427, 4.438)
    }




# %%

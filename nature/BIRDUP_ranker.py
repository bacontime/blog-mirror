# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 02:11:36 2021

@author: RobertWinslow

Given that I have the (species,state) observation counts in a pickle file,
I should be able to directly load those up and calculate various metrics.

Later on, can take these GEOjson files and combine with 
https://eric.clst.org/tech/usgeojson/
To make a nice map?

TODO: Filter to restrict to native range. 
https://www.researchgate.net/post/Is_there_any_database_of_bird_species_that_has_description_of_their_native_range_and_introduced_range_S_Asia

TODO: Markdown for unique version and non-unique version

TODO: Lots of invasive birds to add to VERBOTEN list. Showing up as top bird in Hawaii.
"""

import pandas as pd
import os
from collections import Counter
import pickle
import numpy as np
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

#%% Flags for fiddling with settings

CUTOFF=1000 # Ignore fluke entries with total bird count below this number.
STATECUTOFF=100 #Don't allow a top bird with fewer than this many joint observations.

FLAG_ONLY_USE_USA_OBSERVATIONS = False #                             0
FLAG_RESTRICT_TO_BBS_BIRDS = False #                                 0
FLAG_EXCLUDE_VERBOTEN_BIRDS = False #                                0
FLAG_RESTRICT_TO_EBIRD_COMMONNAME_KEYBIRDS = False #                 0

FLAG_EXCLUDE_VERBOTEN_BIRDS_FROM_TOP = True #                        1 
FLAG_EXCLUDE_REALSTATEBIRDS_FROM_TOP = False #                       0
FLAG_EXCLUDE_AMBIGU_SPECIES_FROM_TOP = True #                        1 

FLAG_EXCLUDE_FAMILY_LABELLED_AS_GENUS = True #                       1
FLAG_EXCLUDE_AMBIGUOUS_GENUS = True # Lorem/Ipsum                    1
FLAG_EXCLUDE_AMBIGUOUS_SPECIES = True # Lorem ipsum/dolor            1
FLAG_EXCLUDE_UNKNOWN_SPECIES = False # Lorem sp.                     0
FLAG_EXCLUDE_HYBRID_SPECIES = True # Lorem ipsum x dolor             1
FLAG_EXCLUDE_DOMESTIC_TYPE = True #Lorem ipsum (Domestic type)       1

FLAG_ENFORCE_UNIQUENESS_ACROSS_ALL_NA = False #If true, canada state birds can't be USA state birds 0


ALPHA_PARAM = 0.65 # For paramaterized phi coefficient 0.65

#%% import data
picklepath = os.path.join(THIS_FOLDER,'listofbirdcounters.pickle')
with open(picklepath, 'rb') as handle:
    (GRANDTOTAL,state_count,genus_count,species_count,genus_state_count,species_state_count) = pickle.load(handle)

#%% List of States

statemap = {'US-AK': 'Alaska', 'US-AL': 'Alabama', 'US-AR': 'Arkansas', 'US-AZ': 'Arizona', 'US-CA': 'California', 'US-CO': 'Colorado', 'US-CT': 'Connecticut', 'US-DC': 'District of Columbia', 'US-DE': 'Delaware', 'US-FL': 'Florida', 'US-GA': 'Georgia', 'US-HI': 'Hawaii', 'US-IA': 'Iowa', 'US-ID': 'Idaho', 'US-IL': 'Illinois', 'US-IN': 'Indiana', 'US-KS': 'Kansas', 'US-KY': 'Kentucky', 'US-LA': 'Louisiana', 'US-MA': 'Massachusetts', 'US-MD': 'Maryland', 'US-ME': 'Maine', 'US-MI': 'Michigan', 'US-MN': 'Minnesota', 'US-MO': 'Missouri', 'US-MS': 'Mississippi', 'US-MT': 'Montana', 'US-NC': 'North Carolina', 'US-ND': 'North Dakota', 'US-NE': 'Nebraska', 'US-NH': 'New Hampshire', 'US-NJ': 'New Jersey', 'US-NM': 'New Mexico', 'US-NV': 'Nevada', 'US-NY': 'New York', 'US-OH': 'Ohio', 'US-OK': 'Oklahoma', 'US-OR': 'Oregon', 'US-PA': 'Pennsylvania', 'US-RI': 'Rhode Island', 'US-SC': 'South Carolina', 'US-SD': 'South Dakota', 'US-TN': 'Tennessee', 'US-TX': 'Texas', 'US-UT': 'Utah', 'US-VA': 'Virginia', 'US-VT': 'Vermont', 'US-WA': 'Washington', 'US-WI': 'Wisconsin', 'US-WV': 'West Virginia', 'US-WY': 'Wyoming'}


#%% Forbidden bird list to exclude the non-native birds?
# Right now it includes slashy things, non-genus terms
VERBOTEN_SPECIES = [
     'Egretta garzetta',
     'Phasianus colchicus',
     'Bubulcus ibis',
     'Acridotheres tristis',
     'Sturnus vulgaris',
     'Alectoris chukar',
     'Cuculus canorus',
     'Tetraogallus himalayensis',
     'Streptopelia decaocto',
     'Zosterops japonicus',
     'Geopelia striata',
     'Paroaria coronata',
     'Passer domesticus',
     'Sturnus vulgaris',
     'Eos bornea',
     'Terek sandpiper',
     'Tadorna tadorna',
     'Perdix perdix',
     'Parus major',
     'Euplectes franciscanus',
     'Myiopsitta monachus',
     'Aratinga nenday',
     'Carduelis carduelis',
     'Agapornis personatus', #lovebird
     'Agapornis roseicollis', #lovebird
     'Muscicapa griseisticta',
     'Calliope calliope',
     'Sibirionetta formosa',
     'Creagrus furcatus',
     'Tarsiger cyanurus',
     'Xenus cinereus',
     'Fringilla montifringilla',
     'Sibirionetta formosa',
     'Passer montanus',
     'Nomonyx dominicus',
     'Amazona amazonica',
     'Grus grus',
     'Melanospiza bicolor',
     'Myiarchus sagrae',
     'Porphyrio poliocephalus',
     'Gracula religiosa',
     'Ara ararauna',
     'Thectocercus acuticaudatus',
     'Brotogeris versicolurus',
     'Columba livia',
     'Cygnus olor',
     '',
     '',
     ]

# Some birds were list only by their family. These are the one's I've noticed:
FAMILY_LABELLED_AS_GENUS = ['Laridae', 'Turdidae', 'Sterninae', 'Sulidae',
                            'Larinae', 'Trochilidae', 'Threskiornithidae', 'Aves',
                            'Cuculidae', 'Tyrannidae', 'Corvidae', 'Fringillidae',
                            'Icteridae', 'Charadriidae', 'Ardeidae', 'Podicipedidae',
                            'Strigiformes', '', '', '',
                            '', '', '', '',
                            '', '', '', '',
                            '', '', '', '',]
        
#'Calonectris diomedea',
VERBOTEN_GENUS = ['',
     '',
     '',
     '',
     '',
     'Brotogeris',
     'Thectocercus',
     'Ara',
     'Gracula',
     'Amazona',
     'Nomonyx',
     'Sibirionetta',
     'Fringilla',
     'Xenus',
     'Phasianus',
     'Bubulcus',
     'Acridotheres',
     'Sturnus',
     'Alectoris',
     'Cuculus',
     'Tetraogallus',
     'Streptopelia',
     'Zosterops',
     'Geopelia',
     'Paroaria',
     'Passer',
     'Sturnus',
     'Eos',
     'Terek',
     'Tadorna',
     'Perdix',
     'Parus',
     'Euplectes',
     'Myiopsitta',
     'Aratinga',
     'Carduelis',
     'Agapornis',
     'Muscicapa',
     'Calliope',
     'Creagrus',
     'Tarsiger',
     '',
     '',
     ]


VERBOTEN_BIRDS = VERBOTEN_SPECIES+VERBOTEN_GENUS

#%% BBS Bird Lists
BBS_GENUS_LIST = ['Butorides', 'Nycticorax', 'Nyctanassa', 'Charadrius', 'Colinus', 'Columba', 'Zenaida', 'Coccyzus', 'Dryobates', 'Dryocopus', 'Melanerpes', 'Colaptes', 'Antrostomus', 'Chaetura', 'Tyrannus', 'Contopus', 'Empidonax', 'Cyanocitta', 'Corvus', 'Sturnus', 'Molothrus', 'Agelaius', 'Sturnella', 'Icterus', 'Quiscalus', 'Spinus', 'Spizella', 'Pipilo', 'Cardinalis', 'Passerina', 'Spiza', 'Piranga', 'Progne', 'Hirundo', 'Lanius', 'Vireo', 'Setophaga', 'Seiurus', 'Geothlypis', 'Icteria', 'Passer', 'Mimus', 'Dumetella', 'Toxostoma', 'Thryothorus', 'Baeolophus', 'Poecile', 'Polioptila', 'Hylocichla', 'Turdus', 'Sialia', 'Anas', 'Aix', 'Coragyps', 'Chordeiles', 'Myiarchus', 'Ammodramus', 'Petrochelidon', 'Stelgidopteryx', 'Mniotilta', 'Protonotaria', 'Sitta', 'Sayornis', 'Bubulcus', 'Archilochus', 'Eremophila', 'Cathartes', 'Buteo', 'Vermivora', 'Thryomanes', 'Megaceryle', 'Strix', 'Bubo', 'Falco', 'Egretta', 'Accipiter', 'Melospiza', 'Bombycilla', 'Helmitheros', 'Parkesia', 'Branta', 'Ardea', 'Haemorhous', 'Phalacrocorax', 'Scolopax', 'Troglodytes', 'Streptopelia', 'Chondestes', 'Meleagris', 'Limnothlypis', 'Tachycineta', 'Peucaea', 'Megascops', 'Podilymbus', 'Fulica', 'Riparia', 'Ixobrychus', 'Pandion', 'Larus', 'Lophodytes', 'Haliaeetus', 'Ictinia', 'Woodpecker', 'Actitis', 'Gallinula', 'Rallus', 'Columbina', 'Eudocimus', 'Elanoides', 'Ardeid', 'Anhinga', 'Dendrocygna', 'Mycteria', 'Circus', 'Tyto', 'Hydroprogne', 'Sternula', 'Rynchops', 'Pelecanus', 'Porphyrio', 'Tringa', 'Ammospiza', 'Cistothorus', 'Leucophaeus', 'Thalasseus', 'Sterna', 'Spatula', 'Haematopus', 'Catharus', 'Gelochelidon', 'Fregata', 'Laterallus', 'Himantopus', 'Aythya', 'Loxia', 'Gull', 'Coragyps / Cathartes', 'Plegadis', 'Perisoreus', 'Acanthis', 'Zonotrichia', 'Junco', 'Leiothlypis', 'Regulus', 'Ixoreus', 'Gallinago', 'Passerculus', 'Cardellina', 'Myadestes', 'Pinicola', 'Passerella', 'Lagopus', 'Aquila', 'Picoides', 'Carduelis', 'Spizelloides', 'Anser', 'Antigone', 'Falcipennis', 'Bucephala', 'Euphagus', 'Gavia', 'Certhia', 'Mareca', 'Bonasa', 'Cygnus', 'Podiceps', 'Surnia', 'Aegolius', 'Mergus', 'Pica', 'Porzana', 'Anthus', 'Chroicocephalus', 'Phalaropus', 'Sphyrapicus', 'Pluvialis', 'Melanitta', 'Calidris', 'Calcarius', 'Phylloscopus', 'Clangula', 'Bartramia', 'Asio', 'Stercorarius', 'Numenius', 'Histrionicus', 'Cinclus', 'Oenanthe', 'Rissa', 'Uria', 'Somateria', 'Brachyramphus', 'Cepphus', 'Dendragapus', 'Selasphorus', 'Glaucidium', 'Trochilid', 'Patagioenas', 'Limnodromus', 'Onychoprion', 'Tympanuchus', 'Fratercula', 'Synthliboramphus', 'Leucosticte', 'Plectrophenax', 'Tern', 'Alauda', 'Phasianus', 'Limosa', 'Motacilla', 'Arenaria', 'Fulmarus', 'Xema', 'Cyanecula', 'Cypseloides', 'Pheucticus', 'Botaurus', 'Carpodacus', 'Pooecetes', 'Calamospiza', 'Chlidonias', 'Centrocercus', 'Recurvirostra', 'Xanthocephalus', 'Centronyx', 'Perdix', 'Oxyura', 'Rhynchophanes', 'Dolichonyx', 'Salpinctes', 'Athene', 'Aechmophorus', 'Nucifraga', 'Coccothraustes', 'Coturnicops', 'Oporornis', 'Gymnorhinus', 'Amphispiza', 'Oreoscoptes', 'Psaltriparus', 'Aphelocoma', 'Callipepla', 'Melozone', 'Artemisiospiza', 'Aeronautes', 'Phalaenoptilus', 'Aimophila', 'Catherpes', 'Gymnogyps', 'Campylorhynchus', 'Auriparus', 'Geococcyx', 'Phainopepla', 'Calypte', 'Pyrocephalus', 'Parabuteo', 'Micrathene', 'Myioborus', 'Peucedramus', 'Psiloscops', 'Elanus', 'Myiodynastes', 'Camptostoma', 'Cynanthus', 'Cyrtonyx', 'Trogon', 'Lampornis', 'Buteogallus', 'Eugenes', 'Amazilia', 'Thryophilus', 'Pachyramphus', 'Alectoris', 'Caracara', 'Calothorax', 'Cerorhinca', 'Oreortyx', 'Chamaea', 'Pavo', 'Brotogeris', 'Aratinga', 'Amazona', 'Sula', 'Lonchura', 'Vidua', 'Aramus', 'Myiopsitta', 'Platalea', 'Cairina', 'Grus', 'Rostrhamus', 'Crotophaga', 'Acridotheres', 'Psittacula', 'Calonectris', 'Nycticorax / Nyctanassa', 'Melopsittacus', 'Alopochen', 'Pitangus', 'Rhodostethia', 'Morus', 'Alca', 'Puffinus', 'Hydrobates', 'Arremonops', 'Nyctidromus', 'Ortalis', 'Cyanocorax', 'Leptotila', 'Geranoaetus', 'Tachybaptus', 'Chloroceryle', 'Chondrohierax', 'Ptychoramphus']


BBS_SPECIES_LIST = ['Vermivora cyanoptera', 'Glaucidium gnoma', 'Glaucidium brasilianum', 'Geothlypis trichas', 'Aramides axillaris', 'Caracara lutosa', 'Arenaria interpres', 'Porzana carolina', 'Anhinga anhinga', 'Pitangus sulphuratus', 'Platalea ajaja', 'Mycteria americana', 'Caracara plancus', 'Haematopus palliatus', 'Arenaria melanocephala', 'Larus heermanni', 'Sula nebouxii', 'Sula leucogaster', 'Setophaga castanea', 'Coereba flaveola', 'Protonotaria citrea', 'Cassiculus melanicterus', 'Rallus elegans', 'Passer domesticus', 'Setophaga dominica', 'Laterallus ruber', 'Coturnicops noveboracensis', 'Laterallus jamaicensis', 'Rallus obsoletus', 'Tyto alba', 'Setophaga pitiayumi', 'Dendrocygna autumnalis', 'Jacana spinosa', 'Setophaga palmarum', 'Falco sparverius', 'Polioptila nigriceps', 'Icterus wagleri', 'Rynchops niger', 'Myiarchus tyrannulus', 'Cynanthus latirostris', 'Campylorhynchus brunneicapillus', 'Columbina passerina', 'Toxostoma curvirostre', 'Callipepla gambelii', 'Colaptes chrysoides', 'Geococcyx californianus', 'Butorides virescens', 'Quiscalus mexicanus', 'Empidonax wrightii', 'Icterus cucullatus', 'Columbina inca', 'Dryobates scalaris', 'Tachybaptus dominicus', 'Sternula antillarum', 'Tachycineta albilinea', 'Cardinalis cardinalis', 'Parkesia noveboracensis', 'Phainopepla nitens', 'Vireo plumbeus', 'Cardinalis sinuatus', 'Peucaea carpalis', 'Passerculus sandwichensis', 'Pyrocephalus rubinus', 'Vireo gilvus', 'Tyrannus verticalis', 'Amazona albifrons', 'Charadrius wilsonia', 'Setophaga petechia', 'Megascops kennicottii', 'Melanerpes formicivorus', 'Turdus migratorius', 'Dryobates arizonae', 'Patagioenas fasciata', 'Pheucticus melanocephalus', 'Passerina caerulea', 'Myadestes occidentalis', 'Baeolophus wollweberi', 'Certhia americana', 'Psaltriparus minimus', 'Tyrannus vociferans', 'Spizella passerina', 'Corvus corax', 'Accipiter cooperii', 'Oreothlypis superciliosa', 'Myiarchus tuberculifer', 'Sialia sialis', 'Setophaga graciae', 'Contopus pertinax', 'Piranga flava', 'Poecile sclateri', 'Aphelocoma wollweberi', 'Cyrtonyx montezumae', 'Trogon mexicanus', 'Colaptes auratus', 'Stelgidopteryx serripennis', 'Myioborus pictus', 'Aimophila ruficeps', 'Basileuterus rufifrons', 'Catharus occidentalis', 'Aimophila rufescens', 'Myioborus miniatus', 'Antrostomus arizonae', 'Cyanocitta stelleri', 'Myiodynastes luteiventris', 'Catharus ustulatus', 'Mitrephanes phaeocercus', 'Sitta carolinensis', 'Basilinna leucotis', 'Lepidocolaptes leucogaster', 'Meleagris gallopavo', 'Junco phaeonotus', 'Icterus parisorum', 'Molothrus aeneus', 'Catharus aurantiirostris', 'Turdus assimilis', 'Callipepla douglasii', 'Haemorhous mexicanus', 'Spinus psaltria', 'Patagioenas flavirostris', 'Melospiza melodia', 'Icterus pustulatus', 'Tyrannus melancholicus', 'Auriparus flaviceps', 'Empidonax traillii', 'Icteria virens', 'Myiarchus cinerascens', 'Vireo bellii', 'Volatinia jacarina', 'Chlidonias niger', 'Coragyps atratus', 'Molothrus ater', 'Tigrisoma mexicanum', 'Icterus bullockii', 'Petrochelidon pyrrhonota', 'Nyctidromus albicollis', 'Anatinae sp.', 'Melanerpes uropygialis', 'Pipilo chlorurus', 'Saltator grandis', 'Crotophaga sulcirostris', 'Ardea herodias', 'Ardea alba', 'Tringa melanoleuca', 'Bubo virginianus', 'Buteo plagiatus', 'Pheugopedius felix', 'Parabuteo unicinctus', 'Chondestes grammacus', 'Calidris minutilla', 'Chordeiles acutipennis', 'Numenius americanus', 'Lanius ludovicianus', 'Camptostoma imberbe', 'Mimus polyglottos', 'Icterus spurius', 'Pandion haliaetus', 'Passerina ciris', 'Empidonax difficilis', 'Podilymbus podiceps', 'Melozone kieneri', 'Buteo jamaicensis', 'Agelaius phoeniceus', 'Pachyramphus aglaiae', 'Ortalis wagleri', 'Columbina talpacoti', 'Corvus sinaloae', 'Thryophilus sinaloa', 'Myiozetetes similis', 'Passerellidae sp. (sparrow sp.)', 'Actitis macularius', 'Tachycineta bicolor', 'Cathartes aura', 'Leucolia violiceps', 'Tachycineta thalassina', 'Leptotila verreauxi', 'Zenaida asiatica', 'Fulica americana', 'Recurvirostra americana', 'Setophaga ruticilla', 'Himantopus mexicanus', 'Hydroprogne caspia', 'Passerina amoena', 'Geothlypis tolmiei', 'Anas acuta', 'Tringa solitaria', 'Parulidae sp.', 'Phalaropus tricolor', 'Cardellina pusilla', 'Setophaga coronata', 'Nycticorax nycticorax', 'Megaceryle alcyon', 'Coccyzus erythropthalmus', 'Sayornis nigricans', 'Setophaga nigrescens', 'Calypte costae', 'Chloroceryle americana', 'Accipitridae sp. (hawk sp.)', 'Troglodytes aedon', 'Charadrius vociferus', 'Falco columbarius', 'Zenaida macroura', 'Circus hudsonius', 'Leiothlypis celata', 'Eupsittula canicularis', 'Heliomaster constantii', 'Turdus rufopalliatus', 'Accipiter striatus', 'Piranga rubra', 'Tyrannus crassirostris', 'Passerina versicolor', 'Contopus sordidulus', 'Euphagus cyanocephalus', 'Phalacrocoracidae sp.', 'Fregata magnificens', 'Egretta rufescens', 'Charadriiformes sp.', 'Egretta thula', 'Sterninae sp.', 'Eudocimus albus', 'Numenius phaeopus', 'Tringa semipalmata', 'Botaurus lentiginosus', 'Pelecanus erythrorhynchos', 'Mniotilta varia', 'Melanotis caerulescens', 'Polioptila caerulea', 'Athene cunicularia', 'Amazilia rutila', 'Trogon elegans', 'Melospiza lincolnii', 'Calothorax lucifer', 'Leiothlypis luciae', 'Limosa fedoa', 'Nannopterum brasilianum', 'Falco peregrinus', 'Contopus sp.', 'Cyanocorax beecheii', 'Egretta tricolor', 'Calidris mauri', 'Zonotrichia leucophrys', 'Nyctanassa violacea', 'Xanthocephalus xanthocephalus', 'Toxostoma bendirei', 'Calocitta colliei', 'Dryocopus lineatus', 'Progne subis', 'Corvus sp. (raven sp.)', 'Spizella pallida', 'Psittaciformes sp. (parakeet sp.)', 'Pooecetes gramineus', 'Sturnella neglecta', 'Piranga ludoviciana', 'Vireo cassinii/solitarius', 'Hirundo rustica', 'Peucaea botterii', 'Pelecanus occidentalis', 'Spatula discors', 'Branta canadensis', 'Anas crecca', 'Larinae sp.', 'Ixobrychus exilis', 'Limnodromus scolopaceus', 'Spatula clypeata', 'Strigiformes sp.', 'Piaya cayana', 'Vireo sp.', 'Plegadis chihi', 'Larus californicus', 'Selasphorus rufus', 'Hirundinidae sp.', 'Vireo atricapilla', 'Icterus abeillei', 'Spatula cyanoptera', 'Buteogallus anthracinus', 'Basileuterus lachrymosus', 'Melanerpes chrysogenys', 'Ammodramus savannarum', 'Sialia currucoides', 'Empidonax affinis', 'Vireo cassinii/solitarius/plumbeus', 'Sporophila torqueola', 'Pheucticus chrysopeplus', 'Anthus rubescens', 'Trogon citreolus', 'Seiurus aurocapilla', 'Mergus serrator', 'Thalasseus maximus', 'Calidris alba', 'Megascops sp.', 'Euphonia godmani', 'Empidonax fulvifrons', 'Corvus cryptoleucus', 'Mareca strepera', 'Chondrohierax uncinatus', 'Passerina cyanea', 'Aythya affinis', 'Campephilus guatemalensis', 'Odontophoridae sp.', 'Charadrius collaris', 'Tringa flavipes', 'Anatidae sp. (teal sp.)', 'Pluvialis squatarola', 'Aythya valisineria', 'Nannopterum auritum', 'Thalasseus elegans', 'Empidonax sp.', 'Sterna forsteri', 'Leucophaeus atricilla', 'Oxyura jamaicensis', 'Aythya americana', 'Leiothlypis ruficapilla', 'Gelochelidon nilotica', 'Larus delawarensis', 'Charadrius semipalmatus', 'Elanus leucurus', 'Larus livens', 'Calidris canutus', 'Trogon sp.', 'Vireo flavoviridis', 'Icterus sp.', 'Granatellus venustus', 'Corvus sp.', 'Cyanocompsa parellina', 'Xiphorhynchus flavigaster', 'Tityra semifasciata', 'Saucerottia beryllina', 'Megarynchus pitangua', 'Micrastur semitorquatus', 'Penelope purpurascens', 'Herpetotheres cachinnans', 'Chordeiles minor', 'Porphyrio martinica', 'Archilochus colubris', 'Apodidae sp.', 'Coccyzus americanus', 'Lampornis clemenciae', 'Catherpes mexicanus', 'Setophaga occidentalis', 'Cardellina rubrifrons', 'Corthylio calendula', 'Cyanocorax dickeyi', 'Picidae sp.', 'Momotus mexicanus', 'Spinus notatus', 'Selasphorus calliope', 'Polioptila sp.', 'Arremon virenticeps', 'Catharus guttatus', 'Eugenes fulgens', 'Sitta sp.', 'Peucedramus taeniatus', 'Atlapetes pileatus', 'Loxia curvirostra', 'Cardellina rubra', 'Sphyrapicus nuchalis', 'Pipilo maculatus', 'Oriturus superciliosus', 'Setophaga townsendi', 'Sphyrapicus varius', 'Geococcyx velox', 'Micrathene whitneyi', 'Pachyramphus major', 'Crypturellus cinnamomeus', 'Cairina moschata', 'Sphyrapicus sp.', 'Sayornis saya', 'Megaceryle torquata', 'Rhodinocichla rosea', 'Streptoprocne semicollaris', 'Cochlearius cochlearius', 'Vireo huttoni', 'Accipiter gentilis', 'Gallinago delicata', 'Antigone canadensis', 'Ridgwayia pinicola', 'Euptilotis neoxenus', 'Sturnella neglecta/magna', 'Sitta pygmaea', 'Salpinctes obsoletus', 'Asio stygius', 'Amphispizopsis quinquestriata', 'Geranoaetus albicaudatus', 'Mareca americana', 'Spinus sp. (goldfinch sp.)', 'Ciccaba virgata', 'Aeronautes saxatalis', 'Selasphorus heloisa', 'Colaptes auricularis', 'Ptiliogonys cinereus', 'Piranga erythrocephala', 'Basileuterus culicivorus', 'Thryomanes bewickii', 'Psilorhinus morio', 'Thryothorus ludovicianus', 'Progne chalybea', 'Setophaga virens', 'Selasphorus platycercus', 'Spinus pinus', 'Campylorhynchus gularis', 'Attila spadiceus', 'Sturnella magna', 'Streptoprocne zonaris', 'Amazona autumnalis', 'Antrostomus ridgwayi', 'Cynanthus auriceps', 'Morococcyx erythropygus', 'Accipitridae sp. (eagle sp.)', 'Piranga bidentata', 'Coccothraustes abeillei', 'Cypseloides niger', 'Chaetura vauxi', 'Archilochus alexandri', 'Vireo cassinii', 'Empidonax oberholseri', 'Chlorophonia elegantissima', 'Progne sinaloae', 'Empidonax difficilis/occidentalis', 'Trochilidae sp.', 'Calocitta formosa', 'Contopus sordidulus/virens', 'Empidonax flaviventris', 'Vireo solitarius', 'Arremonops rufivirgatus', 'Toxostoma longirostre', 'Anthus spragueii', 'Vireo griseus', 'Chloroceryle amazona', 'Icterus galbula', 'Buteo platypterus', 'Sporophila morelleti', 'Icterus graduacauda', 'Ortalis vetula', 'Cyanocorax yncas', 'Corvus imparatus', 'Tyrannus couchii', 'Gallinula galeata', 'Ardeidae sp.', 'Passerina leclancherii', 'Cyanocorax sanblasianus', 'Peucaea ruficauda', 'Dendrocygna bicolor', 'Falco mexicanus', 'Bombycilla cedrorum', 'Leiothlypis virginiae', 'Tyrannus sp. (yellow-bellied)', 'Melozone fusca', 'Basileuterus belli', 'Empidonax hammondii', 'Empidonax minimus', 'Turdus sp.', 'Calamospiza melanocorys', 'Regulus satrapa', 'Passeriformes sp.', 'Turdus grayi', 'Melanerpes aurifrons', 'Vireo olivaceus', 'Peucaea cassinii', 'Egretta caerulea', 'Colinus virginianus', 'Parkesia motacilla', 'Dryobates villosus', 'Campephilus imperialis', 'Myadestes townsendi', 'Sialia mexicana', 'Cinclus mexicanus', 'Coccothraustes vespertinus', 'Vireo cassinii/plumbeus', 'Podiceps nigricollis', 'Empidonax albigularis', 'Calidris bairdii', 'Eremophila alpestris', 'Cathartidae sp.', 'Aphelocoma woodhouseii', 'Sialia sp.', 'Myiarchus nuttingi', 'Troglodytidae sp.', 'Vireo hypochryseus', 'Spizella breweri', 'Myiopagis viridicata', 'Zenaida graysoni', 'Junco hyemalis', 'Buteo albonotatus', 'Junco insularis', 'Vireo pallens', 'Columbidae sp.', 'Geothlypis poliocephala', 'Myiarchus sp.', 'Sporophila sp.', 'Coccyzus minor', 'Geotrygon montana', 'Dryobates fumigatus', 'Spizella atrogularis', 'Selasphorus sp.', 'Parkesia motacilla/noveboracensis', 'Melozone/Pipilo sp.', 'Contopus cooperi', 'Vireolanius pulchellus', 'Asio otus', 'Aegolius acadicus', 'Oreoscoptes montanus', 'Aechmophorus clarkii', 'Cistothorus palustris', 'Pheucticus ludovicianus', 'Aechmophorus occidentalis', 'Empidonax occidentalis', 'Dendrocolaptinae sp.', 'Pluvialis dominica', 'Saucerottia cyanocephala', 'Campylorhynchus zonatus', 'Thamnophilus doliatus', 'Momotus coeruliceps', 'Arremon brunneinucha', 'Diglossa baritula', 'Chlorospingus flavopectus', 'Trogon collaris', 'Vireolanius melitophrys', 'Sayornis phoebe', 'Henicorhina leucophrys', 'Dumetella carolinensis', 'Geothlypis nelsoni', 'Setophaga magnolia', 'Doricha eliza', 'Sittasomus griseicapillus', 'Habia rubica', 'Catharus frantzii', 'Cyclarhis gujanensis', 'Clibanornis rubiginosus', 'Pheugopedius maculipectus', 'Lepidocolaptes affinis', 'Aphelocoma unicolor', 'Atlapetes albinucha', 'Elaenia flavogaster', 'Tiaris olivaceus', 'Euphonia hirundinacea', 'Thraupis abbas', 'Megascops trichopsis', 'Setophaga fusca', 'Phalaenoptilus nuttallii', 'Anas platyrhynchos/diazi', 'Pipilo ocai', 'Aphelocoma ultramarina', 'Dryobates stricklandi', 'Philortyx fasciatus', 'Thryophilus pleurostictus', 'Peucaea humeralis', 'Phaeoptila sordida', 'Ortalis poliocephala', 'Polioptila albiloris', 'Cistothorus platensis', 'Colibri thalassinus', 'Dactylortyx thoracicus', 'Tilmatura dupontii', 'Vireo nelsoni', 'Polioptila melanura', 'Amphispiza bilineata', 'Anas diazi', 'Spiza americana', 'Cairina moschata (Domestic type)', 'Campylorhynchus rufinucha', 'Anser caerulescens', 'Rallus limicola', 'Megascops seductus', 'Puffinus auricularis', 'Setophaga americana', 'Ramphotrigon flammulatum', 'Selasphorus sasin', 'Anser albifrons', 'Callipepla squamata', 'Asio flammeus', 'Toxostoma crissale', 'Falco rufigularis', 'Setophaga pensylvanica', 'Sterna hirundo', 'Glaucidium palmarum', 'Larus argentatus', 'Sarcoramphus papa', 'Psittaciformes sp. (parrot sp.)', 'Pelecanus sp.', 'Lampornis amethystinus', 'Psiloscops flammeolus', 'Campylorhynchus megalopterus', 'Dendrortyx macroura', 'Leiothlypis crissalis', 'Rallidae sp. (rail/crake sp.)', 'Anser/Branta sp.', 'Buteo regalis', 'Rallus tenuirostris', 'Dives dives', 'Euphonia affinis', 'Icterus gularis', 'Accipiter bicolor', 'Baeolophus atricristatus', 'Saltator atriceps', 'Amazilia yucatanensis', 'Rhodothraupis celaeno', 'Setophaga chrysoparia', 'Colaptes rubiginosus', 'Psittacara holochlorus', 'Nyctibius jamaicensis', 'Rupornis magnirostris', 'Piranga leucoptera', 'Uropsila leucogastra', 'Toxostoma ocellatum', 'Claravis pretiosa', 'Automolus ochrolaemus', 'Cyanoloxia cyanoides', 'Saltator maximus', 'Cardellina canadensis', 'Celeus castaneus', 'Psarocolius wagleri', 'Pteroglossus torquatus', 'Ramphocelus sanguinolentus', 'Microrhopias quixensis', 'Cercomacroides tyrannina', 'Anthracothorax prevostii', 'Ramphastos sulfuratus', 'Phaethornis longirostris', 'Heliomaster longirostris', 'Dendrocolaptes sanctithomae', 'Oncostoma cinereigulare', 'Mionectes oleagineus', 'Eupsittula nana', 'Arremon aurantiirostris', 'Legatus leucophaius', 'Habia fuscicauda', 'Amazilia tzacatl', 'Synallaxis erythrothorax', 'Tyrannus forficatus', 'Myiodynastes maculatus', 'Eupherusa eximia', 'Henicorhina leucosticta', 'Pampa curvipennis', 'Chlorestes candida', 'Pseudastur albicollis', 'Momotus coeruliceps/lessonii', 'Amblycercus holosericeus', 'Tolmomyias sulphurescens', 'Vireo flavifrons', 'Empidonax virescens', 'Trogon caligatus', 'Myiarchus crinitus', 'Ramphocaenus melanurus', 'Lipaugus unirufus', 'Phaethornis striigularis', 'Contopus cinereus', 'Campylopterus hemileucurus', 'Ornithion semiflavum', 'Formicarius moniliger', 'Chlorophonia occipitalis', 'Anabacerthia variegaticeps', 'Turdus infuscatus', 'Cyanolyca nanus', 'Lamprolaima rhami', 'Cyanolyca cucullata', 'Micrastur ruficollis', 'Catharus mexicanus', 'Icterus prosthemelas', 'Pyrilia haematotis', 'Pachysylvia decurtata', 'Aulacorhynchus prasinus', 'Cyanerpes cyaneus', 'Rhytipterna holerythra', 'Xiphorhynchus erythropygius', 'Odontophorus guttatus', 'Platyrinchus cancrominus', 'Hylorchilus sumichrasti', 'Myiobius sulphureipygius', 'Tunchiornis ochraceiceps', 'Sclerurus mexicanus', 'Tityra inquisitor', 'Thraupis episcopus', 'Cynanthus canivetii', 'Geranospiza caerulescens', 'Rhynchocyclus brevirostris', 'Crax rubra', 'Psarocolius montezuma', 'Spizaetus ornatus', 'Helmitheros vermivorum', 'Hylocichla mustelina', 'Chloroceryle aenea', 'Busarellus nigricollis', 'Trogon melanocephalus', 'Todirostrum cinereum', 'Buteogallus urubitinga', 'Setophaga citrina', 'Tapera naevia', 'Agamia agami', 'Icterus mesomelas', 'Nomonyx dominicus', 'Leptotila plumbeiceps', 'Calothorax pulcher', 'Campylorhynchus jocosus', 'Peucaea mystacalis', 'Melanerpes hypopolius', 'Aimophila notosticta', 'Xenotriccus mexicanus', 'Vireo brevipennis', 'Melozone albicollis', 'Selasphorus rufus/sasin', 'Petrochelidon fulva', 'Sporophila morelleti/torqueola', 'Bucephala albeola', 'Buteo swainsoni', 'Contopus virens', 'Aramides albiventris', 'Antrostomus salvini', 'Geococcyx velox/californianus', 'Pionus senilis', 'Melospiza georgiana', 'Spizella pusilla', 'Buteo lineatus', 'Geothlypis speciosa', 'Geothlypis sp. (yellowthroat sp.)', 'Turdus rufitorques', 'Dromococcyx phasianellus', 'Chordeiles sp.', 'Laridae sp.', 'Cyrtonyx ocellatus', 'Lophornis helenae', 'Lampornis viridipallens', 'Penelopina nigra', 'Amazona farinosa', 'Pharomachrus mocinno', 'Elanoides forficatus', 'Empidonax flavescens', 'Antrostomus carolinensis', 'Basileuterus sp.', 'Tyrannus tyrannus', 'Tinamidae sp.', 'Tyrannus melancholicus/couchii', 'Arremonops chloronotus', 'Mimus gilvus', 'Cyanocorax yucatanicus', 'Colinus nigrogularis', 'Euphonia sp.', 'Leptodon cayanensis', 'Momotidae sp.', 'Meleagris ocellata', 'Cacicus sp.', 'Tinamus major', 'Phaethornis sp.', 'Crypturellus soui', 'Caprimulgidae sp.', 'Ceratopipra mentalis', 'Columbina sp.', 'Charadrius montanus', 'Sphyrapicus thyroideus', 'Alcedinidae sp.', 'Buteo brachyurus', 'Tyrannidae sp.', 'Anthus sp.', 'Icterus maculialatus', 'Ortalis sp.', 'Glaucidium sp.', 'Icterus chrysater', 'Aspatha gularis', 'Cardellina versicolor', 'Zonotrichia capensis', 'Turdidae sp.', 'Burhinus bistriatus', 'Cynanthus doubledayi', 'Peucaea sumichrasti', 'Leucolia viridifrons', 'Spinus tristis', 'Vermivora chrysoptera', 'Molothrus aeneus/ater', 'Lophornis brachylophus', 'Eupherusa poliocerca', 'Corvidae sp. (jay sp.)', 'Grallaria guatimalensis', 'Zentrygon albifacies', 'Cyanolyca mirabilis', 'Amaurospiza concolor', 'Xiphocolaptes promeropirhynchus', 'Ara sp.', 'Geothlypis formosa', 'Geothlypis philadelphia', 'Spizaetus tyrannus', 'Limnothlypis swainsonii', 'Dendrortyx barbatus', 'Ciccaba nigrolineata', 'Aramus guarauna', 'Chiroxiphia linearis', 'Onychorhynchus coronatus', 'Leiothlypis peregrina', 'Setophaga sp.', 'Harpagus bidentatus', 'Fregata sp.', 'Geotrygon/Leptotrygon/Zentrygon sp.', 'Calidris himantopus', 'Caryothraustes poliogaster', 'Momotus lessonii', 'Molothrus oryzivorus', 'Glaucidium sanchezi', 'Melanerpes pucherani', 'Taraba major', 'Xenops minutus', 'Leptopogon amaurocephalus', 'Lepidocolaptes souleyetii', 'Hylomanes momotula', 'Amaurolimnas concolor', 'Sporophila corvina', 'Glyphorynchus spirurus', 'Manacus candei', 'Calcarius ornatus', 'Calypte anna', 'Icterus pectoralis', 'Pheugopedius sp.', 'Catharus sp.', 'Gymnorhinus cyanocephalus', 'Megascops asio', 'Melanotis hypoleucus', 'Doricha enicura', 'Leucophaeus pipixcan', 'Micrastur sp.', 'Synthliboramphus scrippsi', 'Hydrobates leucorhoa/socorroensis/cheimomnestes', 'Phaethornis mexicanus', 'Charadrius nivosus', 'Calidris melanotos', 'Tyrannus savana', 'Granatellus sallaei', 'Galbula ruficauda', 'Heliornis fulica', 'Lanio aurantius', 'Xenospiza baileyi', 'Vireo leucophrys', 'Henicorhina sp.', 'Spinus sp.', 'Limnodromus griseus/scolopaceus', 'Aquila chrysaetos', 'Sturnus vulgaris', 'Quiscalus palustris', 'Eucometis penicillata', 'Cantorchilus modestus', 'Campylorhynchus chiapensis', 'Sporophila minuta', 'Asio clamator', 'Archilochus colubris/alexandri', 'Nucifraga columbiana', 'Bartramia longicauda', 'Trogon massena', 'Dendrocincla anabatina', 'Empidonax alnorum', 'Aves sp.', 'Scolopacidae sp. (large shorebird sp.)', 'Columba livia', 'Bubulcus ibis', 'Riparia riparia', 'Ictinia mississippiensis', 'Melanoptila glabrirostris', 'Leptotila jamaicensis', 'Elaenia martinica', 'Cynanthus forficatus', 'Vireo bairdi', 'Piranga roseogularis', 'Crotophaga ani', 'Spindalis zena', 'Patagioenas leucocephala', 'Myiarchus yucatanensis', 'Vireo magister', 'Melanerpes pygmaeus', 'Icterus auratus', 'Eumomota superciliosa', 'Urile penicillatus', 'Phaethon aethereus', 'Larus occidentalis', 'Sclerurus guatemalensis', 'Patagioenas nigrirostris', 'Chroicocephalus philadelphia', 'Calidris alpina', 'Toxostoma cinereum', 'Basilinna xantusii', 'Vireo philadelphicus', 'Thalasseus sandvicensis', 'Ramphocelus passerinii', 'Chlorestes eliciae', 'Rostrhamus sociabilis', 'Cathartes burrovianus', 'Haematopus bachmani', 'Ptychoramphus aleuticus', 'Gavia pacifica', 'Urile pelagicus', 'Melanitta perspicillata', 'Hydrobates melania', 'Synthliboramphus craveri', 'Hydrobates microsoma', 'Ardenna creatopus', 'Ardenna grisea', 'Streptoprocne rutila', 'Passerina sp.', 'Gavia immer', 'Artemisiospiza nevadensis', 'Sicalis luteola', 'Falco femoralis', 'Notharchus hyperrhynchus', 'Spinus atriceps', 'Atticora pileata', 'Toxostoma guttatum', 'Puffinus opisthomelas', 'Phalaropus lobatus', 'Hydrobates tethys', 'Gavia stellata', 'Haemorhous cassinii', 'Mergus merganser', 'Larus glaucescens', 'Calidris pusilla', 'Bucephala clangula', 'Limnodromus griseus', 'Calidris virgata', 'Spinus lawrencei', 'Callipepla californica', 'Melozone crissalis', 'Aphelocoma californica', 'Chamaea fasciata', 'Chlorophanes spiza', 'Euphonia gouldi', 'Heliothryx barroti', 'Schiffornis veraepacis', 'Pampa excellens', 'Patagioenas cayennensis', 'Columbina minuta', 'Stilpnia larvata', 'Progne sp.', 'Sporophila funerea', 'Chaetura pelagica', 'Aythya collaris', 'Toxostoma lecontei', 'Artemisiospiza nevadensis/belli', 'Artemisiospiza belli', 'Toxostoma redivivum', 'Branta bernicla', 'Stercorarius pomarinus', 'Phalaropus fulicarius', 'Cerorhinca monocerata', 'Synthliboramphus hypoleucus', 'Rissa tridactyla', 'Turdus plebejus', 'Troglodytes rufociliatus', 'Brotogeris jugularis', 'Selasphorus ellioti', 'Cyanolyca pumilo', 'Aegolius ridgwayi', 'Tringa incana', 'Thalasseus maximus/elegans', 'Setophaga caerulescens', 'Buteo sp.', 'Icteridae sp.', 'Falco sp.', 'Aythya marila/affinis', 'Phoebastria nigripes', 'Hydrobates leucorhous', 'Procellariidae sp. (shearwater sp.)', 'Synthliboramphus scrippsi/hypoleucus/craveri', 'Stercorarius parasiticus', 'Aix sponsa', 'Haematopus palliatus x bachmani', 'Polioptila californica', 'Passerella iliaca', 'Dryobates nuttallii', 'Baeolophus inornatus', 'Haemorhous purpureus', 'Ixoreus naevius', 'Onychoprion fuscatus', 'Zonotrichia albicollis', 'Ictinia plumbea', 'Poecilostreptus cabanisi', 'Bolborhynchus lineola', 'Abeillia abeillei', 'Strix fulvescens', 'Panyptila cayennensis', 'Zimmerius vilissimus', 'Melozone biarcuata', 'Thryophilus rufalbus', 'Basileuterus delattrii', 'Dendrocincla homochroa', 'Pampa rufa', 'Melozone leucotis', 'Xenotriccus callizonus', 'Panyptila sanctihieronymi', 'Piranga olivacea', 'Crypturellus boucardi', 'Pulsatrix perspicillata', 'Florisuga mellivora', 'Xema sabini', 'Apodidae sp. (large swift sp.)', 'Cyanocorax sp.', 'Larus sp.', 'Mergus merganser/serrator', 'Haliaeetus leucocephalus', 'Podiceps auritus', 'Stercorarius sp. (jaeger sp.)', 'Larus brachyrhynchus', 'Fulmarus glacialis', 'Oceanitidae/Hydrobatidae sp.', 'Aechmophorus occidentalis/clarkii', 'Larus glaucoides', 'Nycticorax nycticorax/Nyctanassa violacea', 'Megascops guatemalae', 'Pheucticus ludovicianus/melanocephalus', 'Amazona sp.', 'Sula sp.', 'Ardea/Egretta/Bubulcus sp.', 'Geothlypis flavovelata', 'Cotinga amabilis', 'Gavia sp.', 'Pachyramphus cinnamomeus', 'Leptotila cassinii', 'Leptotila sp.', 'Thamnistes anabatinus', 'Setophaga tigrina', 'Setophaga discolor', 'Microcerculus philomela', 'Chaetura pelagica/vauxi', 'Habia sp.', 'Catharus dryas', 'Psittacara holochlorus/strenuus', 'Synthliboramphus scrippsi/hypoleucus', 'Alcidae sp.', 'Accipiter sp.', 'Dendrocolaptes sp.', 'Patagioenas sp.', 'Calidris sp. (peep sp.)', 'Dysithamnus mentalis', 'Terenotriccus erythrurus', 'Patagioenas speciosa', 'Polioptila bilineata', 'Spizella sp.', 'Piranga sp.', 'Anas platyrhynchos', 'Botaurus pinnatus', 'Pipridae sp.', 'Eupherusa ridgwayi', 'Pipilo maculatus x ocai', 'Forpus cyanopygius', 'Empidonax hammondii/oberholseri', 'Nyctiphrynus mcleodii', 'Petrochelidon pyrrhonota/fulva', 'Onychoprion anaethetus', 'Anous stolidus', 'Pardirallus maculatus', 'Ortalis leucogastra', 'Psarocolius sp.', 'Anatidae sp.', 'Larus occidentalis x glaucescens', 'Zenaida aurita', 'Anatidae sp. (dabbling duck sp.)', 'Glaucidium griseiceps', 'Sula sula', 'Tringa melanoleuca/flavipes', 'Malacoptila panamensis', 'Pachyramphus sp.', 'Saltator sp.', 'Poecile gambeli', 'Oreortyx pictus', 'Sphyrapicus ruber', 'Sterna sp.', 'Zonotrichia atricapilla', 'Geothlypis beldingi', 'Spizaetus melanoleucus', 'Lophostrix cristata', 'Fringillidae sp.', 'Poecilotriccus sylvia', 'Spizella wortheni', 'Plegadis falcinellus', 'Jabiru mycteria', 'Paraclaravis mondetoura', 'Hapalocrex flaviventer', 'Charadrius melodus', 'Icterus bullockii/galbula', 'Vireo altiloquus', 'Megascops barbarus', 'Phalaropus sp.', 'Hydroprogne/Thalasseus sp.', 'Melanerpes sp.', 'Thraupidae sp. (tanager sp.)', 'Podicipedidae sp.', 'Polioptila albiventris', 'Campylorhynchus yucatanicus', 'Phoenicopterus ruber', 'Vireo vicinior', 'Myiodynastes maculatus/luteiventris', 'Threskiornithidae sp. (ibis sp.)', 'Vermivora chrysoptera x cyanoptera (F2 backcross)', 'Anas fulvigula', 'Setophaga striata', 'Corvus brachyrhynchos', 'Columbina passerina/talpacoti', 'Apodidae sp. (small swift sp.)', 'Sphyrapicus varius/nuchalis', 'Mimidae sp.', 'Anas platyrhynchos (Domestic type)', 'Dolichonyx oryzivorus', 'Calidris pusilla/mauri', 'Junco bairdi', 'Limosa haemastica', 'Calidris fuscicollis', 'Antrostomus badius', 'Nyctiphrynus yucatanicus', 'Hylorchilus navai', 'Cyanerpes lucidus', 'Melanitta deglandi', 'Nannopterum auritum/brasilianum', 'Aythya marila', 'Tyrannus dominicensis', 'Falco sp. (large falcon sp.)', 'Lophodytes cucullatus', 'Basileuterus rufifrons/delattrii', 'Calidris sp.', 'Ardenna pacifica', 'Catharus minimus', 'Catharus fuscescens', 'Sula dactylatra', 'Streptopelia decaocto', 'Sterna paradisaea', 'Oceanites oceanicus', 'Plegadis falcinellus/chihi', 'Rallus obsoletus/longirostris/crepitans', 'Motacilla alba', 'Campephilus sp./Dryocopus lineatus', 'Oreophasis derbianus', 'Chaetura sp.', 'Sterna dougallii', 'Atlapetes sp.', 'Setophaga cerulea', 'Cistothorus stellaris', 'Empidonax alnorum/traillii', 'Accipiter striatus/cooperii', 'Falco sp. (small falcon sp.)', 'Pipilo maculatus/erythrophthalmus', 'Haematopus sp.', 'Setophaga pinus', 'Sitta canadensis', 'Agelaius tricolor', 'Crotophaga ani/sulcirostris', 'Toxostoma curvirostre/bendirei', 'Colaptes auratus/chrysoides', 'Buteogallus anthracinus/urubitinga', 'Saucerottia cyanura', 'Sula granti', 'Rallus crepitans', 'Melanerpes lewis', 'Amazona oratrix', 'Aphelocoma wollweberi/ultramarina', 'Mareca penelope', 'Phoebastria immutabilis', 'Myiarchus cinerascens/nuttingi', 'Anser rossii', 'Megascops cooperi', 'Ardenna grisea/tenuirostris', 'Hydropsalis maculicaudus', 'Larus fuscus', 'Cygnus columbianus', 'Sula dactylatra/granti', 'Lonchura punctulata', 'Buteogallus solitarius', 'Melanitta sp.', 'Eupsittula/Aratinga/Thectocercus/Psittacara sp.', 'Calidris ferruginea', 'Phasianus colchicus', 'Mimus graysoni', 'Troglodytes sissonii', 'Spatula discors/cyanoptera', 'Phaeochroa cuvierii', 'Calocitta colliei x formosa', 'Melozone aberti', 'Cathartes sp.', 'Psittacara brevipes', 'Pluvialis fulva', 'Anas platyrhynchos x diazi', 'Ardenna carneipes', 'Stercorarius longicaudus', 'Corvus sp. (crow sp.)', 'Buteogallus sp.', 'Rhynchophanes mccownii', 'Toxostoma rufum', 'Branta hutchinsii/canadensis', 'Ardenna tenuirostris', 'Icterus spurius/cucullatus', 'Limosa lapponica', 'Myioborus sp.', 'Melanitta americana', 'Antrostomus vociferus/arizonae', 'Charadriidae sp.', 'Cypseloides sp.', 'Clangula hyemalis', 'Larus argentatus x hyperboreus', 'Synthliboramphus antiquus', 'Brachyramphus marmoratus', 'Toxostoma sp.', 'Dendrortyx leucophrys', 'Tachycineta sp.', 'Branta hutchinsii', 'Stercorarius maccormicki', 'Icterus bullockii/abeillei', 'Peucaea sp.', 'Euphagus carolinus', 'Cistothorus platensis/palustris', 'Harpia harpyja', 'Lurocalis semitorquatus', 'Accipitriformes/Falconiformes sp.', 'Pluvialis sp.', 'Laniocera rufescens', 'Onychoprion fuscatus/anaethetus', 'Eupherusa cyanophrys', 'Hydrobates sp.', 'Zentrygon carrikeri', 'Phaethon aethereus/rubricauda', 'Phylloscopus fuscatus', 'Zonotrichia querula', 'Sphyrapicus nuchalis x ruber', 'Calypte anna x costae', 'Quiscalus quiscula', 'Hydrobates socorroensis', 'Pterodroma cookii', 'Ardenna bulleri', 'Phalaropus lobatus/fulicarius', 'Heliomaster longirostris/constantii', 'Anthus hodgsoni', 'Anthus cervinus', 'Passerina amoena/cyanea', 'Streptopelia chinensis', 'Anser sp. (Domestic type)', 'Puffinus subalaris', 'Sterna hirundo/paradisaea', 'Arremonops rufivirgatus/chloronotus', 'Vanellus chilensis', 'Podiceps grisegena', 'Gavia adamsii', 'Calothorax lucifer/pulcher', 'Dendrocygna sp.', 'Sterna hirundo/forsteri', 'Larus hyperboreus', 'Lepidocolaptes sp.', 'Larus crassirostris', 'Hydrobates homochroa', 'Motacilla tschutschensis', 'Oceanitidae/Hydrobatidae sp. (dark-rumped)', 'Calcarius lapponicus', 'Centronyx bairdii', 'Charadrius morinellus', 'Poecile sp.', 'Junco hyemalis/phaeonotus', 'Ammodramus savannarum/Centronyx bairdii', 'Morus bassanus', 'Stercorarius pomarinus/parasiticus', 'Pheucticus ludovicianus x melanocephalus', 'Tyrannus sp.', 'Bucephala islandica', 'Aythya sp.', 'Tachycineta bicolor/thalassina', 'Dryobates sp.', 'Streptopelia roseogrisea (Domestic type)', 'Oporornis agilis', 'Fregata minor', 'Buteo plagiatus/nitidus', 'Nyctibius grandis', 'Myiopsitta monachus', 'Anser caerulescens/rossii', 'Troglodytes hiemalis', 'Setophaga townsendi x occidentalis', 'Elaenia frantzii', 'Cypseloides storeri', 'Cardinalis cardinalis/sinuatus', 'Buteo lagopus', 'Dryobates pubescens', 'Psittacara sp.', 'Thraupis sp.', 'Furnariidae sp. (foliage-gleaner sp.)', 'Euphonia minuta', 'Empidonax wrightii/oberholseri', 'Ictinia mississippiensis/plumbea', 'Calidris subruficollis', 'Ramphastos sp.', 'Tityra sp.', 'Amazilia yucatanensis/tzacatl', 'Setophaga americana/pitiayumi', 'Vermivora chrysoptera x cyanoptera', 'Gallinula/Fulica/Porphyrio sp.', 'Puffinus sp. (black-and-white shearwater sp.)', 'Xenus cinereus', 'Calidris minuta', 'Mergellus/Lophodytes/Mergus sp.', 'Spatula discors x cyanoptera', 'Ammospiza leconteii', 'Puffinus puffinus', 'Larus argentatus x glaucescens', 'Histrionicus histrionicus', 'Larus dominicanus', 'Aphelocoma sp.', 'Dryobates scalaris x villosus', 'Dryobates nuttallii x scalaris', 'Hydrobates leucorhous/socorroensis (dark-rumped)', 'Oporornis/Geothlypis sp. (Mourning-type)', 'Calidris pugnax', 'Tyrannus vociferans/verticalis', 'Lonchura malacca', 'Pterodroma phaeopygia/sandwichensis', 'Melopsittacus undulatus (Domestic type)', 'Vermivora chrysoptera x cyanoptera (F1 hybrid)', 'Columba sp.', 'Cuculidae sp.', 'Pavo cristatus', 'Pavo cristatus (Domestic type)', 'Mareca penelope x americana', 'Spatula querquedula', 'Larus marinus', 'Elaenia sp.', 'Euphagus cyanocephalus x Quiscalus mexicanus', 'Pterodroma externa', 'Puffinus nativitatis', 'Pterodroma neglecta', 'Phaethon rubricauda', 'Haemorhous sp.', 'Anas platyrhynchos/fulvigula', 'Troglodytes tanneri', 'Icterus bullockii x galbula', 'Calonectris diomedea', 'Hydrobates cheimomnestes', 'Hydrobates leucorhous/socorroensis', 'Pterodroma sp. (Cookilaria sp.)', 'Stercorarius sp. (skua sp.)', 'Gygis alba', 'Setophaga castanea/striata', 'Ammospiza nelsoni', 'Ammospiza maritima', 'Gymnogyps californianus', 'Calcarius/Rhynchophanes sp.', 'Pterodroma sp.', 'Spatula clypeata x Mareca strepera', 'Setophaga americana x pitiayumi', 'Phylloscopus inornatus', 'Strix sartorii', 'Anhinga rufa', 'Melopsittacus undulatus', 'Quiscalus sp.', 'Leiothlypis sp.', 'Spizella passerina x pallida', 'Haematopus palliatus/bachmani', 'Phoenicopterus ruber/roseus', 'Melospiza lincolnii/georgiana', 'Myrmotherula schisticolor', 'Brachyramphus/Synthliboramphus sp.', 'Anser cygnoides (Domestic type)', 'Gallinula chloropus/galeata', 'Melozone fusca/aberti', 'Anser anser (Domestic type)', 'Columba livia/Patagioenas fasciata', 'Coccyzus americanus/erythropthalmus', 'Oenanthe oenanthe', 'Emberiza pusilla', 'Leucophaeus modestus', 'Uria aalge', 'Anser caerulescens x rossii', 'Troglodytes pacificus', 'Pachyramphus polychopterus', 'Antrostomus sp.', 'Aphelocoma californica/woodhouseii', 'Spizaetus sp.', 'Geothlypis tolmiei/philadelphia', 'Sulidae sp.', 'Cardinalis cardinalis x sinuatus', 'Antrostomus vociferus', 'Tringa brevipes/incana', 'Laterallus exilis', 'Sporophila schistacea', 'Phaethon lepturus', 'Cepphus columba', 'Tringa glareola', 'Streptoprocne sp.', 'Synthliboramphus scrippsi/craveri', 'Ardea sp.', 'Stercorarius parasiticus/longicaudus', 'Piranga flava/rubra', 'Charadrius sp.', 'Streptopelia sp.', 'Tringa sp.', 'Tringa stagnatilis', 'Calypte anna/costae', 'Aechmophorus occidentalis x clarkii', 'Passerina amoena x cyanea', 'Limosa sp.', 'Cynanthus latirostris/doubledayi', 'Setophaga townsendi/occidentalis', 'Calidris alpina x fuscicollis', 'Diomedeidae sp.', 'Scolopacidae sp.', 'Coccyzus sp.', 'Spatula discors x clypeata', 'Sphyrapicus varius x nuchalis', 'Larus occidentalis/livens', 'Geranoaetus/Buteo sp.', 'Dendrocolaptes picumnus', 'Pseudobulweria rostrata', 'Morphnus guianensis', 'Hydrocoloeus minutus', 'Amazona auropalliata', 'Pterodroma cervicalis', 'Mareca americana x Anas acuta', 'Phaethon sp.', 'Actitis hypoleucos/macularius', 'Anous stolidus/minutus', 'Calidris maritima', 'Thalasseus sp.', 'Buteo/eagle sp.', 'Podiceps auritus/nigricollis', 'Ara macao/chloropterus', 'Phaeoptila sordida/Cynanthus doubledayi', 'Rallus sp.', 'Oceanitidae/Hydrobatidae sp. (white-rumped)', 'Puffinus lherminieri', 'Hydrobates castro', 'Ardenna gravis', 'Pheucticus sp.', 'Agelaius phoeniceus/tricolor', 'Ciconiidae sp.', 'Calidris acuminata', 'Melanitta perspicillata/americana', 'Procellariidae sp.', 'Cairina moschata x Anas platyrhynchos', 'Streptopelia roseogrisea', 'Gallinago gallinago/delicata', 'Aratinga nenday', 'Piranga rubra/olivacea', 'Callipepla californica/gambelii', 'Progne tapera', 'Haemorhous mexicanus/purpureus', 'Branta sp.', 'Setophaga townsendi x virens', 'Plegadis falcinellus x chihi', 'Scolopax minor', 'Hydrobates leucorhous/socorroensis (white-rumped)', 'Furnariidae sp.', 'Molothrus bonariensis', 'Petrochelidon sp.', 'Stercorarius sp.', 'Streptopelia decaocto x roseogrisea', 'Cracidae sp.', 'Egretta thula x caerulea', 'Bulweria bulwerii', 'Psittacara mitratus', 'Anous minutus', 'Anas diazi/fulvigula', 'Zonotrichia sp.', 'Ptychoramphus/Aethia sp.', 'Vireo philadelphicus/gilvus', 'Melanerpes aurifrons/carolinus', 'Numida meleagris (Domestic type)', 'Mimus gilvus/polyglottos', 'Anser sp.', 'Mimus gilvus x polyglottos', 'Pionus sp.', 'Sayornis sp.', 'Rallus sp. (large Rallus sp.)', 'Cygnus olor', 'Leucophaeus atricilla/pipixcan', 'Larus argentatus/fuscus', 'Ciccaba sp.', 'Chloroceryle sp.', 'Colibri sp.', 'Dryobates nuttallii/scalaris', 'Streptopelia decaocto/roseogrisea', 'Icterus bullockii x abeillei', 'Gallinula galeata x Fulica americana', 'Aquila chrysaetos/Haliaeetus leucocephalus', 'Corthylio calendula/Regulus satrapa', 'Larus sp. (white-winged gull sp.)', 'Larus argentatus x dominicanus', 'Fulica sp.', 'Mareca penelope/americana', 'Larus argentatus x fuscus', 'Peucaea botterii/cassinii', 'Aramides albiventris/cajaneus', 'Accipiter cooperii/gentilis', 'Sphyrapicus varius x ruber', 'Anas diazi x fulvigula', 'Tyrannus verticalis x tyrannus', 'Thamnophilidae sp. (antshrike sp.)', 'Tarsiger cyanurus', 'Calocitta colliei/formosa', 'Cyanoliseus patagonus', 'Oceanites sp.', 'Vireo olivaceus/chivi', 'Vireo olivaceus/flavoviridis', 'Uria lomvia', 'Acridotheres cristatellus', 'Acanthis hornemanni', 'Melanerpes erythrocephalus', 'Aythya fuligula', 'Bombycilla garrulus', 'Anas rubripes', 'Perdix perdix', 'Lanius borealis', 'Perisoreus canadensis', 'Loxia leucoptera', 'Melanerpes carolinus', 'Pipilo erythrophthalmus', 'Pinicola enucleator', 'Picoides arcticus', 'Strix varia', 'Bubo scandiacus', 'Acanthis flammea', 'Poecile hudsonicus', 'Pluvialis apricaria', 'Loxia sp.', 'Plectrophenax nivalis', 'Leucosticte tephrocotis', 'Baeolophus bicolor', 'Catharus bicknelli', 'Somateria mollissima', 'Dryobates albolarvatus', 'Somateria spectabilis', 'Calcarius pictus', 'Bonasa umbellus', 'Poecile atricapillus', 'Pica hudsonia', 'Spizelloides arborea', 'Bucephala clangula/islandica', 'Fringilla montifringilla', 'Chroicocephalus ridibundus', 'Cyanocitta cristata', 'Cepphus grylle', 'Acanthis flammea/hornemanni', 'Picoides dorsalis', 'Dryocopus pileatus', 'Phalacrocorax carbo', 'Alauda arvensis', 'Cygnus buccinator/columbianus', 'Alle alle', 'Alca torda', 'Poecile rufescens', 'Lagopus lagopus', 'Cygnus buccinator', 'Tympanuchus phasianellus', 'Aegolius funereus', 'Lagopus muta', 'Dendragapus fuliginosus', 'Fratercula arctica', 'Anas platyrhynchos x rubripes', 'Canachites canadensis', 'Fratercula cirrhata', 'Thalassarche chlororhynchos', 'Mergellus albellus', 'Centronyx henslowii', 'Pagophila eburnea', 'Corvus ossifragus', 'Chlidonias leucopterus', 'Limosa limosa', 'Larus canus', 'Egretta garzetta', 'Rhodostethia rosea', 'Anas platyrhynchos/rubripes', 'Dendragapus obscurus', 'Acanthis sp.', 'Lagopus leucura', 'Hydrobates furcatus', 'Empidonomus varius', 'Calidris ruficollis', 'Ectopistes migratorius', 'Tetraoninae sp.', 'Branta leucopsis', 'Grus americana', 'Alectoris chukar', 'Dryobates pubescens/villosus', 'Bombycilla garrulus/cedrorum', 'Vermivora chrysoptera/cyanoptera', 'Spizella/Spizelloides sp.', 'Cygnus cygnus', 'Fratercula corniculata', 'Larus michahellis', 'Tringa erythropus', 'Luscinia svecica', 'Centrocercus urophasianus x Tympanuchus phasianellus', 'Picoides dorsalis/arcticus', 'Lagopus sp.', 'Aix galericulata', 'Charadrius hiaticula', 'Cygnus sp.', 'Vanellus vanellus', 'Anser brachyrhynchus', 'Charadrius mongolus', 'Fringilla coelebs', 'Setophaga kirtlandii', 'Brachyramphus brevirostris', 'Larus schistisagus', 'Catharus minimus/bicknelli', 'Calidris ptilocnemis', 'Uria/Alca sp.', 'Corvus monedula', 'Bucephala clangula x islandica', 'Aythya collaris x marila', 'Pluvialis dominica/fulva', 'Larus canus/brachyrhynchus', 'Lanius sp.', 'Turdus pilaris', 'Tadorna tadorna', 'Pterodroma hasitata', 'Pluvialis apricaria/dominica/fulva', 'Passer montanus', 'Stercorarius skua', 'Anser serrirostris', 'Larus occidentalis/glaucescens', 'Ammospiza nelsoni/caudacuta', 'Emberiza rustica', 'Anas platyrhynchos x acuta', 'Prunella montanella', 'Lanius cristatus', 'Dendragapus obscurus/fuliginosus', 'Anas sp.', 'Tringa totanus', 'Anser anser (Domestic type) x Branta canadensis', 'Turdus eunomus', 'Grus grus', 'Ixoreus naevius/Turdus migratorius', 'Brachyramphus perdix', 'Haematopus ostralegus', 'Numenius madagascariensis', 'Lanius ludovicianus/borealis', 'Carduelis carduelis', 'Uria aalge/lomvia', 'Somateria sp.', 'Calidris temminckii', 'Poecile atricapillus/gambeli', 'Turdus iliacus', 'Anser canagicus', 'Poecile cinctus', 'Chroicocephalus ridibundus x Larus delawarensis', 'Troglodytes pacificus/hiemalis', 'Sphyrapicus nuchalis/ruber', 'Falco tinnunculus', 'Milvus milvus/migrans', 'Larus argentatus x marinus', 'Calidris pygmaea', 'Mareca strepera x Anas platyrhynchos', 'Somateria spectabilis/mollissima', 'Mareca falcata', 'Pterodroma ultima', 'Phalacrocorax carbo/Nannopterum auritum', 'Poecile atricapillus x gambeli', 'Passer domesticus x montanus', 'Tringa nebularia', 'Mareca americana x Anas crecca', 'Bonasa umbellus/Canachites canadensis', 'Polysticta stelleri', 'Bucephala clangula x Lophodytes cucullatus', 'Anser caerulescens x Branta canadensis', 'Tympanuchus cupido', 'Phoebastria albatrus', 'Vireo philadelphicus/olivaceus', 'Lymnocryptes minimus', 'Quiscalus major/mexicanus', 'Euphagus carolinus/cyanocephalus', 'Numenius tenuirostris', 'Podiceps sp.', 'Peucaea aestivalis', 'Mareca americana x Anas platyrhynchos', 'Anser sp. (Domestic type) x Branta canadensis', 'Asio otus/flammeus', 'Zonotrichia leucophrys/albicollis', 'Gavia immer/adamsii', 'Acanthis flammea x hornemanni', 'Anser cygnoides (Domestic type) x Branta canadensis', 'Anser caerulescens x Branta hutchinsii', 'Acanthis/Spinus sp.', 'Calonectris diomedea/Ardenna gravis', 'Larus argentatus/glaucoides', 'Crex crex', 'Fulica atra', 'Bucephala albeola x clangula', 'Setophaga palmarum x coronata', 'Sialia sialis x currucoides', 'Numenius borealis', 'Calliope calliope', 'Gallinago gallinago', 'Anser anser x Branta canadensis', 'Aythya valisineria x americana', 'Leucophaeus atricilla x Larus delawarensis', 'Turdus merula', 'Tympanuchus phasianellus x cupido', 'Motacilla sp.', 'Poecile carolinensis', 'Geothlypis philadelphia x trichas', 'Chlidonias sp.', 'Zonotrichia leucophrys x albicollis', 'Haemorhous purpureus/cassinii', 'Numenius arquata', 'Streptopelia orientalis', 'Aythya americana x collaris', 'Mareca strepera x Anas crecca', 'Ammospiza sp.', 'Puffinus baroli', 'Anser albifrons x Branta canadensis', 'Ammodramus savannarum/Centronyx henslowii', 'Saxicola maurus', 'Aethia psittacula', 'Sturnella neglecta x magna', 'Larus glaucescens x hyperboreus', 'Charadrius hiaticula/semipalmatus', 'Pterodroma feae', 'Tadorna ferruginea', 'Branta leucopsis x canadensis', 'Tachycineta thalassina x Petrochelidon pyrrhonota', 'Larus hyperboreus x marinus', 'Gavia arctica', 'Mareca strepera x Anas acuta', 'Ammospiza caudacuta', 'Sibirionetta formosa', 'Aethia cristatella', 'Cygnus olor x buccinator', 'Phylloscopus borealis', 'Calidris fuscicollis x subruficollis', 'Nymphicus hollandicus (Domestic type)', 'Setophaga nigrescens/townsendi', 'Plectrophenax hyperboreus', 'Larus michahellis/fuscus', 'Diomedea sp.', 'Asio sp.', 'Aythya collaris x affinis', 'Plectrophenax nivalis/hyperboreus', 'Pterodroma inexpectata', 'Aythya fuligula x marila/affinis', 'Larus californicus x argentatus', 'Egretta gularis', 'Anser anser', 'Aythya fuligula x marila', 'Turdus philomelos', 'Aythya americana x affinis', 'Zonotrichia atricapilla x albicollis', 'Bucephala clangula/islandica x Lophodytes cucullatus', 'Apus apus', 'Spinus spinus', 'Bucephala albeola x Lophodytes cucullatus', 'Aythya collaris x marila/affinis', 'Pterodroma cahow', 'Quiscalus major', 'Thalassarche melanophris', 'Somateria spectabilis x mollissima', 'Larus schistisagus x glaucescens', 'Apus pacificus', 'Anser fabalis/serrirostris', 'Numenius tahitiensis', 'Zonotrichia leucophrys x atricapilla', 'Spatula clypeata x Anas platyrhynchos', 'Aythya collaris x fuligula', 'Gavia arctica/pacifica', 'Pipilo maculatus x erythrophthalmus', 'Motacilla citreola', 'Archilochus alexandri x Selasphorus rufus', 'Junco hyemalis x Zonotrichia albicollis', 'Buteo lineatus x jamaicensis', 'Pelagodroma marina', 'Setophaga nigrescens x townsendi', 'Ardea cinerea', 'Cuculus canorus', 'Gallinago sp.', 'Acridotheres tristis', 'Anser caerulescens x albifrons', 'Setophaga magnolia x caerulescens', 'Leiothlypis ruficapilla x Setophaga magnolia', 'Aythya fuligula x affinis', 'Rallus elegans/limicola', 'Anser fabalis', 'Setophaga magnolia x coronata', 'Calidris acuminata/melanotos', 'Rallus elegans/crepitans', 'Meleagris gallopavo (Domestic type)', 'Pterodroma sandwichensis', 'Setophaga magnolia x pensylvanica', 'Anser anser x cygnoides (Domestic type)', 'Spizella pallida x pusilla', 'Aythya americana x marila', 'Spatula cyanoptera x clypeata', 'Chloris sinica', 'Anser caerulescens/rossii x Branta hutchinsii/canadensis', 'Aythya americana x marila/affinis', 'Spatula cyanoptera x Anas crecca', 'Mareca strepera x americana', 'Poecile carolinensis/atricapillus', 'Bubo sp.', 'Anser albifrons x Branta hutchinsii', 'Calypte anna x Selasphorus rufus', 'Phasianidae sp. (pheasant sp.)', 'Toxostoma rufum/longirostre', 'Buteo lineatus/platypterus', 'Spinus pinus x tristis', 'Poecile carolinensis x atricapillus', 'Numenius sp.', 'Turdus viscivorus', 'Larus argentatus/glaucescens', 'Archilochus alexandri x Calypte anna', 'Calidris ptilocnemis/maritima', 'Himantopus mexicanus x Recurvirostra americana', 'Emberiza aureola', 'Bucephala islandica x Lophodytes cucullatus', 'Aquila sp.', 'Hirundo rustica x Petrochelidon pyrrhonota', 'Buteo jamaicensis x lagopus', 'Melanitta fusca/deglandi/stejnegeri', 'Cyanocitta stelleri x cristata', 'Calcarius lapponicus x Plectrophenax nivalis', 'Emberiza leucocephalos', 'Aythya valisineria x collaris', 'Columba palumbus', 'Aix sponsa x Lophodytes cucullatus', 'Ixobrychus sp.', 'Ammospiza leconteii/nelsoni', 'Vireo sp. (Red-eyed Vireo complex)', 'Passer domesticus/montanus', 'Somateria fischeri', 'Cyanocitta stelleri x Aphelocoma californica', 'Spatula discors x Anas crecca', 'Tringa brevipes', 'Lanius collurio', 'Aythya ferina', 'Coccothraustes coccothraustes', 'Sterna dougallii x hirundo', 'Rissa brevirostris', 'Bucephala albeola x clangula/islandica', 'Anthus spinoletta/rubescens', 'Spizella passerina x pusilla', 'Anser rossii x Branta hutchinsii', 'Melanitta deglandi/stejnegeri', 'Gruidae sp.', 'Haliaeetus pelagicus', 'Butorides virescens/striata', 'Anas acuta x crecca', 'Alaudidae sp.', 'Corvus brachyrhynchos/ossifragus', 'Stercorarius pomarinus/longicaudus', 'Caprimulgus sp.', 'Melospiza melodia x lincolnii', 'Nymphicus hollandicus', 'Netta rufina', 'Cacatua galerita', 'Melanitta fusca', 'Cygnus atratus', 'Pyrrhula pyrrhula', 'Alopochen aegyptiaca', 'Anser indicus', 'Chloris chloris', 'Crithagra mozambica', 'Parus major', 'Anodorhynchus hyacinthinus', 'Glaucidium/Aegolius sp. (pygmy-owl/saw-whet owl sp.)', 'Callonetta leucophrys', 'Euplectes orix', 'Uraeginthus bengalus', 'Mareca sibilatrix', 'Agapornis sp.', 'Gallus gallus (Domestic type)', 'Numida meleagris', 'Phoenicopterus chilensis', 'Chrysolophus pictus', 'Marmaronetta angustirostris', 'Colius striatus', 'Alectoris rufa', 'Pheucticus aureoventris', 'Anser rossii x Branta canadensis', 'Serinus canaria (Domestic type)', 'Alectoris graeca', 'Lophornis pavoninus', 'Leptoptilos crumenifer', 'Anas bahamensis', 'Amadina erythrocephala', 'Goura victoria', 'Paridae sp.', 'Coturnix japonica', 'Psephotus haematonotus', 'Scopus umbretta', 'Streptopelia senegalensis', 'Euplectes franciscanus', 'Spheniscus demersus', 'Psittacula krameri', 'Caloenas nicobarica', 'Aix sponsa x galericulata', 'Anser cygnoides', 'Lophura nycthemera', 'Pyrrhura molinae', 'Spizixos semitorques', 'Estrilda astrild', 'Stizoptera bichenovii', 'Pternistis afer', 'Cyanocorax chrysops', 'Sagittarius serpentarius', 'Pelecanus onocrotalus', 'Lophonetta specularioides', 'Eudromia elegans', 'Agapornis roseicollis', 'Atelornis pittoides', 'Chrysolophus amherstiae', 'Polyplectron chalcurum', 'Serinus sp.', 'Tadorna cana', 'Agapornis fischeri', 'Serinus canaria', 'Taeniopygia guttata', 'Poicephalus rufiventris', 'Coturnix coturnix', 'Agapornis pullarius', 'Branta ruficollis', 'Coturnix coturnix/coromandelica', 'Phylloscopus inornatus/humei', 'Ara ararauna', 'Chloebia gouldiae', 'Dacelo novaeguineae', 'Gracula religiosa', 'Procellaria sp.', 'Strix aluco', 'Epthianura crocea', 'Anas platyrhynchos x superciliosa', 'Synoicus/Coturnix sp.', 'Padda oryzivora', 'Threskiornis aethiopicus', 'Streptopelia capicola', 'Amazona viridigenalis', 'Zapornia flavirostra', 'Falco biarmicus', 'Phoenicopteridae sp.', 'Gallinula chloropus', 'Cyanistes caeruleus', 'Synoicus chinensis', 'Corvus corone', 'Calypte anna x Selasphorus calliope', 'Mareca americana x Anas rubripes', 'Aphelocoma coerulescens', 'Eudocimus ruber', 'Dromaius novaehollandiae', 'Antigone canadensis x Grus grus', 'Struthio camelus', 'Corvus albus', 'Spizelloides arborea x Zonotrichia querula', 'Trochalopteron elliotii', 'Bucorvus abyssinicus', 'Merops nubicus', 'Lonchura striata', 'Pyrrhoplectes epauletta', 'Paroaria coronata', 'Pavo muticus', 'Phylloscopus sp.', 'Crithagra sp.', 'Conuropsis carolinensis', 'Campephilus principalis', 'Sitta pusilla', 'Dryobates borealis', 'Vermivora bachmanii', 'Molothrus bonariensis/ater', 'Motacilla flava/tschutschensis', 'Anas platyrhynchos x fulvigula', 'Thalasseus sandvicensis x elegans', 'Aix sponsa x Anas platyrhynchos', 'Vidua macroura', 'Vireo olivaceus/altiloquus', 'Aethia pusilla', 'Urile urile', 'Calidris subminuta', 'Cuculus optatus', 'Onychoprion aleuticus', 'Calidris tenuirostris', 'Jynx torquilla', 'Turdus obscurus', 'Motacilla cinerea', 'Actitis hypoleucos', 'Anas zonorhyncha', 'Aethia pygmaea', 'Hirundapus caudacutus', 'Egretta eulophotes', 'Delichon urbicum', 'Carpodacus erythrinus', 'Anthus gustavi', 'Upupa epops', 'Caprimulgus jotaka', 'Emberiza schoeniclus', 'Haliaeetus albicilla', 'Otus sunia', 'Muscicapa sibirica', 'Phylloscopus borealis/examinandus', 'Tringa ochropus', 'Phylloscopus sibilatrix', 'Cuculus sp.', 'Cuculus canorus/optatus', 'Helopsaltes ochotensis', 'Emberiza variabilis', 'Phylloscopus examinandus', 'Muscicapa griseisticta', 'Ficedula parva', 'Ficedula albicilla', 'Cepphus grylle/columba', 'Buteo buteo', 'Falco subbuteo', 'Himantopus himantopus', 'Rissa tridactyla/brevirostris', 'Locustella lanceolata', 'Muscicapa dauurica', 'Ficedula mugimaki', 'Glareola maldivarum', 'Larvivora cyane', 'Dendrocopos major', 'Charadrius dubius', 'Calidris falcinellus', 'Motacilla flava', 'Fratercula sp.', 'Ficedula narcissina', 'Ixobrychus sinensis', 'Numenius minutus', 'Anthus trivialis/hodgsoni', 'Gallinago stenura', 'Charadrius alexandrinus/nivosus', 'Turdus eunomus/naumanni', 'Anser erythropus', 'Plectrophenax nivalis x hyperboreus', 'Accipiter soloensis', 'Leucosticte sp.', 'Anthus trivialis', 'Melanitta stejnegeri', 'Ardeola bacchus', 'Emberiza elegans', 'Turdus naumanni', 'Circus sp.', 'Circus cyaneus/hudsonius', 'Larvivora sibilans', 'Zapornia pusilla', 'Accipiter nisus', 'Circus cyaneus', 'Larus schistisagus x hyperboreus', 'Anthropoides virgo', 'Curruca curruca', 'Muscicapa striata', 'Thalassarche salvini', 'Hydrobates monorhis', 'Sternula albifrons/antillarum', 'Ardea intermedia', 'Phoebastria immutabilis x nigripes', 'Emberiza pallasi', 'Phylloscopus proregulus', 'Ninox japonica', 'Phylloscopus trochilus', 'Calidris ruficollis/minuta', 'Acrocephalus schoenobaenus', 'Emberiza chrysophrys', 'Gallinago solitaria', 'Acrocephalus dumetorum', 'Pterodroma solandri', 'Lanius borealis/excubitor', 'Leucosticte arctoa', 'Botaurus stellaris', 'Uria aalge x lomvia', 'Phylloscopus collybita', 'Phoenicurus phoenicurus', 'Carpodacus roseus', 'Milvus migrans', 'Oenanthe pleschanka', 'Arundinax aedon', 'Locustella fluviatilis', 'Phylloscopus xanthodryas/borealis/examinandus', 'Somateria fischeri x spectabilis', 'Buteo rufinus', 'Ichthyaetus ichthyaetus', 'Emberiza sp.', 'Helopsaltes certhiola', 'Ardea alba/intermedia', 'Muscicapa griseisticta/sibirica', 'Grus monacha', 'Monticola saxatilis', 'Hydrobates sp. (Band-rumped complex)', 'Baeolophus ridgwayi', 'Baeolophus wollweberi/ridgwayi', 'Rhynchopsitta pachyrhyncha', 'Baeolophus inornatus/ridgwayi', 'Piranga ludoviciana x bidentata', 'Polioptila melanura x nigriceps', 'Leucosticte atrata', 'Eugenes fulgens x Saucerottia beryllina', 'Callipepla squamata x gambelii', 'Piranga flava x bidentata', 'Cynanthus latirostris x Leucolia violiceps', 'Piranga rubra x ludoviciana', 'Calothorax lucifer x Calypte costae', 'Archilochus alexandri x Calypte costae', 'Setophaga coronata x townsendi', 'Calothorax lucifer x Calypte anna', 'Archilochus alexandri x Cynanthus latirostris', 'Agapornis personatus', 'Tyrannus verticalis x forficatus', 'Streptopelia decaocto x Zenaida macroura', 'Melozone fusca x aberti', 'Myioborus pictus x miniatus', 'Calypte anna x Cynanthus latirostris', 'Calypte anna x Selasphorus sp.', 'Setophaga nigrescens/occidentalis', 'Dryobates pubescens/scalaris', 'Colaptes auratus x chrysoides', 'Calothorax lucifer x Archilochus alexandri', 'Anas rubripes/fulvigula', 'Thalassarche cauta', 'Pica nuttalli', 'Brotogeris chiriri', 'Aphelocoma insularis', 'Centrocercus urophasianus', 'Psittacara erythrogenys', 'Pycnonotus jocosus', 'Brotogeris versicolurus', 'Larus belcheri', 'Amazona finschi', 'Creagrus furcatus', 'Diomedea exulans', 'Calonectris leucomelas', 'Tachycineta bicolor x Hirundo rustica', 'Callipepla californica x gambelii', 'Brotogeris versicolurus/chiriri', 'Dryobates nuttallii x villosus', 'Zosterops palpebrosus', 'Pterodroma gouldi', 'Estrilda sp.', 'Spermestes cucullata', 'Pterodroma longirostris', 'Alauda arvensis/gulgula', 'Zosterops simplex', 'Estrilda melpoda', 'Phoebetria palpebrata', 'Dryobates pubescens x nuttallii', 'Thectocercus acuticaudatus', 'Pelecanus rufescens', 'Thalassarche cauta/salvini/eremita', 'Charadrius leschenaultii', 'Thalassarche eremita', 'Psittacara mitratus/erythrogenys', 'Hydrobates hornbyi', 'Procellaria parkinsoni', 'Hydrobates tristrami', 'Centrocercus urophasianus/minimus', 'Geothlypis trichas x Setophaga petechia', 'Fregata ariel', 'Puffinus newelli', 'Vireo philadelphicus x olivaceus', 'Sayornis nigricans x saya', 'Procellaria aequinoctialis', 'Calidris tenuirostris x virgata', 'Nycticorax nycticorax x Nyctanassa violacea', 'Estrildidae sp.', 'Leucosticte australis', 'Geranoaetus polyosoma', 'Sayornis nigricans x phoebe', 'Setophaga citrina x petechia', 'Dryobates pubescens x villosus', 'Spizella pallida x breweri', 'Spatula clypeata x Mareca americana', 'Vireo gilvus x olivaceus', 'Cyanocitta stelleri x Aphelocoma woodhouseii', 'Contopus sordidulus x virens', 'Selasphorus rufus x platycercus', 'Megascops kennicottii x asio', 'Buteo jamaicensis x regalis', 'Tympanuchus cupido/pallidicinctus', 'Colinus virginianus x Callipepla squamata', 'Nannopterum auritum x brasilianum', 'Anas platyrhynchos x diazi/fulvigula', 'Melozone fusca x Pipilo maculatus', 'Geothlypis tolmiei x philadelphia', 'Archilochus colubris x alexandri', 'Pipilo chlorurus x maculatus', 'Camptorhynchus labradorius', 'Egretta caerulea x tricolor', 'Branta leucopsis x hutchinsii', 'Chlidonias hybrida', 'Irena puella', 'Argusianus argus', 'Coracias caudatus', 'Ramphocelus carbo', 'Gallicolumba tristigmata', 'Eurypyga helias', 'Pteroglossus viridis', 'Progne elegans', 'Progne cryptoleuca', 'Agelaius humeralis', 'Porphyrio poliocephalus', 'Chordeiles gundlachii', 'Tachornis phoenicobia', 'Nesophlox evelynae', 'Ephippiorhynchus asiaticus', 'Ara severus', 'Amazona amazonica', 'Eudocimus albus x ruber', 'Geotrygon chrysia', 'Psittacula cyanocephala', 'Myiarchus sagrae', 'Tachycineta cyaneoviridis', 'Amazona aestiva', 'Psittacara leucophthalmus', 'Melanospiza bicolor', 'Mimus gundlachii', 'Amazona ochrocephala', 'Vireo crassirostris', 'Streptopelia turtur', 'Aratinga weddellii', 'Contopus caribaeus', 'Dendrocygna viduata', 'Chroicocephalus cirrocephalus', 'Psittacara finschi', 'Sturnidae sp.', 'Pionus maximiliani', 'Psittacara wagleri', 'Brotogeris versicolurus x chiriri', 'Tyrannus caudifasciatus', 'Corvus splendens', 'Euplectes sp.', 'Ciconia episcopus', 'Ara ararauna x macao', 'Turdus plumbeus', 'Egretta thula x tricolor', 'Phonipara canora', 'Tyrannus melancholicus x dominicensis', 'Brotogeris sp.', 'Porphyrio sp. (swamphen sp.)', 'Vireo gundlachii', 'Hydrobates pelagicus', 'Ardea herodias x alba', 'Petrochelidon pyrrhonota x fulva', 'Geopelia cuneata', 'Sicalis flaveola', 'Erithacus rubecula', 'Coccyzus melacoryphus', 'Patagioenas squamosa', 'Egretta garzetta x thula', 'Setophaga cerulea x americana', 'Setophaga magnolia x palmarum', 'Anas platyrhynchos x zonorhyncha', 'Mimus gundlachii x polyglottos', 'Calonectris diomedea/edwardsii', 'Setophaga petechia x discolor', 'Branta sandvicensis', 'Zosterops japonicus', 'Geopelia striata', 'Fulica alai', 'Garrulax canorus', 'Copsychus malabaricus', 'Himatione sanguinea', 'Buteo solitarius', 'Chasiempis sandwichensis', 'Drepanis coccinea', 'Chlorodrepanis virens', 'Myadestes obscurus', 'Leiothrix lutea', 'Pycnonotus cafer', 'Magumma parva', 'Chasiempis sclateri', 'Chlorodrepanis stejnegeri', 'Lonchura atricapilla', 'Amandava amandava', 'Chasiempis ibidis', 'Anas wyvilliana', 'Zosteropidae sp.', 'Loxops caeruleirostris', 'Oreomystis bairdi', 'Myadestes myadestinus', 'Gallus gallus', 'Hemignathus wilsoni', 'Loxioides bailleui', 'Myadestes lanaiensis', 'Palmeria dolei', 'Paroreomyza montana', 'Pseudonestor xanthophrys', 'Anas platyrhynchos x wyvilliana', 'Moho braccatus', 'Psittirostra psittacea', 'Loxops coccineus', 'Loxops mana', 'Euodice cantans', 'Francolinus francolinus', 'Pternistis erckelii', 'Ortygornis pondicerianus', 'Horornis diphone', 'Aerodramus bartschi', 'Chlorodrepanis flava', 'Lophura leucomelanos', 'Glaucestrilda caerulescens', 'Paroaria capitata', 'Estrilda troglodytes', 'Pterorhinus pectoralis', 'Loxops ochraceus', 'Melamprosops phaeosoma', 'Onychoprion lunatus', 'Anas platyrhynchos/wyvilliana', 'Hemignathus hanapepe', 'Lonchura sp.', 'Pterodroma hypoleuca', 'Thalasseus bergii', 'Pterodroma nigripennis', 'Anous ceruleus', 'Pterocles exustus', 'Anas laysanensis', 'Telespiza cantans', 'Netta peposaca', 'Cacatua moluccensis', 'Lonchura molucca', 'Acrocephalus familiaris', 'Telespiza ultima', 'Cacatua alba', 'Phasianidae sp. (francolin sp.)', 'Pionus menstruus', 'Spatula querquedula/Anas crecca', 'Cacatua sp.', 'Cacatua goffiniana', 'Thalassarche sp.', 'Drepanidinae sp.', 'Pterodroma heraldica', 'Plegadis chihi/ridgwayi', 'Leiothrichidae sp. (laughingthrush sp.)', 'Acridotheres sp.', 'Zosterops sp.', 'Larosterna inca', 'Loxia curvirostra/sinesciuris', 'Loxia sinesciuris', 'Empidonax difficilis x occidentalis', 'Archilochus alexandri x Selasphorus calliope', 'Selasphorus calliope x rufus', 'Phaetusa simplex', 'Setophaga americana x dominica', 'Elaenia parvirostris', 'Elaenia parvirostris/albiceps', 'Passer sp.', 'Tympanuchus cupido x pallidicinctus', 'Empidonomus aurantioatrocristatus', 'Quiscalus major x mexicanus', 'Stelgidopteryx serripennis/ruficollis', 'Molothrus bonariensis/aeneus', 'Ammospiza nelsoni x caudacuta', 'Pterodroma arminjoniana', 'Anthropoides paradiseus', 'Cygnus buccinator x columbianus', 'Chroicocephalus novaehollandiae', 'Calonectris edwardsii', 'Pterodroma madeira/feae', 'Poicephalus senegalus', 'Calidris ferruginea x melanotos', 'Trugon terrestris', 'Falco vespertinus', 'Vermivora cyanoptera x Setophaga discolor', 'Euplectes albonotatus', 'Anas platyrhynchos x Aythya americana', 'Setophaga castanea x striata', 'Aythya baeri', 'Aythya nyroca/baeri', 'Sterna hirundo x paradisaea', 'Crithagra flaviventris', 'Passerellidae/Parulidae sp. (trilling song)', 'Rallus tenuirostris/elegans', 'Cygnus buccinator x cygnus', 'Setophaga ruticilla x americana', 'Zonotrichia leucophrys x querula', 'Limosa haemastica/fedoa', 'Foudia madagascariensis', 'Anas georgica', 'Spizella passerina/Helmitheros vermivorum', 'Alectoris rufa/graeca', 'Carpodacus sp.', 'Quiscalus quiscula x mexicanus', 'Setophaga coronata x nigrescens', 'Anas platyrhynchos x crecca', 'Loxia curvirostra x Spinus pinus', 'Tetraogallus himalayensis', 'Anser caerulescens x Branta bernicla', 'Corvus cornix', 'Rallus elegans x crepitans', 'Corvus albicollis', 'Setophaga coronata x dominica', 'Psittacula eupatria', 'Ara macao', 'Melanerpes aurifrons x carolinus', 'Junco hyemalis x phaeonotus', 'Porphyrio flavirostris', 'Tyrannus couchii x forficatus', 'Branta bernicla x hutchinsii', 'Melanitta perspicillata x deglandi', 'Melanitta nigra/americana', 'Vireo flavifrons x solitarius', 'Pterodroma madeira', 'Larus argentatus x glaucoides', 'Pterodroma arminjoniana/heraldica', 'Fregetta tropica', 'Cygnus melancoryphus', 'Anas erythrorhyncha', 'Afropavo congensis', 'Mareca penelope x Anas acuta', 'Elaenia albiceps', 'Scolopax rusticola', 'Baeolophus bicolor x atricristatus', 'Baeolophus bicolor/atricristatus', 'Pheucticus chrysogaster', 'Strix occidentalis x varia', 'Sialia mexicana x currucoides', 'Melanitta nigra', 'Strix occidentalis/varia', 'Selasphorus rufus x sasin', 'Spinus psaltria x tristis', 'Strix sp.', 'Agelastes meleagrides', 'Coscoroba coscoroba', 'Tadorna variegata', 'Pionites melanocephalus', 'Icterus gularis x graduacauda', 'Geothlypis poliocephala x trichas', 'Leiothlypis crissalis x virginiae', 'Buteo swainsoni x lagopus', 'Antigone canadensis x Grus americana', 'Dendrocygna arborea', 'Setophaga graciae x nigrescens', 'Dryobates pubescens x scalaris', 'Geothlypis trichas x Basileuterus rufifrons', 'Passerina cyanea x ciris', 'Calypte anna x Selasphorus sasin', 'Dendrocygna autumnalis x bicolor', 'Psittacula sp.', 'Amazona viridigenalis x autumnalis', 'Passerina versicolor x ciris', 'Toxostoma curvirostre x longirostre', 'Amazona viridigenalis x finschi', 'Pygochelidon cyanoleuca', 'Phoenicopterus roseus', 'Anas platyrhynchos x Netta rufina', 'Phrygilus/Idiopsar/Geospizopsis/Rhopospina sp.', 'Dendragapus obscurus x Tympanuchus phasianellus', 'Phoeniconaias minor', 'Selasphorus calliope x platycercus', 'Vidua chalybeata', 'Phoeniculus purpureus', 'Aptenodytes forsteri', 'Rhipidura cockerelli', 'Psittacula eques', 'Catharus fuscescens x bicknelli', 'Mustelirallus erythrops', 'Circus aeruginosus', 'Charadrius mongolus/leschenaultii', 'Cacatua sulphurea', 'Nothoprocta perdicaria', 'Poecile gambeli x hudsonicus', 'Melospiza melodia x georgiana', 'Lophura swinhoii', 'Geothlypis tolmiei x trichas', 'Tachycineta bicolor x thalassina', 'Stelgidopteryx serripennis x Tachycineta thalassina', 'Mimus longicaudatus', 'Aramides ypecaha', 'Spermestes bicolor', 'Recurvirostridae sp.', 'Ara militaris', 'Syrmaticus reevesii', 'Macronectes halli', 'Ploceus cucullatus', 'Eos bornea', 'Cygnus columbianus/cygnus', 'Lophodytes cucullatus x Mergus merganser', 'Anser rossii x albifrons']

#%% Real world state birds. Evaluate based on number of matches.
REALSTATEBIRDS = {
    'US-AL': 'Colaptes auratus',
    'US-AK': 'Lagopus lagopus',
    'US-AZ': 'Campylorhynchus brunneicapillus',
    'US-AR': 'Mimus polyglottos',
    'US-CA': 'Callipepla californica',
    'US-CO': 'Calamospiza melanocorys',
    'US-CT': 'Turdus migratorius',
    'US-DE': 'Gallus gallus',
    'US-DC': 'Hylocichla mustelina',
    'US-FL': 'Mimus polyglottos',
    'US-GA': 'Toxostoma rufum',
    'US-HI': 'Branta sandvicensis',
    'US-ID': 'Sialia currucoides',
    'US-IL': 'Cardinalis cardinalis',
    'US-IN': 'Cardinalis cardinalis',
    'US-IA': 'Spinus tristis',
    'US-KS': 'Sturnella neglecta',
    'US-KY': 'Cardinalis cardinalis',
    'US-LA': 'Pelecanus occidentalis',
    'US-ME': 'Poecile sp.',
    'US-MD': 'Icterus galbula',
    'US-MA': 'Poecile atricapillus', #atricapilla
    'US-MI': 'Turdus migratorius',
    'US-MN': 'Gavia immer',
    'US-MS': 'Mimus polyglottos',
    'US-MO': 'Sialia sialis',
    'US-MT': 'Sturnella neglecta',
    'US-NE': 'Sturnella neglecta',
    'US-NV': 'Sialia currucoides',
    'US-NH': 'Haemorhous purpureus', #Carpodacus purpureus
    'US-NJ': 'Spinus tristis',
    'US-NM': 'Geococcyx californianus',
    'US-NY': 'Sialia sialis',
    'US-NC': 'Cardinalis cardinalis',
    'US-ND': 'Sturnella neglecta',
    'US-OH': 'Cardinalis cardinalis',
    'US-OK': 'Tyrannus forficatus',
    'US-OR': 'Sturnella neglecta',
    'US-PA': 'Bonasa umbellus',
    'US-RI': 'Gallus gallus',
    'US-SC': 'Thryothorus ludovicianus',
    'US-SD': 'Phasianus colchicus',
    'US-TN': 'Mimus polyglottos',
    'US-TX': 'Mimus polyglottos',
    'US-UT': 'Larus californicus',
    'US-VT': 'Catharus guttatus',
    'US-VA': 'Cardinalis cardinalis',
    'US-WA': 'Spinus tristis',
    'US-WV': 'Cardinalis cardinalis',
    'US-WI': 'Turdus migratorius',
    'US-WY': 'Sturnella neglecta',}

REALSTATEBIRD_LIST = [bird.split(' ')[0] for bird in REALSTATEBIRDS.values()]+list(REALSTATEBIRDS.values())



#And there are some iconic birds it would be nice to have.
ICONICBIRDLIST = ['Cardinalis','Haliaeetus','Cyanocitta','Corvus',
                  'Selasphorus','Archilochus','Meleagris','Falco','Strix',]


#%% Common bird names 

''' Not in BBS (But Hawaii isn't in BBS, nor is Mexico)
Aethia Auklet
Zosterops White-Eyes
Cuculus Cuckoo
Tetraogallus Snowcock
Tadorna Shelduck
Pterodroma Gadfly Petrel
Oceanites Storm Petrel
Pagophila Ivory gull
Nannopterum Cormorant
'''


genus_commonname_map = {'': '',
    '': '',
    '': '',
    '': '',
    'Branta leucopsis': 'Barnacle Goose',
    'Fringilla montifringilla': 'Brambling',
    'Urile': 'Cormorant',
    'Urile urile': 'Violet Shag',
    'Spatula querquedula': 'Garganey',
    'Alle alle': 'Dovekie',
    'Agapornis': 'Lovebird',
    'Strix': 'Wood Owl',
    'Gavia': 'Loon',
    'Ardenna': 'Shearwater',
    'Alca': 'Razorbill',
    'Puffinus': 'Shearwater',
    'Aratinga': 'Conure',
    'Aethia' : 'Auklet' ,
    'Mimus' : 'Mockingbird' ,
    'Passerina' : 'Bunting' ,
    'Auriparus' : 'Verdin' ,
    'Chamaea' : 'Wrentit' ,
    'Pica' : 'Magpie' ,
    'Dumetella' : 'Gray Catbird' ,
    'Chaetura' : 'Swift' ,
    'Calidris' : 'Sandpiper' ,
    'Eudocimus' : 'Ibis' ,
    'Toxostoma' : 'Thrasher' ,
    'Zosterops' : 'White-Eyes' ,
    'Troglodytes' : 'House Wren' ,
    'Streptopelia' : 'Collared Dove' ,
    'Passer' : 'True Sparrow' ,
    'Centronyx' : 'Sparrow' ,
    'Sturnella' : 'Meadowlark' ,
    'Cathartes' : 'Turkey Vulture' ,
    'Bubulcus' : 'Cattle Egret' ,
    'Melanitta' : 'Scoter' ,
    'Coragyps' : 'Black Vulture' ,
    'Somateria' : 'Eider' ,
    'Cygnus' : 'Swan' ,
    'Dryobates' : 'Woodpecker' ,
    'Melanerpes' : 'Woodpecker' ,
    'Thalasseus' : 'Crested Tern' ,
    'Nucifraga' : 'Nutcracker' ,
    'Sialia' : 'Bluebird' ,
    'Tympanuchus' : 'Prarie Chicken' ,
    'Spiza' : 'Dickcissel' ,
    'Sitta' : 'Nuthatch' ,
    'Leucophaeus' : 'Gull' ,
    'Geococcyx' : 'Roadrunner' ,
    'Callipepla' : 'Crested Quail' ,
    'Larus' : 'Gull' ,
    'Cardinalis' : 'Cardinal' ,
    'Ictinia' : 'Mississippi Kite' ,
    'Aphelocoma' : 'Scrub Jay' ,
    'Baeolophus' : 'Titmouse' ,
    'Phalacrocorax' : 'Cormorant' ,
    'Mycteria' : 'Stork' ,
    'Bartramia' : 'Upland Sandpiper' ,
    'Pipilo' : 'Towhee' ,
    'Caracara' : 'Caracara' ,
    'Aechmophorus' : 'Grebe' ,
    'Thryothorus' : 'Carolina Wren' ,
    'Seiurus' : 'Ovenbird' ,
    'Calypte' : 'Hummingbird' ,
    'Antigone' : 'Crane' ,
    'Dryocopus' : 'Woodpecker' ,
    'Aquila' : 'True Eagle' ,
    'Lanius' : 'Shrike' ,
    'Corvus' : 'Crow' ,
    'Spatula' : 'Shoveler/Teal' ,
    'Acanthis' : 'Redpoll' ,
    'Acridotheres' : 'Myna' ,
    'Falco' : 'Falcon' ,
    'Spizella' : 'Sparrow' ,
    'Ardea' : 'Heron' ,
    'Pelecanus' : 'Pelican' ,
    'Xanthocephalus' : 'Yellow-headed Blackbird' ,
    'Catharus' : 'Nightingale-thrush' ,
    'Selasphorus' : 'Hummingbird' ,
    'Branta' : 'Black Goose' ,
    'Setophaga' : 'Warbler' ,
    'Tyrannus' : 'Kingbird/Flycatcher' ,
    'Anhinga' : 'Darter' ,
    'Morus' : 'Gannet' ,
    'Cyanocitta' : 'Blue Jay' ,
    'Buteo' : 'Hawk' ,
    'Poecile' : 'Chickadee' ,
    'Melospiza' : 'Song Sparrow' ,
    'Sturnus' : 'Starling' ,
    'Spinus' : 'Goldfinch' ,
    'Turdus' : 'Robin' ,
    'Zenaida' : 'Mourning Dove' ,
    'Centrocercus' : 'Sage-grouse' ,
    'Cerorhinca' : 'Rhinoceros Puffin' ,
    'Alectoris' : 'Rock Partridge' ,
    'Cuculus' : 'Cuckoo' ,
    'Hylocichla' : 'Wood Thrush' ,
    'Protonotaria' : 'Prothonotary warbler' ,
    'Tetraogallus' : 'Snowcock' ,
    'Haematopus' : 'Oystercatcher' ,
    'Tadorna' : 'Shelduck' ,
    'Pterodroma' : 'Gadfly Petrel' ,
    'Colinus' : 'Bobwhite' ,
    'Aix' : 'Wood Duck' ,
    'Calonectris' : 'Shearwater' ,
    'Artemisiospiza' : 'Sparrow' ,
    'Icteria' : 'Yellow-breasted Chat' ,
    'Oceanites' : 'Storm Petrel' ,
    'Pagophila' : 'Ivory gull' ,
    'Sayornis' : 'Phoebe' ,
    'Colaptes' : 'Woodpecker' ,
    'Tringa' : 'Tattlers' ,
    'Anas' : 'Mallard' ,
    'Haemorhous' : 'Rosefinch' ,
    'Quiscalus' : 'Grackle' ,
    'Vireo' : 'Vireo' ,
    'Junco' : 'Junco' ,
    'Agelaius' : 'Blackbird' ,
    'Tachycineta' : 'Swallow' ,
    'Columba' : 'Pigeon' ,
    'Zonotrichia' : 'Sparrow' ,
    'Charadrius' : 'Plover' ,
    'Aythya' : 'Diving Duck' ,
    'Haliaeetus' : 'Sea Eagle' ,
    'Bucephala' : 'Goldeneye' ,
    'Nannopterum' : 'Cormorant' ,
    'Molothrus' : 'Cowbird' ,
    'Pandion' : 'Osprey' ,
    'Icterus' : 'Oriole' ,
    'Egretta' : 'Egret' ,
    'Phasianus' : 'Pheasant' ,
    'Fratercula' : 'Puffin' ,
    'Rissa' : 'Kittiwake' ,
    'Oreoscoptes' : 'Sage Thrasher' ,
    'Sterna' : 'Tern' ,
    'Euphagus' : 'Blackbird' ,
    'Spizelloides' : 'Winter Sparrow' ,
    'Fulica' : 'Coot' ,
    'Anser' : 'Grey Goose' ,
    'Meleagris' : 'Turkey' ,
    'Pluvialis' : 'Plover' ,
    'Rhynchophanes' : 'Longspur' ,
    'Scolopax' : 'Woodcock' ,
    'Accipiter' : 'Quail Hawk' ,
    'Megascops' : 'Screech Owl' ,
    'Calcarius' : 'Longspur' ,
    'Oxyura' : 'Stiff-tailed Duck' ,
    'Certhia' : 'Treecreeper' ,
    'Calamospiza' : 'Lark Bunting' ,
    'Gymnorhinus' : 'Pinyon Jay' ,
    'Myiarchus' : 'Tyrant Flycatcher' ,
    'Podiceps' : 'Grebe' ,
    'Bonasa' : 'Ruffed Grouse' ,
    'Oporornis' : 'Connecticut Warbler' ,
    'Antrostomus' : 'Nightjar' ,
    'Coccyzus' : 'Cuckoo' ,
    'Bombycilla' : 'Waxwing' ,
    'Vermivora' : 'Warbler' ,
    'Polioptila' : 'Gnatcatcher' ,
    'Cepphus' : 'Guillemot' ,
    'Recurvirostra' : 'Avocet' ,
    'Perdix' : 'Partridge' ,
    'Cynanthus' : 'Hummingbird' ,
    'Himatione sanguinea' : 'Apapane' ,
    'Grus' : 'Crane' ,
    'Euplectes' : 'Bishop' ,
    'Carduelis' : 'Goldfinch' ,
    'Rynchops' : 'Skimmer' ,
    'Phainopepla' : 'Phainopepla' ,
    'Aethia psittacula' : 'Parakeet auklet' ,
    '' : '' ,
    '' : '' ,
    '' : '' ,
    }

#%% Wikipedia page redirects
wikipedia_mapping = {'Aix':'https://en.wikipedia.org/wiki/Aix_(bird)',
                    'Pica':'https://en.wikipedia.org/wiki/Pica_(genus)',
                    'Cygnus':'https://en.wikipedia.org/wiki/Swan',
                    'Troglodytes':'https://en.wikipedia.org/wiki/Troglodytes_(bird)',
                    'Aquila':'https://en.wikipedia.org/wiki/Aquila_(bird)',
                    'Antigone':'https://en.wikipedia.org/wiki/Antigone_(bird)',
                    'Caracara':'https://en.wikipedia.org/wiki/Caracara_(genus)',
                    'Bartramia':'https://en.wikipedia.org/wiki/Bartramia_(bird)',
                    'Spatula':'https://en.wikipedia.org/wiki/Spatula_(bird)',
                    'Acanthis':'https://en.wikipedia.org/wiki/Redpoll',
                    'Falco':'https://en.wikipedia.org/wiki/Falcon',
                    'Ardea':'https://en.wikipedia.org/wiki/Ardea_(bird)',
                    'Morus':'https://en.wikipedia.org/wiki/Gannet',
                    'Spinus':'https://en.wikipedia.org/wiki/Spinus_(bird)',
                    'Zenaida':'https://en.wikipedia.org/wiki/Zenaida_doves',
                    'Columba':'https://en.wikipedia.org/wiki/Columba_(bird)',
                    'Bucephala':'https://en.wikipedia.org/wiki/Goldeneye_(duck)',
                    'Pandion':'https://en.wikipedia.org/wiki/Pandion_(bird)',
                    'Icterus':'https://en.wikipedia.org/wiki/New_World_oriole',
                    'Rissa':'https://en.wikipedia.org/wiki/Kittiwake',
                    'Fulica':'https://en.wikipedia.org/wiki/Coot',
                    'Grus':'https://en.wikipedia.org/wiki/Grus_(genus)',
                    'Gavia':'https://en.wikipedia.org/wiki/Loon',
                    'Strix':'https://en.wikipedia.org/wiki/Strix_(bird)',
                    'Dryobates arizonae':'https://en.wikipedia.org/wiki/Arizona_woodpecker',
                    '':'',
                    '':'',
                    '':'',
                    '':'',
                    '':'',
                    '':'',}


#%% BBS Common names

BBS_commonname_map = {'Dendrocygna autumnalis': 'Black-bellied Whistling-Duck',
    'Dendrocygna bicolor': 'Fulvous Whistling-Duck',
    'Anser canagicus': 'Emperor Goose',
    'Anser caerulescens': 'Snow Goose',
    'Anser caerulescens (blue form)': '(Blue Goose) Snow Goose',
    'Anser rossii': "Ross's Goose",
    'Anser albifrons': 'Greater White-fronted Goose',
    'Branta bernicla': 'Brant',
    'Branta bernicla nigricans': '(Black Brant) Brant',
    'Branta hutchinsii': 'Cackling Goose',
    'Branta canadensis': 'Canada Goose',
    'Cygnus olor': 'Mute Swan',
    'Cygnus buccinator': 'Trumpeter Swan',
    'Cygnus columbianus': 'Tundra Swan',
    'Alopochen aegyptiaca': 'Egyptian Goose',
    'Cairina moschata': 'Muscovy Duck',
    'Aix sponsa': 'Wood Duck',
    'Spatula discors': 'Blue-winged Teal',
    'Spatula cyanoptera': 'Cinnamon Teal',
    'Spatula clypeata': 'Northern Shoveler',
    'Mareca strepera': 'Gadwall',
    'Mareca penelope': 'Eurasian Wigeon',
    'Mareca americana': 'American Wigeon',
    'Anas platyrhynchos': 'Mallard',
    'Anas platyrhynchos diazi': '(Mexican Duck) Mallard',
    'Anas rubripes': 'American Black Duck',
    'Anas fulvigula': 'Mottled Duck',
    'Anas platyrhynchos x rubripes or fulvigula': 'hybrid Mallard x Black Duck or Mottled Duck',
    'Anas acuta': 'Northern Pintail',
    'Anas crecca': 'Green-winged Teal',
    'Aythya valisineria': 'Canvasback',
    'Aythya americana': 'Redhead',
    'Aythya collaris': 'Ring-necked Duck',
    'Aythya fuligula': 'Tufted Duck',
    'Aythya marila': 'Greater Scaup',
    'Aythya affinis': 'Lesser Scaup',
    'Aythya marila / affinis': 'unid. Greater Scaup / Lesser Scaup',
    'Somateria spectabilis': 'King Eider',
    'Somateria mollissima': 'Common Eider',
    'Histrionicus histrionicus': 'Harlequin Duck',
    'Melanitta perspicillata': 'Surf Scoter',
    'Melanitta deglandi': 'White-winged Scoter',
    'Melanitta americana': 'Black Scoter',
    'Melanitta sp.': 'unid. scoter',
    'Clangula hyemalis': 'Long-tailed Duck',
    'Bucephala albeola': 'Bufflehead',
    'Bucephala clangula': 'Common Goldeneye',
    'Bucephala islandica': "Barrow's Goldeneye",
    'Bucephala clangula / islandica': "unid. Common Goldeneye / Barrow's Goldeneye",
    'Lophodytes cucullatus': 'Hooded Merganser',
    'Mergus merganser': 'Common Merganser',
    'Mergus serrator': 'Red-breasted Merganser',
    'Oxyura jamaicensis': 'Ruddy Duck',
    'Ortalis vetula': 'Plain Chachalaca',
    'Oreortyx pictus': 'Mountain Quail',
    'Colinus virginianus': 'Northern Bobwhite',
    'Callipepla squamata': 'Scaled Quail',
    'Callipepla californica': 'California Quail',
    'Callipepla gambelii': "Gambel's Quail",
    'Cyrtonyx montezumae': 'Montezuma Quail',
    'Alectoris chukar': 'Chukar',
    'Perdix perdix': 'Gray Partridge',
    'Phasianus colchicus': 'Ring-necked Pheasant',
    'Pavo cristatus': 'Indian Peafowl',
    'Bonasa umbellus': 'Ruffed Grouse',
    'Centrocercus urophasianus': 'Greater Sage-Grouse',
    'Centrocercus minimus': 'Gunnison Sage-Grouse',
    'Falcipennis canadensis': 'Spruce Grouse',
    'Lagopus lagopus': 'Willow Ptarmigan',
    'Lagopus muta': 'Rock Ptarmigan',
    'Lagopus leucura': 'White-tailed Ptarmigan',
    'Dendragapus obscurus': 'Dusky Grouse',
    'Dendragapus fuliginosus': 'Sooty Grouse',
    'Dendragapus obscurus / fuliginosus': 'unid. Dusky Grouse / Sooty Grouse',
    'Tympanuchus phasianellus': 'Sharp-tailed Grouse',
    'Tympanuchus cupido': 'Greater Prairie-Chicken',
    'Tympanuchus pallidicinctus': 'Lesser Prairie-Chicken',
    'Meleagris gallopavo': 'Wild Turkey',
    'Tachybaptus dominicus': 'Least Grebe',
    'Podilymbus podiceps': 'Pied-billed Grebe',
    'Podiceps auritus': 'Horned Grebe',
    'Podiceps grisegena': 'Red-necked Grebe',
    'Podiceps nigricollis': 'Eared Grebe',
    'Aechmophorus occidentalis': 'Western Grebe',
    'Aechmophorus clarkii': "Clark's Grebe",
    'Aechmophorus occidentalis / clarkii': "unid. Western Grebe / Clark's Grebe",
    'Columba livia': 'Rock Pigeon',
    'Patagioenas leucocephala': 'White-crowned Pigeon',
    'Patagioenas flavirostris': 'Red-billed Pigeon',
    'Patagioenas fasciata': 'Band-tailed Pigeon',
    'Streptopelia roseogrisea': 'African Collared-Dove (a.k.a. Ringed Turtle-Dove)',
    'Streptopelia decaocto': 'Eurasian Collared-Dove',
    'Streptopelia chinensis': 'Spotted Dove',
    'Columbina inca': 'Inca Dove',
    'Columbina passerina': 'Common Ground Dove',
    'Columbina talpacoti': 'Ruddy Ground Dove',
    'Leptotila verreauxi': 'White-tipped Dove',
    'Zenaida asiatica': 'White-winged Dove',
    'Zenaida macroura': 'Mourning Dove',
    'Crotophaga ani': 'Smooth-billed Ani',
    'Crotophaga sulcirostris': 'Groove-billed Ani',
    'Geococcyx californianus': 'Greater Roadrunner',
    'Coccyzus americanus': 'Yellow-billed Cuckoo',
    'Coccyzus minor': 'Mangrove Cuckoo',
    'Coccyzus erythropthalmus': 'Black-billed Cuckoo',
    'Coccyzus americanus / erythropthalmus': 'unid. Yellow-billed Cuckoo / Black-billed Cuckoo',
    'Chordeiles acutipennis': 'Lesser Nighthawk',
    'Chordeiles minor': 'Common Nighthawk',
    'Chordeiles gundlachii': 'Antillean Nighthawk',
    'Chordeiles acutipennis / minor': 'unid. Lesser Nighthawk / Common Nighthawk',
    'Chordeiles minor / gundlachii': 'unid. Common Nighthawk / Antillean Nighthawk',
    'Nyctidromus albicollis': 'Common Pauraque',
    'Phalaenoptilus nuttallii': 'Common Poorwill',
    'Antrostomus carolinensis': "Chuck-will's-widow",
    'Antrostomus vociferus': 'Eastern Whip-poor-will',
    'Antrostomus arizonae': 'Mexican Whip-poor-will',
    'Cypseloides niger': 'Black Swift',
    'Chaetura pelagica': 'Chimney Swift',
    'Chaetura vauxi': "Vaux's Swift",
    'Aeronautes saxatalis': 'White-throated Swift',
    'Eugenes fulgens': "Rivoli's Hummingbird",
    'Lampornis clemenciae': 'Blue-throated Mountain-gem',
    'Calothorax lucifer': 'Lucifer Hummingbird',
    'Archilochus colubris': 'Ruby-throated Hummingbird',
    'Archilochus alexandri': 'Black-chinned Hummingbird',
    'Archilochus colubris / alexandri': 'unid. Ruby-throated / Black-chinned Hummingbird',
    'Calypte anna': "Anna's Hummingbird",
    'Calypte costae': "Costa's Hummingbird",
    'Selasphorus platycercus': 'Broad-tailed Hummingbird',
    'Selasphorus rufus': 'Rufous Hummingbird',
    'Selasphorus sasin': "Allen's Hummingbird",
    'Selasphorus rufus / sasin': "unid. Rufous Hummingbird / Allen's Hummingbird",
    'Trochilid sp.': 'unid. hummingbird',
    'Selasphorus calliope': 'Calliope Hummingbird',
    'Cynanthus latirostris': 'Broad-billed Hummingbird',
    'Amazilia yucatanensis': 'Buff-bellied Hummingbird',
    'Amazilia violiceps': 'Violet-crowned Hummingbird',
    'Coturnicops noveboracensis': 'Yellow Rail',
    'Laterallus jamaicensis': 'Black Rail',
    'Rallus obsoletus': "Ridgway's Rail",
    'Rallus crepitans': 'Clapper Rail',
    'Rallus elegans': 'King Rail',
    'Rallus crepitans / elegans': 'unid. Clapper / King Rail',
    'Rallus limicola': 'Virginia Rail',
    'Porzana carolina': 'Sora',
    'Porphyrio martinicus': 'Purple Gallinule',
    'Porphyrio porphyrio': 'Purple Swamphen',
    'Gallinula galeata': 'Common Gallinule',
    'Fulica americana': 'American Coot',
    'Aramus guarauna': 'Limpkin',
    'Antigone canadensis': 'Sandhill Crane',
    'Grus americana': 'Whooping Crane',
    'Himantopus mexicanus': 'Black-necked Stilt',
    'Recurvirostra americana': 'American Avocet',
    'Haematopus palliatus': 'American Oystercatcher',
    'Haematopus bachmani': 'Black Oystercatcher',
    'Pluvialis squatarola': 'Black-bellied Plover',
    'Pluvialis dominica': 'American Golden-Plover',
    'Pluvialis fulva': 'Pacific Golden-Plover',
    'Charadrius vociferus': 'Killdeer',
    'Charadrius hiaticula': 'Common Ringed Plover',
    'Charadrius semipalmatus': 'Semipalmated Plover',
    'Charadrius melodus': 'Piping Plover',
    'Charadrius wilsonia': "Wilson's Plover",
    'Charadrius montanus': 'Mountain Plover',
    'Charadrius nivosus': 'Snowy Plover',
    'Bartramia longicauda': 'Upland Sandpiper',
    'Numenius tahitiensis': 'Bristle-thighed Curlew',
    'Numenius phaeopus': 'Whimbrel',
    'Numenius americanus': 'Long-billed Curlew',
    'Limosa lapponica': 'Bar-tailed Godwit',
    'Limosa haemastica': 'Hudsonian Godwit',
    'Limosa fedoa': 'Marbled Godwit',
    'Arenaria interpres': 'Ruddy Turnstone',
    'Arenaria melanocephala': 'Black Turnstone',
    'Calidris canutus': 'Red Knot',
    'Calidris virgata': 'Surfbird',
    'Calidris pugnax': 'Ruff',
    'Calidris acuminata': 'Sharp-tailed Sandpiper',
    'Calidris himantopus': 'Stilt Sandpiper',
    'Calidris ruficollis': 'Red-necked Stint',
    'Calidris alba': 'Sanderling',
    'Calidris alpina': 'Dunlin',
    'Calidris ptilocnemis': 'Rock Sandpiper',
    'Calidris maritima': 'Purple Sandpiper',
    'Calidris bairdii': "Baird's Sandpiper",
    'Calidris minutilla': 'Least Sandpiper',
    'Calidris fuscicollis': 'White-rumped Sandpiper',
    'Calidris subruficollis': 'Buff-breasted Sandpiper',
    'Calidris melanotos': 'Pectoral Sandpiper',
    'Calidris pusilla': 'Semipalmated Sandpiper',
    'Calidris mauri': 'Western Sandpiper',
    'Calidris sp.': "unid. small ''peep'' sandpiper",
    'Limnodromus griseus': 'Short-billed Dowitcher',
    'Limnodromus scolopaceus': 'Long-billed Dowitcher',
    'Limnodromus griseus / scolopaceus': 'unid. Short-billed / Long-billed Dowitcher',
    'Scolopax minor': 'American Woodcock',
    'Gallinago delicata': "Wilson's Snipe",
    'Actitis hypoleucos': 'Common Sandpiper',
    'Actitis macularius': 'Spotted Sandpiper',
    'Tringa solitaria': 'Solitary Sandpiper',
    'Tringa incana': 'Wandering Tattler',
    'Tringa flavipes': 'Lesser Yellowlegs',
    'Tringa melanoleuca / flavipes': 'unid. Greater Yellowlegs / Lesser Yellowlegs',
    'Tringa semipalmata': 'Willet',
    'Tringa nebularia': 'Common Greenshank',
    'Tringa melanoleuca': 'Greater Yellowlegs',
    'Phalaropus tricolor': "Wilson's Phalarope",
    'Phalaropus lobatus': 'Red-necked Phalarope',
    'Stercorarius pomarinus': 'Pomarine Jaeger',
    'Stercorarius parasiticus': 'Parasitic Jaeger',
    'Stercorarius longicaudus': 'Long-tailed Jaeger',
    'Uria aalge': 'Common Murre',
    'Uria lomvia': 'Thick-billed Murre',
    'Uria aalge / lomvia': 'unid. Common Murre / Thick-billed Murre',
    'Alca torda': 'Razorbill',
    'Cepphus grylle': 'Black Guillemot',
    'Cepphus columba': 'Pigeon Guillemot',
    'Brachyramphus marmoratus': 'Marbled Murrelet',
    'Brachyramphus brevirostris': "Kittlitz's Murrelet",
    'Synthliboramphus antiquus': 'Ancient Murrelet',
    'Ptychoramphus aleuticus': "Cassin's Auklet",
    'Cerorhinca monocerata': 'Rhinoceros Auklet',
    'Fratercula corniculata': 'Horned Puffin',
    'Fratercula cirrhata': 'Tufted Puffin',
    'Rissa tridactyla': 'Black-legged Kittiwake',
    'Xema sabini': "Sabine's Gull",
    'Chroicocephalus philadelphia': "Bonaparte's Gull",
    'Chroicocephalus ridibundus': 'Black-headed Gull',
    'Hydrocoloeus minutus': 'Little Gull',
    'Rhodostethia rosea': "Ross's Gull",
    'Leucophaeus atricilla': 'Laughing Gull',
    'Leucophaeus pipixcan': "Franklin's Gull",
    'Larus heermanni': "Heermann's Gull",
    'Larus canus': 'Mew Gull',
    'Larus delawarensis': 'Ring-billed Gull',
    'Larus occidentalis': 'Western Gull',
    'Larus californicus': 'California Gull',
    'Larus argentatus': 'Herring Gull',
    'Larus glaucoides': 'Iceland Gull',
    'Larus fuscus': 'Lesser Black-backed Gull',
    'Larus schistisagus': 'Slaty-backed Gull',
    'Larus glaucescens': 'Glaucous-winged Gull',
    'Larus occidentalis x glaucescens': 'hybrid Western Gull x Glaucous-winged Gull',
    'Larus hyperboreus': 'Glaucous Gull',
    'Larus marinus': 'Great Black-backed Gull',
    'Gull sp.': 'unid. gull',
    'Onychoprion aleuticus': 'Aleutian Tern',
    'Sternula antillarum': 'Least Tern',
    'Gelochelidon nilotica': 'Gull-billed Tern',
    'Hydroprogne caspia': 'Caspian Tern',
    'Chlidonias niger': 'Black Tern',
    'Sterna dougallii': 'Roseate Tern',
    'Sterna hirundo': 'Common Tern',
    'Sterna paradisaea': 'Arctic Tern',
    'Sterna forsteri': "Forster's Tern",
    'Thalasseus maximus': 'Royal Tern',
    'Thalasseus sandvicensis': 'Sandwich Tern',
    'Thalasseus elegans': 'Elegant Tern',
    'Tern sp.': 'unid. tern',
    'Rynchops niger': 'Black Skimmer',
    'Gavia stellata': 'Red-throated Loon',
    'Gavia arctica': 'Arctic Loon',
    'Gavia pacifica': 'Pacific Loon',
    'Gavia immer': 'Common Loon',
    'Gavia adamsii': 'Yellow-billed Loon',
    'Gavia sp.': 'unid. loon',
    'Hydrobates leucorhous': "Leach's Storm-Petrel",
    'Fulmarus glacialis': 'Northern Fulmar',
    'Calonectris diomedea': "Cory's Shearwater",
    'Puffinus puffinus': 'Manx Shearwater',
    'Mycteria americana': 'Wood Stork',
    'Fregata magnificens': 'Magnificent Frigatebird',
    'Sula dactylatra': 'Masked Booby',
    'Sula nebouxii': 'Blue-footed Booby',
    'Sula leucogaster': 'Brown Booby',
    'Morus bassanus': 'Northern Gannet',
    'Phalacrocorax penicillatus': "Brandt's Cormorant",
    'Phalacrocorax brasilianus': 'Neotropic Cormorant',
    'Phalacrocorax auritus': 'Double-crested Cormorant',
    'Phalacrocorax brasilianus / auritus': 'unid. Neotropic / Double-crested Cormorant',
    'Phalacrocorax carbo': 'Great Cormorant',
    'Phalacrocorax auritus / carbo': 'unid. Double-crested Cormorant / Great Cormorant',
    'Phalacrocorax pelagicus': 'Pelagic Cormorant',
    'Phalacrocorax sp.': 'unid. west coast cormorant',
    'Anhinga anhinga': 'Anhinga',
    'Pelecanus erythrorhynchos': 'American White Pelican',
    'Pelecanus occidentalis': 'Brown Pelican',
    'Botaurus lentiginosus': 'American Bittern',
    'Ixobrychus exilis': 'Least Bittern',
    'Ardea herodias': 'Great Blue Heron',
    'Ardea herodias occidentalis': '(Great White Heron) Great Blue Heron',
    'Ardea alba': 'Great Egret',
    'Egretta garzetta': 'Little Egret',
    'Egretta thula': 'Snowy Egret',
    'Egretta caerulea': 'Little Blue Heron',
    'Egretta tricolor': 'Tricolored Heron',
    'Egretta rufescens': 'Reddish Egret',
    'Bubulcus ibis': 'Cattle Egret',
    'Butorides virescens': 'Green Heron',
    'Nycticorax nycticorax': 'Black-crowned Night-Heron',
    'Nyctanassa violacea': 'Yellow-crowned Night-Heron',
    'Nycticorax / Nyctanassa nycticorax / violacea': 'unid Black-crowned / Yellow-crowned Night-Heron',
    'Ardeid sp.': 'unid. heron / egret',
    'Eudocimus albus': 'White Ibis',
    'Plegadis falcinellus': 'Glossy Ibis',
    'Plegadis chihi': 'White-faced Ibis',
    'Plegadis falcinellus / chihi': 'unid. Glossy Ibis / White-faced Ibis',
    'Platalea ajaja': 'Roseate Spoonbill',
    'Coragyps atratus': 'Black Vulture',
    'Cathartes aura': 'Turkey Vulture',
    'Coragyps / Cathartes atratus / aura': 'unid. Black Vulture / Turkey Vulture',
    'Gymnogyps californianus': 'California Condor',
    'Pandion haliaetus': 'Osprey',
    'Elanus leucurus': 'White-tailed Kite',
    'Chondrohierax uncinatus': 'Hook-billed Kite',
    'Elanoides forficatus': 'Swallow-tailed Kite',
    'Aquila chrysaetos': 'Golden Eagle',
    'Circus hudsonius': 'Northern Harrier',
    'Accipiter striatus': 'Sharp-shinned Hawk',
    'Accipiter cooperii': "Cooper's Hawk",
    'Accipiter gentilis': 'Northern Goshawk',
    'Accipiter sp.': 'unid. Accipiter hawk',
    'Haliaeetus leucocephalus': 'Bald Eagle',
    'Ictinia mississippiensis': 'Mississippi Kite',
    'Rostrhamus sociabilis': 'Snail Kite',
    'Buteogallus anthracinus': 'Common Black Hawk',
    'Parabuteo unicinctus': "Harris's Hawk",
    'Geranoaetus albicaudatus': 'White-tailed Hawk',
    'Buteo plagiatus': 'Gray Hawk',
    'Buteo lineatus': 'Red-shouldered Hawk',
    'Buteo platypterus': 'Broad-winged Hawk',
    'Buteo brachyurus': 'Short-tailed Hawk',
    'Buteo swainsoni': "Swainson's Hawk",
    'Buteo albonotatus': 'Zone-tailed Hawk',
    'Buteo jamaicensis': 'Red-tailed Hawk',
    'Buteo jamaicensis harlani': "(Harlan's Hawk) Red-tailed Hawk",
    'Buteo lagopus': 'Rough-legged Hawk',
    'Buteo regalis': 'Ferruginous Hawk',
    'Buteo sp.': 'unid. Buteo hawk',
    'Tyto alba': 'Barn Owl',
    'Psiloscops flammeolus': 'Flammulated Owl',
    'Megascops kennicottii': 'Western Screech-Owl',
    'Megascops asio': 'Eastern Screech-Owl',
    'Megascops trichopsis': 'Whiskered Screech-Owl',
    'Bubo virginianus': 'Great Horned Owl',
    'Bubo scandiacus': 'Snowy Owl',
    'Surnia ulula': 'Northern Hawk Owl',
    'Glaucidium gnoma': 'Northern Pygmy-Owl',
    'Glaucidium brasilianum': 'Ferruginous Pygmy-Owl',
    'Micrathene whitneyi': 'Elf Owl',
    'Athene cunicularia': 'Burrowing Owl',
    'Strix occidentalis': 'Spotted Owl',
    'Strix varia': 'Barred Owl',
    'Strix nebulosa': 'Great Gray Owl',
    'Asio otus': 'Long-eared Owl',
    'Asio flammeus': 'Short-eared Owl',
    'Aegolius funereus': 'Boreal Owl',
    'Aegolius acadicus': 'Northern Saw-whet Owl',
    'Trogon elegans': 'Elegant Trogon',
    'Megaceryle torquata': 'Ringed Kingfisher',
    'Megaceryle alcyon': 'Belted Kingfisher',
    'Chloroceryle americana': 'Green Kingfisher',
    'Melanerpes lewis': "Lewis's Woodpecker",
    'Melanerpes erythrocephalus': 'Red-headed Woodpecker',
    'Melanerpes formicivorus': 'Acorn Woodpecker',
    'Melanerpes uropygialis': 'Gila Woodpecker',
    'Melanerpes aurifrons': 'Golden-fronted Woodpecker',
    'Melanerpes carolinus': 'Red-bellied Woodpecker',
    'Sphyrapicus thyroideus': "Williamson's Sapsucker",
    'Sphyrapicus varius': 'Yellow-bellied Sapsucker',
    'Sphyrapicus nuchalis': 'Red-naped Sapsucker',
    'Sphyrapicus ruber': 'Red-breasted Sapsucker',
    'Sphyrapicus sp.': 'unid. sapsucker',
    'Picoides dorsalis': 'American Three-toed Woodpecker',
    'Picoides arcticus': 'Black-backed Woodpecker',
    'Dryobates pubescens': 'Downy Woodpecker',
    'Dryobates nuttallii': "Nuttall's Woodpecker",
    'Dryobates scalaris': 'Ladder-backed Woodpecker',
    'Dryobates borealis': 'Red-cockaded Woodpecker',
    'Dryobates villosus': 'Hairy Woodpecker',
    'Dryobates albolarvatus': 'White-headed Woodpecker',
    'Dryobates arizonae': 'Arizona Woodpecker',
    'Colaptes auratus': '(unid. Red/Yellow Shafted) Northern Flicker',
    'Colaptes auratus auratus': '(Yellow-shafted Flicker) Northern Flicker',
    'Colaptes auratus cafer': '(Red-shafted Flicker) Northern Flicker',
    'Colaptes auratus auratus x auratus cafer': 'hybrid Northern Flicker (Red x Yellow-shafted)',
    'Colaptes chrysoides': 'Gilded Flicker',
    'Dryocopus pileatus': 'Pileated Woodpecker',
    'Woodpecker sp.': 'unid. woodpecker',
    'Caracara cheriway': 'Crested Caracara',
    'Falco sparverius': 'American Kestrel',
    'Falco columbarius': 'Merlin',
    'Falco femoralis': 'Aplomado Falcon',
    'Falco rusticolus': 'Gyrfalcon',
    'Falco peregrinus': 'Peregrine Falcon',
    'Falco mexicanus': 'Prairie Falcon',
    'Myiopsitta monachus': 'Monk Parakeet',
    'Aratinga nenday': 'Nanday Parakeet',
    'Brotogeris chiriri': 'Yellow-chevroned Parakeet',
    'Brotogeris versicolurus / chiriri': 'unid. White-winged / Yellow-chevroned Parakeet',
    'Amazona viridigenalis': 'Red-crowned Parrot',
    'Psittacula krameri': 'Rose-ringed Parakeet',
    'Melopsittacus undulatus': 'Budgerigar',
    'Pachyramphus aglaiae': 'Rose-throated Becard',
    'Camptostoma imberbe': 'Northern Beardless-Tyrannulet',
    'Myiarchus tuberculifer': 'Dusky-capped Flycatcher',
    'Myiarchus cinerascens': 'Ash-throated Flycatcher',
    'Myiarchus crinitus': 'Great Crested Flycatcher',
    'Myiarchus tyrannulus': 'Brown-crested Flycatcher',
    'Pitangus sulphuratus': 'Great Kiskadee',
    'Myiodynastes luteiventris': 'Sulphur-bellied Flycatcher',
    'Tyrannus melancholicus': 'Tropical Kingbird',
    'Tyrannus couchii': "Couch's Kingbird",
    'Tyrannus melancholicus / couchii': "unid. Tropical Kingbird / Couch's Kingbird",
    'Tyrannus vociferans': "Cassin's Kingbird",
    'Tyrannus crassirostris': 'Thick-billed Kingbird',
    'Tyrannus verticalis': 'Western Kingbird',
    'Tyrannus vociferans / verticalis': "unid. Cassin's Kingbird / Western Kingbird",
    'Tyrannus tyrannus': 'Eastern Kingbird',
    'Tyrannus dominicensis': 'Gray Kingbird',
    'Tyrannus forficatus': 'Scissor-tailed Flycatcher',
    'Tyrannus savana': 'Fork-tailed Flycatcher',
    'Contopus cooperi': 'Olive-sided Flycatcher',
    'Contopus pertinax': 'Greater Pewee',
    'Contopus sordidulus': 'Western Wood-Pewee',
    'Contopus virens': 'Eastern Wood-Pewee',
    'Empidonax flaviventris': 'Yellow-bellied Flycatcher',
    'Empidonax virescens': 'Acadian Flycatcher',
    'Empidonax alnorum': 'Alder Flycatcher',
    'Empidonax traillii': 'Willow Flycatcher',
    'Empidonax alnorum / traillii': 'unid. Alder Flycatcher / Willow Flycatcher',
    'Empidonax minimus': 'Least Flycatcher',
    'Empidonax hammondii': "Hammond's Flycatcher",
    'Empidonax wrightii': 'Gray Flycatcher',
    'Empidonax oberholseri': 'Dusky Flycatcher',
    'Empidonax hammondii / oberholseri': "unid. Hammond's Flycatcher / Dusky Flycatcher",
    'Empidonax difficilis': 'Pacific-slope Flycatcher',
    'Empidonax occidentalis': 'Cordilleran Flycatcher',
    'Empidonax difficilis / occidentalis': 'unid. Cordilleran / Pacific-slope Flycatcher',
    'Empidonax fulvifrons': 'Buff-breasted Flycatcher',
    'Empidonax sp.': 'unid. Empidonax flycatcher',
    'Sayornis nigricans': 'Black Phoebe',
    'Sayornis phoebe': 'Eastern Phoebe',
    'Sayornis saya': "Say's Phoebe",
    'Pyrocephalus rubinus': 'Vermilion Flycatcher',
    'Lanius ludovicianus': 'Loggerhead Shrike',
    'Lanius borealis': 'Northern Shrike',
    'Vireo atricapilla': 'Black-capped Vireo',
    'Vireo griseus': 'White-eyed Vireo',
    'Vireo bellii': "Bell's Vireo",
    'Vireo vicinior': 'Gray Vireo',
    'Vireo huttoni': "Hutton's Vireo",
    'Vireo flavifrons': 'Yellow-throated Vireo',
    'Vireo cassinii': "Cassin's Vireo",
    'Vireo solitarius': 'Blue-headed Vireo',
    'Vireo cassinii / solitarius': "unid. Cassin's Vireo / Blue-headed Vireo",
    'Vireo plumbeus': 'Plumbeous Vireo',
    'Vireo plumbeus / cassinii': "unid. Plumbeous Vireo / Cassin's Vireo",
    'Vireo philadelphicus': 'Philadelphia Vireo',
    'Vireo gilvus': 'Warbling Vireo',
    'Vireo olivaceus': 'Red-eyed Vireo',
    'Vireo altiloquus': 'Black-whiskered Vireo',
    'Perisoreus canadensis': 'Canada Jay',
    'Cyanocorax yncas': 'Green Jay',
    'Gymnorhinus cyanocephalus': 'Pinyon Jay',
    'Cyanocitta stelleri': "Steller's Jay",
    'Cyanocitta cristata': 'Blue Jay',
    'Aphelocoma coerulescens': 'Florida Scrub-Jay',
    'Aphelocoma insularis': 'Island Scrub-Jay',
    'Aphelocoma californica': 'California Scrub-Jay',
    'Aphelocoma woodhouseii': "Woodhouse's Scrub-Jay",
    'Aphelocoma californica / woodhouseii': "unid. California Scrub-Jay / Woodhouse's Scrub-Jay",
    'Aphelocoma wollweberi': 'Mexican Jay',
    'Nucifraga columbiana': "Clark's Nutcracker",
    'Pica hudsonia': 'Black-billed Magpie',
    'Pica nuttalli': 'Yellow-billed Magpie',
    'Corvus brachyrhynchos': 'American Crow',
    'Corvus caurinus': 'Northwestern Crow',
    'Corvus ossifragus': 'Fish Crow',
    'Corvus brachyrhynchos / ossifragus': 'unid. American Crow / Fish Crow',
    'Corvus brachyrhynchos / caurinus': 'unid. American Crow / Northwestern Crow',
    'Corvus cryptoleucus': 'Chihuahuan Raven',
    'Corvus corax': 'Common Raven',
    'Corvus cryptoleucus / corax': 'unid. Chihuahuan Raven / Common Raven',
    'Alauda arvensis': 'Eurasian Skylark',
    'Eremophila alpestris': 'Horned Lark',
    'Riparia riparia': 'Bank Swallow',
    'Tachycineta bicolor': 'Tree Swallow',
    'Tachycineta thalassina': 'Violet-green Swallow',
    'Stelgidopteryx serripennis': 'Northern Rough-winged Swallow',
    'Progne subis': 'Purple Martin',
    'Hirundo rustica': 'Barn Swallow',
    'Petrochelidon pyrrhonota': 'Cliff Swallow',
    'Petrochelidon fulva': 'Cave Swallow',
    'Petrochelidon pyrrhonota / fulva': 'unid. Cave Swallow / Cliff Swallow',
    'Poecile carolinensis': 'Carolina Chickadee',
    'Poecile atricapillus': 'Black-capped Chickadee',
    'Poecile gambeli': 'Mountain Chickadee',
    'Poecile sclateri': 'Mexican Chickadee',
    'Poecile rufescens': 'Chestnut-backed Chickadee',
    'Poecile hudsonicus': 'Boreal Chickadee',
    'Poecile carolinensis / atricapillus': 'unid. Carolina Chickadee / Black-capped Chickadee',
    'Poecile atricapillus / gambeli': 'unid. Black-capped Chickadee / Mountain Chickadee',
    'Poecile atricapillus / hudsonicus': 'unid. Black-capped Chickadee / Boreal Chickadee',
    'Poecile sp.': 'unid. western chickadee species',
    'Baeolophus wollweberi': 'Bridled Titmouse',
    'Baeolophus inornatus': 'Oak Titmouse',
    'Baeolophus ridgwayi': 'Juniper Titmouse',
    'Baeolophus inornatus / ridgwayi': 'unid. Oak Titmouse / Juniper Titmouse',
    'Baeolophus bicolor': 'Tufted Titmouse',
    'Baeolophus atricristatus': 'Black-crested Titmouse',
    'Baeolophus bicolor / atricristatus': 'unid. Tufted Titmouse / Black-crested Titmouse',
    'Auriparus flaviceps': 'Verdin',
    'Psaltriparus minimus': 'Bushtit',
    'Sitta canadensis': 'Red-breasted Nuthatch',
    'Sitta carolinensis': 'White-breasted Nuthatch',
    'Sitta pygmaea': 'Pygmy Nuthatch',
    'Sitta pusilla': 'Brown-headed Nuthatch',
    'Certhia americana': 'Brown Creeper',
    'Salpinctes obsoletus': 'Rock Wren',
    'Catherpes mexicanus': 'Canyon Wren',
    'Troglodytes aedon': 'House Wren',
    'Troglodytes pacificus': 'Pacific Wren',
    'Troglodytes hiemalis': 'Winter Wren',
    'Troglodytes pacificus / hiemalis': 'unid. Pacific Wren / Winter Wren',
    'Cistothorus platensis': 'Sedge Wren',
    'Cistothorus palustris': 'Marsh Wren',
    'Thryothorus ludovicianus': 'Carolina Wren',
    'Thryomanes bewickii': "Bewick's Wren",
    'Campylorhynchus brunneicapillus': 'Cactus Wren',
    'Thryophilus sinaloa': 'Sinaloa Wren',
    'Polioptila caerulea': 'Blue-gray Gnatcatcher',
    'Polioptila californica': 'California Gnatcatcher',
    'Polioptila melanura': 'Black-tailed Gnatcatcher',
    'Polioptila caerulea / melanura': 'unid. Blue-gray / Black-tailed Gnatcatcher',
    'Cinclus mexicanus': 'American Dipper',
    'Regulus satrapa': 'Golden-crowned Kinglet',
    'Regulus calendula': 'Ruby-crowned Kinglet',
    'Phylloscopus borealis': 'Arctic Warbler',
    'Chamaea fasciata': 'Wrentit',
    'Cyanecula svecica': 'Bluethroat',
    'Oenanthe oenanthe': 'Northern Wheatear',
    'Sialia sialis': 'Eastern Bluebird',
    'Sialia mexicana': 'Western Bluebird',
    'Sialia currucoides': 'Mountain Bluebird',
    'Myadestes townsendi': "Townsend's Solitaire",
    'Catharus fuscescens': 'Veery',
    'Catharus minimus': 'Gray-cheeked Thrush',
    'Catharus bicknelli': "Bicknell's Thrush",
    'Catharus ustulatus': "Swainson's Thrush",
    'Catharus guttatus': 'Hermit Thrush',
    'Hylocichla mustelina': 'Wood Thrush',
    'Turdus migratorius': 'American Robin',
    'Ixoreus naevius': 'Varied Thrush',
    'Dumetella carolinensis': 'Gray Catbird',
    'Toxostoma curvirostre': 'Curve-billed Thrasher',
    'Toxostoma rufum': 'Brown Thrasher',
    'Toxostoma longirostre': 'Long-billed Thrasher',
    'Toxostoma bendirei': "Bendire's Thrasher",
    'Toxostoma redivivum': 'California Thrasher',
    'Toxostoma lecontei': "LeConte's Thrasher",
    'Toxostoma crissale': 'Crissal Thrasher',
    'Oreoscoptes montanus': 'Sage Thrasher',
    'Mimus gundlachii': 'Bahama Mockingbird',
    'Mimus polyglottos': 'Northern Mockingbird',
    'Sturnus vulgaris': 'European Starling',
    'Acridotheres tristis': 'Common Myna',
    'Bombycilla garrulus': 'Bohemian Waxwing',
    'Bombycilla cedrorum': 'Cedar Waxwing',
    'Bombycilla garrulus / cedrorum': 'unid. Cedar Waxwing / Bohemian Waxwing',
    'Phainopepla nitens': 'Phainopepla',
    'Peucedramus taeniatus': 'Olive Warbler',
    'Euplectes franciscanus': 'Northern Red Bishop',
    'Vidua macroura': 'Pin-tailed Whydah',
    'Lonchura punctulata': 'Scaly-breasted Munia',
    'Passer domesticus': 'House Sparrow',
    'Passer montanus': 'Eurasian Tree Sparrow',
    'Motacilla tschutschensis': 'Eastern Yellow Wagtail',
    'Motacilla alba': 'White Wagtail',
    'Anthus cervinus': 'Red-throated Pipit',
    'Anthus rubescens': 'American Pipit',
    'Anthus spragueii': "Sprague's Pipit",
    'Coccothraustes vespertinus': 'Evening Grosbeak',
    'Pinicola enucleator': 'Pine Grosbeak',
    'Leucosticte tephrocotis': 'Gray-crowned Rosy-Finch',
    'Leucosticte atrata': 'Black Rosy-Finch',
    'Leucosticte australis': 'Brown-capped Rosy-Finch',
    'Haemorhous mexicanus': 'House Finch',
    'Haemorhous purpureus': 'Purple Finch',
    'Haemorhous cassinii': "Cassin's Finch",
    'Carpodacus purpureus / cassinii / mexicanus': "unid. Purple Finch / Cassin's Finch / House Finch",
    'Acanthis flammea': 'Common Redpoll',
    'Acanthis hornemanni': 'Hoary Redpoll',
    'Carduelis flammea / hornemanni': 'unid. Common Redpoll / Hoary Redpoll',
    'Loxia curvirostra': 'Red Crossbill',
    'Loxia sinesciuris / curvirostra': 'Unid. Cassia Crossbill / Red Crossbill',
    'Loxia leucoptera': 'White-winged Crossbill',
    'Loxia curvirostra / leucoptera': 'unid. Red Crossbill / White-winged Crossbill',
    'Carduelis carduelis': 'European Goldfinch',
    'Spinus pinus': 'Pine Siskin',
    'Spinus psaltria': 'Lesser Goldfinch',
    'Spinus lawrencei': "Lawrence's Goldfinch",
    'Spinus tristis': 'American Goldfinch',
    'Calcarius lapponicus': 'Lapland Longspur',
    'Calcarius ornatus': 'Chestnut-collared Longspur',
    'Calcarius pictus': "Smith's Longspur",
    'Rhynchophanes mccownii': "McCown's Longspur",
    'Plectrophenax nivalis': 'Snow Bunting',
    'Peucaea carpalis': 'Rufous-winged Sparrow',
    'Peucaea botterii': "Botteri's Sparrow",
    'Peucaea cassinii': "Cassin's Sparrow",
    'Peucaea aestivalis': "Bachman's Sparrow",
    'Ammodramus savannarum': 'Grasshopper Sparrow',
    'Arremonops rufivirgatus': 'Olive Sparrow',
    'Amphispiza bilineata': 'Black-throated Sparrow',
    'Chondestes grammacus': 'Lark Sparrow',
    'Calamospiza melanocorys': 'Lark Bunting',
    'Spizella passerina': 'Chipping Sparrow',
    'Spizella pallida': 'Clay-colored Sparrow',
    'Spizella atrogularis': 'Black-chinned Sparrow',
    'Spizella pusilla': 'Field Sparrow',
    'Spizella breweri': "Brewer's Sparrow",
    'Passerella iliaca': 'Fox Sparrow',
    'Spizelloides arborea': 'American Tree Sparrow',
    'Junco hyemalis hyemalis': '(Slate-colored Junco) Dark-eyed Junco',
    'Junco hyemalis oreganus': '(Oregon Junco) Dark-eyed Junco',
    'Junco hyemalis mearnsi': '(Pink-sided Junco) Dark-eyed Junco',
    'Junco hyemalis aikeni': '(White-winged Junco) Dark-eyed Junco',
    'Junco hyemalis caniceps': '(Gray-headed Junco) Dark-eyed Junco',
    'Junco hyemalis': '(unid. race) Dark-eyed Junco',
    'Junco phaeonotus': 'Yellow-eyed Junco',
    'Zonotrichia leucophrys': 'White-crowned Sparrow',
    'Zonotrichia atricapilla': 'Golden-crowned Sparrow',
    'Zonotrichia querula': "Harris's Sparrow",
    'Zonotrichia albicollis': 'White-throated Sparrow',
    'Artemisiospiza nevadensis': 'Sagebrush Sparrow',
    'Artemisiospiza belli': "Bell's Sparrow",
    'Artemisiospiza nevadensis / belli': "unid. Sagebrush Sparrow / Bell's Sparrow",
    'Pooecetes gramineus': 'Vesper Sparrow',
    'Ammospiza leconteii': "LeConte's Sparrow",
    'Ammospiza maritima': 'Seaside Sparrow',
    'Ammospiza nelsoni': "Nelson's Sparrow",
    'Ammospiza caudacuta': 'Saltmarsh Sparrow',
    'Centronyx bairdii': "Baird's Sparrow",
    'Centronyx henslowii': "Henslow's Sparrow",
    'Passerculus sandwichensis': 'Savannah Sparrow',
    'Melospiza melodia': 'Song Sparrow',
    'Melospiza lincolnii': "Lincoln's Sparrow",
    'Melospiza georgiana': 'Swamp Sparrow',
    'Melozone fusca': 'Canyon Towhee',
    'Melozone aberti': "Abert's Towhee",
    'Melozone crissalis': 'California Towhee',
    'Aimophila ruficeps': 'Rufous-crowned Sparrow',
    'Pipilo chlorurus': 'Green-tailed Towhee',
    'Pipilo maculatus': 'Spotted Towhee',
    'Pipilo erythrophthalmus': 'Eastern Towhee',
    'Pipilo maculatus / erythrophthalmus': 'unid. Spotted Towhee / Eastern Towhee',
    'Icteria virens': 'Yellow-breasted Chat',
    'Xanthocephalus xanthocephalus': 'Yellow-headed Blackbird',
    'Dolichonyx oryzivorus': 'Bobolink',
    'Sturnella magna': 'Eastern Meadowlark',
    'Sturnella neglecta': 'Western Meadowlark',
    'Sturnella magna / neglecta': 'unid. Eastern Meadowlark / Western Meadowlark',
    'Icterus spurius': 'Orchard Oriole',
    'Icterus cucullatus': 'Hooded Oriole',
    'Icterus bullockii': "Bullock's Oriole",
    'Icterus pectoralis': 'Spot-breasted Oriole',
    'Icterus gularis': 'Altamira Oriole',
    'Icterus graduacauda': "Audubon's Oriole",
    'Icterus galbula': 'Baltimore Oriole',
    'Icterus bullockii x galbula': "hybrid Bullock's Oriole x Baltimore Oriole",
    'Icterus bullockii / galbula': "unid. Bullock's Oriole / Baltimore Oriole",
    'Icterus parisorum': "Scott's Oriole",
    'Agelaius phoeniceus': 'Red-winged Blackbird',
    'Agelaius tricolor': 'Tricolored Blackbird',
    'Molothrus bonariensis': 'Shiny Cowbird',
    'Molothrus aeneus': 'Bronzed Cowbird',
    'Molothrus ater': 'Brown-headed Cowbird',
    'Molothrus aeneus / ater': 'unid. Bronzed Cowbird / Brown-headed Cowbird',
    'Euphagus carolinus': 'Rusty Blackbird',
    'Euphagus cyanocephalus': "Brewer's Blackbird",
    'Quiscalus quiscula': 'Common Grackle',
    'Quiscalus major': 'Boat-tailed Grackle',
    'Quiscalus mexicanus': 'Great-tailed Grackle',
    'Quiscalus major / mexicanus': 'unid. Boat-tailed Grackle / Great-tailed Grackle',
    'Seiurus aurocapilla': 'Ovenbird',
    'Helmitheros vermivorum': 'Worm-eating Warbler',
    'Parkesia motacilla': 'Louisiana Waterthrush',
    'Parkesia noveboracensis': 'Northern Waterthrush',
    'Vermivora chrysoptera': 'Golden-winged Warbler',
    'Vermivora cyanoptera': 'Blue-winged Warbler',
    'Vermivora cyanoptera x chrysoptera': "Brewster's Warbler (Golden-winged x Blue-winged)",
    'Vermivora chrysoptera x cyanoptera': "Lawrence's Warbler (Golden-winged x Blue-winged)",
    'Mniotilta varia': 'Black-and-white Warbler',
    'Protonotaria citrea': 'Prothonotary Warbler',
    'Limnothlypis swainsonii': "Swainson's Warbler",
    'Leiothlypis peregrina': 'Tennessee Warbler',
    'Leiothlypis celata': 'Orange-crowned Warbler',
    'Leiothlypis luciae': "Lucy's Warbler",
    'Leiothlypis ruficapilla': 'Nashville Warbler',
    'Leiothlypis virginiae': "Virginia's Warbler",
    'Oporornis agilis': 'Connecticut Warbler',
    'Geothlypis tolmiei': "MacGillivray's Warbler",
    'Geothlypis philadelphia': 'Mourning Warbler',
    'Geothlypis formosa': 'Kentucky Warbler',
    'Geothlypis trichas': 'Common Yellowthroat',
    'Setophaga citrina': 'Hooded Warbler',
    'Setophaga ruticilla': 'American Redstart',
    'Setophaga kirtlandii': "Kirtland's Warbler",
    'Setophaga tigrina': 'Cape May Warbler',
    'Setophaga cerulea': 'Cerulean Warbler',
    'Setophaga americana': 'Northern Parula',
    'Setophaga pitiayumi': 'Tropical Parula',
    'Setophaga magnolia': 'Magnolia Warbler',
    'Setophaga castanea': 'Bay-breasted Warbler',
    'Setophaga fusca': 'Blackburnian Warbler',
    'Setophaga petechia': 'Yellow Warbler',
    'Setophaga pensylvanica': 'Chestnut-sided Warbler',
    'Setophaga striata': 'Blackpoll Warbler',
    'Setophaga caerulescens': 'Black-throated Blue Warbler',
    'Setophaga palmarum': 'Palm Warbler',
    'Setophaga pinus': 'Pine Warbler',
    'Setophaga coronata coronata': '(Myrtle Warbler) Yellow-rumped Warbler',
    'Setophaga coronata audoboni': "(Audubon's Warbler) Yellow-rumped Warbler",
    'Setophaga coronata': "(unid. Myrtle/Audubon's) Yellow-rumped Warbler",
    'Setophaga dominica': 'Yellow-throated Warbler',
    'Setophaga discolor': 'Prairie Warbler',
    'Setophaga graciae': "Grace's Warbler",
    'Setophaga nigrescens': 'Black-throated Gray Warbler',
    'Setophaga townsendi': "Townsend's Warbler",
    'Setophaga occidentalis': 'Hermit Warbler',
    'Setophaga townsendi x occidentalis': "hybrid Townsend's Warbler x Hermit Warbler",
    'Setophaga townsendi / occidentalis': "unid. Townsend's Warbler / Hermit Warbler",
    'Setophaga chrysoparia': 'Golden-cheeked Warbler',
    'Setophaga virens': 'Black-throated Green Warbler',
    'Cardellina canadensis': 'Canada Warbler',
    'Cardellina pusilla': "Wilson's Warbler",
    'Cardellina rubrifrons': 'Red-faced Warbler',
    'Myioborus pictus': 'Painted Redstart',
    'Piranga flava': 'Hepatic Tanager',
    'Piranga rubra': 'Summer Tanager',
    'Piranga olivacea': 'Scarlet Tanager',
    'Piranga ludoviciana': 'Western Tanager',
    'Cardinalis cardinalis': 'Northern Cardinal',
    'Cardinalis sinuatus': 'Pyrrhuloxia',
    'Cardinalis cardinalis / sinuatus': 'unid. Northern Cardinal / Pyrrhuloxia',
    'Pheucticus ludovicianus': 'Rose-breasted Grosbeak',
    'Pheucticus melanocephalus': 'Black-headed Grosbeak',
    'Passerina caerulea': 'Blue Grosbeak',
    'Passerina amoena': 'Lazuli Bunting',
    'Passerina cyanea': 'Indigo Bunting',
    'Passerina amoena x cyanea': 'hybrid Lazuli Bunting x Indigo Bunting',
    'Passerina versicolor': 'Varied Bunting',
    'Passerina ciris': 'Painted Bunting',
    'Spiza americana': 'Dickcissel'}

#BBS_commonname_map = dict() #TODO: Remove this later.

#%% eBird Bird List common names
eBird_commonname_map = {'Rhea americana': 'Greater Rhea', 'Crypturellus transfasciatus': 'Pale-browed Tinamou', 'Dendrocygna viduata': 'White-faced Whistling-Duck', 'Dendrocygna autumnalis': 'Black-bellied Whistling-Duck', 'Dendrocygna arborea': 'West Indian Whistling-Duck', 'Dendrocygna bicolor': 'Fulvous Whistling-Duck', 'Anser canagicus': 'Emperor Goose', 'Anser caerulescens': 'Snow Goose', 'Anser rossii': "Ross's Goose", 'Anser albifrons': 'Greater White-fronted Goose', 'Branta bernicla': 'Brant', 'Branta hutchinsii': 'Cackling Goose', 'Branta canadensis': 'Canada Goose', 'Cygnus olor': 'Mute Swan', 'Cygnus melancoryphus': 'Black-necked Swan', 'Cygnus buccinator': 'Trumpeter Swan', 'Cygnus columbianus': 'Tundra Swan', 'Coscoroba coscoroba': 'Coscoroba Swan', 'Oressochen jubatus': 'Orinoco Goose', 'Oressochen melanopterus': 'Andean Goose', 'Alopochen aegyptiaca': 'Egyptian Goose', 'Tadorna variegata': 'Paradise Shelduck', 'Tadorna tadorna': 'Common Shelduck', 'Cairina moschata': 'Muscovy Duck', 'Aix sponsa': 'Wood Duck', 'Hymenolaimus malacorhynchos': 'Blue Duck', 'Spatula discors': 'Blue-winged Teal', 'Spatula cyanoptera': 'Cinnamon Teal', 'Spatula clypeata': 'Northern Shoveler', 'Mareca strepera': 'Gadwall', 'Mareca penelope': 'Eurasian Wigeon', 'Mareca americana': 'American Wigeon', 'Anas platyrhynchos': 'Mallard', 'Anas diazi': 'Mexican Duck', 'Anas rubripes': 'American Black Duck', 'Anas fulvigula': 'Mottled Duck', 'Anas bahamensis': 'White-cheeked Pintail', 'Anas acuta': 'Northern Pintail', 'Anas georgica': 'Yellow-billed Pintail', 'Anas crecca': 'Green-winged Teal', 'Anas gracilis': 'Gray Teal', 'Netta peposaca': 'Rosy-billed Pochard', 'Aythya valisineria': 'Canvasback', 'Aythya americana': 'Redhead', 'Aythya collaris': 'Ring-necked Duck', 'Aythya fuligula': 'Tufted Duck', 'Aythya marila': 'Greater Scaup', 'Aythya affinis': 'Lesser Scaup', 'Polysticta stelleri': "Steller's Eider", 'Somateria fischeri': 'Spectacled Eider', 'Somateria spectabilis': 'King Eider', 'Somateria mollissima': 'Common Eider', 'Histrionicus histrionicus': 'Harlequin Duck', 'Melanitta perspicillata': 'Surf Scoter', 'Melanitta deglandi': 'White-winged Scoter', 'Melanitta americana': 'Black Scoter', 'Clangula hyemalis': 'Long-tailed Duck', 'Bucephala albeola': 'Bufflehead', 'Bucephala clangula': 'Common Goldeneye', 'Bucephala islandica': "Barrow's Goldeneye", 'Lophodytes cucullatus': 'Hooded Merganser', 'Mergus merganser': 'Common Merganser', 'Mergus serrator': 'Red-breasted Merganser', 'Heteronetta atricapilla': 'Black-headed Duck', 'Nomonyx dominicus': 'Masked Duck', 'Oxyura jamaicensis': 'Ruddy Duck', 'Ortalis vetula': 'Plain Chachalaca', 'Ortalis columbiana': 'Colombian Chachalaca', 'Pipile jacutinga': 'Black-fronted Piping-Guan', 'Crax fasciolata': 'Bare-faced Curassow', 'Oreortyx pictus': 'Mountain Quail', 'Colinus virginianus': 'Northern Bobwhite', 'Callipepla squamata': 'Scaled Quail', 'Callipepla californica': 'California Quail', 'Callipepla gambelii': "Gambel's Quail", 'Cyrtonyx montezumae': 'Montezuma Quail', 'Odontophorus melanonotus': 'Dark-backed Wood-Quail', 'Meleagris gallopavo': 'Wild Turkey', 'Bonasa umbellus': 'Ruffed Grouse', 'Centrocercus urophasianus': 'Greater Sage-Grouse', 'Centrocercus minimus': 'Gunnison Sage-Grouse', 'Dendragapus obscurus': 'Dusky Grouse', 'Dendragapus fuliginosus': 'Sooty Grouse', 'Tympanuchus phasianellus': 'Sharp-tailed Grouse', 'Tympanuchus cupido': 'Greater Prairie-Chicken', 'Tympanuchus pallidicinctus': 'Lesser Prairie-Chicken', 'Lagopus leucura': 'White-tailed Ptarmigan', 'Lagopus lagopus': 'Willow Ptarmigan', 'Lagopus muta': 'Rock Ptarmigan', 'Canachites canadensis': 'Spruce Grouse', 'Perdix perdix': 'Gray Partridge', 'Phasianus colchicus': 'Ring-necked Pheasant', 'Gallus sonneratii': 'Gray Junglefowl', 'Ortygornis gularis': 'Swamp Francolin', 'Coturnix coturnix': 'Common Quail', 'Alectoris chukar': 'Chukar', 'Phoenicopterus chilensis': 'Chilean Flamingo', 'Tachybaptus dominicus': 'Least Grebe', 'Podilymbus podiceps': 'Pied-billed Grebe', 'Podiceps auritus': 'Horned Grebe', 'Podiceps grisegena': 'Red-necked Grebe', 'Podiceps nigricollis': 'Eared Grebe', 'Podiceps occipitalis': 'Silvery Grebe', 'Aechmophorus occidentalis': 'Western Grebe', 'Aechmophorus clarkii': "Clark's Grebe", 'Columba livia': 'Rock Pigeon', 'Patagioenas leucocephala': 'White-crowned Pigeon', 'Patagioenas flavirostris': 'Red-billed Pigeon', 'Patagioenas fasciata': 'Band-tailed Pigeon', 'Streptopelia turtur': 'European Turtle-Dove', 'Streptopelia decaocto': 'Eurasian Collared-Dove', 'Streptopelia capicola': 'Ring-necked Dove', 'Streptopelia chinensis': 'Spotted Dove', 'Columbina inca': 'Inca Dove', 'Columbina passerina': 'Common Ground Dove', 'Columbina talpacoti': 'Ruddy Ground Dove', 'Columbina buckleyi': 'Ecuadorian Ground Dove', 'Geotrygon montana': 'Ruddy Quail-Dove', 'Leptotila verreauxi': 'White-tipped Dove', 'Zenaida meloda': 'West Peruvian Dove', 'Zenaida asiatica': 'White-winged Dove', 'Zenaida macroura': 'Mourning Dove', 'Hemiphaga novaeseelandiae': 'New Zealand Pigeon', 'Pterocles orientalis': 'Black-bellied Sandgrouse', 'Crotophaga ani': 'Smooth-billed Ani', 'Crotophaga sulcirostris': 'Groove-billed Ani', 'Morococcyx erythropygus': 'Lesser Ground-Cuckoo', 'Geococcyx californianus': 'Greater Roadrunner', 'Clamator jacobinus': 'Pied Cuckoo', 'Coccyzus americanus': 'Yellow-billed Cuckoo', 'Coccyzus minor': 'Mangrove Cuckoo', 'Coccyzus erythropthalmus': 'Black-billed Cuckoo', 'Eudynamys scolopaceus': 'Asian Koel', 'Eudynamys orientalis': 'Pacific Koel', 'Scythrops novaehollandiae': 'Channel-billed Cuckoo', 'Chrysococcyx lucidus': 'Shining Bronze-Cuckoo', 'Hierococcyx sparverioides': 'Large Hawk-Cuckoo', 'Cuculus canorus': 'Common Cuckoo', 'Cuculus optatus': 'Oriental Cuckoo', 'Chordeiles acutipennis': 'Lesser Nighthawk', 'Chordeiles minor': 'Common Nighthawk', 'Chordeiles gundlachii': 'Antillean Nighthawk', 'Nyctidromus albicollis': 'Common Pauraque', 'Phalaenoptilus nuttallii': 'Common Poorwill', 'Antrostomus carolinensis': "Chuck-will's-widow", 'Antrostomus vociferus': 'Eastern Whip-poor-will', 'Antrostomus arizonae': 'Mexican Whip-poor-will', 'Caprimulgus ruficollis': 'Red-necked Nightjar', 'Caprimulgus europaeus': 'Eurasian Nightjar', 'Nyctibius griseus': 'Common Potoo', 'Cypseloides niger': 'Black Swift', 'Chaetura pelagica': 'Chimney Swift', 'Chaetura vauxi': "Vaux's Swift", 'Apus melba': 'Alpine Swift', 'Apus apus': 'Common Swift', 'Apus unicolor': 'Plain Swift', 'Apus pallidus': 'Pallid Swift', 'Aeronautes saxatalis': 'White-throated Swift', 'Panyptila sanctihieronymi': 'Great Swallow-tailed Swift', 'Colibri serrirostris': 'White-vented Violetear', 'Colibri coruscans': 'Sparkling Violetear', 'Colibri delphinae': 'Brown Violetear', 'Colibri thalassinus': 'Mexican Violetear', 'Colibri cyanotus': 'Lesser Violetear', 'Sephanoides sephaniodes': 'Green-backed Firecrown', 'Ramphomicron microrhynchum': 'Purple-backed Thornbill', 'Coeligena torquata': 'Collared Inca', 'Patagona gigas': 'Giant Hummingbird', 'Eugenes fulgens': "Rivoli's Hummingbird", 'Heliomaster furcifer': 'Blue-tufted Starthroat', 'Lampornis clemenciae': 'Blue-throated Mountain-gem', 'Thaumastura cora': 'Peruvian Sheartail', 'Rhodopis vesper': 'Oasis Hummingbird', 'Calothorax lucifer': 'Lucifer Hummingbird', 'Archilochus colubris': 'Ruby-throated Hummingbird', 'Archilochus alexandri': 'Black-chinned Hummingbird', 'Calypte anna': "Anna's Hummingbird", 'Calypte costae': "Costa's Hummingbird", 'Selasphorus calliope': 'Calliope Hummingbird', 'Selasphorus rufus': 'Rufous Hummingbird', 'Selasphorus sasin': "Allen's Hummingbird", 'Selasphorus platycercus': 'Broad-tailed Hummingbird', 'Cynanthus latirostris/doubledayi': 'Broad-billed/Turquoise-crowned Hummingbird', 'Chlorostilbon lucidus': 'Glittering-bellied Emerald', 'Basilinna xantusii': "Xantus's Hummingbird", 'Leucolia violiceps': 'Violet-crowned Hummingbird', 'Saucerottia beryllina': 'Berylline Hummingbird', 'Saucerottia cyanifrons': 'Indigo-capped Hummingbird', 'Amazilia yucatanensis': 'Buff-bellied Hummingbird', 'Amazilia luciae': 'Honduran Emerald', 'Rallus obsoletus': "Ridgway's Rail", 'Rallus elegans': 'King Rail', 'Rallus crepitans': 'Clapper Rail', 'Rallus limicola': 'Virginia Rail', 'Porzana carolina': 'Sora', 'Gallinula galeata': 'Common Gallinule', 'Fulica americana': 'American Coot', 'Porphyrio martinica': 'Purple Gallinule', 'Porphyrio poliocephalus': 'Gray-headed Swamphen', 'Coturnicops noveboracensis': 'Yellow Rail', 'Laterallus jamaicensis': 'Black Rail', 'Aramus guarauna': 'Limpkin', 'Antigone canadensis': 'Sandhill Crane', 'Antigone antigone': 'Sarus Crane', 'Grus americana': 'Whooping Crane', 'Himantopus himantopus': 'Black-winged Stilt', 'Himantopus mexicanus': 'Black-necked Stilt', 'Recurvirostra americana': 'American Avocet', 'Haematopus finschi': 'South Island Oystercatcher', 'Haematopus palliatus': 'American Oystercatcher', 'Haematopus ater': 'Blackish Oystercatcher', 'Haematopus leucopodus': 'Magellanic Oystercatcher', 'Haematopus bachmani': 'Black Oystercatcher', 'Pluvialis squatarola': 'Black-bellied Plover', 'Pluvialis dominica': 'American Golden-Plover', 'Pluvialis fulva': 'Pacific Golden-Plover', 'Vanellus vanellus': 'Northern Lapwing', 'Vanellus chilensis': 'Southern Lapwing', 'Charadrius obscurus': 'Red-breasted Dotterel', 'Charadrius falklandicus': 'Two-banded Plover', 'Charadrius bicinctus': 'Double-banded Plover', 'Charadrius alexandrinus': 'Kentish Plover', 'Charadrius nivosus': 'Snowy Plover', 'Charadrius wilsonia': "Wilson's Plover", 'Charadrius semipalmatus': 'Semipalmated Plover', 'Charadrius melodus': 'Piping Plover', 'Charadrius vociferus': 'Killdeer', 'Charadrius montanus': 'Mountain Plover', 'Charadrius modestus': 'Rufous-chested Dotterel', 'Anarhynchus frontalis': 'Wrybill', 'Nycticryphes semicollaris': 'South American Painted-Snipe', 'Jacana spinosa': 'Northern Jacana', 'Bartramia longicauda': 'Upland Sandpiper', 'Numenius tahitiensis': 'Bristle-thighed Curlew', 'Numenius phaeopus': 'Whimbrel', 'Numenius americanus': 'Long-billed Curlew', 'Numenius arquata': 'Eurasian Curlew', 'Limosa lapponica': 'Bar-tailed Godwit', 'Limosa haemastica': 'Hudsonian Godwit', 'Limosa fedoa': 'Marbled Godwit', 'Arenaria interpres': 'Ruddy Turnstone', 'Arenaria melanocephala': 'Black Turnstone', 'Calidris canutus': 'Red Knot', 'Calidris virgata': 'Surfbird', 'Calidris himantopus': 'Stilt Sandpiper', 'Calidris ruficollis': 'Red-necked Stint', 'Calidris alba': 'Sanderling', 'Calidris alpina': 'Dunlin', 'Calidris ptilocnemis': 'Rock Sandpiper', 'Calidris maritima': 'Purple Sandpiper', 'Calidris bairdii': "Baird's Sandpiper", 'Calidris minutilla': 'Least Sandpiper', 'Calidris fuscicollis': 'White-rumped Sandpiper', 'Calidris subruficollis': 'Buff-breasted Sandpiper', 'Calidris melanotos': 'Pectoral Sandpiper', 'Calidris pusilla': 'Semipalmated Sandpiper', 'Calidris mauri': 'Western Sandpiper', 'Limnodromus griseus': 'Short-billed Dowitcher', 'Limnodromus scolopaceus': 'Long-billed Dowitcher', 'Scolopax rusticola': 'Eurasian Woodcock', 'Scolopax minor': 'American Woodcock', 'Gallinago delicata': "Wilson's Snipe", 'Phalaropus tricolor': "Wilson's Phalarope", 'Phalaropus lobatus': 'Red-necked Phalarope', 'Actitis macularius': 'Spotted Sandpiper', 'Tringa solitaria': 'Solitary Sandpiper', 'Tringa incana': 'Wandering Tattler', 'Tringa melanoleuca': 'Greater Yellowlegs', 'Tringa semipalmata': 'Willet', 'Tringa flavipes': 'Lesser Yellowlegs', 'Glareola maldivarum': 'Oriental Pratincole', 'Stercorarius pomarinus': 'Pomarine Jaeger', 'Stercorarius parasiticus': 'Parasitic Jaeger', 'Stercorarius longicaudus': 'Long-tailed Jaeger', 'Cepphus columba': 'Pigeon Guillemot', 'Brachyramphus marmoratus': 'Marbled Murrelet', 'Saundersilarus saundersi': "Saunders's Gull", 'Chroicocephalus philadelphia': "Bonaparte's Gull", 'Chroicocephalus novaehollandiae': 'Silver Gull', 'Hydrocoloeus minutus': 'Little Gull', 'Leucophaeus atricilla': 'Laughing Gull', 'Leucophaeus pipixcan': "Franklin's Gull", 'Ichthyaetus audouinii': "Audouin's Gull", 'Larus crassirostris': 'Black-tailed Gull', 'Larus heermanni': "Heermann's Gull", 'Larus canus/brachyrhynchus': 'Common/Short-billed Gull', 'Larus delawarensis': 'Ring-billed Gull', 'Larus occidentalis': 'Western Gull', 'Larus californicus': 'California Gull', 'Larus argentatus': 'Herring Gull', 'Larus glaucoides': 'Iceland Gull', 'Larus fuscus': 'Lesser Black-backed Gull', 'Larus glaucescens': 'Glaucous-winged Gull', 'Larus hyperboreus': 'Glaucous Gull', 'Larus marinus': 'Great Black-backed Gull', 'Onychoprion aleuticus': 'Aleutian Tern', 'Sternula antillarum': 'Least Tern', 'Gelochelidon nilotica': 'Gull-billed Tern', 'Hydroprogne caspia': 'Caspian Tern', 'Chlidonias niger': 'Black Tern', 'Chlidonias leucopterus': 'White-winged Tern', 'Sterna dougallii': 'Roseate Tern', 'Sterna hirundo': 'Common Tern', 'Sterna paradisaea': 'Arctic Tern', 'Sterna hirundinacea': 'South American Tern', 'Sterna forsteri': "Forster's Tern", 'Thalasseus maximus': 'Royal Tern', 'Thalasseus bergii': 'Great Crested Tern', 'Thalasseus sandvicensis': 'Sandwich Tern', 'Thalasseus elegans': 'Elegant Tern', 'Rynchops niger': 'Black Skimmer', 'Gavia stellata': 'Red-throated Loon', 'Gavia arctica': 'Arctic Loon', 'Gavia pacifica': 'Pacific Loon', 'Gavia immer': 'Common Loon', 'Gavia adamsii': 'Yellow-billed Loon', 'Puffinus mauretanicus': 'Balearic Shearwater', 'Ciconia nigra': 'Black Stork', 'Ciconia maguari': 'Maguari Stork', 'Ciconia ciconia': 'White Stork', 'Mycteria americana': 'Wood Stork', 'Fregata magnificens': 'Magnificent Frigatebird', 'Anhinga anhinga': 'Anhinga', 'Microcarbo melanoleucos': 'Little Pied Cormorant', 'Urile penicillatus': "Brandt's Cormorant", 'Urile pelagicus': 'Pelagic Cormorant', 'Phalacrocorax carbo': 'Great Cormorant', 'Nannopterum auritum': 'Double-crested Cormorant', 'Nannopterum brasilianum': 'Neotropic Cormorant', 'Pelecanus erythrorhynchos': 'American White Pelican', 'Pelecanus occidentalis': 'Brown Pelican', 'Pelecanus onocrotalus': 'Great White Pelican', 'Botaurus lentiginosus': 'American Bittern', 'Ixobrychus minutus': 'Little Bittern', 'Ixobrychus exilis': 'Least Bittern', 'Ardea herodias': 'Great Blue Heron', 'Ardea alba': 'Great Egret', 'Egretta thula': 'Snowy Egret', 'Egretta caerulea': 'Little Blue Heron', 'Egretta tricolor': 'Tricolored Heron', 'Egretta rufescens': 'Reddish Egret', 'Bubulcus ibis': 'Cattle Egret', 'Butorides virescens': 'Green Heron', 'Nycticorax nycticorax': 'Black-crowned Night-Heron', 'Nyctanassa violacea': 'Yellow-crowned Night-Heron', 'Eudocimus albus': 'White Ibis', 'Plegadis falcinellus': 'Glossy Ibis', 'Plegadis chihi': 'White-faced Ibis', 'Mesembrinibis cayennensis': 'Green Ibis', 'Platalea minor': 'Black-faced Spoonbill', 'Platalea ajaja': 'Roseate Spoonbill', 'Gymnogyps californianus': 'California Condor', 'Vultur gryphus': 'Andean Condor', 'Coragyps atratus': 'Black Vulture', 'Cathartes aura': 'Turkey Vulture', 'Pandion haliaetus': 'Osprey', 'Elanus caeruleus': 'Black-winged Kite', 'Elanus leucurus': 'White-tailed Kite', 'Neophron percnopterus': 'Egyptian Vulture', 'Chondrohierax uncinatus': 'Hook-billed Kite', 'Pernis apivorus': 'European Honey-buzzard', 'Pernis ptilorhynchus': 'Oriental Honey-buzzard', 'Elanoides forficatus': 'Swallow-tailed Kite', 'Circaetus gallicus': 'Short-toed Snake-Eagle', 'Aquila chrysaetos': 'Golden Eagle', 'Rostrhamus sociabilis': 'Snail Kite', 'Ictinia mississippiensis': 'Mississippi Kite', 'Ictinia plumbea': 'Plumbeous Kite', 'Butastur indicus': 'Gray-faced Buzzard', 'Circus hudsonius': 'Northern Harrier', 'Circus pygargus': "Montagu's Harrier", 'Accipiter soloensis': 'Chinese Sparrowhawk', 'Accipiter striatus': 'Sharp-shinned Hawk', 'Accipiter cooperii': "Cooper's Hawk", 'Accipiter gentilis': 'Northern Goshawk', 'Milvus milvus': 'Red Kite', 'Milvus migrans': 'Black Kite', 'Haliastur indus': 'Brahminy Kite', 'Haliaeetus leucocephalus': 'Bald Eagle', 'Buteogallus anthracinus': 'Common Black Hawk', 'Parabuteo unicinctus': "Harris's Hawk", 'Geranoaetus albicaudatus': 'White-tailed Hawk', 'Geranoaetus melanoleucus': 'Black-chested Buzzard-Eagle', 'Buteo plagiatus': 'Gray Hawk', 'Buteo lineatus': 'Red-shouldered Hawk', 'Buteo platypterus': 'Broad-winged Hawk', 'Buteo brachyurus': 'Short-tailed Hawk', 'Buteo albigula': 'White-throated Hawk', 'Buteo swainsoni': "Swainson's Hawk", 'Buteo albonotatus': 'Zone-tailed Hawk', 'Buteo jamaicensis': 'Red-tailed Hawk', 'Buteo lagopus': 'Rough-legged Hawk', 'Buteo regalis': 'Ferruginous Hawk', 'Tyto alba': 'Barn Owl', 'Otus scops/cyprius': 'Eurasian/Cyprus Scops-Owl', 'Psiloscops flammeolus': 'Flammulated Owl', 'Megascops trichopsis': 'Whiskered Screech-Owl', 'Megascops kennicottii': 'Western Screech-Owl', 'Megascops asio': 'Eastern Screech-Owl', 'Bubo virginianus': 'Great Horned Owl', 'Bubo scandiacus': 'Snowy Owl', 'Surnia ulula': 'Northern Hawk Owl', 'Glaucidium gnoma': 'Northern Pygmy-Owl', 'Glaucidium brasilianum': 'Ferruginous Pygmy-Owl', 'Athene cunicularia': 'Burrowing Owl', 'Strix occidentalis': 'Spotted Owl', 'Strix varia': 'Barred Owl', 'Asio otus': 'Long-eared Owl', 'Asio flammeus': 'Short-eared Owl', 'Aegolius acadicus': 'Northern Saw-whet Owl', 'Ninox novaeseelandiae': 'Morepork', 'Pharomachrus mocinno': 'Resplendent Quetzal', 'Trogon elegans': 'Elegant Trogon', 'Upupa epops': 'Eurasian Hoopoe', 'Anthracoceros coronatus': 'Malabar Pied-Hornbill', 'Aspatha gularis': 'Blue-throated Motmot', 'Momotus coeruliceps': 'Blue-capped Motmot', 'Momotus lessonii': "Lesson's Motmot", 'Eumomota superciliosa': 'Turquoise-browed Motmot', 'Alcedo atthis': 'Common Kingfisher', 'Halcyon pileata': 'Black-capped Kingfisher', 'Todiramphus sanctus': 'Sacred Kingfisher', 'Megaceryle torquata': 'Ringed Kingfisher', 'Megaceryle alcyon': 'Belted Kingfisher', 'Chloroceryle americana': 'Green Kingfisher', 'Merops ornatus': 'Rainbow Bee-eater', 'Merops apiaster': 'European Bee-eater', 'Coracias garrulus': 'European Roller', 'Coracias benghalensis': 'Indian Roller', 'Psilopogon haemacephalus': 'Coppersmith Barbet', 'Capito hypoleucus': 'White-mantled Barbet', 'Ramphastos sulfuratus': 'Keel-billed Toucan', 'Jynx torquilla': 'Eurasian Wryneck', 'Sphyrapicus thyroideus': "Williamson's Sapsucker", 'Sphyrapicus varius': 'Yellow-bellied Sapsucker', 'Sphyrapicus nuchalis': 'Red-naped Sapsucker', 'Sphyrapicus ruber': 'Red-breasted Sapsucker', 'Melanerpes candidus': 'White Woodpecker', 'Melanerpes lewis': "Lewis's Woodpecker", 'Melanerpes erythrocephalus': 'Red-headed Woodpecker', 'Melanerpes formicivorus': 'Acorn Woodpecker', 'Melanerpes uropygialis': 'Gila Woodpecker', 'Melanerpes aurifrons': 'Golden-fronted Woodpecker', 'Melanerpes carolinus': 'Red-bellied Woodpecker', 'Picoides dorsalis': 'American Three-toed Woodpecker', 'Picoides arcticus': 'Black-backed Woodpecker', 'Dryobates pubescens': 'Downy Woodpecker', 'Dryobates nuttallii': "Nuttall's Woodpecker", 'Dryobates scalaris': 'Ladder-backed Woodpecker', 'Dryobates borealis': 'Red-cockaded Woodpecker', 'Dryobates villosus': 'Hairy Woodpecker', 'Dryobates albolarvatus': 'White-headed Woodpecker', 'Dryobates arizonae': 'Arizona Woodpecker', 'Campephilus guatemalensis': 'Pale-billed Woodpecker', 'Picus viridis': 'Eurasian Green Woodpecker', 'Picus sharpei': 'Iberian Green Woodpecker', 'Dryocopus lineatus': 'Lineated Woodpecker', 'Dryocopus pileatus': 'Pileated Woodpecker', 'Dryocopus schulzii': 'Black-bodied Woodpecker', 'Colaptes auratus': 'Northern Flicker', 'Colaptes chrysoides': 'Gilded Flicker', 'Caracara plancus': 'Crested Caracara', 'Falco sparverius': 'American Kestrel', 'Falco eleonorae': "Eleonora's Falcon", 'Falco columbarius': 'Merlin', 'Falco novaeseelandiae': 'New Zealand Falcon', 'Falco femoralis': 'Aplomado Falcon', 'Falco deiroleucus': 'Orange-breasted Falcon', 'Falco peregrinus': 'Peregrine Falcon', 'Falco mexicanus': 'Prairie Falcon', 'Nestor meridionalis': 'New Zealand Kaka', 'Psilopsiagon aurifrons': 'Mountain Parakeet', 'Myiopsitta monachus': 'Monk Parakeet', 'Brotogeris versicolurus': 'White-winged Parakeet', 'Brotogeris chiriri': 'Yellow-chevroned Parakeet', 'Brotogeris jugularis': 'Orange-chinned Parakeet', 'Pionus menstruus': 'Blue-headed Parrot', 'Amazona viridigenalis': 'Red-crowned Parrot', 'Amazona auropalliata': 'Yellow-naped Parrot', 'Amazona aestiva': 'Turquoise-fronted Parrot', 'Rhynchopsitta terrisi': 'Maroon-fronted Parrot', 'Eupsittula pertinax': 'Brown-throated Parakeet', 'Aratinga nenday': 'Nanday Parakeet', 'Ara ararauna': 'Blue-and-yellow Macaw', 'Ara ambiguus': 'Great Green Macaw', 'Ara macao': 'Scarlet Macaw', 'Ara chloropterus': 'Red-and-green Macaw', 'Acanthisitta chloris': 'Rifleman', 'Pitta brachyura': 'Indian Pitta', 'Willisornis poecilinotus': 'Common Scale-backed Antbird', 'Pteroptochos castaneus': 'Chestnut-throated Huet-huet', 'Formicarius analis': 'Black-faced Antthrush', 'Lepidocolaptes souleyetii': 'Streak-headed Woodcreeper', 'Asthenes anthoides': 'Austral Canastero', 'Corapipo altera': 'White-ruffed Manakin', 'Carpornis melanocephala': 'Black-headed Berryeater', 'Phytotoma raimondii': 'Peruvian Plantcutter', 'Procnias nudicollis': 'Bare-throated Bellbird', 'Pachyramphus aglaiae': 'Rose-throated Becard', 'Mionectes olivaceus': 'Olive-striped Flycatcher', 'Mionectes oleagineus': 'Ochre-bellied Flycatcher', 'Camptostoma imberbe': 'Northern Beardless-Tyrannulet', 'Elaenia parvirostris': 'Small-billed Elaenia', 'Elaenia albiceps': 'White-crested Elaenia', 'Elaenia frantzii': 'Mountain Elaenia', 'Lathrotriccus griseipectus': 'Gray-breasted Flycatcher', 'Contopus cooperi': 'Olive-sided Flycatcher', 'Contopus pertinax': 'Greater Pewee', 'Contopus sordidulus': 'Western Wood-Pewee', 'Contopus virens': 'Eastern Wood-Pewee', 'Empidonax flaviventris': 'Yellow-bellied Flycatcher', 'Empidonax virescens': 'Acadian Flycatcher', 'Empidonax alnorum': 'Alder Flycatcher', 'Empidonax traillii': 'Willow Flycatcher', 'Empidonax minimus': 'Least Flycatcher', 'Empidonax hammondii': "Hammond's Flycatcher", 'Empidonax wrightii': 'Gray Flycatcher', 'Empidonax oberholseri': 'Dusky Flycatcher', 'Empidonax difficilis': 'Pacific-slope Flycatcher', 'Empidonax occidentalis': 'Cordilleran Flycatcher', 'Empidonax fulvifrons': 'Buff-breasted Flycatcher', 'Sayornis nigricans': 'Black Phoebe', 'Sayornis phoebe': 'Eastern Phoebe', 'Sayornis saya': "Say's Phoebe", 'Pyrocephalus rubinus': 'Vermilion Flycatcher', 'Lessonia rufa': 'Austral Negrito', 'Hymenops perspicillatus': 'Spectacled Tyrant', 'Muscisaxicola maculirostris': 'Spot-billed Ground-Tyrant', 'Muscisaxicola rufivertex': 'Rufous-naped Ground-Tyrant', 'Muscisaxicola albilora': 'White-browed Ground-Tyrant', 'Agriornis micropterus': 'Gray-bellied Shrike-Tyrant', 'Myiarchus tuberculifer': 'Dusky-capped Flycatcher', 'Myiarchus cinerascens': 'Ash-throated Flycatcher', 'Myiarchus crinitus': 'Great Crested Flycatcher', 'Myiarchus tyrannulus': 'Brown-crested Flycatcher', 'Pitangus sulphuratus': 'Great Kiskadee', 'Myiodynastes maculatus': 'Streaked Flycatcher', 'Myiodynastes luteiventris': 'Sulphur-bellied Flycatcher', 'Legatus leucophaius': 'Piratic Flycatcher', 'Tyrannus niveigularis': 'Snowy-throated Kingbird', 'Tyrannus melancholicus': 'Tropical Kingbird', 'Tyrannus couchii': "Couch's Kingbird", 'Tyrannus vociferans': "Cassin's Kingbird", 'Tyrannus crassirostris': 'Thick-billed Kingbird', 'Tyrannus verticalis': 'Western Kingbird', 'Tyrannus tyrannus': 'Eastern Kingbird', 'Tyrannus dominicensis': 'Gray Kingbird', 'Tyrannus forficatus': 'Scissor-tailed Flycatcher', 'Tyrannus savana': 'Fork-tailed Flycatcher', 'Prosthemadera novaeseelandiae': 'Tui', 'Anthornis melanura': 'New Zealand Bellbird', 'Pardalotus striatus': 'Striated Pardalote', 'Lalage tricolor': 'White-winged Triller', 'Mohoua albicilla': 'Whitehead', 'Cyclarhis gujanensis': 'Rufous-browed Peppershrike', 'Vireolanius pulchellus': 'Green Shrike-Vireo', 'Vireo atricapilla': 'Black-capped Vireo', 'Vireo griseus': 'White-eyed Vireo', 'Vireo pallens': 'Mangrove Vireo', 'Vireo bellii': "Bell's Vireo", 'Vireo vicinior': 'Gray Vireo', 'Vireo huttoni': "Hutton's Vireo", 'Vireo flavifrons': 'Yellow-throated Vireo', 'Vireo cassinii': "Cassin's Vireo", 'Vireo solitarius': 'Blue-headed Vireo', 'Vireo plumbeus': 'Plumbeous Vireo', 'Vireo philadelphicus': 'Philadelphia Vireo', 'Vireo gilvus': 'Warbling Vireo', 'Vireo leucophrys': 'Brown-capped Vireo', 'Vireo olivaceus': 'Red-eyed Vireo', 'Vireo flavoviridis': 'Yellow-green Vireo', 'Vireo altiloquus': 'Black-whiskered Vireo', 'Aegithina nigrolutea': 'White-tailed Iora', 'Rhipidura javanica': 'Malaysian Pied-Fantail', 'Rhipidura rufifrons': 'Rufous Fantail', 'Rhipidura albiscapa': 'Gray Fantail', 'Rhipidura fuliginosa': 'New Zealand Fantail', 'Terpsiphone paradisi': 'Indian Paradise-Flycatcher', 'Myiagra rubecula': 'Leaden Flycatcher', 'Lanius collurio': 'Red-backed Shrike', 'Lanius cristatus': 'Brown Shrike', 'Lanius schach': 'Long-tailed Shrike', 'Lanius ludovicianus': 'Loggerhead Shrike', 'Lanius borealis': 'Northern Shrike', 'Lanius meridionalis': 'Iberian Gray Shrike', 'Lanius minor': 'Lesser Gray Shrike', 'Lanius collaris': 'Southern Fiscal', 'Lanius senator': 'Woodchat Shrike', 'Perisoreus canadensis': 'Canada Jay', 'Psilorhinus morio': 'Brown Jay', 'Cyanocorax yncas': 'Green Jay', 'Cyanocorax melanocyaneus': 'Bushy-crested Jay', 'Gymnorhinus cyanocephalus': 'Pinyon Jay', 'Cyanocitta stelleri': "Steller's Jay", 'Cyanocitta cristata': 'Blue Jay', 'Aphelocoma coerulescens': 'Florida Scrub-Jay', 'Aphelocoma insularis': 'Island Scrub-Jay', 'Aphelocoma californica': 'California Scrub-Jay', 'Aphelocoma woodhouseii': "Woodhouse's Scrub-Jay", 'Aphelocoma wollweberi': 'Mexican Jay', 'Cyanopica cooki': 'Iberian Magpie', 'Cyanopica cyanus': 'Azure-winged Magpie', 'Dendrocitta leucogastra': 'White-bellied Treepie', 'Pica hudsonia': 'Black-billed Magpie', 'Pica nuttalli': 'Yellow-billed Magpie', 'Nucifraga columbiana': "Clark's Nutcracker", 'Pyrrhocorax pyrrhocorax': 'Red-billed Chough', 'Pyrrhocorax graculus': 'Yellow-billed Chough', 'Corvus brachyrhynchos': 'American Crow', 'Corvus ossifragus': 'Fish Crow', 'Corvus cryptoleucus': 'Chihuahuan Raven', 'Corvus corax': 'Common Raven', 'Petroica longipes': 'North Island Robin', 'Petroica australis': 'South Island Robin', 'Lophophanes cristatus': 'Crested Tit', 'Poecile lugubris': 'Sombre Tit', 'Poecile palustris': 'Marsh Tit', 'Poecile carolinensis': 'Carolina Chickadee', 'Poecile atricapillus': 'Black-capped Chickadee', 'Poecile gambeli': 'Mountain Chickadee', 'Poecile sclateri': 'Mexican Chickadee', 'Poecile rufescens': 'Chestnut-backed Chickadee', 'Poecile hudsonicus': 'Boreal Chickadee', 'Poecile cinctus': 'Gray-headed Chickadee', 'Cyanistes caeruleus': 'Eurasian Blue Tit', 'Baeolophus wollweberi': 'Bridled Titmouse', 'Baeolophus inornatus': 'Oak Titmouse', 'Baeolophus ridgwayi': 'Juniper Titmouse', 'Baeolophus bicolor': 'Tufted Titmouse', 'Baeolophus atricristatus': 'Black-crested Titmouse', 'Parus major': 'Great Tit', 'Auriparus flaviceps': 'Verdin', 'Eremophila alpestris': 'Horned Lark', 'Lullula arborea': 'Wood Lark', 'Alauda arvensis': 'Eurasian Skylark', 'Prinia maculosa': 'Karoo Prinia', 'Hippolais polyglotta': 'Melodious Warbler', 'Acrocephalus dumetorum': "Blyth's Reed Warbler", 'Acrocephalus scirpaceus': 'Eurasian Reed Warbler', 'Acrocephalus arundinaceus': 'Great Reed Warbler', 'Locustella luscinioides': "Savi's Warbler", 'Locustella naevia': 'Common Grasshopper-Warbler', 'Pygochelidon cyanoleuca': 'Blue-and-white Swallow', 'Orochelidon murina': 'Brown-bellied Swallow', 'Stelgidopteryx serripennis': 'Northern Rough-winged Swallow', 'Progne subis': 'Purple Martin', 'Progne chalybea': 'Gray-breasted Martin', 'Progne elegans': 'Southern Martin', 'Progne tapera': 'Brown-chested Martin', 'Tachycineta bicolor': 'Tree Swallow', 'Tachycineta albiventer': 'White-winged Swallow', 'Tachycineta thalassina': 'Violet-green Swallow', 'Riparia riparia': 'Bank Swallow', 'Hirundo rustica': 'Barn Swallow', 'Cecropis daurica': 'Red-rumped Swallow', 'Petrochelidon pyrrhonota': 'Cliff Swallow', 'Petrochelidon fulva': 'Cave Swallow', 'Delichon urbicum': 'Common House-Martin', 'Pycnonotus sinensis': 'Light-vented Bulbul', 'Pycnonotus xanthopygos': 'White-spectacled Bulbul', 'Pycnonotus xantholaemus': 'Yellow-throated Bulbul', 'Hypsipetes leucocephalus': 'Black Bulbul', 'Phylloscopus bonelli': "Western Bonelli's Warbler", 'Phylloscopus trochilus': 'Willow Warbler', 'Phylloscopus collybita': 'Common Chiffchaff', 'Phylloscopus ibericus': 'Iberian Chiffchaff', 'Phylloscopus borealis': 'Arctic Warbler', 'Phylloscopus occipitalis': 'Western Crowned Warbler', 'Horornis diphone': 'Japanese Bush Warbler', 'Psaltriparus minimus': 'Bushtit', 'Sylvia atricapilla': 'Eurasian Blackcap', 'Curruca melanocephala': 'Sardinian Warbler', 'Curruca undata': 'Dartford Warbler', 'Fulvetta vinipectus': 'White-browed Fulvetta', 'Chamaea fasciata': 'Wrentit', 'Zosterops virens': 'Cape White-eye', 'Dumetia atriceps': 'Dark-fronted Babbler', 'Trochalopteron erythrocephalum': 'Chestnut-crowned Laughingthrush', 'Heterophasia auricularis': 'White-eared Sibia', 'Pterorhinus delesserti': 'Wayanad Laughingthrush', 'Corthylio calendula': 'Ruby-crowned Kinglet', 'Regulus satrapa': 'Golden-crowned Kinglet', 'Regulus ignicapilla': 'Common Firecrest', 'Sitta castanea': 'Indian Nuthatch', 'Sitta canadensis': 'Red-breasted Nuthatch', 'Sitta carolinensis': 'White-breasted Nuthatch', 'Sitta pygmaea': 'Pygmy Nuthatch', 'Sitta pusilla': 'Brown-headed Nuthatch', 'Certhia americana': 'Brown Creeper', 'Certhia brachydactyla': 'Short-toed Treecreeper', 'Polioptila caerulea': 'Blue-gray Gnatcatcher', 'Polioptila melanura': 'Black-tailed Gnatcatcher', 'Polioptila californica': 'California Gnatcatcher', 'Salpinctes obsoletus': 'Rock Wren', 'Catherpes mexicanus': 'Canyon Wren', 'Troglodytes aedon': 'House Wren', 'Troglodytes pacificus': 'Pacific Wren', 'Troglodytes hiemalis': 'Winter Wren', 'Cistothorus stellaris': 'Sedge Wren', 'Cistothorus palustris': 'Marsh Wren', 'Thryothorus ludovicianus': 'Carolina Wren', 'Thryomanes bewickii': "Bewick's Wren", 'Campylorhynchus rufinucha': 'Rufous-naped Wren', 'Campylorhynchus brunneicapillus': 'Cactus Wren', 'Cinclus mexicanus': 'American Dipper', 'Sturnus vulgaris': 'European Starling', 'Sturnus unicolor': 'Spotless Starling', 'Acridotheres tristis': 'Common Myna', 'Lamprotornis superbus': 'Superb Starling', 'Dumetella carolinensis': 'Gray Catbird', 'Toxostoma curvirostre': 'Curve-billed Thrasher', 'Toxostoma rufum': 'Brown Thrasher', 'Toxostoma longirostre': 'Long-billed Thrasher', 'Toxostoma bendirei': "Bendire's Thrasher", 'Toxostoma redivivum': 'California Thrasher', 'Toxostoma lecontei': "LeConte's Thrasher", 'Toxostoma crissale': 'Crissal Thrasher', 'Oreoscoptes montanus': 'Sage Thrasher', 'Mimus triurus': 'White-banded Mockingbird', 'Mimus polyglottos': 'Northern Mockingbird', 'Sialia sialis': 'Eastern Bluebird', 'Sialia mexicana': 'Western Bluebird', 'Sialia currucoides': 'Mountain Bluebird', 'Myadestes townsendi': "Townsend's Solitaire", 'Ixoreus naevius': 'Varied Thrush', 'Catharus aurantiirostris': 'Orange-billed Nightingale-Thrush', 'Catharus fuscescens': 'Veery', 'Catharus minimus': 'Gray-cheeked Thrush', 'Catharus bicknelli': "Bicknell's Thrush", 'Catharus ustulatus': "Swainson's Thrush", 'Catharus guttatus': 'Hermit Thrush', 'Hylocichla mustelina': 'Wood Thrush', 'Turdus flavipes': 'Yellow-legged Thrush', 'Turdus grayi': 'Clay-colored Thrush', 'Turdus migratorius': 'American Robin', 'Turdus fuscater': 'Great Thrush', 'Muscicapa ferruginea': 'Ferruginous Flycatcher', 'Muscicapa muttui': 'Brown-breasted Flycatcher', 'Cercotrichas galactotes': 'Rufous-tailed Scrub-Robin', 'Copsychus fulicatus': 'Indian Robin', 'Copsychus saularis': 'Oriental Magpie-Robin', 'Erithacus rubecula': 'European Robin', 'Larvivora brunnea': 'Indian Blue Robin', 'Irania gutturalis': 'White-throated Robin', 'Luscinia luscinia': 'Thrush Nightingale', 'Luscinia svecica': 'Bluethroat', 'Ficedula hypoleuca': 'European Pied Flycatcher', 'Phoenicurus phoenicurus': 'Common Redstart', 'Phoenicurus ochruros': 'Black Redstart', 'Phoenicurus auroreus': 'Daurian Redstart', 'Monticola saxatilis': 'Rufous-tailed Rock-Thrush', 'Monticola solitarius': 'Blue Rock-Thrush', 'Saxicola rubicola': 'European Stonechat', 'Oenanthe oenanthe': 'Northern Wheatear', 'Bombycilla garrulus': 'Bohemian Waxwing', 'Bombycilla cedrorum': 'Cedar Waxwing', 'Phainopepla nitens': 'Phainopepla', 'Peucedramus taeniatus': 'Olive Warbler', 'Plocepasser mahali': 'White-browed Sparrow-Weaver', 'Lonchura punctulata': 'Scaly-breasted Munia', 'Prunella modularis': 'Dunnock', 'Passer domesticus': 'House Sparrow', 'Passer cinnamomeus': 'Russet Sparrow', 'Passer montanus': 'Eurasian Tree Sparrow', 'Motacilla cinerea': 'Gray Wagtail', 'Motacilla flava': 'Western Yellow Wagtail', 'Motacilla tschutschensis': 'Eastern Yellow Wagtail', 'Motacilla alba': 'White Wagtail', 'Anthus novaeseelandiae': 'Australasian Pipit', 'Anthus berthelotii': "Berthelot's Pipit", 'Anthus pratensis': 'Meadow Pipit', 'Anthus trivialis': 'Tree Pipit', 'Anthus petrosus': 'Rock Pipit', 'Anthus rubescens': 'American Pipit', 'Anthus spragueii': "Sprague's Pipit", 'Fringilla coelebs': 'Common Chaffinch', 'Chlorophonia cyanocephala': 'Golden-rumped Euphonia', 'Coccothraustes vespertinus': 'Evening Grosbeak', 'Pinicola enucleator': 'Pine Grosbeak', 'Leucosticte tephrocotis': 'Gray-crowned Rosy-Finch', 'Leucosticte atrata': 'Black Rosy-Finch', 'Leucosticte australis': 'Brown-capped Rosy-Finch', 'Haemorhous mexicanus': 'House Finch', 'Haemorhous purpureus': 'Purple Finch', 'Haemorhous cassinii': "Cassin's Finch", 'Acanthis flammea': 'Common Redpoll', 'Acanthis hornemanni': 'Hoary Redpoll', 'Loxia curvirostra': 'Red Crossbill', 'Loxia sinesciuris': 'Cassia Crossbill', 'Loxia leucoptera': 'White-winged Crossbill', 'Serinus serinus': 'European Serin', 'Spinus pinus': 'Pine Siskin', 'Spinus psaltria': 'Lesser Goldfinch', 'Spinus lawrencei': "Lawrence's Goldfinch", 'Spinus tristis': 'American Goldfinch', 'Calcarius lapponicus': 'Lapland Longspur', 'Calcarius ornatus': 'Chestnut-collared Longspur', 'Calcarius pictus': "Smith's Longspur", 'Rhynchophanes mccownii': 'Thick-billed Longspur', 'Plectrophenax nivalis': 'Snow Bunting', 'Emberiza cirlus': 'Cirl Bunting', 'Emberiza citrinella': 'Yellowhammer', 'Emberiza hortulana': 'Ortolan Bunting', 'Emberiza aureola': 'Yellow-breasted Bunting', 'Oreothraupis arremonops': 'Tanager Finch', 'Peucaea carpalis': 'Rufous-winged Sparrow', 'Peucaea cassinii': "Cassin's Sparrow", 'Peucaea aestivalis': "Bachman's Sparrow", 'Ammodramus savannarum': 'Grasshopper Sparrow', 'Arremonops rufivirgatus': 'Olive Sparrow', 'Amphispizopsis quinquestriata': 'Five-striped Sparrow', 'Spizella passerina': 'Chipping Sparrow', 'Spizella pallida': 'Clay-colored Sparrow', 'Spizella atrogularis': 'Black-chinned Sparrow', 'Spizella pusilla': 'Field Sparrow', 'Spizella breweri': "Brewer's Sparrow", 'Amphispiza bilineata': 'Black-throated Sparrow', 'Chondestes grammacus': 'Lark Sparrow', 'Calamospiza melanocorys': 'Lark Bunting', 'Spizelloides arborea': 'American Tree Sparrow', 'Passerella iliaca': 'Fox Sparrow', 'Junco hyemalis': 'Dark-eyed Junco', 'Junco phaeonotus': 'Yellow-eyed Junco', 'Zonotrichia capensis': 'Rufous-collared Sparrow', 'Zonotrichia leucophrys': 'White-crowned Sparrow', 'Zonotrichia atricapilla': 'Golden-crowned Sparrow', 'Zonotrichia querula': "Harris's Sparrow", 'Zonotrichia albicollis': 'White-throated Sparrow', 'Artemisiospiza nevadensis': 'Sagebrush Sparrow', 'Artemisiospiza belli': "Bell's Sparrow", 'Pooecetes gramineus': 'Vesper Sparrow', 'Ammospiza leconteii': "LeConte's Sparrow", 'Ammospiza maritima': 'Seaside Sparrow', 'Ammospiza nelsoni': "Nelson's Sparrow", 'Ammospiza caudacuta': 'Saltmarsh Sparrow', 'Passerculus sandwichensis': 'Savannah Sparrow', 'Centronyx bairdii': "Baird's Sparrow", 'Centronyx henslowii': "Henslow's Sparrow", 'Melospiza melodia': 'Song Sparrow', 'Melospiza lincolnii': "Lincoln's Sparrow", 'Melospiza georgiana': 'Swamp Sparrow', 'Melozone fusca': 'Canyon Towhee', 'Melozone aberti': "Abert's Towhee", 'Melozone crissalis': 'California Towhee', 'Melozone leucotis': 'White-eared Ground-Sparrow', 'Melozone biarcuata': 'White-faced Ground-Sparrow', 'Aimophila ruficeps': 'Rufous-crowned Sparrow', 'Pipilo chlorurus': 'Green-tailed Towhee', 'Pipilo maculatus': 'Spotted Towhee', 'Pipilo erythrophthalmus': 'Eastern Towhee', 'Atlapetes flaviceps': 'Yellow-headed Brushfinch', 'Nesospingus speculiferus': 'Puerto Rican Tanager', 'Icteria virens': 'Yellow-breasted Chat', 'Xanthocephalus xanthocephalus': 'Yellow-headed Blackbird', 'Dolichonyx oryzivorus': 'Bobolink', 'Sturnella neglecta': 'Western Meadowlark', 'Sturnella magna': 'Eastern Meadowlark', 'Psarocolius wagleri': 'Chestnut-headed Oropendola', 'Icterus portoricensis': 'Puerto Rican Oriole', 'Icterus spurius': 'Orchard Oriole', 'Icterus cucullatus': 'Hooded Oriole', 'Icterus bullockii': "Bullock's Oriole", 'Icterus gularis': 'Altamira Oriole', 'Icterus graduacauda': "Audubon's Oriole", 'Icterus galbula': 'Baltimore Oriole', 'Icterus abeillei': 'Black-backed Oriole', 'Icterus parisorum': "Scott's Oriole", 'Agelaius phoeniceus': 'Red-winged Blackbird', 'Agelaius tricolor': 'Tricolored Blackbird', 'Molothrus rufoaxillaris': 'Screaming Cowbird', 'Molothrus bonariensis': 'Shiny Cowbird', 'Molothrus aeneus': 'Bronzed Cowbird', 'Molothrus ater': 'Brown-headed Cowbird', 'Euphagus carolinus': 'Rusty Blackbird', 'Euphagus cyanocephalus': "Brewer's Blackbird", 'Quiscalus quiscula': 'Common Grackle', 'Quiscalus major': 'Boat-tailed Grackle', 'Quiscalus mexicanus': 'Great-tailed Grackle', 'Quiscalus nicaraguensis': 'Nicaraguan Grackle', 'Hypopyrrhus pyrohypogaster': 'Red-bellied Grackle', 'Xanthopsar flavus': 'Saffron-cowled Blackbird', 'Seiurus aurocapilla': 'Ovenbird', 'Helmitheros vermivorum': 'Worm-eating Warbler', 'Parkesia motacilla': 'Louisiana Waterthrush', 'Parkesia noveboracensis': 'Northern Waterthrush', 'Vermivora chrysoptera': 'Golden-winged Warbler', 'Vermivora cyanoptera': 'Blue-winged Warbler', 'Mniotilta varia': 'Black-and-white Warbler', 'Protonotaria citrea': 'Prothonotary Warbler', 'Limnothlypis swainsonii': "Swainson's Warbler", 'Oreothlypis superciliosa': 'Crescent-chested Warbler', 'Oreothlypis gutturalis': 'Flame-throated Warbler', 'Leiothlypis peregrina': 'Tennessee Warbler', 'Leiothlypis celata': 'Orange-crowned Warbler', 'Leiothlypis crissalis': 'Colima Warbler', 'Leiothlypis luciae': "Lucy's Warbler", 'Leiothlypis ruficapilla': 'Nashville Warbler', 'Leiothlypis virginiae': "Virginia's Warbler", 'Oporornis agilis': 'Connecticut Warbler', 'Geothlypis poliocephala': 'Gray-crowned Yellowthroat', 'Geothlypis aequinoctialis': 'Masked Yellowthroat', 'Geothlypis tolmiei': "MacGillivray's Warbler", 'Geothlypis philadelphia': 'Mourning Warbler', 'Geothlypis formosa': 'Kentucky Warbler', 'Geothlypis semiflava': 'Olive-crowned Yellowthroat', 'Geothlypis speciosa': 'Black-polled Yellowthroat', 'Geothlypis beldingi': "Belding's Yellowthroat", 'Geothlypis rostrata': 'Bahama Yellowthroat', 'Geothlypis flavovelata': 'Altamira Yellowthroat', 'Geothlypis trichas': 'Common Yellowthroat', 'Catharopeza bishopi': 'Whistling Warbler', 'Setophaga plumbea': 'Plumbeous Warbler', 'Setophaga angelae': 'Elfin-woods Warbler', 'Setophaga pharetra': 'Arrowhead Warbler', 'Setophaga citrina': 'Hooded Warbler', 'Setophaga ruticilla': 'American Redstart', 'Setophaga kirtlandii': "Kirtland's Warbler", 'Setophaga tigrina': 'Cape May Warbler', 'Setophaga cerulea': 'Cerulean Warbler', 'Setophaga americana': 'Northern Parula', 'Setophaga pitiayumi': 'Tropical Parula', 'Setophaga magnolia': 'Magnolia Warbler', 'Setophaga castanea': 'Bay-breasted Warbler', 'Setophaga fusca': 'Blackburnian Warbler', 'Setophaga petechia': 'Yellow Warbler', 'Setophaga pensylvanica': 'Chestnut-sided Warbler', 'Setophaga striata': 'Blackpoll Warbler', 'Setophaga caerulescens': 'Black-throated Blue Warbler', 'Setophaga palmarum': 'Palm Warbler', 'Setophaga pityophila': 'Olive-capped Warbler', 'Setophaga pinus': 'Pine Warbler', 'Setophaga coronata': 'Yellow-rumped Warbler', 'Setophaga dominica': 'Yellow-throated Warbler', 'Setophaga flavescens': 'Bahama Warbler', 'Setophaga vitellina': 'Vitelline Warbler', 'Setophaga discolor': 'Prairie Warbler', 'Setophaga adelaidae': "Adelaide's Warbler", 'Setophaga subita': 'Barbuda Warbler', 'Setophaga delicata': 'St. Lucia Warbler', 'Setophaga graciae': "Grace's Warbler", 'Setophaga nigrescens': 'Black-throated Gray Warbler', 'Setophaga townsendi': "Townsend's Warbler", 'Setophaga occidentalis': 'Hermit Warbler', 'Setophaga chrysoparia': 'Golden-cheeked Warbler', 'Setophaga virens': 'Black-throated Green Warbler', 'Basileuterus lachrymosus': 'Fan-tailed Warbler', 'Basileuterus rufifrons/delattrii': 'Rufous-capped/Chestnut-capped Warbler', 'Basileuterus melanogenys': 'Black-cheeked Warbler', 'Basileuterus belli': 'Golden-browed Warbler', 'Basileuterus culicivorus': 'Golden-crowned Warbler', 'Basileuterus melanotis': 'Costa Rican Warbler', 'Basileuterus tristriatus': 'Three-striped Warbler', 'Myiothlypis basilica': 'Santa Marta Warbler', 'Myiothlypis luteoviridis': 'Citrine Warbler', 'Myiothlypis leucophrys': 'White-striped Warbler', 'Myiothlypis flaveola': 'Flavescent Warbler', 'Myiothlypis leucoblephara': 'White-browed Warbler', 'Myiothlypis signata': 'Pale-legged Warbler', 'Myiothlypis nigrocristata': 'Black-crested Warbler', 'Myiothlypis fulvicauda': 'Buff-rumped Warbler', 'Myiothlypis rivularis': 'Riverbank Warbler', 'Myiothlypis bivittata': 'Two-banded Warbler', 'Myiothlypis chrysogaster': 'Golden-bellied Warbler', 'Myiothlypis cinereicollis': 'Gray-throated Warbler', 'Myiothlypis conspicillata': 'White-lored Warbler', 'Myiothlypis fraseri': 'Gray-and-gold Warbler', 'Myiothlypis coronata': 'Russet-crowned Warbler', 'Cardellina canadensis': 'Canada Warbler', 'Cardellina pusilla': "Wilson's Warbler", 'Cardellina rubrifrons': 'Red-faced Warbler', 'Cardellina rubra': 'Red Warbler', 'Cardellina versicolor': 'Pink-headed Warbler', 'Myioborus pictus': 'Painted Redstart', 'Myioborus miniatus': 'Slate-throated Redstart', 'Myioborus brunniceps': 'Brown-capped Redstart', 'Myioborus torquatus': 'Collared Redstart', 'Myioborus ornatus': 'Golden-fronted Redstart', 'Myioborus melanocephalus': 'Spectacled Redstart', 'Myioborus albifrons': 'White-fronted Redstart', 'Piranga flava': 'Hepatic Tanager', 'Piranga rubra': 'Summer Tanager', 'Piranga olivacea': 'Scarlet Tanager', 'Piranga ludoviciana': 'Western Tanager', 'Habia cristata': 'Crested Ant-Tanager', 'Rhodothraupis celaeno': 'Crimson-collared Grosbeak', 'Cardinalis cardinalis': 'Northern Cardinal', 'Cardinalis sinuatus': 'Pyrrhuloxia', 'Pheucticus ludovicianus': 'Rose-breasted Grosbeak', 'Pheucticus melanocephalus': 'Black-headed Grosbeak', 'Cyanocompsa parellina': 'Blue Bunting', 'Passerina caerulea': 'Blue Grosbeak', 'Passerina amoena': 'Lazuli Bunting', 'Passerina cyanea': 'Indigo Bunting', 'Passerina ciris': 'Painted Bunting', 'Spiza americana': 'Dickcissel', 'Bangsia melanochlamys': 'Black-and-gold Tanager', 'Bangsia edwardsi': 'Moss-backed Tanager', 'Bangsia aureocincta': 'Gold-ringed Tanager', 'Thraupis episcopus': 'Blue-gray Tanager', 'Stilpnia vitriolina': 'Scrub Tanager', 'Tangara chilensis': 'Paradise Tanager', 'Dacnis hartlaubi': 'Turquoise Dacnis', 'Cyanerpes cyaneus': 'Red-legged Honeycreeper', 'Rhopospina alaudina': 'Band-tailed Sierra Finch', 'Sicalis taczanowskii': 'Sulphur-throated Finch', 'Volatinia jacarina': 'Blue-black Grassquit', 'Sporophila lineola': 'Lined Seedeater', 'Sporophila morelleti': "Morelet's Seedeater", 'Rhodospingus cruentus': 'Crimson-breasted Finch'}



#%% Optionally process counts to restrict observations only to the US    
if FLAG_ONLY_USE_USA_OBSERVATIONS:
    USA_statelist = list(REALSTATEBIRDS.keys())
    USA_new_genus_count = Counter()
    USA_new_species_count = Counter() 
    USA_new_genus_state_count = Counter() 
    USA_new_species_state_count = Counter() 
    USA_GRANDTOTAL = 0
    for state in USA_statelist:
        USA_GRANDTOTAL += state_count[state]
        for genus in genus_count.keys():
            count = genus_state_count[(genus,state)]
            USA_new_genus_count[genus] += count
            USA_new_genus_state_count[(genus,state)] += count
        for species in species_count.keys():
            count = species_state_count[(species,state)]
            USA_new_species_count[species] += count
            USA_new_species_state_count[(species,state)] += count

    genus_count = +USA_new_genus_count
    species_count = +USA_new_species_count
    genus_state_count = +USA_new_genus_state_count
    species_state_count = +USA_new_species_state_count
    GRANDTOTAL = USA_GRANDTOTAL
    

#%% Check against our filter flags to decide how to clean problem birds. 

n_purged = 0

for species in species_count:
    genus = species.split(' ')[0]
    n_species = species_count[species]
    #assert genus in genus_count.keys() # (It works.)
    
    if FLAG_RESTRICT_TO_BBS_BIRDS and species not in BBS_SPECIES_LIST:
        flag_purge_this_bird = True
    elif FLAG_EXCLUDE_VERBOTEN_BIRDS and species in VERBOTEN_SPECIES: 
        flag_purge_this_bird = True
    elif FLAG_RESTRICT_TO_EBIRD_COMMONNAME_KEYBIRDS and species not in eBird_commonname_map.keys():
        flag_purge_this_bird = True
        
    elif FLAG_EXCLUDE_FAMILY_LABELLED_AS_GENUS and 'inae sp' in species: #subfamily
        flag_purge_this_bird = True
    elif FLAG_EXCLUDE_FAMILY_LABELLED_AS_GENUS and 'idae sp' in species: #family
        flag_purge_this_bird = True
    elif FLAG_EXCLUDE_FAMILY_LABELLED_AS_GENUS and 'formes sp' in species: #order
        flag_purge_this_bird = True
    elif FLAG_EXCLUDE_FAMILY_LABELLED_AS_GENUS and 'Aves' == genus: 
        flag_purge_this_bird = True
        print(species,n_species)
    #elif FLAG_EXCLUDE_FAMILY_LABELLED_AS_GENUS and genus in FAMILY_LABELLED_AS_GENUS: 
    #    flag_purge_this_bird = True
    
    elif FLAG_EXCLUDE_AMBIGUOUS_GENUS and '/' in genus: 
        flag_purge_this_bird = True
    elif FLAG_EXCLUDE_AMBIGUOUS_SPECIES and '/' in species: 
        flag_purge_this_bird = True
    elif FLAG_EXCLUDE_UNKNOWN_SPECIES and 'sp.' in species: 
        flag_purge_this_bird = True
    elif FLAG_EXCLUDE_HYBRID_SPECIES and ' x ' in species: 
        flag_purge_this_bird = True
    elif FLAG_EXCLUDE_DOMESTIC_TYPE and '(Domestic type)' in species: 
        flag_purge_this_bird = True
        
    elif n_species < CUTOFF:
        #print("Too uncommon:",species,n_species)
        flag_purge_this_bird = True
    else:
        flag_purge_this_bird = False
    
    # Now that we've figured out whether to purge the bird, let's do so at most once.
    if flag_purge_this_bird:
        n_purged+=1
        n_species = species_count[species] # Put this down here, so we don't double-purge a species.
        #print(species,n_species)
        GRANDTOTAL -= n_species
        genus_count[genus] -= n_species
        species_count[species] -= n_species
        assert species_count[species] == 0
        
        for state in state_count.keys():
            n_joint = species_state_count[(species,state)]
            genus_state_count[(genus,state)] -= n_joint
            species_state_count[(species,state)] -= n_joint
           
#Clean up remaining mess. Remove the 0s from dictionary.
species_state_count = +species_state_count
genus_state_count = +genus_state_count
species_count = +species_count
genus_count = +genus_count

#%% Template Functions. They are written generically, 
# so that I should be able to plug in whatever metric I want.
# (As long as that metric is derived from the confusion matrix.)


def calculate_genus_scores(metric):
    results = dict()
    for item in genus_state_count.items():
        genus = item[0][0]
        state = item[0][1]
        n_joint = genus_state_count[(genus,state)]
        n_state = state_count[state]
        n_genus = genus_count[genus]
        # Exclude genus which has been filtered out. 
        if n_genus > 0: 
            score = metric(n_joint,n_state,n_genus)
        else:
            score = -9999
        results[(genus,state)] = (n_joint,score)
    sorted_results = sorted(results.items(), key=lambda item: (-item[1][1],-item[1][0]))
    return sorted_results

def calculate_species_scores(metric):
    results = dict()
    for item in species_state_count.items():
        species = item[0][0]
        state = item[0][1]
        n_joint = species_state_count[(species,state)]
        n_state = state_count[state]
        n_species = species_count[species]
        # Exclude species which has been filtered out. 
        if n_species > 0: 
            score = metric(n_joint,n_state,n_species)
        else:
            score = -999999
        results[(species,state)] = (n_joint,score)
    sorted_results = sorted(results.items(), key=lambda item: (-item[1][1],-item[1][0]))
    return sorted_results

def subsort_by_state(birdscore):
    return sorted(birdscore, key=lambda item: item[0][1])


#%% Functions for saving to Output Files


def scoreitem_to_rowlist(item):
    n_joint=str(item[1][0])
    if item[1][1] < -1000:
        return False
    score = "{:.6f}".format(item[1][1])
    #return '|'+item[0][0]+'|'+item[0][1]+'|'+n_joint+'|'+score+'|'
    return item[0][0]+','+item[0][1]+','+n_joint+','+score
    
def save_scorelist(filename,scorelist,extension=".csv"):
    filepath = os.path.join(THIS_FOLDER,"BIRDUP",filename+extension)
    with open(filepath,'w') as birdfile:
        #birdfile.write('|Bird|State|Count|Score|\n|---|---|---|---|\n')
        birdfile.write('Bird,State,Count,Score\n')
        birdfile.write('\n'.join([scoreitem_to_rowlist(item) for item in scorelist if scoreitem_to_rowlist(item)]))
        birdfile.write('\n')

def save_list(filename,scorelist,extension=".md"):
    filepath = os.path.join(THIS_FOLDER,"BIRDUP",filename+extension)
    with open(filepath,'w', encoding="utf-8") as birdfile:
        birdfile.write('\n'.join([str(item) for item in scorelist]))
        birdfile.write('\n')
        
        
        
#%% Functions for ranking and organizing the score lists.        
        
def quick_top_birdscores(scorelist):
    "Find the top scoring (first appearing) bird for each state."
    "Only works if birds are pre-sorted."
    birdmapping = dict()
    for entry in scorelist:
        state = entry[0][1]
        if state not in statemap.keys():
            continue
        bird = entry[0][0]
        score = entry[1][1]
        if state not in birdmapping:
            birdmapping[state] = entry
    #for state in state_count: #Iterate through this list of keys bc they are pre-sorted.
    return [birdmapping[state] for state in sorted(birdmapping.keys())]

def find_duplicate_topbirds(top_birds):
    birds = [item[0][0] for item in top_birds]
    birdcount =  Counter(birds)
    # subtract 1 from each bird
    birdcount.subtract(Counter(set(birds)))
    # clear out the singular (now zero) birds
    dupebirds = +birdcount
    # Add 1 back to each bird
    return dupebirds+Counter(dupebirds.keys())

def quick_top_statescores(scorelist):
    "Find the top scoring state for each bird, as a way of preventing duplicates."
    "Only works if birds are pre-sorted."
    #This method has problems. Some states end up with fluke birds.
    #Sometimes one state is generally more birdular, leaving a neighbor state with scraps.
    statemapping = dict()
    for entry in scorelist:
        state = entry[0][1]
        bird = entry[0][0]
        score = entry[1][1]
        if bird not in statemapping:
            statemapping[bird] = entry
    #for state in state_count: #Iterate through this list of keys bc they are pre-sorted.
    return [statemapping[bird] for bird in statemapping.keys()]

def unique_top_birdscores(scorelist):
    ''' 1. Give each state its top bird.
        2. If two states have the same bird, remove each lower score from the list of options.
        3. Repeat until all states have a unique top bird.'''
    validscorelist = scorelist.copy()
    candidatebirds = []
    
    duplicateFLAG = True
    while (duplicateFLAG == True):
        candidatebirds = quick_top_birdscores(validscorelist)
        candidatebirds = sorted(candidatebirds, key=lambda item: -item[1][1])
        
        encounteredbirdset = set()
        duplicateFLAG = False
        for entry in candidatebirds:
            bird = entry[0][0]
            state = entry[0][1] 
            count = entry[1][0]
            
            if FLAG_EXCLUDE_AMBIGU_SPECIES_FROM_TOP and 'sp.' in bird:
                duplicateFLAG = True #not actually a duplicate, but something to exclude
                validscorelist.remove(entry)
                continue
            if FLAG_EXCLUDE_VERBOTEN_BIRDS_FROM_TOP and bird in VERBOTEN_BIRDS:
                duplicateFLAG = True #not actually a duplicate, but something to exclude
                validscorelist.remove(entry)
                continue
            if FLAG_EXCLUDE_REALSTATEBIRDS_FROM_TOP and bird in REALSTATEBIRD_LIST:
                duplicateFLAG = True #not actually a duplicate, but something to exclude
                validscorelist.remove(entry)
                continue
            if count < STATECUTOFF:
                duplicateFLAG = True #not actually a duplicate, but something to exclude
                validscorelist.remove(entry)
                continue
            
            do_I_care_FLAG = 'US-' in state or FLAG_ENFORCE_UNIQUENESS_ACROSS_ALL_NA 
            if bird in encounteredbirdset and do_I_care_FLAG:
                duplicateFLAG = True
                validscorelist.remove(entry)
            if do_I_care_FLAG:
                encounteredbirdset.add(bird)
            
            
    return sorted(candidatebirds, key=lambda item: item[0][1])
    

#%% Functions for Evaluating how good a set of state birds is.

def compare_to_REALSTATEBIRDS(top_birds):
    score = 0
    matches = []
    for entry in top_birds:
        state = entry[0][1]
        bird = entry[0][0]
        if state in REALSTATEBIRDS.keys():
            #Genus or species match.
            if REALSTATEBIRDS[state] == bird:
                score += 1
                matches.append((bird,state))
            if REALSTATEBIRDS[state].split(' ')[0] == bird:
                score += 1
                matches.append((bird,state))
    return score,matches

def check_for_iconic_birds(top_birds):
    score = 0
    for entry in top_birds:
        state = entry[0][1]
        bird = entry[0][0]
        if state in REALSTATEBIRDS.keys():
            #Genus or species match.
            if bird in ICONICBIRDLIST:
                score += 1
                #print(bird,state)
    return score




#%% Functions for Preparing the markdown tables

def find_example_of_genus(target_state,target_genus,species_scorelist):
    for entry in species_scorelist:
        state = entry[0][1]
        species = entry[0][0]
        if FLAG_EXCLUDE_AMBIGU_SPECIES_FROM_TOP and 'sp.' in species:
            continue
        genus = species.split(' ')[0]
        if state==target_state and genus==target_genus:
            if species:
                return species
            else:
                print("No species found",target_state,target_genus)
                return target_genus
    print("No species found",target_state,target_genus)
    return target_genus

def get_bird_wiki_url(bird):
    "Some bird genus names are simple enough to lead to disambiguation pages."
    if ' sp.' in bird:
        bird = bird.split(' ')[0]
    if bird in wikipedia_mapping:
        return wikipedia_mapping[bird]
    else:
        return 'https://en.wikipedia.org/wiki/'+bird.replace(' ','_')
    
def get_bird_commonname(bird):
    "Look up the scientific name in a dictionary or common names."
    if bird in genus_commonname_map:
        return genus_commonname_map[bird]
    elif bird in eBird_commonname_map:
        return eBird_commonname_map[bird]
    elif bird in BBS_commonname_map:
        return BBS_commonname_map[bird]
    else:
        return ''

def determine_asterisk(bird,state):
    note = ''
    if bird in REALSTATEBIRDS[state]:
        note += '‡'
    elif bird in REALSTATEBIRD_LIST:
        note += '†'
    if bird in VERBOTEN_BIRDS:
        note += '*' #Worried up this borking up the markdown.
    return note


def format_list_as_markdown_table(top_birds, species_scorelist=None):
    markdown_row_list = []
    for entry in top_birds:
        state = entry[0][1]
        bird = entry[0][0]
        count = str(entry[1][0])
        score = "{:.4f}".format(entry[1][1])
        
        note = determine_asterisk(bird,state)
        
        url = get_bird_wiki_url(bird)
        commonname = get_bird_commonname(bird)
        rowstring = '| '+state+' | '+count+' | ['+bird+']('+url+')'+note+' | '+commonname+' |'
        if species_scorelist:
            species = find_example_of_genus(state,bird,species_scorelist)
            commonname_sp = get_bird_commonname(species)
            url_sp = get_bird_wiki_url(species)
            rowstring +=  ' ['+species+']('+url_sp+') | '+commonname_sp+' |'
        #rowstring = '| '+state+' | ['+bird+']('+url+') | '+str(score)+' |'
        markdown_row_list.append(rowstring)
        
    header = ['| State | Count | Bird | Common Name |','|--:|---|---|---|']
    if species_scorelist:
        header[0]+=' Example Species | Common Name |'
        header[1]+='---|---|'
   
    if species_scorelist:
        header = ['### Top Unique State Birds When Sorted by Genus','',]+header
    else: 
        header = ['### Top Unique State Birds When Sorted by Species','',]+header
        
    return header+markdown_row_list    
    
def format_list_as_tables_per_state(scorelist, species_scorelist=None):
    MAX_ROWS_PER_STATE = 10    
    
    titletext = "Top Species for "
    if species_scorelist:
        titletext = "Top Genera for "
    
    markdown_row_list = []
    for state in statemap.keys():
        
        
        
        markdown_row_list.append('### '+titletext+statemap[state]+' ('+state+')\n')
        header = ['| Score | Bird | Common Name | Count |','|---|---|---|---|']
        if species_scorelist:
            header[0]+=' Example Species | Common Name |'
            header[1]+='---|---|'
        markdown_row_list += header
        
        num_rows = 0
        for entry in scorelist:
            if num_rows >= MAX_ROWS_PER_STATE: 
                break
            if state == entry[0][1]:
                num_rows += 1
                bird = entry[0][0]
                score = "{:.4f}".format(entry[1][1])
                count = str(entry[1][0])
                
                note = determine_asterisk(bird,state)
                    
                url = get_bird_wiki_url(bird)
                commonname = get_bird_commonname(bird)
                rowstring = '| '+score+' | ['+bird+']('+url+')'+note+' | '+commonname+' | '+count+' |' 
                
                if species_scorelist:
                    species = find_example_of_genus(state,bird,species_scorelist)
                    commonname_sp = get_bird_commonname(species)
                    url_sp = get_bird_wiki_url(species)
                    rowstring +=  ' ['+species+']('+url_sp+') | '+commonname_sp+' |'
                markdown_row_list.append(rowstring)
        
        markdown_row_list += ['','','','','','',]
        
    return markdown_row_list    


















#%% Wrapper Function to call all of the above in the right order and combine the results.


def do_the_works_gs(filename,metric):
    '''Calculate rankings using both species and Genus. 
    Species score is used in generating genus markdown table.'''
    print("Generating BIRDUP",filename)
    
    species_birdscore = calculate_species_scores(metric)
    sp_summary, sp_states = generate_output_lists(filename+'_species',species_birdscore)
                          
    genus_birdscore = calculate_genus_scores(metric)
    gn_summary, gn_states = generate_output_lists(filename+'_genus',genus_birdscore,species_birdscore)
    
    combined_tables  = ["\n\n\n\n## Top Scoring Unique State Birds\n"]
    combined_tables += ['\n\n']+gn_summary+['\n\n']+sp_summary+['\n\n\n\n']
    combined_tables += ["\n\n\n\n## Scores for Bird Genera by State\n"]+gn_states
    combined_tables += ["\n\n\n\n## Scores for Bird Species by State\n"]+sp_states
    save_list(filename+'_markdownoutputcombined',combined_tables,extension=".md")
    
    
def generate_output_lists(filename,birdscore,species_birdscore=None):
    save_scorelist(filename+'_byscore',birdscore)

    birdscore_bystate = subsort_by_state(birdscore)
    save_scorelist(filename+'_bystate',birdscore_bystate)
    
    top_birds = quick_top_birdscores(birdscore)
    #save_scorelist(filename+'_topbirds',top_birds)
    
    top_states = quick_top_statescores(birdscore)
    #save_scorelist(filename+'_topstates',top_states)
    
    unique_top_birds = unique_top_birdscores(birdscore)
    #save_scorelist(filename+'_uniquetopbirds',unique_top_birds)
    print(compare_to_REALSTATEBIRDS(unique_top_birds))
    
    mdutb_overview = format_list_as_markdown_table(unique_top_birds,species_birdscore)
    #save_list(filename+'_markdownsource',mdutb_overview,extension=".md")
    
    state_tables = format_list_as_tables_per_state(birdscore,species_birdscore)
    #save_list(filename+'_markdownperstate',state_tables,extension=".md")
    
    return mdutb_overview,state_tables

#%% Various metrics

def markedness(n_joint,n_state,n_bird):
    "Calculates the informedness of the state as a diagnostic test for the bird"
    TPR = n_joint / n_bird
    FPR = (n_state - n_joint) / (GRANDTOTAL - n_bird)
    return TPR-FPR
    
def informedness(n_joint,n_state,n_bird):
    "Calculates the informedness of the bird as a diagnostic test for the state"
    TPR = n_joint / n_state
    FPR = (n_bird - n_joint) / (GRANDTOTAL - n_state)
    return TPR-FPR

def YulePhi(n_joint,n_state,n_bird):
    "Calculates the coorelation between state and bird"
    numer = GRANDTOTAL*n_joint - n_state*n_bird
    denom = (n_state*n_bird*(GRANDTOTAL-n_state)*(GRANDTOTAL-n_bird))**(1/2)
    #Weird. This should work. Don't know why it doesn't
    #Oh, it's because these can go negative. That's why.
    #altM = markedness(n_joint,n_state,n_bird)
    #altI = informedness(n_joint,n_state,n_bird)
    #assert (altM*altI)**(1/2) - numer/denom < .01
    return numer/denom


#Get roadrunner for new mexicofor alpha in range 0.5 to 0.7
def paramaterizedPhi(n_joint,n_state,n_bird):
    "YulePhi is geometric mean of marked.. and informed..; this uses some other weighting"
    altM = max(0,markedness(n_joint,n_state,n_bird))
    altI = max(0,informedness(n_joint,n_state,n_bird))
    return (altM**ALPHA_PARAM)*(altI**(1-ALPHA_PARAM))


def normalizedTPR(n_joint,n_state,n_bird):
    "Calculates the naive BIRDUP, but adjusted for density of sitings in that state"
    "Ranking should be equivalent to p(BandS)/(p(B)*p(S))"
    TPR = n_joint / n_bird
    prob_joint = n_joint / GRANDTOTAL
    prob_bird = n_bird / GRANDTOTAL
    prob_state = n_state / GRANDTOTAL
    assert abs(prob_joint/(prob_bird*prob_state)-GRANDTOTAL*TPR/n_state) < 0.001
    return prob_joint/(prob_bird*prob_state)

def naiveprevalence(n_joint,n_state,n_bird):
    "What fraction of birds in that state are that bird?"
    return n_joint / n_state


def agreement(n_joint,n_state,n_bird):
    "percent of observations which are bird in state or !bird in !state"
    TN = GRANDTOTAL - n_state - n_bird + n_joint
    return (TN + n_joint) / GRANDTOTAL

def jaccard(n_joint,n_state,n_bird):
    "Jaccard index is intersection over union"
    TN = GRANDTOTAL - n_state - n_bird + n_joint
    return (n_joint) / (GRANDTOTAL-TN)

def fowlkes_mallows(n_joint,n_state,n_bird):
    ""
    return np.sqrt((n_joint / n_bird) * (n_joint / n_state))

def cohenkappa(n_joint,n_state,n_bird):
    "Agreement adjusted for chance agreement."
    po = agreement(n_joint,n_state,n_bird)
    prob_bird = n_bird / GRANDTOTAL
    prob_state = n_state / GRANDTOTAL
    pe = prob_bird*prob_state + (1-prob_bird)*(1-prob_state)
    return (po - pe) / (1 - pe)


def basicbirdup(n_joint,n_state,n_bird):
    ""
    return n_joint/n_bird


def birdupplusprevalence(n_joint,n_state,n_bird):
    ""
    return (n_joint/n_bird) + 10*(n_joint/n_state)


def birduptimeslog(n_joint,n_state,n_bird):
    "Tried to give a bit of a boost to common birds. Dissapoint results."
    return (n_joint/n_bird) * np.log(n_joint+1)

def simplecount(n_joint,n_state,n_bird):
    ""
    return n_joint

#%% Call all the functions. Determine all the birdest birds. Yeehaw!


do_the_works_gs('Markedness',markedness)

do_the_works_gs('WeightedInfoMark',paramaterizedPhi)
do_the_works_gs('YulePhi',YulePhi)

do_the_works_gs('Informedness',informedness)
do_the_works_gs('normalizedTPR',normalizedTPR)
do_the_works_gs('prevalance',naiveprevalence)
do_the_works_gs('jaccard',jaccard)
do_the_works_gs('fowlkesmallows',fowlkes_mallows)
do_the_works_gs('agreement',agreement)
do_the_works_gs('cohenkappa',cohenkappa)
do_the_works_gs('basicbirdup',basicbirdup)
do_the_works_gs('birdupplusprevalence',birdupplusprevalence)
do_the_works_gs('birduptimeslog',birduptimeslog)
do_the_works_gs('simplecount',simplecount)


#%% Iterate through parameterized phi, output the top birds at each step.
#Yeah, I know I shouldn't be using a globalvar to change the value of a single fn's paramater.
#*shrug*

if False:
    weightgrid = np.linspace(0,1,21)
    records_of_top_birds = dict()
    for state in state_count:
        records_of_top_birds[state] = []
    for w in weightgrid:
        ALPHA_PARAM = w
        birdscore = calculate_genus_scores(paramaterizedPhi)
        top_birds = quick_top_birdscores(birdscore)
        unique_top_birds = unique_top_birdscores(birdscore)
        print(compare_to_REALSTATEBIRDS(unique_top_birds), check_for_iconic_birds(unique_top_birds), ALPHA_PARAM)
        for entry in unique_top_birds:
            state = entry[0][1]
            bird = entry[0][0]
            records_of_top_birds[state].append(bird)
    filepath = os.path.join(THIS_FOLDER,"BIRDUP","WeightedInfoMarkGenus_iterationResults"+".txt")
    with open(filepath,'w') as birdfile:
            birdfile.write('\n'.join([str(item) for item in records_of_top_birds.items()]))
            birdfile.write('\n')


#%%TODO: Compare Yulephi and weighted to see where the disagreement lies.











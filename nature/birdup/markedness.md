---
title: "Bird Scores - Markedness"
parent: New State Birds
grand_parent: Science and Nature
has_children: false
---


This BIRDUP scoring system is based on  [Youden's J statistic](https://en.wikipedia.org/wiki/Youden%27s_J_statistic).
The way I'm using it here, 
It's essentially the difference between how common a bird is in a state and how common that bird is elsewhere in North America.

Youden's J statistic is usually used to evaluate the performance of a diagnostic test.
If we interpret these bird scores that way, we're essentially evaluating states as diagnostic tests of whether you're seeing a particular type of bird. 

$$\gdef\nBird{🦃}
\gdef\nState{🗽}
\gdef\nTotal{N}
\gdef\nJoint{📋}$$

These scores use observation records from the eBird database[^ebirdcitation].
Each observation is for a specific species of bird in a specific state.
- Let $N$ be the total number of observations in the data.
- Let $\nBird$ be the total number of observations of a specific bird species or genus.
- Let $\nState$ be the total number of observations taking place in a specific state.
- Let $\nJoint$ be the the joint observation count: the total number of observations of that specific type of bird in that specific state.

Here, the Bird Score for a pair of state and bird is 

$$\Delta p = \frac{\nJoint}{\nBird} - \frac{\nState - \nJoint}{\nTotal - \nBird}$$

The dual of this measurement, called [informedness](informedness), swaps the roll of state and bird in the formula.

<details closed markdown="block">
  <summary>
    Table of contents
  </summary>
- TOC
{:toc}
</details>

In the tables below, `†` indicates that the bird genus is represented among actual state birds.  
`‡` indicates that the bird is the actual state bird for that state.  
`＊` indicates a bird that is non-native and so excluded it form. A lack of `*` does not necessarily mean the bird *is* native.

[^ebirdcitation]: eBird Basic Dataset. Version: EBD_relSep-2021. Cornell Lab of Ornithology, Ithaca, New York. Sep 2021.






## Scores for Bird Genera

### Top Scoring Unique State Birds

| State | Score | Bird | Common Name | Example Species | Common Name |
|--:|---|---|---|---|---|
| AK | 0.9934 | [Muscicapa](https://en.wikipedia.org/wiki/Muscicapa) |  | [Muscicapa griseisticta](https://en.wikipedia.org/wiki/Muscicapa_griseisticta) |  |
| AL | 0.0552 | [Grus](https://en.wikipedia.org/wiki/Grus_(genus)) | Crane | [Grus americana](https://en.wikipedia.org/wiki/Grus_americana) | Whooping Crane |
| AR | 0.0145 | [Antrostomus](https://en.wikipedia.org/wiki/Antrostomus) | Nightjar | [Antrostomus sp.](https://en.wikipedia.org/wiki/Antrostomus) |  |
| AZ | 0.9008 | [Agapornis](https://en.wikipedia.org/wiki/Agapornis) |  | [Agapornis personatus](https://en.wikipedia.org/wiki/Agapornis_personatus) |  |
| CA | 0.5597 | [Chamaea](https://en.wikipedia.org/wiki/Chamaea) | Wrentit | [Chamaea fasciata](https://en.wikipedia.org/wiki/Chamaea_fasciata) | Wrentit |
| CO | 0.2735 | [Rhynchophanes](https://en.wikipedia.org/wiki/Rhynchophanes) | Longspur | [Rhynchophanes mccownii](https://en.wikipedia.org/wiki/Rhynchophanes_mccownii) | Thick-billed Longspur |
| CT | 0.0668 | [Threskiornithidae](https://en.wikipedia.org/wiki/Threskiornithidae) |  | [Threskiornithidae sp. (ibis sp.)](https://en.wikipedia.org/wiki/Threskiornithidae) |  |
| DC | 0.0134 | [Melopsittacus](https://en.wikipedia.org/wiki/Melopsittacus) |  | [Melopsittacus undulatus (Domestic type)](https://en.wikipedia.org/wiki/Melopsittacus_undulatus_(Domestic_type)) |  |
| DE | 0.0331 | [Ammospiza](https://en.wikipedia.org/wiki/Ammospiza) |  | [Ammospiza maritima](https://en.wikipedia.org/wiki/Ammospiza_maritima) | Seaside Sparrow |
| FL | 0.9494 | [Melanospiza](https://en.wikipedia.org/wiki/Melanospiza) |  | [Melanospiza bicolor](https://en.wikipedia.org/wiki/Melanospiza_bicolor) |  |
| GA | 0.0912 | [Limnothlypis](https://en.wikipedia.org/wiki/Limnothlypis) |  | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler |
| HI | 0.9980 | [Himatione](https://en.wikipedia.org/wiki/Himatione) |  | [Himatione sanguinea](https://en.wikipedia.org/wiki/Himatione_sanguinea) | Apapane |
| IA | 0.0245 | [Rhodostethia](https://en.wikipedia.org/wiki/Rhodostethia) |  | [Rhodostethia rosea](https://en.wikipedia.org/wiki/Rhodostethia_rosea) | Ross's Gull |
| ID | 0.2104 | [Tarsiger](https://en.wikipedia.org/wiki/Tarsiger) |  | [Tarsiger cyanurus](https://en.wikipedia.org/wiki/Tarsiger_cyanurus) |  |
| IL | 0.1907 | [Centronyx](https://en.wikipedia.org/wiki/Centronyx) | Sparrow | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow |
| IN | 0.0257 | [Oporornis](https://en.wikipedia.org/wiki/Oporornis) | Connecticut Warbler | [Oporornis agilis](https://en.wikipedia.org/wiki/Oporornis_agilis) | Connecticut Warbler |
| KS | 0.0768 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| KY | 0.0185 | [Ectopistes](https://en.wikipedia.org/wiki/Ectopistes) |  | [Ectopistes migratorius](https://en.wikipedia.org/wiki/Ectopistes_migratorius) |  |
| LA | 0.0844 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| MA | 0.5510 | [Pelagodroma](https://en.wikipedia.org/wiki/Pelagodroma) |  | [Pelagodroma marina](https://en.wikipedia.org/wiki/Pelagodroma_marina) |  |
| MD | 0.0483 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| ME | 0.1952 | [Somateria](https://en.wikipedia.org/wiki/Somateria) | Eider | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider |
| MI | 0.0842 | [Cygnus](https://en.wikipedia.org/wiki/Swan) | Swan | [Cygnus sp.](https://en.wikipedia.org/wiki/Swan) |  |
| MN | 0.1065 | [Pagophila](https://en.wikipedia.org/wiki/Pagophila) | Ivory gull | [Pagophila eburnea](https://en.wikipedia.org/wiki/Pagophila_eburnea) |  |
| MO | 0.1044 | [Mergellus](https://en.wikipedia.org/wiki/Mergellus) |  | [Mergellus albellus](https://en.wikipedia.org/wiki/Mergellus_albellus) |  |
| MS | 0.0306 | [Gelochelidon](https://en.wikipedia.org/wiki/Gelochelidon) |  | [Gelochelidon nilotica](https://en.wikipedia.org/wiki/Gelochelidon_nilotica) | Gull-billed Tern |
| MT | 0.1324 | [Sibirionetta](https://en.wikipedia.org/wiki/Sibirionetta) |  | [Sibirionetta formosa](https://en.wikipedia.org/wiki/Sibirionetta_formosa) |  |
| NC | 0.3693 | [Pterodroma](https://en.wikipedia.org/wiki/Pterodroma) | Gadfly Petrel | [Pterodroma feae](https://en.wikipedia.org/wiki/Pterodroma_feae) |  |
| ND | 0.1107 | [Tympanuchus](https://en.wikipedia.org/wiki/Tympanuchus) | Prarie Chicken | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse |
| NE | 0.0258 | [Colinus](https://en.wikipedia.org/wiki/Colinus) | Bobwhite | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite |
| NH | 0.0275 | [Cuculidae](https://en.wikipedia.org/wiki/Cuculidae) |  | [Cuculidae sp.](https://en.wikipedia.org/wiki/Cuculidae) |  |
| NJ | 0.2287 | [Vanellus](https://en.wikipedia.org/wiki/Vanellus) |  | [Vanellus vanellus](https://en.wikipedia.org/wiki/Vanellus_vanellus) | Northern Lapwing |
| NM | 0.2172 | [Gymnorhinus](https://en.wikipedia.org/wiki/Gymnorhinus) | Pinyon Jay | [Gymnorhinus cyanocephalus](https://en.wikipedia.org/wiki/Gymnorhinus_cyanocephalus) | Pinyon Jay |
| NV | 0.1247 | [Artemisiospiza](https://en.wikipedia.org/wiki/Artemisiospiza) | Sparrow | [Artemisiospiza nevadensis](https://en.wikipedia.org/wiki/Artemisiospiza_nevadensis) | Sagebrush Sparrow |
| NY | 0.8710 | [Crex](https://en.wikipedia.org/wiki/Crex) |  | [Crex crex](https://en.wikipedia.org/wiki/Crex_crex) |  |
| OH | 0.0998 | [Fringilla](https://en.wikipedia.org/wiki/Fringilla) |  | [Fringilla montifringilla](https://en.wikipedia.org/wiki/Fringilla_montifringilla) |  |
| OK | 0.0311 | [Nomonyx](https://en.wikipedia.org/wiki/Nomonyx) |  | [Nomonyx dominicus](https://en.wikipedia.org/wiki/Nomonyx_dominicus) | Masked Duck |
| OR | 0.4319 | [Oreortyx](https://en.wikipedia.org/wiki/Oreortyx) |  | [Oreortyx pictus](https://en.wikipedia.org/wiki/Oreortyx_pictus) | Mountain Quail |
| PA | 0.0974 | [Aves](https://en.wikipedia.org/wiki/Aves) |  | [Aves sp.](https://en.wikipedia.org/wiki/Aves) |  |
| RI | 0.2711 | [Xenus](https://en.wikipedia.org/wiki/Xenus) |  | [Xenus cinereus](https://en.wikipedia.org/wiki/Xenus_cinereus) |  |
| SC | 0.0872 | [Mycteria](https://en.wikipedia.org/wiki/Mycteria) | Stork | [Mycteria americana](https://en.wikipedia.org/wiki/Mycteria_americana) | Wood Stork |
| SD | 0.0381 | [Bartramia](https://en.wikipedia.org/wiki/Bartramia_(bird)) | Upland Sandpiper | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper |
| TN | 0.0352 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| TX | 0.9136 | [Spermestes](https://en.wikipedia.org/wiki/Spermestes) |  | [Spermestes cucullata](https://en.wikipedia.org/wiki/Spermestes_cucullata) |  |
| UT | 0.1869 | [Psiloscops](https://en.wikipedia.org/wiki/Psiloscops) |  | [Psiloscops flammeolus](https://en.wikipedia.org/wiki/Psiloscops_flammeolus) | Flammulated Owl |
| VA | 0.0644 | [Numida](https://en.wikipedia.org/wiki/Numida) |  | [Numida meleagris (Domestic type)](https://en.wikipedia.org/wiki/Numida_meleagris_(Domestic_type)) |  |
| VT | 0.0297 | [Bonasa](https://en.wikipedia.org/wiki/Bonasa)† | Ruffed Grouse | [Bonasa umbellus](https://en.wikipedia.org/wiki/Bonasa_umbellus) | Ruffed Grouse |
| WA | 0.9451 | [Creagrus](https://en.wikipedia.org/wiki/Creagrus) |  | [Creagrus furcatus](https://en.wikipedia.org/wiki/Creagrus_furcatus) |  |
| WI | 0.1417 | [Antigone](https://en.wikipedia.org/wiki/Antigone_(bird)) | Crane | [Antigone canadensis](https://en.wikipedia.org/wiki/Antigone_canadensis) | Sandhill Crane |
| WV | 0.0128 | [Helmitheros](https://en.wikipedia.org/wiki/Helmitheros) |  | [Helmitheros vermivorum](https://en.wikipedia.org/wiki/Helmitheros_vermivorum) | Worm-eating Warbler |
| WY | 0.1964 | [Centrocercus](https://en.wikipedia.org/wiki/Centrocercus) | Sage-grouse | [Centrocercus urophasianus](https://en.wikipedia.org/wiki/Centrocercus_urophasianus) | Greater Sage-Grouse |





### Top Genera for Alaska (AK)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.9934 | [Muscicapa](https://en.wikipedia.org/wiki/Muscicapa) |  | 281 | [Muscicapa griseisticta](https://en.wikipedia.org/wiki/Muscicapa_griseisticta) |  |
| 0.9904 | [Calliope](https://en.wikipedia.org/wiki/Calliope) |  | 331 | [Calliope calliope](https://en.wikipedia.org/wiki/Calliope_calliope) |  |
| 0.9809 | [Aethia](https://en.wikipedia.org/wiki/Aethia) | Auklet | 31286 | [Aethia pygmaea](https://en.wikipedia.org/wiki/Aethia_pygmaea) |  |
| 0.9742 | [Luscinia](https://en.wikipedia.org/wiki/Luscinia) |  | 3311 | [Luscinia svecica](https://en.wikipedia.org/wiki/Luscinia_svecica) | Bluethroat |
| 0.9646 | [Carpodacus](https://en.wikipedia.org/wiki/Carpodacus)† |  | 202 | [Carpodacus erythrinus](https://en.wikipedia.org/wiki/Carpodacus_erythrinus) |  |
| 0.9486 | [Lymnocryptes](https://en.wikipedia.org/wiki/Lymnocryptes) |  | 192 | [Lymnocryptes minimus](https://en.wikipedia.org/wiki/Lymnocryptes_minimus) |  |
| 0.9304 | [Ficedula](https://en.wikipedia.org/wiki/Ficedula) |  | 119 | [Ficedula albicilla](https://en.wikipedia.org/wiki/Ficedula_albicilla) |  |
| 0.9286 | [Pyrrhula](https://en.wikipedia.org/wiki/Pyrrhula) |  | 101 | [Pyrrhula pyrrhula](https://en.wikipedia.org/wiki/Pyrrhula_pyrrhula) |  |
| 0.9283 | [Polysticta](https://en.wikipedia.org/wiki/Polysticta) |  | 7277 | [Polysticta stelleri](https://en.wikipedia.org/wiki/Polysticta_stelleri) | Steller's Eider |
| 0.9267 | [Phylloscopus](https://en.wikipedia.org/wiki/Phylloscopus) |  | 6210 | [Phylloscopus collybita](https://en.wikipedia.org/wiki/Phylloscopus_collybita) | Common Chiffchaff |






### Top Genera for Alabama (AL)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0607 | [Limnothlypis](https://en.wikipedia.org/wiki/Limnothlypis) |  | 2905 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler |
| 0.0552 | [Grus](https://en.wikipedia.org/wiki/Grus_(genus)) | Crane | 1504 | [Grus americana](https://en.wikipedia.org/wiki/Grus_americana) | Whooping Crane |
| 0.0311 | [Caprimulgidae](https://en.wikipedia.org/wiki/Caprimulgidae) |  | 31 | [Caprimulgidae sp.](https://en.wikipedia.org/wiki/Caprimulgidae) |  |
| 0.0310 | [Lonchura](https://en.wikipedia.org/wiki/Lonchura) |  | 1698 | [Lonchura punctulata](https://en.wikipedia.org/wiki/Lonchura_punctulata) | Scaly-breasted Munia |
| 0.0257 | [Gelochelidon](https://en.wikipedia.org/wiki/Gelochelidon) |  | 2926 | [Gelochelidon nilotica](https://en.wikipedia.org/wiki/Gelochelidon_nilotica) | Gull-billed Tern |
| 0.0227 | [Thalasseus](https://en.wikipedia.org/wiki/Thalasseus) | Crested Tern | 24522 | [Thalasseus sandvicensis](https://en.wikipedia.org/wiki/Thalasseus_sandvicensis) | Sandwich Tern |
| 0.0219 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 9976 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0163 | [Helmitheros](https://en.wikipedia.org/wiki/Helmitheros) |  | 4757 | [Helmitheros vermivorum](https://en.wikipedia.org/wiki/Helmitheros_vermivorum) | Worm-eating Warbler |
| 0.0149 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 130529 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0142 | [Icteria](https://en.wikipedia.org/wiki/Icteria) | Yellow-breasted Chat | 10981 | [Icteria virens](https://en.wikipedia.org/wiki/Icteria_virens) | Yellow-breasted Chat |






### Top Genera for Arkansas (AR)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0323 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | 10710 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| 0.0198 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 10491 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0158 | [Colinus](https://en.wikipedia.org/wiki/Colinus) | Bobwhite | 7000 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite |
| 0.0145 | [Antrostomus](https://en.wikipedia.org/wiki/Antrostomus) | Nightjar | 4355 | [Antrostomus sp.](https://en.wikipedia.org/wiki/Antrostomus) |  |
| 0.0140 | [Icteria](https://en.wikipedia.org/wiki/Icteria) | Yellow-breasted Chat | 10221 | [Icteria virens](https://en.wikipedia.org/wiki/Icteria_virens) | Yellow-breasted Chat |
| 0.0132 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 6445 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0112 | [Coccyzus](https://en.wikipedia.org/wiki/Coccyzus) | Cuckoo | 17013 | [Coccyzus americanus](https://en.wikipedia.org/wiki/Coccyzus_americanus) | Yellow-billed Cuckoo |
| 0.0095 | [Passerina](https://en.wikipedia.org/wiki/Passerina) | Bunting | 55044 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting |
| 0.0081 | [Icteridae](https://en.wikipedia.org/wiki/Icteridae) |  | 2515 | [Icteridae sp.](https://en.wikipedia.org/wiki/Icteridae) |  |
| 0.0080 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 91280 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |






### Top Genera for Arizona (AZ)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.9008 | [Agapornis](https://en.wikipedia.org/wiki/Agapornis) |  | 23299 | [Agapornis personatus](https://en.wikipedia.org/wiki/Agapornis_personatus) |  |
| 0.8669 | [Amphispizopsis](https://en.wikipedia.org/wiki/Amphispizopsis) |  | 5685 | [Amphispizopsis quinquestriata](https://en.wikipedia.org/wiki/Amphispizopsis_quinquestriata) | Five-striped Sparrow |
| 0.7680 | [Eugenes](https://en.wikipedia.org/wiki/Eugenes) |  | 59354 | [Eugenes fulgens](https://en.wikipedia.org/wiki/Eugenes_fulgens) | Rivoli's Hummingbird |
| 0.7565 | [Cyrtonyx](https://en.wikipedia.org/wiki/Cyrtonyx) |  | 13850 | [Cyrtonyx montezumae](https://en.wikipedia.org/wiki/Cyrtonyx_montezumae) | Montezuma Quail |
| 0.7214 | [Phainopepla](https://en.wikipedia.org/wiki/Phainopepla) | Phainopepla | 200508 | [Phainopepla nitens](https://en.wikipedia.org/wiki/Phainopepla_nitens) | Phainopepla |
| 0.6746 | [Auriparus](https://en.wikipedia.org/wiki/Auriparus) | Verdin | 386191 | [Auriparus flaviceps](https://en.wikipedia.org/wiki/Auriparus_flaviceps) | Verdin |
| 0.6635 | [Euptilotis](https://en.wikipedia.org/wiki/Euptilotis) |  | 1168 | [Euptilotis neoxenus](https://en.wikipedia.org/wiki/Euptilotis_neoxenus) |  |
| 0.6624 | [Cynanthus](https://en.wikipedia.org/wiki/Cynanthus) | Hummingbird | 169527 | [Cynanthus latirostris](https://en.wikipedia.org/wiki/Cynanthus_latirostris) | Broad-billed Hummingbird |
| 0.6261 | [Micrathene](https://en.wikipedia.org/wiki/Micrathene) |  | 13070 | [Micrathene whitneyi](https://en.wikipedia.org/wiki/Micrathene_whitneyi) | Elf Owl |
| 0.6089 | [Gymnogyps](https://en.wikipedia.org/wiki/Gymnogyps) |  | 5524 | [Gymnogyps californianus](https://en.wikipedia.org/wiki/Gymnogyps_californianus) | California Condor |






### Top Genera for California (CA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.7177 | [Euplectes](https://en.wikipedia.org/wiki/Euplectes)* | Bishop | 1315 | [Euplectes franciscanus](https://en.wikipedia.org/wiki/Euplectes_franciscanus) | Northern Red Bishop |
| 0.5597 | [Chamaea](https://en.wikipedia.org/wiki/Chamaea) | Wrentit | 57649 | [Chamaea fasciata](https://en.wikipedia.org/wiki/Chamaea_fasciata) | Wrentit |
| 0.4400 | [Oreortyx](https://en.wikipedia.org/wiki/Oreortyx) |  | 8665 | [Oreortyx pictus](https://en.wikipedia.org/wiki/Oreortyx_pictus) | Mountain Quail |
| 0.3131 | [Vidua](https://en.wikipedia.org/wiki/Vidua) |  | 103 | [Vidua macroura](https://en.wikipedia.org/wiki/Vidua_macroura) | Pin-tailed Whydah |
| 0.3036 | [Elanus](https://en.wikipedia.org/wiki/Elanus) |  | 40693 | [Elanus leucurus](https://en.wikipedia.org/wiki/Elanus_leucurus) | White-tailed Kite |
| 0.2123 | [Ptychoramphus](https://en.wikipedia.org/wiki/Ptychoramphus) |  | 5326 | [Ptychoramphus aleuticus](https://en.wikipedia.org/wiki/Ptychoramphus_aleuticus) | Cassin's Auklet |
| 0.2080 | [Brotogeris](https://en.wikipedia.org/wiki/Brotogeris) |  | 2407 | [Brotogeris chiriri](https://en.wikipedia.org/wiki/Brotogeris_chiriri) | Yellow-chevroned Parakeet |
| 0.2041 | [Chloris](https://en.wikipedia.org/wiki/Chloris) |  | 23 | [Chloris sinica](https://en.wikipedia.org/wiki/Chloris_sinica) |  |
| 0.1668 | [Artemisiospiza](https://en.wikipedia.org/wiki/Artemisiospiza) | Sparrow | 7516 | [Artemisiospiza belli](https://en.wikipedia.org/wiki/Artemisiospiza_belli) | Bell's Sparrow |
| 0.1594 | [Melozone](https://en.wikipedia.org/wiki/Melozone) |  | 129054 | [Melozone crissalis](https://en.wikipedia.org/wiki/Melozone_crissalis) | California Towhee |






### Top Genera for Colorado (CO)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.2735 | [Rhynchophanes](https://en.wikipedia.org/wiki/Rhynchophanes) | Longspur | 5484 | [Rhynchophanes mccownii](https://en.wikipedia.org/wiki/Rhynchophanes_mccownii) | Thick-billed Longspur |
| 0.2623 | [Leucosticte](https://en.wikipedia.org/wiki/Leucosticte) |  | 21537 | [Leucosticte australis](https://en.wikipedia.org/wiki/Leucosticte_australis) | Brown-capped Rosy-Finch |
| 0.2582 | [Calamospiza](https://en.wikipedia.org/wiki/Calamospiza)‡ | Lark Bunting | 28847 | [Calamospiza melanocorys](https://en.wikipedia.org/wiki/Calamospiza_melanocorys) | Lark Bunting |
| 0.2201 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | 387306 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| 0.1882 | [Myadestes](https://en.wikipedia.org/wiki/Myadestes) |  | 73348 | [Myadestes townsendi](https://en.wikipedia.org/wiki/Myadestes_townsendi) | Townsend's Solitaire |
| 0.1810 | [Gymnorhinus](https://en.wikipedia.org/wiki/Gymnorhinus) | Pinyon Jay | 12356 | [Gymnorhinus cyanocephalus](https://en.wikipedia.org/wiki/Gymnorhinus_cyanocephalus) | Pinyon Jay |
| 0.1772 | [Corvidae](https://en.wikipedia.org/wiki/Corvidae) |  | 211 | [Corvidae sp. (jay sp.)](https://en.wikipedia.org/wiki/Corvidae) |  |
| 0.1693 | [Oreoscoptes](https://en.wikipedia.org/wiki/Oreoscoptes) | Sage Thrasher | 17639 | [Oreoscoptes montanus](https://en.wikipedia.org/wiki/Oreoscoptes_montanus) | Sage Thrasher |
| 0.1676 | [Cinclus](https://en.wikipedia.org/wiki/Cinclus) |  | 24773 | [Cinclus mexicanus](https://en.wikipedia.org/wiki/Cinclus_mexicanus) | American Dipper |
| 0.1629 | [Selasphorus](https://en.wikipedia.org/wiki/Selasphorus) | Hummingbird | 210475 | [Selasphorus platycercus](https://en.wikipedia.org/wiki/Selasphorus_platycercus) | Broad-tailed Hummingbird |






### Top Genera for Connecticut (CT)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0668 | [Threskiornithidae](https://en.wikipedia.org/wiki/Threskiornithidae) |  | 48 | [Threskiornithidae sp. (ibis sp.)](https://en.wikipedia.org/wiki/Threskiornithidae) |  |
| 0.0429 | [Myiopsitta](https://en.wikipedia.org/wiki/Myiopsitta)* |  | 6889 | [Myiopsitta monachus](https://en.wikipedia.org/wiki/Myiopsitta_monachus) | Monk Parakeet |
| 0.0390 | [Phalacrocorax](https://en.wikipedia.org/wiki/Phalacrocorax) | Cormorant | 7306 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant |
| 0.0333 | [Haematopus](https://en.wikipedia.org/wiki/Haematopus) | Oystercatcher | 22502 | [Haematopus palliatus](https://en.wikipedia.org/wiki/Haematopus_palliatus) | American Oystercatcher |
| 0.0303 | [Ardeidae](https://en.wikipedia.org/wiki/Ardeidae) |  | 250 | [Ardeidae sp.](https://en.wikipedia.org/wiki/Ardeidae) |  |
| 0.0287 | [Vermivora](https://en.wikipedia.org/wiki/Vermivora) | Warbler | 21206 | [Vermivora cyanoptera](https://en.wikipedia.org/wiki/Vermivora_cyanoptera) | Blue-winged Warbler |
| 0.0286 | [Helmitheros](https://en.wikipedia.org/wiki/Helmitheros) |  | 9088 | [Helmitheros vermivorum](https://en.wikipedia.org/wiki/Helmitheros_vermivorum) | Worm-eating Warbler |
| 0.0233 | [Cathartidae](https://en.wikipedia.org/wiki/Cathartidae) |  | 215 | [Cathartidae sp.](https://en.wikipedia.org/wiki/Cathartidae) |  |
| 0.0210 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)† | Wood Thrush | 47578 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina) | Wood Thrush |
| 0.0200 | [Ammospiza](https://en.wikipedia.org/wiki/Ammospiza) |  | 9103 | [Ammospiza sp.](https://en.wikipedia.org/wiki/Ammospiza) |  |






### Top Genera for District of Columbia (DC)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0134 | [Melopsittacus](https://en.wikipedia.org/wiki/Melopsittacus) |  | 25 | [Melopsittacus undulatus (Domestic type)](https://en.wikipedia.org/wiki/Melopsittacus_undulatus_(Domestic_type)) |  |
| 0.0069 | [Chaetura](https://en.wikipedia.org/wiki/Chaetura) | Swift | 24475 | [Chaetura pelagica](https://en.wikipedia.org/wiki/Chaetura_pelagica) | Chimney Swift |
| 0.0043 | [Accipitridae](https://en.wikipedia.org/wiki/Accipitridae) |  | 838 | [Accipitridae sp. (hawk sp.)](https://en.wikipedia.org/wiki/Accipitridae) |  |
| 0.0037 | [Oporornis](https://en.wikipedia.org/wiki/Oporornis) | Connecticut Warbler | 188 | [Oporornis agilis](https://en.wikipedia.org/wiki/Oporornis_agilis) | Connecticut Warbler |
| 0.0036 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 41998 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0035 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)‡ | Wood Thrush | 7815 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina) | Wood Thrush |
| 0.0027 | [Polioptila](https://en.wikipedia.org/wiki/Polioptila) | Gnatcatcher | 16764 | [Polioptila caerulea](https://en.wikipedia.org/wiki/Polioptila_caerulea) | Blue-gray Gnatcatcher |
| 0.0026 | [Passer](https://en.wikipedia.org/wiki/Passer)* | True Sparrow | 42950 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus) | House Sparrow |
| 0.0026 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 30486 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0026 | [Xema](https://en.wikipedia.org/wiki/Xema) |  | 207 | [Xema sabini](https://en.wikipedia.org/wiki/Xema_sabini) | Sabine's Gull |






### Top Genera for Delaware (DE)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0462 | [Threskiornithidae](https://en.wikipedia.org/wiki/Threskiornithidae) |  | 31 | [Threskiornithidae sp. (ibis sp.)](https://en.wikipedia.org/wiki/Threskiornithidae) |  |
| 0.0331 | [Ammospiza](https://en.wikipedia.org/wiki/Ammospiza) |  | 10452 | [Ammospiza maritima](https://en.wikipedia.org/wiki/Ammospiza_maritima) | Seaside Sparrow |
| 0.0250 | [Recurvirostra](https://en.wikipedia.org/wiki/Recurvirostra) | Avocet | 16285 | [Recurvirostra americana](https://en.wikipedia.org/wiki/Recurvirostra_americana) | American Avocet |
| 0.0196 | [Phalacrocorax](https://en.wikipedia.org/wiki/Phalacrocorax) | Cormorant | 3537 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant |
| 0.0192 | [Pelagodroma](https://en.wikipedia.org/wiki/Pelagodroma) |  | 45 | [Pelagodroma marina](https://en.wikipedia.org/wiki/Pelagodroma_marina) |  |
| 0.0189 | [Leucophaeus](https://en.wikipedia.org/wiki/Leucophaeus) | Gull | 53108 | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull |
| 0.0183 | [Charadriiformes](https://en.wikipedia.org/wiki/Charadriiformes) |  | 2078 | [Charadriiformes sp.](https://en.wikipedia.org/wiki/Charadriiformes) |  |
| 0.0182 | [Limnodromus](https://en.wikipedia.org/wiki/Limnodromus) |  | 21701 | [Limnodromus griseus](https://en.wikipedia.org/wiki/Limnodromus_griseus) | Short-billed Dowitcher |
| 0.0179 | [Sterna](https://en.wikipedia.org/wiki/Sterna) | Tern | 42296 | [Sterna forsteri](https://en.wikipedia.org/wiki/Sterna_forsteri) | Forster's Tern |
| 0.0171 | [Scolopacidae](https://en.wikipedia.org/wiki/Scolopacidae) |  | 90 | [Scolopacidae sp. (large shorebird sp.)](https://en.wikipedia.org/wiki/Scolopacidae) |  |






### Top Genera for Florida (FL)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.9494 | [Melanospiza](https://en.wikipedia.org/wiki/Melanospiza) |  | 1164 | [Melanospiza bicolor](https://en.wikipedia.org/wiki/Melanospiza_bicolor) |  |
| 0.9494 | [Tachornis](https://en.wikipedia.org/wiki/Tachornis) |  | 290 | [Tachornis phoenicobia](https://en.wikipedia.org/wiki/Tachornis_phoenicobia) |  |
| 0.9489 | [Gracula](https://en.wikipedia.org/wiki/Gracula) |  | 2142 | [Gracula religiosa](https://en.wikipedia.org/wiki/Gracula_religiosa) |  |
| 0.9386 | [Thectocercus](https://en.wikipedia.org/wiki/Thectocercus) |  | 6770 | [Thectocercus acuticaudatus](https://en.wikipedia.org/wiki/Thectocercus_acuticaudatus) |  |
| 0.9347 | [Ara](https://en.wikipedia.org/wiki/Ara) |  | 2611 | [Ara ararauna](https://en.wikipedia.org/wiki/Ara_ararauna) | Blue-and-yellow Macaw |
| 0.9343 | [Aratinga](https://en.wikipedia.org/wiki/Aratinga)* | Conure | 47057 | [Aratinga nenday](https://en.wikipedia.org/wiki/Aratinga_nenday) | Nanday Parakeet |
| 0.8933 | [Nesophlox](https://en.wikipedia.org/wiki/Nesophlox) |  | 101 | [Nesophlox evelynae](https://en.wikipedia.org/wiki/Nesophlox_evelynae) |  |
| 0.8713 | [Aramus](https://en.wikipedia.org/wiki/Aramus) |  | 184399 | [Aramus guarauna](https://en.wikipedia.org/wiki/Aramus_guarauna) | Limpkin |
| 0.7842 | [Callonetta](https://en.wikipedia.org/wiki/Callonetta) |  | 293 | [Callonetta leucophrys](https://en.wikipedia.org/wiki/Callonetta_leucophrys) |  |
| 0.7301 | [Rostrhamus](https://en.wikipedia.org/wiki/Rostrhamus) |  | 32354 | [Rostrhamus sociabilis](https://en.wikipedia.org/wiki/Rostrhamus_sociabilis) | Snail Kite |






### Top Genera for Georgia (GA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0912 | [Limnothlypis](https://en.wikipedia.org/wiki/Limnothlypis) |  | 4722 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler |
| 0.0605 | [Vanellus](https://en.wikipedia.org/wiki/Vanellus) |  | 167 | [Vanellus vanellus](https://en.wikipedia.org/wiki/Vanellus_vanellus) | Northern Lapwing |
| 0.0516 | [Mycteria](https://en.wikipedia.org/wiki/Mycteria) | Stork | 28067 | [Mycteria americana](https://en.wikipedia.org/wiki/Mycteria_americana) | Wood Stork |
| 0.0427 | [Toxostoma](https://en.wikipedia.org/wiki/Toxostoma)‡ | Thrasher | 179633 | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum) | Brown Thrasher |
| 0.0396 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | 16431 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| 0.0385 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 395603 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0300 | [Pipilo](https://en.wikipedia.org/wiki/Pipilo) | Towhee | 264143 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee |
| 0.0297 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 249060 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0291 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 288903 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0287 | [Antrostomus](https://en.wikipedia.org/wiki/Antrostomus) | Nightjar | 10360 | [Antrostomus carolinensis](https://en.wikipedia.org/wiki/Antrostomus_carolinensis) | Chuck-will's-widow |






### Top Genera for Hawaii (HI)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.9981 | [Zosterops](https://en.wikipedia.org/wiki/Zosterops)* | White-Eyes | 82840 | [Zosterops japonicus](https://en.wikipedia.org/wiki/Zosterops_japonicus) |  |
| 0.9981 | [Geopelia](https://en.wikipedia.org/wiki/Geopelia)* |  | 78346 | [Geopelia striata](https://en.wikipedia.org/wiki/Geopelia_striata) |  |
| 0.9980 | [Himatione](https://en.wikipedia.org/wiki/Himatione) |  | 35689 | [Himatione sanguinea](https://en.wikipedia.org/wiki/Himatione_sanguinea) | Apapane |
| 0.9980 | [Chlorodrepanis](https://en.wikipedia.org/wiki/Chlorodrepanis) |  | 34136 | [Chlorodrepanis virens](https://en.wikipedia.org/wiki/Chlorodrepanis_virens) |  |
| 0.9980 | [Paroaria](https://en.wikipedia.org/wiki/Paroaria)* |  | 56710 | [Paroaria capitata](https://en.wikipedia.org/wiki/Paroaria_capitata) |  |
| 0.9980 | [Copsychus](https://en.wikipedia.org/wiki/Copsychus) |  | 18329 | [Copsychus malabaricus](https://en.wikipedia.org/wiki/Copsychus_malabaricus) |  |
| 0.9980 | [Leiothrix](https://en.wikipedia.org/wiki/Leiothrix) |  | 17965 | [Leiothrix lutea](https://en.wikipedia.org/wiki/Leiothrix_lutea) |  |
| 0.9980 | [Chasiempis](https://en.wikipedia.org/wiki/Chasiempis) |  | 17400 | [Chasiempis sandwichensis](https://en.wikipedia.org/wiki/Chasiempis_sandwichensis) |  |
| 0.9980 | [Drepanis](https://en.wikipedia.org/wiki/Drepanis) |  | 17194 | [Drepanis coccinea](https://en.wikipedia.org/wiki/Drepanis_coccinea) |  |
| 0.9980 | [Ortygornis](https://en.wikipedia.org/wiki/Ortygornis) |  | 16235 | [Ortygornis pondicerianus](https://en.wikipedia.org/wiki/Ortygornis_pondicerianus) |  |






### Top Genera for Iowa (IA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0325 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 15850 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0291 | [Phasianus](https://en.wikipedia.org/wiki/Phasianus)†* | Pheasant | 21293 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus) | Ring-necked Pheasant |
| 0.0245 | [Rhodostethia](https://en.wikipedia.org/wiki/Rhodostethia) |  | 76 | [Rhodostethia rosea](https://en.wikipedia.org/wiki/Rhodostethia_rosea) | Ross's Gull |
| 0.0181 | [Centronyx](https://en.wikipedia.org/wiki/Centronyx) | Sparrow | 1961 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow |
| 0.0082 | [Perdix](https://en.wikipedia.org/wiki/Perdix)* | Partridge | 679 | [Perdix perdix](https://en.wikipedia.org/wiki/Perdix_perdix) | Gray Partridge |
| 0.0078 | [Strix](https://en.wikipedia.org/wiki/Strix_(bird)) | Wood Owl | 9534 | [Strix varia](https://en.wikipedia.org/wiki/Strix_varia) | Barred Owl |
| 0.0062 | [Spizelloides](https://en.wikipedia.org/wiki/Spizelloides) | Winter Sparrow | 15618 | [Spizelloides arborea](https://en.wikipedia.org/wiki/Spizelloides_arborea) | American Tree Sparrow |
| 0.0061 | [Anser](https://en.wikipedia.org/wiki/Anser) | Grey Goose | 13545 | [Anser fabalis](https://en.wikipedia.org/wiki/Anser_fabalis) |  |
| 0.0057 | [Petrochelidon](https://en.wikipedia.org/wiki/Petrochelidon) |  | 13799 | [Petrochelidon pyrrhonota](https://en.wikipedia.org/wiki/Petrochelidon_pyrrhonota) | Cliff Swallow |
| 0.0050 | [Pheucticus](https://en.wikipedia.org/wiki/Pheucticus) |  | 23362 | [Pheucticus ludovicianus](https://en.wikipedia.org/wiki/Pheucticus_ludovicianus) | Rose-breasted Grosbeak |






### Top Genera for Idaho (ID)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.2104 | [Tarsiger](https://en.wikipedia.org/wiki/Tarsiger) |  | 156 | [Tarsiger cyanurus](https://en.wikipedia.org/wiki/Tarsiger_cyanurus) |  |
| 0.1077 | [Centrocercus](https://en.wikipedia.org/wiki/Centrocercus) | Sage-grouse | 1305 | [Centrocercus urophasianus](https://en.wikipedia.org/wiki/Centrocercus_urophasianus) | Greater Sage-Grouse |
| 0.0973 | [Alectoris](https://en.wikipedia.org/wiki/Alectoris)* | Rock Partridge | 3634 | [Alectoris chukar](https://en.wikipedia.org/wiki/Alectoris_chukar) | Chukar |
| 0.0684 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | 118106 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| 0.0631 | [Oreoscoptes](https://en.wikipedia.org/wiki/Oreoscoptes) | Sage Thrasher | 6303 | [Oreoscoptes montanus](https://en.wikipedia.org/wiki/Oreoscoptes_montanus) | Sage Thrasher |
| 0.0603 | [Perdix](https://en.wikipedia.org/wiki/Perdix)* | Partridge | 3493 | [Perdix perdix](https://en.wikipedia.org/wiki/Perdix_perdix) | Gray Partridge |
| 0.0517 | [Callipepla](https://en.wikipedia.org/wiki/Callipepla)† | Crested Quail | 53404 | [Callipepla californica](https://en.wikipedia.org/wiki/Callipepla_californica) | California Quail |
| 0.0471 | [Artemisiospiza](https://en.wikipedia.org/wiki/Artemisiospiza) | Sparrow | 2206 | [Artemisiospiza nevadensis](https://en.wikipedia.org/wiki/Artemisiospiza_nevadensis) | Sagebrush Sparrow |
| 0.0467 | [Psiloscops](https://en.wikipedia.org/wiki/Psiloscops) |  | 575 | [Psiloscops flammeolus](https://en.wikipedia.org/wiki/Psiloscops_flammeolus) | Flammulated Owl |
| 0.0391 | [Prunella](https://en.wikipedia.org/wiki/Prunella) |  | 51 | [Prunella montanella](https://en.wikipedia.org/wiki/Prunella_montanella) |  |






### Top Genera for Illinois (IL)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.2943 | [Carduelis](https://en.wikipedia.org/wiki/Carduelis)* | Goldfinch | 1798 | [Carduelis carduelis](https://en.wikipedia.org/wiki/Carduelis_carduelis) | European Goldfinch |
| 0.1907 | [Centronyx](https://en.wikipedia.org/wiki/Centronyx) | Sparrow | 18756 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow |
| 0.1000 | [Oporornis](https://en.wikipedia.org/wiki/Oporornis) | Connecticut Warbler | 4029 | [Oporornis agilis](https://en.wikipedia.org/wiki/Oporornis_agilis) | Connecticut Warbler |
| 0.0818 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 46626 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0678 | [Myiopsitta](https://en.wikipedia.org/wiki/Myiopsitta)* |  | 11545 | [Myiopsitta monachus](https://en.wikipedia.org/wiki/Myiopsitta_monachus) | Monk Parakeet |
| 0.0467 | [Hydroprogne](https://en.wikipedia.org/wiki/Hydroprogne) |  | 70704 | [Hydroprogne caspia](https://en.wikipedia.org/wiki/Hydroprogne_caspia) | Caspian Tern |
| 0.0386 | [Spizelloides](https://en.wikipedia.org/wiki/Spizelloides) | Winter Sparrow | 94643 | [Spizelloides arborea](https://en.wikipedia.org/wiki/Spizelloides_arborea) | American Tree Sparrow |
| 0.0341 | [Pagophila](https://en.wikipedia.org/wiki/Pagophila) | Ivory gull | 233 | [Pagophila eburnea](https://en.wikipedia.org/wiki/Pagophila_eburnea) |  |
| 0.0337 | [Chaetura](https://en.wikipedia.org/wiki/Chaetura) | Swift | 163030 | [Chaetura pelagica](https://en.wikipedia.org/wiki/Chaetura_pelagica) | Chimney Swift |
| 0.0295 | [Tyrannidae](https://en.wikipedia.org/wiki/Tyrannidae) |  | 2615 | [Tyrannidae sp.](https://en.wikipedia.org/wiki/Tyrannidae) |  |






### Top Genera for Indiana (IN)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0745 | [Centronyx](https://en.wikipedia.org/wiki/Centronyx) | Sparrow | 7607 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow |
| 0.0300 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 15774 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0257 | [Oporornis](https://en.wikipedia.org/wiki/Oporornis) | Connecticut Warbler | 1255 | [Oporornis agilis](https://en.wikipedia.org/wiki/Oporornis_agilis) | Connecticut Warbler |
| 0.0243 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 16357 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0236 | [Colinus](https://en.wikipedia.org/wiki/Colinus) | Bobwhite | 12791 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite |
| 0.0160 | [Spizelloides](https://en.wikipedia.org/wiki/Spizelloides) | Winter Sparrow | 42933 | [Spizelloides arborea](https://en.wikipedia.org/wiki/Spizelloides_arborea) | American Tree Sparrow |
| 0.0144 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)† | Wood Thrush | 38634 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina) | Wood Thrush |
| 0.0141 | [Icteria](https://en.wikipedia.org/wiki/Icteria) | Yellow-breasted Chat | 15339 | [Icteria virens](https://en.wikipedia.org/wiki/Icteria_virens) | Yellow-breasted Chat |
| 0.0138 | [Eremophila](https://en.wikipedia.org/wiki/Eremophila) |  | 32496 | [Eremophila alpestris](https://en.wikipedia.org/wiki/Eremophila_alpestris) | Horned Lark |
| 0.0131 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 224909 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |






### Top Genera for Kansas (KS)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0768 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 36284 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0581 | [Colinus](https://en.wikipedia.org/wiki/Colinus) | Bobwhite | 22554 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite |
| 0.0562 | [Bartramia](https://en.wikipedia.org/wiki/Bartramia_(bird)) | Upland Sandpiper | 8401 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper |
| 0.0417 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | 14481 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| 0.0344 | [Chondestes](https://en.wikipedia.org/wiki/Chondestes) |  | 24003 | [Chondestes grammacus](https://en.wikipedia.org/wiki/Chondestes_grammacus) | Lark Sparrow |
| 0.0337 | [Tympanuchus](https://en.wikipedia.org/wiki/Tympanuchus) | Prarie Chicken | 2429 | [Tympanuchus cupido](https://en.wikipedia.org/wiki/Tympanuchus_cupido) | Greater Prairie-Chicken |
| 0.0326 | [Ammodramus](https://en.wikipedia.org/wiki/Ammodramus) |  | 12774 | [Ammodramus savannarum](https://en.wikipedia.org/wiki/Ammodramus_savannarum) | Grasshopper Sparrow |
| 0.0258 | [Sturnella](https://en.wikipedia.org/wiki/Sturnella)‡ | Meadowlark | 92201 | [Sturnella magna](https://en.wikipedia.org/wiki/Sturnella_magna) | Eastern Meadowlark |
| 0.0218 | [Columbidae](https://en.wikipedia.org/wiki/Columbidae) |  | 486 | [Columbidae sp.](https://en.wikipedia.org/wiki/Columbidae) |  |
| 0.0216 | [Phasianus](https://en.wikipedia.org/wiki/Phasianus)†* | Pheasant | 18980 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus) | Ring-necked Pheasant |






### Top Genera for Kentucky (KY)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0185 | [Ectopistes](https://en.wikipedia.org/wiki/Ectopistes) |  | 5 | [Ectopistes migratorius](https://en.wikipedia.org/wiki/Ectopistes_migratorius) |  |
| 0.0169 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 8107 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0163 | [Limnothlypis](https://en.wikipedia.org/wiki/Limnothlypis) |  | 959 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler |
| 0.0141 | [Colinus](https://en.wikipedia.org/wiki/Colinus) | Bobwhite | 6725 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite |
| 0.0136 | [Icteria](https://en.wikipedia.org/wiki/Icteria) | Yellow-breasted Chat | 10504 | [Icteria virens](https://en.wikipedia.org/wiki/Icteria_virens) | Yellow-breasted Chat |
| 0.0114 | [Helmitheros](https://en.wikipedia.org/wiki/Helmitheros) |  | 3656 | [Helmitheros vermivorum](https://en.wikipedia.org/wiki/Helmitheros_vermivorum) | Worm-eating Warbler |
| 0.0090 | [Coccyzus](https://en.wikipedia.org/wiki/Coccyzus) | Cuckoo | 15629 | [Coccyzus americanus](https://en.wikipedia.org/wiki/Coccyzus_americanus) | Yellow-billed Cuckoo |
| 0.0085 | [Coragyps](https://en.wikipedia.org/wiki/Coragyps) | Black Vulture | 35716 | [Coragyps atratus](https://en.wikipedia.org/wiki/Coragyps_atratus) | Black Vulture |
| 0.0080 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 98073 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0078 | [Passerina](https://en.wikipedia.org/wiki/Passerina) | Bunting | 51917 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting |






### Top Genera for Louisiana (LA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0844 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | 27044 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| 0.0723 | [Limnothlypis](https://en.wikipedia.org/wiki/Limnothlypis) |  | 3553 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler |
| 0.0665 | [Coturnicops](https://en.wikipedia.org/wiki/Coturnicops) |  | 942 | [Coturnicops noveboracensis](https://en.wikipedia.org/wiki/Coturnicops_noveboracensis) | Yellow Rail |
| 0.0637 | [Gelochelidon](https://en.wikipedia.org/wiki/Gelochelidon) |  | 6719 | [Gelochelidon nilotica](https://en.wikipedia.org/wiki/Gelochelidon_nilotica) | Gull-billed Tern |
| 0.0516 | [Platalea](https://en.wikipedia.org/wiki/Platalea) |  | 22937 | [Platalea ajaja](https://en.wikipedia.org/wiki/Platalea_ajaja) | Roseate Spoonbill |
| 0.0496 | [Bubulcus](https://en.wikipedia.org/wiki/Bubulcus)* | Cattle Egret | 50157 | [Bubulcus ibis](https://en.wikipedia.org/wiki/Bubulcus_ibis) | Cattle Egret |
| 0.0483 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 20585 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0437 | [Dendrocygna](https://en.wikipedia.org/wiki/Dendrocygna) |  | 28529 | [Dendrocygna bicolor](https://en.wikipedia.org/wiki/Dendrocygna_bicolor) | Fulvous Whistling-Duck |
| 0.0423 | [Eudocimus](https://en.wikipedia.org/wiki/Eudocimus) | Ibis | 63812 | [Eudocimus albus](https://en.wikipedia.org/wiki/Eudocimus_albus) | White Ibis |
| 0.0386 | [Anhinga](https://en.wikipedia.org/wiki/Anhinga) | Darter | 37903 | [Anhinga anhinga](https://en.wikipedia.org/wiki/Anhinga_anhinga) | Anhinga |






### Top Genera for Massachusetts (MA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.5510 | [Pelagodroma](https://en.wikipedia.org/wiki/Pelagodroma) |  | 1036 | [Pelagodroma marina](https://en.wikipedia.org/wiki/Pelagodroma_marina) |  |
| 0.3149 | [Calonectris](https://en.wikipedia.org/wiki/Calonectris) | Shearwater | 16342 | [Calonectris diomedea](https://en.wikipedia.org/wiki/Calonectris_diomedea) | Cory's Shearwater |
| 0.2581 | [Oceanites](https://en.wikipedia.org/wiki/Oceanites) | Storm Petrel | 17049 | [Oceanites oceanicus](https://en.wikipedia.org/wiki/Oceanites_oceanicus) |  |
| 0.2488 | [Puffinus](https://en.wikipedia.org/wiki/Puffinus) | Shearwater | 13352 | [Puffinus puffinus](https://en.wikipedia.org/wiki/Puffinus_puffinus) | Manx Shearwater |
| 0.2420 | [Procellariidae](https://en.wikipedia.org/wiki/Procellariidae) |  | 2490 | [Procellariidae sp. (shearwater sp.)](https://en.wikipedia.org/wiki/Procellariidae) |  |
| 0.2284 | [Alle](https://en.wikipedia.org/wiki/Alle) |  | 4466 | [Alle alle](https://en.wikipedia.org/wiki/Alle_alle) |  |
| 0.2253 | [Vanellus](https://en.wikipedia.org/wiki/Vanellus) |  | 553 | [Vanellus vanellus](https://en.wikipedia.org/wiki/Vanellus_vanellus) | Northern Lapwing |
| 0.2088 | [Somateria](https://en.wikipedia.org/wiki/Somateria) | Eider | 147688 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider |
| 0.1911 | [Alca](https://en.wikipedia.org/wiki/Alca) | Razorbill | 19874 | [Alca torda](https://en.wikipedia.org/wiki/Alca_torda) | Razorbill |
| 0.1783 | [Phalacrocorax](https://en.wikipedia.org/wiki/Phalacrocorax) | Cormorant | 28983 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant |






### Top Genera for Maryland (MD)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0483 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 543555 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0454 | [Coragyps](https://en.wikipedia.org/wiki/Coragyps) | Black Vulture | 184681 | [Coragyps atratus](https://en.wikipedia.org/wiki/Coragyps_atratus) | Black Vulture |
| 0.0392 | [Helmitheros](https://en.wikipedia.org/wiki/Helmitheros) |  | 14340 | [Helmitheros vermivorum](https://en.wikipedia.org/wiki/Helmitheros_vermivorum) | Worm-eating Warbler |
| 0.0340 | [Oceanites](https://en.wikipedia.org/wiki/Oceanites) | Storm Petrel | 3652 | [Oceanites oceanicus](https://en.wikipedia.org/wiki/Oceanites_oceanicus) |  |
| 0.0332 | [Ammodramus](https://en.wikipedia.org/wiki/Ammodramus) |  | 19100 | [Ammodramus savannarum](https://en.wikipedia.org/wiki/Ammodramus_savannarum) | Grasshopper Sparrow |
| 0.0329 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)† | Wood Thrush | 82855 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina) | Wood Thrush |
| 0.0316 | [Calonectris](https://en.wikipedia.org/wiki/Calonectris) | Shearwater | 2816 | [Calonectris diomedea](https://en.wikipedia.org/wiki/Calonectris_diomedea) | Cory's Shearwater |
| 0.0305 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 20992 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0304 | [Alle](https://en.wikipedia.org/wiki/Alle) |  | 1004 | [Alle alle](https://en.wikipedia.org/wiki/Alle_alle) |  |
| 0.0284 | [Coccyzus](https://en.wikipedia.org/wiki/Coccyzus) | Cuckoo | 60128 | [Coccyzus americanus](https://en.wikipedia.org/wiki/Coccyzus_americanus) | Yellow-billed Cuckoo |






### Top Genera for Maine (ME)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.1952 | [Somateria](https://en.wikipedia.org/wiki/Somateria) | Eider | 127240 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider |
| 0.1745 | [Fratercula](https://en.wikipedia.org/wiki/Fratercula) | Puffin | 17505 | [Fratercula arctica](https://en.wikipedia.org/wiki/Fratercula_arctica) |  |
| 0.1505 | [Cepphus](https://en.wikipedia.org/wiki/Cepphus) | Guillemot | 58921 | [Cepphus grylle](https://en.wikipedia.org/wiki/Cepphus_grylle) | Black Guillemot |
| 0.1498 | [Alca](https://en.wikipedia.org/wiki/Alca) | Razorbill | 14447 | [Alca torda](https://en.wikipedia.org/wiki/Alca_torda) | Razorbill |
| 0.1297 | [Oceanites](https://en.wikipedia.org/wiki/Oceanites) | Storm Petrel | 8358 | [Oceanites oceanicus](https://en.wikipedia.org/wiki/Oceanites_oceanicus) |  |
| 0.1228 | [Phalacrocorax](https://en.wikipedia.org/wiki/Phalacrocorax) | Cormorant | 18634 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant |
| 0.0886 | [Hydrobates](https://en.wikipedia.org/wiki/Hydrobates) |  | 7559 | [Hydrobates leucorhous](https://en.wikipedia.org/wiki/Hydrobates_leucorhous) | Leach's Storm-Petrel |
| 0.0682 | [Morus](https://en.wikipedia.org/wiki/Gannet) | Gannet | 25405 | [Morus bassanus](https://en.wikipedia.org/wiki/Morus_bassanus) | Northern Gannet |
| 0.0464 | [Clangula](https://en.wikipedia.org/wiki/Clangula) |  | 34160 | [Clangula hyemalis](https://en.wikipedia.org/wiki/Clangula_hyemalis) | Long-tailed Duck |
| 0.0459 | [Puffinus](https://en.wikipedia.org/wiki/Puffinus) | Shearwater | 2786 | [Puffinus puffinus](https://en.wikipedia.org/wiki/Puffinus_puffinus) | Manx Shearwater |






### Top Genera for Michigan (MI)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0985 | [Antigone](https://en.wikipedia.org/wiki/Antigone_(bird)) | Crane | 176499 | [Antigone canadensis](https://en.wikipedia.org/wiki/Antigone_canadensis) | Sandhill Crane |
| 0.0842 | [Cygnus](https://en.wikipedia.org/wiki/Swan) | Swan | 236621 | [Cygnus sp.](https://en.wikipedia.org/wiki/Swan) |  |
| 0.0571 | [Spizelloides](https://en.wikipedia.org/wiki/Spizelloides) | Winter Sparrow | 125158 | [Spizelloides arborea](https://en.wikipedia.org/wiki/Spizelloides_arborea) | American Tree Sparrow |
| 0.0477 | [Pagophila](https://en.wikipedia.org/wiki/Pagophila) | Ivory gull | 295 | [Pagophila eburnea](https://en.wikipedia.org/wiki/Pagophila_eburnea) |  |
| 0.0441 | [Podicipedidae](https://en.wikipedia.org/wiki/Podicipedidae) |  | 494 | [Podicipedidae sp.](https://en.wikipedia.org/wiki/Podicipedidae) |  |
| 0.0405 | [Ardeidae](https://en.wikipedia.org/wiki/Ardeidae) |  | 401 | [Ardeidae sp.](https://en.wikipedia.org/wiki/Ardeidae) |  |
| 0.0320 | [Fringillidae](https://en.wikipedia.org/wiki/Fringillidae) |  | 1450 | [Fringillidae sp.](https://en.wikipedia.org/wiki/Fringillidae) |  |
| 0.0310 | [Pheucticus](https://en.wikipedia.org/wiki/Pheucticus) |  | 147923 | [Pheucticus ludovicianus](https://en.wikipedia.org/wiki/Pheucticus_ludovicianus) | Rose-breasted Grosbeak |
| 0.0289 | [Meleagris](https://en.wikipedia.org/wiki/Meleagris) | Turkey | 90666 | [Meleagris gallopavo](https://en.wikipedia.org/wiki/Meleagris_gallopavo) | Wild Turkey |
| 0.0286 | [Vermivora](https://en.wikipedia.org/wiki/Vermivora) | Warbler | 29441 | [Vermivora cyanoptera](https://en.wikipedia.org/wiki/Vermivora_cyanoptera) | Blue-winged Warbler |






### Top Genera for Minnesota (MN)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.1065 | [Pagophila](https://en.wikipedia.org/wiki/Pagophila) | Ivory gull | 459 | [Pagophila eburnea](https://en.wikipedia.org/wiki/Pagophila_eburnea) |  |
| 0.0792 | [Tympanuchus](https://en.wikipedia.org/wiki/Tympanuchus) | Prarie Chicken | 5462 | [Tympanuchus cupido](https://en.wikipedia.org/wiki/Tympanuchus_cupido) | Greater Prairie-Chicken |
| 0.0720 | [Fringillidae](https://en.wikipedia.org/wiki/Fringillidae) |  | 2025 | [Fringillidae sp.](https://en.wikipedia.org/wiki/Fringillidae) |  |
| 0.0582 | [Phasianus](https://en.wikipedia.org/wiki/Phasianus)†* | Pheasant | 46603 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus) | Ring-necked Pheasant |
| 0.0534 | [Oporornis](https://en.wikipedia.org/wiki/Oporornis) | Connecticut Warbler | 2176 | [Oporornis agilis](https://en.wikipedia.org/wiki/Oporornis_agilis) | Connecticut Warbler |
| 0.0455 | [Picoides](https://en.wikipedia.org/wiki/Picoides) |  | 6040 | [Picoides arcticus](https://en.wikipedia.org/wiki/Picoides_arcticus) | Black-backed Woodpecker |
| 0.0398 | [Pinicola](https://en.wikipedia.org/wiki/Pinicola) |  | 13668 | [Pinicola enucleator](https://en.wikipedia.org/wiki/Pinicola_enucleator) | Pine Grosbeak |
| 0.0372 | [Perisoreus](https://en.wikipedia.org/wiki/Perisoreus) |  | 14026 | [Perisoreus canadensis](https://en.wikipedia.org/wiki/Perisoreus_canadensis) | Canada Jay |
| 0.0321 | [Acanthis](https://en.wikipedia.org/wiki/Redpoll) | Redpoll | 32330 | [Acanthis hornemanni](https://en.wikipedia.org/wiki/Acanthis_hornemanni) | Hoary Redpoll |
| 0.0289 | [Strigiformes](https://en.wikipedia.org/wiki/Strigiformes) |  | 492 | [Strigiformes sp.](https://en.wikipedia.org/wiki/Strigiformes) |  |






### Top Genera for Missouri (MO)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.1044 | [Mergellus](https://en.wikipedia.org/wiki/Mergellus) |  | 109 | [Mergellus albellus](https://en.wikipedia.org/wiki/Mergellus_albellus) |  |
| 0.0679 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 34191 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0497 | [Colinus](https://en.wikipedia.org/wiki/Colinus) | Bobwhite | 21081 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite |
| 0.0352 | [Centronyx](https://en.wikipedia.org/wiki/Centronyx) | Sparrow | 4090 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow |
| 0.0287 | [Icteria](https://en.wikipedia.org/wiki/Icteria) | Yellow-breasted Chat | 22318 | [Icteria virens](https://en.wikipedia.org/wiki/Icteria_virens) | Yellow-breasted Chat |
| 0.0274 | [Coccyzus](https://en.wikipedia.org/wiki/Coccyzus) | Cuckoo | 42272 | [Coccyzus americanus](https://en.wikipedia.org/wiki/Coccyzus_americanus) | Yellow-billed Cuckoo |
| 0.0265 | [Strix](https://en.wikipedia.org/wiki/Strix_(bird)) | Wood Owl | 29694 | [Strix varia](https://en.wikipedia.org/wiki/Strix_varia) | Barred Owl |
| 0.0256 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 13589 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0243 | [Anser](https://en.wikipedia.org/wiki/Anser) | Grey Goose | 46182 | [Anser cygnoides (Domestic type)](https://en.wikipedia.org/wiki/Anser_cygnoides_(Domestic_type)) |  |
| 0.0229 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | 10221 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |






### Top Genera for Mississippi (MS)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0354 | [Limnothlypis](https://en.wikipedia.org/wiki/Limnothlypis) |  | 1697 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler |
| 0.0306 | [Gelochelidon](https://en.wikipedia.org/wiki/Gelochelidon) |  | 3142 | [Gelochelidon nilotica](https://en.wikipedia.org/wiki/Gelochelidon_nilotica) | Gull-billed Tern |
| 0.0234 | [Rynchops](https://en.wikipedia.org/wiki/Rynchops) | Skimmer | 8333 | [Rynchops niger](https://en.wikipedia.org/wiki/Rynchops_niger) | Black Skimmer |
| 0.0196 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 8279 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0174 | [Thalasseus](https://en.wikipedia.org/wiki/Thalasseus) | Crested Tern | 17938 | [Thalasseus maximus](https://en.wikipedia.org/wiki/Thalasseus_maximus) | Royal Tern |
| 0.0169 | [Sternula](https://en.wikipedia.org/wiki/Sternula) |  | 7879 | [Sternula antillarum](https://en.wikipedia.org/wiki/Sternula_antillarum) | Least Tern |
| 0.0166 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | 5820 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| 0.0135 | [Callonetta](https://en.wikipedia.org/wiki/Callonetta) |  | 6 | [Callonetta leucophrys](https://en.wikipedia.org/wiki/Callonetta_leucophrys) |  |
| 0.0108 | [Pelecanus](https://en.wikipedia.org/wiki/Pelecanus)† | Pelican | 30763 | [Pelecanus occidentalis](https://en.wikipedia.org/wiki/Pelecanus_occidentalis) | Brown Pelican |
| 0.0104 | [Rallus](https://en.wikipedia.org/wiki/Rallus) |  | 9579 | [Rallus sp. (large Rallus sp.)](https://en.wikipedia.org/wiki/Rallus) |  |






### Top Genera for Montana (MT)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.1832 | [Rhynchophanes](https://en.wikipedia.org/wiki/Rhynchophanes) | Longspur | 3501 | [Rhynchophanes mccownii](https://en.wikipedia.org/wiki/Rhynchophanes_mccownii) | Thick-billed Longspur |
| 0.1324 | [Sibirionetta](https://en.wikipedia.org/wiki/Sibirionetta) |  | 43 | [Sibirionetta formosa](https://en.wikipedia.org/wiki/Sibirionetta_formosa) |  |
| 0.1315 | [Nucifraga](https://en.wikipedia.org/wiki/Nucifraga) | Nutcracker | 24361 | [Nucifraga columbiana](https://en.wikipedia.org/wiki/Nucifraga_columbiana) | Clark's Nutcracker |
| 0.1289 | [Perdix](https://en.wikipedia.org/wiki/Perdix)* | Partridge | 7149 | [Perdix perdix](https://en.wikipedia.org/wiki/Perdix_perdix) | Gray Partridge |
| 0.1130 | [Centrocercus](https://en.wikipedia.org/wiki/Centrocercus) | Sage-grouse | 1377 | [Centrocercus urophasianus](https://en.wikipedia.org/wiki/Centrocercus_urophasianus) | Greater Sage-Grouse |
| 0.1021 | [Tetraoninae](https://en.wikipedia.org/wiki/Tetraoninae) |  | 164 | [Tetraoninae sp.](https://en.wikipedia.org/wiki/Tetraoninae) |  |
| 0.0885 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | 151463 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| 0.0679 | [Tympanuchus](https://en.wikipedia.org/wiki/Tympanuchus) | Prarie Chicken | 4325 | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse |
| 0.0668 | [Cinclus](https://en.wikipedia.org/wiki/Cinclus) |  | 9534 | [Cinclus mexicanus](https://en.wikipedia.org/wiki/Cinclus_mexicanus) | American Dipper |
| 0.0658 | [Aquila](https://en.wikipedia.org/wiki/Aquila_(bird)) | True Eagle | 17889 | [Aquila chrysaetos](https://en.wikipedia.org/wiki/Aquila_chrysaetos) | Golden Eagle |






### Top Genera for North Carolina (NC)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.3693 | [Pterodroma](https://en.wikipedia.org/wiki/Pterodroma) | Gadfly Petrel | 7392 | [Pterodroma feae](https://en.wikipedia.org/wiki/Pterodroma_feae) |  |
| 0.2432 | [Calonectris](https://en.wikipedia.org/wiki/Calonectris) | Shearwater | 12415 | [Calonectris diomedea](https://en.wikipedia.org/wiki/Calonectris_diomedea) | Cory's Shearwater |
| 0.1671 | [Puffinus](https://en.wikipedia.org/wiki/Puffinus) | Shearwater | 8919 | [Puffinus lherminieri](https://en.wikipedia.org/wiki/Puffinus_lherminieri) |  |
| 0.1227 | [Oceanites](https://en.wikipedia.org/wiki/Oceanites) | Storm Petrel | 8420 | [Oceanites oceanicus](https://en.wikipedia.org/wiki/Oceanites_oceanicus) |  |
| 0.1053 | [Onychoprion](https://en.wikipedia.org/wiki/Onychoprion) |  | 3740 | [Onychoprion anaethetus](https://en.wikipedia.org/wiki/Onychoprion_anaethetus) |  |
| 0.0915 | [Cathartidae](https://en.wikipedia.org/wiki/Cathartidae) |  | 645 | [Cathartidae sp.](https://en.wikipedia.org/wiki/Cathartidae) |  |
| 0.0746 | [Limnothlypis](https://en.wikipedia.org/wiki/Limnothlypis) |  | 4154 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler |
| 0.0574 | [Hydrobates](https://en.wikipedia.org/wiki/Hydrobates) |  | 5837 | [Hydrobates pelagicus](https://en.wikipedia.org/wiki/Hydrobates_pelagicus) |  |
| 0.0474 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 484010 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0414 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 22210 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |






### Top Genera for North Dakota (ND)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.1107 | [Tympanuchus](https://en.wikipedia.org/wiki/Tympanuchus) | Prarie Chicken | 6539 | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse |
| 0.0652 | [Perdix](https://en.wikipedia.org/wiki/Perdix)* | Partridge | 3576 | [Perdix perdix](https://en.wikipedia.org/wiki/Perdix_perdix) | Gray Partridge |
| 0.0513 | [Bartramia](https://en.wikipedia.org/wiki/Bartramia_(bird)) | Upland Sandpiper | 7042 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper |
| 0.0352 | [Phasianus](https://en.wikipedia.org/wiki/Phasianus)†* | Pheasant | 24049 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus) | Ring-necked Pheasant |
| 0.0326 | [Xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus) | Yellow-headed Blackbird | 18180 | [Xanthocephalus xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus_xanthocephalus) | Yellow-headed Blackbird |
| 0.0303 | [Chlidonias](https://en.wikipedia.org/wiki/Chlidonias) |  | 9608 | [Chlidonias niger](https://en.wikipedia.org/wiki/Chlidonias_niger) | Black Tern |
| 0.0281 | [Coturnicops](https://en.wikipedia.org/wiki/Coturnicops) |  | 385 | [Coturnicops noveboracensis](https://en.wikipedia.org/wiki/Coturnicops_noveboracensis) | Yellow Rail |
| 0.0259 | [Calcarius](https://en.wikipedia.org/wiki/Calcarius) | Longspur | 6966 | [Calcarius ornatus](https://en.wikipedia.org/wiki/Calcarius_ornatus) | Chestnut-collared Longspur |
| 0.0239 | [Calamospiza](https://en.wikipedia.org/wiki/Calamospiza)† | Lark Bunting | 2739 | [Calamospiza melanocorys](https://en.wikipedia.org/wiki/Calamospiza_melanocorys) | Lark Bunting |
| 0.0234 | [Ammodramus](https://en.wikipedia.org/wiki/Ammodramus) |  | 8173 | [Ammodramus savannarum](https://en.wikipedia.org/wiki/Ammodramus_savannarum) | Grasshopper Sparrow |






### Top Genera for Nebraska (NE)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0692 | [Tympanuchus](https://en.wikipedia.org/wiki/Tympanuchus) | Prarie Chicken | 4213 | [Tympanuchus cupido](https://en.wikipedia.org/wiki/Tympanuchus_cupido) | Greater Prairie-Chicken |
| 0.0423 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 19658 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0365 | [Bartramia](https://en.wikipedia.org/wiki/Bartramia_(bird)) | Upland Sandpiper | 5257 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper |
| 0.0258 | [Colinus](https://en.wikipedia.org/wiki/Colinus) | Bobwhite | 10081 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite |
| 0.0257 | [Phasianus](https://en.wikipedia.org/wiki/Phasianus)†* | Pheasant | 18728 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus) | Ring-necked Pheasant |
| 0.0238 | [Calamospiza](https://en.wikipedia.org/wiki/Calamospiza)† | Lark Bunting | 2834 | [Calamospiza melanocorys](https://en.wikipedia.org/wiki/Calamospiza_melanocorys) | Lark Bunting |
| 0.0232 | [Ammodramus](https://en.wikipedia.org/wiki/Ammodramus) |  | 8437 | [Ammodramus savannarum](https://en.wikipedia.org/wiki/Ammodramus_savannarum) | Grasshopper Sparrow |
| 0.0195 | [Chondestes](https://en.wikipedia.org/wiki/Chondestes) |  | 13158 | [Chondestes grammacus](https://en.wikipedia.org/wiki/Chondestes_grammacus) | Lark Sparrow |
| 0.0155 | [Sturnella](https://en.wikipedia.org/wiki/Sturnella)‡ | Meadowlark | 52365 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta) | Western Meadowlark |
| 0.0126 | [Rhodostethia](https://en.wikipedia.org/wiki/Rhodostethia) |  | 43 | [Rhodostethia rosea](https://en.wikipedia.org/wiki/Rhodostethia_rosea) | Ross's Gull |






### Top Genera for New Hampshire (NH)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.2408 | [Tadorna](https://en.wikipedia.org/wiki/Tadorna)* | Shelduck | 179 | [Tadorna tadorna](https://en.wikipedia.org/wiki/Tadorna_tadorna) | Common Shelduck |
| 0.0275 | [Cuculidae](https://en.wikipedia.org/wiki/Cuculidae) |  | 16 | [Cuculidae sp.](https://en.wikipedia.org/wiki/Cuculidae) |  |
| 0.0262 | [Coturnix](https://en.wikipedia.org/wiki/Coturnix) |  | 4 | [Coturnix japonica](https://en.wikipedia.org/wiki/Coturnix_japonica) |  |
| 0.0251 | [Alle](https://en.wikipedia.org/wiki/Alle) |  | 546 | [Alle alle](https://en.wikipedia.org/wiki/Alle_alle) |  |
| 0.0226 | [Phalacrocorax](https://en.wikipedia.org/wiki/Phalacrocorax) | Cormorant | 4048 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant |
| 0.0205 | [Somateria](https://en.wikipedia.org/wiki/Somateria) | Eider | 16705 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider |
| 0.0178 | [Oceanites](https://en.wikipedia.org/wiki/Oceanites) | Storm Petrel | 1443 | [Oceanites oceanicus](https://en.wikipedia.org/wiki/Oceanites_oceanicus) |  |
| 0.0136 | [Alca](https://en.wikipedia.org/wiki/Alca) | Razorbill | 1811 | [Alca torda](https://en.wikipedia.org/wiki/Alca_torda) | Razorbill |
| 0.0135 | [Bonasa](https://en.wikipedia.org/wiki/Bonasa)† | Ruffed Grouse | 8834 | [Bonasa umbellus](https://en.wikipedia.org/wiki/Bonasa_umbellus) | Ruffed Grouse |
| 0.0134 | [Seiurus](https://en.wikipedia.org/wiki/Seiurus) | Ovenbird | 34197 | [Seiurus aurocapilla](https://en.wikipedia.org/wiki/Seiurus_aurocapilla) | Ovenbird |






### Top Genera for New Jersey (NJ)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.2287 | [Vanellus](https://en.wikipedia.org/wiki/Vanellus) |  | 552 | [Vanellus vanellus](https://en.wikipedia.org/wiki/Vanellus_vanellus) | Northern Lapwing |
| 0.1686 | [Cuculidae](https://en.wikipedia.org/wiki/Cuculidae) |  | 92 | [Cuculidae sp.](https://en.wikipedia.org/wiki/Cuculidae) |  |
| 0.1156 | [Haematopus](https://en.wikipedia.org/wiki/Haematopus) | Oystercatcher | 68430 | [Haematopus palliatus](https://en.wikipedia.org/wiki/Haematopus_palliatus) | American Oystercatcher |
| 0.1035 | [Rynchops](https://en.wikipedia.org/wiki/Rynchops) | Skimmer | 40882 | [Rynchops niger](https://en.wikipedia.org/wiki/Rynchops_niger) | Black Skimmer |
| 0.0980 | [Gelochelidon](https://en.wikipedia.org/wiki/Gelochelidon) |  | 11666 | [Gelochelidon nilotica](https://en.wikipedia.org/wiki/Gelochelidon_nilotica) | Gull-billed Tern |
| 0.0949 | [Ammospiza](https://en.wikipedia.org/wiki/Ammospiza) |  | 32984 | [Ammospiza maritima](https://en.wikipedia.org/wiki/Ammospiza_maritima) | Seaside Sparrow |
| 0.0932 | [Alle](https://en.wikipedia.org/wiki/Alle) |  | 2087 | [Alle alle](https://en.wikipedia.org/wiki/Alle_alle) |  |
| 0.0907 | [Morus](https://en.wikipedia.org/wiki/Gannet) | Gannet | 37469 | [Morus bassanus](https://en.wikipedia.org/wiki/Morus_bassanus) | Northern Gannet |
| 0.0732 | [Pelagodroma](https://en.wikipedia.org/wiki/Pelagodroma) |  | 181 | [Pelagodroma marina](https://en.wikipedia.org/wiki/Pelagodroma_marina) |  |
| 0.0711 | [Phalacrocorax](https://en.wikipedia.org/wiki/Phalacrocorax) | Cormorant | 13721 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant |






### Top Genera for New Mexico (NM)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.2172 | [Gymnorhinus](https://en.wikipedia.org/wiki/Gymnorhinus) | Pinyon Jay | 13673 | [Gymnorhinus cyanocephalus](https://en.wikipedia.org/wiki/Gymnorhinus_cyanocephalus) | Pinyon Jay |
| 0.1402 | [Geococcyx](https://en.wikipedia.org/wiki/Geococcyx)‡ | Roadrunner | 46838 | [Geococcyx californianus](https://en.wikipedia.org/wiki/Geococcyx_californianus) | Greater Roadrunner |
| 0.1306 | [Leucosticte](https://en.wikipedia.org/wiki/Leucosticte) |  | 10584 | [Leucosticte atrata](https://en.wikipedia.org/wiki/Leucosticte_atrata) | Black Rosy-Finch |
| 0.0834 | [Myadestes](https://en.wikipedia.org/wiki/Myadestes) |  | 32323 | [Myadestes townsendi](https://en.wikipedia.org/wiki/Myadestes_townsendi) | Townsend's Solitaire |
| 0.0815 | [Amphispiza](https://en.wikipedia.org/wiki/Amphispiza) |  | 23571 | [Amphispiza bilineata](https://en.wikipedia.org/wiki/Amphispiza_bilineata) | Black-throated Sparrow |
| 0.0802 | [Salpinctes](https://en.wikipedia.org/wiki/Salpinctes) |  | 22761 | [Salpinctes obsoletus](https://en.wikipedia.org/wiki/Salpinctes_obsoletus) | Rock Wren |
| 0.0799 | [Melozone](https://en.wikipedia.org/wiki/Melozone) |  | 66915 | [Melozone fusca](https://en.wikipedia.org/wiki/Melozone_fusca) | Canyon Towhee |
| 0.0768 | [Aeronautes](https://en.wikipedia.org/wiki/Aeronautes) |  | 14189 | [Aeronautes saxatalis](https://en.wikipedia.org/wiki/Aeronautes_saxatalis) | White-throated Swift |
| 0.0754 | [Artemisiospiza](https://en.wikipedia.org/wiki/Artemisiospiza) | Sparrow | 3551 | [Artemisiospiza nevadensis](https://en.wikipedia.org/wiki/Artemisiospiza_nevadensis) | Sagebrush Sparrow |
| 0.0715 | [Calamospiza](https://en.wikipedia.org/wiki/Calamospiza)† | Lark Bunting | 8353 | [Calamospiza melanocorys](https://en.wikipedia.org/wiki/Calamospiza_melanocorys) | Lark Bunting |






### Top Genera for Nevada (NV)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.9960 | [Tetraogallus](https://en.wikipedia.org/wiki/Tetraogallus)* | Snowcock | 672 | [Tetraogallus himalayensis](https://en.wikipedia.org/wiki/Tetraogallus_himalayensis) |  |
| 0.1247 | [Artemisiospiza](https://en.wikipedia.org/wiki/Artemisiospiza) | Sparrow | 5324 | [Artemisiospiza nevadensis](https://en.wikipedia.org/wiki/Artemisiospiza_nevadensis) | Sagebrush Sparrow |
| 0.0866 | [Gymnorhinus](https://en.wikipedia.org/wiki/Gymnorhinus) | Pinyon Jay | 5444 | [Gymnorhinus cyanocephalus](https://en.wikipedia.org/wiki/Gymnorhinus_cyanocephalus) | Pinyon Jay |
| 0.0662 | [Oreoscoptes](https://en.wikipedia.org/wiki/Oreoscoptes) | Sage Thrasher | 6385 | [Oreoscoptes montanus](https://en.wikipedia.org/wiki/Oreoscoptes_montanus) | Sage Thrasher |
| 0.0523 | [Centrocercus](https://en.wikipedia.org/wiki/Centrocercus) | Sage-grouse | 645 | [Centrocercus urophasianus](https://en.wikipedia.org/wiki/Centrocercus_urophasianus) | Greater Sage-Grouse |
| 0.0504 | [Phainopepla](https://en.wikipedia.org/wiki/Phainopepla) | Phainopepla | 14504 | [Phainopepla nitens](https://en.wikipedia.org/wiki/Phainopepla_nitens) | Phainopepla |
| 0.0496 | [Auriparus](https://en.wikipedia.org/wiki/Auriparus) | Verdin | 29373 | [Auriparus flaviceps](https://en.wikipedia.org/wiki/Auriparus_flaviceps) | Verdin |
| 0.0492 | [Callipepla](https://en.wikipedia.org/wiki/Callipepla)† | Crested Quail | 49041 | [Callipepla gambelii](https://en.wikipedia.org/wiki/Callipepla_gambelii) | Gambel's Quail |
| 0.0475 | [Alectoris](https://en.wikipedia.org/wiki/Alectoris)* | Rock Partridge | 1810 | [Alectoris chukar](https://en.wikipedia.org/wiki/Alectoris_chukar) | Chukar |
| 0.0463 | [Amphispiza](https://en.wikipedia.org/wiki/Amphispiza) |  | 12902 | [Amphispiza bilineata](https://en.wikipedia.org/wiki/Amphispiza_bilineata) | Black-throated Sparrow |






### Top Genera for New York (NY)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.8710 | [Crex](https://en.wikipedia.org/wiki/Crex) |  | 178 | [Crex crex](https://en.wikipedia.org/wiki/Crex_crex) |  |
| 0.2971 | [Carduelis](https://en.wikipedia.org/wiki/Carduelis)* | Goldfinch | 1971 | [Carduelis carduelis](https://en.wikipedia.org/wiki/Carduelis_carduelis) | European Goldfinch |
| 0.1124 | [Aves](https://en.wikipedia.org/wiki/Aves) |  | 3092 | [Aves sp.](https://en.wikipedia.org/wiki/Aves) |  |
| 0.1050 | [Pelagodroma](https://en.wikipedia.org/wiki/Pelagodroma) |  | 286 | [Pelagodroma marina](https://en.wikipedia.org/wiki/Pelagodroma_marina) |  |
| 0.0685 | [Vermivora](https://en.wikipedia.org/wiki/Vermivora) | Warbler | 61677 | [Vermivora cyanoptera](https://en.wikipedia.org/wiki/Vermivora_cyanoptera) | Blue-winged Warbler |
| 0.0659 | [Phalacrocorax](https://en.wikipedia.org/wiki/Phalacrocorax) | Cormorant | 16757 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant |
| 0.0650 | [Clangula](https://en.wikipedia.org/wiki/Clangula) |  | 69918 | [Clangula hyemalis](https://en.wikipedia.org/wiki/Clangula_hyemalis) | Long-tailed Duck |
| 0.0581 | [Haematopus](https://en.wikipedia.org/wiki/Haematopus) | Oystercatcher | 54113 | [Haematopus palliatus](https://en.wikipedia.org/wiki/Haematopus_palliatus) | American Oystercatcher |
| 0.0550 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)† | Wood Thrush | 150414 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina) | Wood Thrush |
| 0.0530 | [Myiopsitta](https://en.wikipedia.org/wiki/Myiopsitta)* |  | 13166 | [Myiopsitta monachus](https://en.wikipedia.org/wiki/Myiopsitta_monachus) | Monk Parakeet |






### Top Genera for Ohio (OH)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0998 | [Fringilla](https://en.wikipedia.org/wiki/Fringilla) |  | 632 | [Fringilla montifringilla](https://en.wikipedia.org/wiki/Fringilla_montifringilla) |  |
| 0.0684 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 36537 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0550 | [Centronyx](https://en.wikipedia.org/wiki/Centronyx) | Sparrow | 7629 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow |
| 0.0467 | [Scolopax](https://en.wikipedia.org/wiki/Scolopax) | Woodcock | 21715 | [Scolopax minor](https://en.wikipedia.org/wiki/Scolopax_minor) | American Woodcock |
| 0.0422 | [Tyrannidae](https://en.wikipedia.org/wiki/Tyrannidae) |  | 3465 | [Tyrannidae sp.](https://en.wikipedia.org/wiki/Tyrannidae) |  |
| 0.0391 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)† | Wood Thrush | 98855 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina) | Wood Thrush |
| 0.0334 | [Oporornis](https://en.wikipedia.org/wiki/Oporornis) | Connecticut Warbler | 2121 | [Oporornis agilis](https://en.wikipedia.org/wiki/Oporornis_agilis) | Connecticut Warbler |
| 0.0304 | [Spizelloides](https://en.wikipedia.org/wiki/Spizelloides) | Winter Sparrow | 91542 | [Spizelloides arborea](https://en.wikipedia.org/wiki/Spizelloides_arborea) | American Tree Sparrow |
| 0.0302 | [Vermivora](https://en.wikipedia.org/wiki/Vermivora) | Warbler | 31737 | [Vermivora cyanoptera](https://en.wikipedia.org/wiki/Vermivora_cyanoptera) | Blue-winged Warbler |
| 0.0299 | [Chroicocephalus](https://en.wikipedia.org/wiki/Chroicocephalus) |  | 56168 | [Chroicocephalus philadelphia](https://en.wikipedia.org/wiki/Chroicocephalus_philadelphia) | Bonaparte's Gull |






### Top Genera for Oklahoma (OK)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.1586 | [Tadorna](https://en.wikipedia.org/wiki/Tadorna)* | Shelduck | 118 | [Tadorna ferruginea](https://en.wikipedia.org/wiki/Tadorna_ferruginea) |  |
| 0.0713 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | 21873 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| 0.0311 | [Nomonyx](https://en.wikipedia.org/wiki/Nomonyx) |  | 46 | [Nomonyx dominicus](https://en.wikipedia.org/wiki/Nomonyx_dominicus) | Masked Duck |
| 0.0295 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 14500 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0249 | [Bartramia](https://en.wikipedia.org/wiki/Bartramia_(bird)) | Upland Sandpiper | 3825 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper |
| 0.0242 | [Colinus](https://en.wikipedia.org/wiki/Colinus) | Bobwhite | 9753 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite |
| 0.0229 | [Chondestes](https://en.wikipedia.org/wiki/Chondestes) |  | 15360 | [Chondestes grammacus](https://en.wikipedia.org/wiki/Chondestes_grammacus) | Lark Sparrow |
| 0.0119 | [Geococcyx](https://en.wikipedia.org/wiki/Geococcyx)† | Roadrunner | 5124 | [Geococcyx californianus](https://en.wikipedia.org/wiki/Geococcyx_californianus) | Greater Roadrunner |
| 0.0115 | [Tyrannus](https://en.wikipedia.org/wiki/Tyrannus)‡ | Kingbird/Flycatcher | 70179 | [Tyrannus forficatus](https://en.wikipedia.org/wiki/Tyrannus_forficatus) | Scissor-tailed Flycatcher |
| 0.0111 | [Aimophila](https://en.wikipedia.org/wiki/Aimophila) |  | 2308 | [Aimophila ruficeps](https://en.wikipedia.org/wiki/Aimophila_ruficeps) | Rufous-crowned Sparrow |






### Top Genera for Oregon (OR)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.4319 | [Oreortyx](https://en.wikipedia.org/wiki/Oreortyx) |  | 8746 | [Oreortyx pictus](https://en.wikipedia.org/wiki/Oreortyx_pictus) | Mountain Quail |
| 0.3822 | [Chloris](https://en.wikipedia.org/wiki/Chloris) |  | 43 | [Chloris sinica](https://en.wikipedia.org/wiki/Chloris_sinica) |  |
| 0.3605 | [Chamaea](https://en.wikipedia.org/wiki/Chamaea) | Wrentit | 38911 | [Chamaea fasciata](https://en.wikipedia.org/wiki/Chamaea_fasciata) | Wrentit |
| 0.2879 | [Aphelocoma](https://en.wikipedia.org/wiki/Aphelocoma) | Scrub Jay | 374161 | [Aphelocoma californica](https://en.wikipedia.org/wiki/Aphelocoma_californica) | California Scrub-Jay |
| 0.2665 | [Corvidae](https://en.wikipedia.org/wiki/Corvidae) |  | 307 | [Corvidae sp. (jay sp.)](https://en.wikipedia.org/wiki/Corvidae) |  |
| 0.2328 | [Ptychoramphus](https://en.wikipedia.org/wiki/Ptychoramphus) |  | 6098 | [Ptychoramphus aleuticus](https://en.wikipedia.org/wiki/Ptychoramphus_aleuticus) | Cassin's Auklet |
| 0.2172 | [Phoebastria](https://en.wikipedia.org/wiki/Phoebastria) |  | 8958 | [Phoebastria nigripes](https://en.wikipedia.org/wiki/Phoebastria_nigripes) |  |
| 0.1915 | [Ixoreus](https://en.wikipedia.org/wiki/Ixoreus) |  | 82130 | [Ixoreus naevius](https://en.wikipedia.org/wiki/Ixoreus_naevius) | Varied Thrush |
| 0.1648 | [Psaltriparus](https://en.wikipedia.org/wiki/Psaltriparus) |  | 141123 | [Psaltriparus minimus](https://en.wikipedia.org/wiki/Psaltriparus_minimus) | Bushtit |
| 0.1565 | [Urile](https://en.wikipedia.org/wiki/Urile) |  | 76024 | [Urile penicillatus](https://en.wikipedia.org/wiki/Urile_penicillatus) | Brandt's Cormorant |






### Top Genera for Pennsylvania (PA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0974 | [Aves](https://en.wikipedia.org/wiki/Aves) |  | 2489 | [Aves sp.](https://en.wikipedia.org/wiki/Aves) |  |
| 0.0882 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)† | Wood Thrush | 171036 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina) | Wood Thrush |
| 0.0820 | [Cuculidae](https://en.wikipedia.org/wiki/Cuculidae) |  | 56 | [Cuculidae sp.](https://en.wikipedia.org/wiki/Cuculidae) |  |
| 0.0701 | [Cathartidae](https://en.wikipedia.org/wiki/Cathartidae) |  | 622 | [Cathartidae sp.](https://en.wikipedia.org/wiki/Cathartidae) |  |
| 0.0437 | [Dumetella](https://en.wikipedia.org/wiki/Dumetella) | Gray Catbird | 456717 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird |
| 0.0403 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 557667 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0371 | [Seiurus](https://en.wikipedia.org/wiki/Seiurus) | Ovenbird | 127243 | [Seiurus aurocapilla](https://en.wikipedia.org/wiki/Seiurus_aurocapilla) | Ovenbird |
| 0.0370 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 620147 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0283 | [Helmitheros](https://en.wikipedia.org/wiki/Helmitheros) |  | 14138 | [Helmitheros vermivorum](https://en.wikipedia.org/wiki/Helmitheros_vermivorum) | Worm-eating Warbler |
| 0.0258 | [Chaetura](https://en.wikipedia.org/wiki/Chaetura) | Swift | 169326 | [Chaetura pelagica](https://en.wikipedia.org/wiki/Chaetura_pelagica) | Chimney Swift |






### Top Genera for Rhode Island (RI)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.6080 | [Cuculus](https://en.wikipedia.org/wiki/Cuculus)* | Cuckoo | 672 | [Cuculus canorus](https://en.wikipedia.org/wiki/Cuculus_canorus) | Common Cuckoo |
| 0.2711 | [Xenus](https://en.wikipedia.org/wiki/Xenus) |  | 194 | [Xenus cinereus](https://en.wikipedia.org/wiki/Xenus_cinereus) |  |
| 0.0584 | [Phalacrocorax](https://en.wikipedia.org/wiki/Phalacrocorax) | Cormorant | 8422 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant |
| 0.0368 | [Mergellus](https://en.wikipedia.org/wiki/Mergellus) |  | 37 | [Mergellus albellus](https://en.wikipedia.org/wiki/Mergellus_albellus) |  |
| 0.0268 | [Somateria](https://en.wikipedia.org/wiki/Somateria) | Eider | 18190 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider |
| 0.0167 | [Histrionicus](https://en.wikipedia.org/wiki/Histrionicus) |  | 4628 | [Histrionicus histrionicus](https://en.wikipedia.org/wiki/Histrionicus_histrionicus) | Harlequin Duck |
| 0.0164 | [Calonectris](https://en.wikipedia.org/wiki/Calonectris) | Shearwater | 907 | [Calonectris diomedea](https://en.wikipedia.org/wiki/Calonectris_diomedea) | Cory's Shearwater |
| 0.0138 | [Alca](https://en.wikipedia.org/wiki/Alca) | Razorbill | 1489 | [Alca torda](https://en.wikipedia.org/wiki/Alca_torda) | Razorbill |
| 0.0136 | [Cathartidae](https://en.wikipedia.org/wiki/Cathartidae) |  | 95 | [Cathartidae sp.](https://en.wikipedia.org/wiki/Cathartidae) |  |
| 0.0122 | [Ammospiza](https://en.wikipedia.org/wiki/Ammospiza) |  | 4029 | [Ammospiza caudacuta](https://en.wikipedia.org/wiki/Ammospiza_caudacuta) | Saltmarsh Sparrow |






### Top Genera for South Carolina (SC)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0872 | [Mycteria](https://en.wikipedia.org/wiki/Mycteria) | Stork | 40234 | [Mycteria americana](https://en.wikipedia.org/wiki/Mycteria_americana) | Wood Stork |
| 0.0716 | [Charadriidae](https://en.wikipedia.org/wiki/Charadriidae) |  | 117 | [Charadriidae sp.](https://en.wikipedia.org/wiki/Charadriidae) |  |
| 0.0674 | [Cathartidae](https://en.wikipedia.org/wiki/Cathartidae) |  | 454 | [Cathartidae sp.](https://en.wikipedia.org/wiki/Cathartidae) |  |
| 0.0598 | [Limnothlypis](https://en.wikipedia.org/wiki/Limnothlypis) |  | 3114 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler |
| 0.0586 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | 20288 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| 0.0553 | [Anhinga](https://en.wikipedia.org/wiki/Anhinga) | Darter | 52941 | [Anhinga anhinga](https://en.wikipedia.org/wiki/Anhinga_anhinga) | Anhinga |
| 0.0456 | [Threskiornithidae](https://en.wikipedia.org/wiki/Threskiornithidae) |  | 34 | [Threskiornithidae sp. (ibis sp.)](https://en.wikipedia.org/wiki/Threskiornithidae) |  |
| 0.0384 | [Rynchops](https://en.wikipedia.org/wiki/Rynchops) | Skimmer | 15485 | [Rynchops niger](https://en.wikipedia.org/wiki/Rynchops_niger) | Black Skimmer |
| 0.0376 | [Rallus](https://en.wikipedia.org/wiki/Rallus) |  | 33856 | [Rallus crepitans](https://en.wikipedia.org/wiki/Rallus_crepitans) | Clapper Rail |
| 0.0370 | [Gelochelidon](https://en.wikipedia.org/wiki/Gelochelidon) |  | 4480 | [Gelochelidon nilotica](https://en.wikipedia.org/wiki/Gelochelidon_nilotica) | Gull-billed Tern |






### Top Genera for South Dakota (SD)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0542 | [Tympanuchus](https://en.wikipedia.org/wiki/Tympanuchus) | Prarie Chicken | 3235 | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse |
| 0.0381 | [Bartramia](https://en.wikipedia.org/wiki/Bartramia_(bird)) | Upland Sandpiper | 5213 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper |
| 0.0313 | [Calamospiza](https://en.wikipedia.org/wiki/Calamospiza)† | Lark Bunting | 3391 | [Calamospiza melanocorys](https://en.wikipedia.org/wiki/Calamospiza_melanocorys) | Lark Bunting |
| 0.0219 | [Phasianus](https://en.wikipedia.org/wiki/Phasianus)‡* | Pheasant | 15094 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus) | Ring-necked Pheasant |
| 0.0181 | [Athene](https://en.wikipedia.org/wiki/Athene) |  | 1976 | [Athene cunicularia](https://en.wikipedia.org/wiki/Athene_cunicularia) | Burrowing Owl |
| 0.0167 | [Xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus) | Yellow-headed Blackbird | 9544 | [Xanthocephalus xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus_xanthocephalus) | Yellow-headed Blackbird |
| 0.0119 | [Aeronautes](https://en.wikipedia.org/wiki/Aeronautes) |  | 2257 | [Aeronautes saxatalis](https://en.wikipedia.org/wiki/Aeronautes_saxatalis) | White-throated Swift |
| 0.0113 | [Ammodramus](https://en.wikipedia.org/wiki/Ammodramus) |  | 4140 | [Ammodramus savannarum](https://en.wikipedia.org/wiki/Ammodramus_savannarum) | Grasshopper Sparrow |
| 0.0106 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 5350 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0095 | [Corvidae](https://en.wikipedia.org/wiki/Corvidae) |  | 12 | [Corvidae sp. (jay sp.)](https://en.wikipedia.org/wiki/Corvidae) |  |






### Top Genera for Tennessee (TN)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0424 | [Limnothlypis](https://en.wikipedia.org/wiki/Limnothlypis) |  | 2385 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler |
| 0.0352 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 16980 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0295 | [Icteria](https://en.wikipedia.org/wiki/Icteria) | Yellow-breasted Chat | 22678 | [Icteria virens](https://en.wikipedia.org/wiki/Icteria_virens) | Yellow-breasted Chat |
| 0.0253 | [Colinus](https://en.wikipedia.org/wiki/Colinus) | Bobwhite | 12762 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite |
| 0.0249 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 264394 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0246 | [Helmitheros](https://en.wikipedia.org/wiki/Helmitheros) |  | 7863 | [Helmitheros vermivorum](https://en.wikipedia.org/wiki/Helmitheros_vermivorum) | Worm-eating Warbler |
| 0.0230 | [Grus](https://en.wikipedia.org/wiki/Grus_(genus)) | Crane | 869 | [Grus monacha](https://en.wikipedia.org/wiki/Grus_monacha) |  |
| 0.0219 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 181103 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0197 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | 9261 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| 0.0197 | [Mimus](https://en.wikipedia.org/wiki/Mimus)‡ | Mockingbird | 199634 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |






### Top Genera for Texas (TX)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.9136 | [Spermestes](https://en.wikipedia.org/wiki/Spermestes) |  | 120 | [Spermestes cucullata](https://en.wikipedia.org/wiki/Spermestes_cucullata) |  |
| 0.8348 | [Geranoaetus](https://en.wikipedia.org/wiki/Geranoaetus) |  | 54492 | [Geranoaetus albicaudatus](https://en.wikipedia.org/wiki/Geranoaetus_albicaudatus) | White-tailed Hawk |
| 0.7278 | [Arremonops](https://en.wikipedia.org/wiki/Arremonops) |  | 82550 | [Arremonops rufivirgatus](https://en.wikipedia.org/wiki/Arremonops_rufivirgatus) | Olive Sparrow |
| 0.6732 | [Caracara](https://en.wikipedia.org/wiki/Caracara_(genus)) | Caracara | 249608 | [Caracara plancus](https://en.wikipedia.org/wiki/Caracara_plancus) | Crested Caracara |
| 0.6550 | [Nyctidromus](https://en.wikipedia.org/wiki/Nyctidromus) |  | 31129 | [Nyctidromus albicollis](https://en.wikipedia.org/wiki/Nyctidromus_albicollis) | Common Pauraque |
| 0.6522 | [Tachybaptus](https://en.wikipedia.org/wiki/Tachybaptus) |  | 65119 | [Tachybaptus dominicus](https://en.wikipedia.org/wiki/Tachybaptus_dominicus) | Least Grebe |
| 0.6201 | [Cyanocorax](https://en.wikipedia.org/wiki/Cyanocorax) |  | 150450 | [Cyanocorax yncas](https://en.wikipedia.org/wiki/Cyanocorax_yncas) | Green Jay |
| 0.6032 | [Parabuteo](https://en.wikipedia.org/wiki/Parabuteo) |  | 80483 | [Parabuteo unicinctus](https://en.wikipedia.org/wiki/Parabuteo_unicinctus) | Harris's Hawk |
| 0.5380 | [Nomonyx](https://en.wikipedia.org/wiki/Nomonyx) |  | 774 | [Nomonyx dominicus](https://en.wikipedia.org/wiki/Nomonyx_dominicus) | Masked Duck |
| 0.5256 | [Chloroceryle](https://en.wikipedia.org/wiki/Chloroceryle) |  | 42946 | [Chloroceryle americana](https://en.wikipedia.org/wiki/Chloroceryle_americana) | Green Kingfisher |






### Top Genera for Utah (UT)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.1930 | [Alectoris](https://en.wikipedia.org/wiki/Alectoris)* | Rock Partridge | 7064 | [Alectoris chukar](https://en.wikipedia.org/wiki/Alectoris_chukar) | Chukar |
| 0.1869 | [Psiloscops](https://en.wikipedia.org/wiki/Psiloscops) |  | 2119 | [Psiloscops flammeolus](https://en.wikipedia.org/wiki/Psiloscops_flammeolus) | Flammulated Owl |
| 0.1671 | [Gymnogyps](https://en.wikipedia.org/wiki/Gymnogyps) |  | 1515 | [Gymnogyps californianus](https://en.wikipedia.org/wiki/Gymnogyps_californianus) | California Condor |
| 0.1244 | [Gymnorhinus](https://en.wikipedia.org/wiki/Gymnorhinus) | Pinyon Jay | 7974 | [Gymnorhinus cyanocephalus](https://en.wikipedia.org/wiki/Gymnorhinus_cyanocephalus) | Pinyon Jay |
| 0.1188 | [Centrocercus](https://en.wikipedia.org/wiki/Centrocercus) | Sage-grouse | 1455 | [Centrocercus urophasianus](https://en.wikipedia.org/wiki/Centrocercus_urophasianus) | Greater Sage-Grouse |
| 0.0968 | [Oreoscoptes](https://en.wikipedia.org/wiki/Oreoscoptes) | Sage Thrasher | 9559 | [Oreoscoptes montanus](https://en.wikipedia.org/wiki/Oreoscoptes_montanus) | Sage Thrasher |
| 0.0869 | [Aquila](https://en.wikipedia.org/wiki/Aquila_(bird)) | True Eagle | 23315 | [Aquila chrysaetos](https://en.wikipedia.org/wiki/Aquila_chrysaetos) | Golden Eagle |
| 0.0751 | [Aeronautes](https://en.wikipedia.org/wiki/Aeronautes) |  | 13570 | [Aeronautes saxatalis](https://en.wikipedia.org/wiki/Aeronautes_saxatalis) | White-throated Swift |
| 0.0736 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | 129642 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| 0.0707 | [Leucosticte](https://en.wikipedia.org/wiki/Leucosticte) |  | 5931 | [Leucosticte atrata](https://en.wikipedia.org/wiki/Leucosticte_atrata) | Black Rosy-Finch |






### Top Genera for Virginia (VA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0644 | [Numida](https://en.wikipedia.org/wiki/Numida) |  | 232 | [Numida meleagris (Domestic type)](https://en.wikipedia.org/wiki/Numida_meleagris_(Domestic_type)) |  |
| 0.0571 | [Helmitheros](https://en.wikipedia.org/wiki/Helmitheros) |  | 18144 | [Helmitheros vermivorum](https://en.wikipedia.org/wiki/Helmitheros_vermivorum) | Worm-eating Warbler |
| 0.0560 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 597727 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0415 | [Coragyps](https://en.wikipedia.org/wiki/Coragyps) | Black Vulture | 174913 | [Coragyps atratus](https://en.wikipedia.org/wiki/Coragyps_atratus) | Black Vulture |
| 0.0386 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 23888 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0368 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 344496 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0367 | [Coccyzus](https://en.wikipedia.org/wiki/Coccyzus) | Cuckoo | 68865 | [Coccyzus americanus](https://en.wikipedia.org/wiki/Coccyzus_americanus) | Yellow-billed Cuckoo |
| 0.0337 | [Dryocopus](https://en.wikipedia.org/wiki/Dryocopus) | Woodpecker | 195902 | [Dryocopus pileatus](https://en.wikipedia.org/wiki/Dryocopus_pileatus) | Pileated Woodpecker |
| 0.0305 | [Troglodytidae](https://en.wikipedia.org/wiki/Troglodytidae) |  | 1142 | [Troglodytidae sp.](https://en.wikipedia.org/wiki/Troglodytidae) |  |
| 0.0293 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 475019 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |






### Top Genera for Vermont (VT)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0297 | [Bonasa](https://en.wikipedia.org/wiki/Bonasa)† | Ruffed Grouse | 16963 | [Bonasa umbellus](https://en.wikipedia.org/wiki/Bonasa_umbellus) | Ruffed Grouse |
| 0.0254 | [Tetraoninae](https://en.wikipedia.org/wiki/Tetraoninae) |  | 52 | [Tetraoninae sp.](https://en.wikipedia.org/wiki/Tetraoninae) |  |
| 0.0243 | [Seiurus](https://en.wikipedia.org/wiki/Seiurus) | Ovenbird | 56705 | [Seiurus aurocapilla](https://en.wikipedia.org/wiki/Seiurus_aurocapilla) | Ovenbird |
| 0.0216 | [Dolichonyx](https://en.wikipedia.org/wiki/Dolichonyx) |  | 18269 | [Dolichonyx oryzivorus](https://en.wikipedia.org/wiki/Dolichonyx_oryzivorus) | Bobolink |
| 0.0198 | [Canachites](https://en.wikipedia.org/wiki/Canachites) |  | 1039 | [Canachites canadensis](https://en.wikipedia.org/wiki/Canachites_canadensis) | Spruce Grouse |
| 0.0180 | [Scolopax](https://en.wikipedia.org/wiki/Scolopax) | Woodcock | 7351 | [Scolopax minor](https://en.wikipedia.org/wiki/Scolopax_minor) | American Woodcock |
| 0.0152 | [Spizelloides](https://en.wikipedia.org/wiki/Spizelloides) | Winter Sparrow | 34849 | [Spizelloides arborea](https://en.wikipedia.org/wiki/Spizelloides_arborea) | American Tree Sparrow |
| 0.0145 | [Acanthis](https://en.wikipedia.org/wiki/Redpoll) | Redpoll | 16066 | [Acanthis flammea](https://en.wikipedia.org/wiki/Acanthis_flammea) | Common Redpoll |
| 0.0139 | [Sphyrapicus](https://en.wikipedia.org/wiki/Sphyrapicus) |  | 46917 | [Sphyrapicus varius](https://en.wikipedia.org/wiki/Sphyrapicus_varius) | Yellow-bellied Sapsucker |
| 0.0138 | [Botaurus](https://en.wikipedia.org/wiki/Botaurus) |  | 6920 | [Botaurus lentiginosus](https://en.wikipedia.org/wiki/Botaurus_lentiginosus) | American Bittern |






### Top Genera for Washington (WA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.9451 | [Creagrus](https://en.wikipedia.org/wiki/Creagrus) |  | 488 | [Creagrus furcatus](https://en.wikipedia.org/wiki/Creagrus_furcatus) |  |
| 0.5010 | [Cerorhinca](https://en.wikipedia.org/wiki/Cerorhinca) | Rhinoceros Puffin | 56517 | [Cerorhinca monocerata](https://en.wikipedia.org/wiki/Cerorhinca_monocerata) | Rhinoceros Auklet |
| 0.4907 | [Prunella](https://en.wikipedia.org/wiki/Prunella) |  | 589 | [Prunella montanella](https://en.wikipedia.org/wiki/Prunella_montanella) |  |
| 0.2925 | [Ptychoramphus](https://en.wikipedia.org/wiki/Ptychoramphus) |  | 7628 | [Ptychoramphus aleuticus](https://en.wikipedia.org/wiki/Ptychoramphus_aleuticus) | Cassin's Auklet |
| 0.2786 | [Urile](https://en.wikipedia.org/wiki/Urile) |  | 128798 | [Urile penicillatus](https://en.wikipedia.org/wiki/Urile_penicillatus) | Brandt's Cormorant |
| 0.2416 | [Alcidae](https://en.wikipedia.org/wiki/Alcidae) |  | 2842 | [Alcidae sp.](https://en.wikipedia.org/wiki/Alcidae) |  |
| 0.2383 | [Chrysolophus](https://en.wikipedia.org/wiki/Chrysolophus) |  | 32 | [Chrysolophus pictus](https://en.wikipedia.org/wiki/Chrysolophus_pictus) |  |
| 0.2288 | [Ixoreus](https://en.wikipedia.org/wiki/Ixoreus) |  | 98229 | [Ixoreus naevius](https://en.wikipedia.org/wiki/Ixoreus_naevius) | Varied Thrush |
| 0.2240 | [Podicipedidae](https://en.wikipedia.org/wiki/Podicipedidae) |  | 1692 | [Podicipedidae sp.](https://en.wikipedia.org/wiki/Podicipedidae) |  |
| 0.2228 | [Cepphus](https://en.wikipedia.org/wiki/Cepphus) | Guillemot | 92260 | [Cepphus columba](https://en.wikipedia.org/wiki/Cepphus_columba) | Pigeon Guillemot |






### Top Genera for Wisconsin (WI)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.9598 | [Parus](https://en.wikipedia.org/wiki/Parus)* |  | 729 | [Parus major](https://en.wikipedia.org/wiki/Parus_major) | Great Tit |
| 0.1417 | [Antigone](https://en.wikipedia.org/wiki/Antigone_(bird)) | Crane | 231517 | [Antigone canadensis](https://en.wikipedia.org/wiki/Antigone_canadensis) | Sandhill Crane |
| 0.1073 | [Carduelis](https://en.wikipedia.org/wiki/Carduelis)* | Goldfinch | 755 | [Carduelis carduelis](https://en.wikipedia.org/wiki/Carduelis_carduelis) | European Goldfinch |
| 0.0699 | [Centronyx](https://en.wikipedia.org/wiki/Centronyx) | Sparrow | 8403 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow |
| 0.0599 | [Vermivora](https://en.wikipedia.org/wiki/Vermivora) | Warbler | 43527 | [Vermivora chrysoptera](https://en.wikipedia.org/wiki/Vermivora_chrysoptera) | Golden-winged Warbler |
| 0.0516 | [Meleagris](https://en.wikipedia.org/wiki/Meleagris) | Turkey | 120796 | [Meleagris gallopavo](https://en.wikipedia.org/wiki/Meleagris_gallopavo) | Wild Turkey |
| 0.0366 | [Scolopax](https://en.wikipedia.org/wiki/Scolopax) | Woodcock | 17392 | [Scolopax minor](https://en.wikipedia.org/wiki/Scolopax_minor) | American Woodcock |
| 0.0354 | [Chlidonias](https://en.wikipedia.org/wiki/Chlidonias) |  | 18353 | [Chlidonias leucopterus](https://en.wikipedia.org/wiki/Chlidonias_leucopterus) | White-winged Tern |
| 0.0346 | [Bonasa](https://en.wikipedia.org/wiki/Bonasa)† | Ruffed Grouse | 27246 | [Bonasa umbellus](https://en.wikipedia.org/wiki/Bonasa_umbellus) | Ruffed Grouse |
| 0.0338 | [Pheucticus](https://en.wikipedia.org/wiki/Pheucticus) |  | 147853 | [Pheucticus ludovicianus](https://en.wikipedia.org/wiki/Pheucticus_ludovicianus) | Rose-breasted Grosbeak |






### Top Genera for West Virginia (WV)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0157 | [Limnothlypis](https://en.wikipedia.org/wiki/Limnothlypis) |  | 850 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler |
| 0.0128 | [Helmitheros](https://en.wikipedia.org/wiki/Helmitheros) |  | 3533 | [Helmitheros vermivorum](https://en.wikipedia.org/wiki/Helmitheros_vermivorum) | Worm-eating Warbler |
| 0.0110 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)† | Wood Thrush | 20027 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina) | Wood Thrush |
| 0.0079 | [Dryocopus](https://en.wikipedia.org/wiki/Dryocopus) | Woodpecker | 37014 | [Dryocopus pileatus](https://en.wikipedia.org/wiki/Dryocopus_pileatus) | Pileated Woodpecker |
| 0.0073 | [Picidae](https://en.wikipedia.org/wiki/Picidae) |  | 1137 | [Picidae sp.](https://en.wikipedia.org/wiki/Picidae) |  |
| 0.0061 | [Coccyzus](https://en.wikipedia.org/wiki/Coccyzus) | Cuckoo | 10480 | [Coccyzus americanus](https://en.wikipedia.org/wiki/Coccyzus_americanus) | Yellow-billed Cuckoo |
| 0.0058 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 67983 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0053 | [Pipilo](https://en.wikipedia.org/wiki/Pipilo) | Towhee | 51062 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee |
| 0.0049 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 71638 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0045 | [Vermivora](https://en.wikipedia.org/wiki/Vermivora) | Warbler | 4123 | [Vermivora cyanoptera](https://en.wikipedia.org/wiki/Vermivora_cyanoptera) | Blue-winged Warbler |






### Top Genera for Wyoming (WY)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.1964 | [Centrocercus](https://en.wikipedia.org/wiki/Centrocercus) | Sage-grouse | 2281 | [Centrocercus urophasianus](https://en.wikipedia.org/wiki/Centrocercus_urophasianus) | Greater Sage-Grouse |
| 0.1183 | [Rhynchophanes](https://en.wikipedia.org/wiki/Rhynchophanes) | Longspur | 2228 | [Rhynchophanes mccownii](https://en.wikipedia.org/wiki/Rhynchophanes_mccownii) | Thick-billed Longspur |
| 0.0773 | [Nucifraga](https://en.wikipedia.org/wiki/Nucifraga) | Nutcracker | 14068 | [Nucifraga columbiana](https://en.wikipedia.org/wiki/Nucifraga_columbiana) | Clark's Nutcracker |
| 0.0623 | [Leucosticte](https://en.wikipedia.org/wiki/Leucosticte) |  | 4885 | [Leucosticte atrata](https://en.wikipedia.org/wiki/Leucosticte_atrata) | Black Rosy-Finch |
| 0.0612 | [Oreoscoptes](https://en.wikipedia.org/wiki/Oreoscoptes) | Sage Thrasher | 5825 | [Oreoscoptes montanus](https://en.wikipedia.org/wiki/Oreoscoptes_montanus) | Sage Thrasher |
| 0.0470 | [Calamospiza](https://en.wikipedia.org/wiki/Calamospiza)† | Lark Bunting | 5086 | [Calamospiza melanocorys](https://en.wikipedia.org/wiki/Calamospiza_melanocorys) | Lark Bunting |
| 0.0457 | [Aquila](https://en.wikipedia.org/wiki/Aquila_(bird)) | True Eagle | 11895 | [Aquila chrysaetos](https://en.wikipedia.org/wiki/Aquila_chrysaetos) | Golden Eagle |
| 0.0404 | [Artemisiospiza](https://en.wikipedia.org/wiki/Artemisiospiza) | Sparrow | 1788 | [Artemisiospiza nevadensis](https://en.wikipedia.org/wiki/Artemisiospiza_nevadensis) | Sagebrush Sparrow |
| 0.0394 | [Cinclus](https://en.wikipedia.org/wiki/Cinclus) |  | 5444 | [Cinclus mexicanus](https://en.wikipedia.org/wiki/Cinclus_mexicanus) | American Dipper |
| 0.0385 | [Dendragapus](https://en.wikipedia.org/wiki/Dendragapus) |  | 2239 | [Dendragapus obscurus](https://en.wikipedia.org/wiki/Dendragapus_obscurus) | Dusky Grouse |










## Scores for Bird Species

### Top Scoring Unique State Birds

| State | Score | Bird | Common Name |
|--:|---|---|---|
| AK | 0.9934 | [Urile urile](https://en.wikipedia.org/wiki/Urile_urile) |  |
| AL | 0.0607 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler |
| AR | 0.0686 | [Antrostomus sp.](https://en.wikipedia.org/wiki/Antrostomus) |  |
| AZ | 0.9691 | [Agapornis personatus](https://en.wikipedia.org/wiki/Agapornis_personatus) |  |
| CA | 0.9851 | [Pica nuttalli](https://en.wikipedia.org/wiki/Pica_nuttalli) | Yellow-billed Magpie |
| CO | 0.7193 | [Leucosticte australis](https://en.wikipedia.org/wiki/Leucosticte_australis) | Brown-capped Rosy-Finch |
| CT | 0.1904 | [Ammospiza sp.](https://en.wikipedia.org/wiki/Ammospiza) |  |
| DC | 0.1111 | [Larus michahellis](https://en.wikipedia.org/wiki/Larus_michahellis) |  |
| DE | 0.1585 | [Chlidonias leucopterus](https://en.wikipedia.org/wiki/Chlidonias_leucopterus) | White-winged Tern |
| FL | 0.9494 | [Amazona amazonica](https://en.wikipedia.org/wiki/Amazona_amazonica) |  |
| GA | 0.2768 | [Sitta pusilla](https://en.wikipedia.org/wiki/Sitta_pusilla) | Brown-headed Nuthatch |
| HI | 0.9980 | [Himatione sanguinea](https://en.wikipedia.org/wiki/Himatione_sanguinea) | Apapane |
| IA | 0.0378 | [Larus crassirostris](https://en.wikipedia.org/wiki/Larus_crassirostris) | Black-tailed Gull |
| ID | 0.9937 | [Loxia sinesciuris](https://en.wikipedia.org/wiki/Loxia_sinesciuris) | Cassia Crossbill |
| IL | 0.2272 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow |
| IN | 0.1326 | [Tringa erythropus](https://en.wikipedia.org/wiki/Tringa_erythropus) |  |
| KS | 0.2114 | [Zonotrichia querula](https://en.wikipedia.org/wiki/Zonotrichia_querula) | Harris's Sparrow |
| KY | 0.0278 | [Geothlypis formosa](https://en.wikipedia.org/wiki/Geothlypis_formosa) | Kentucky Warbler |
| LA | 0.1090 | [Quiscalus sp.](https://en.wikipedia.org/wiki/Quiscalus) |  |
| MA | 0.9674 | [Falco vespertinus](https://en.wikipedia.org/wiki/Falco_vespertinus) |  |
| MD | 0.4003 | [Larus dominicanus](https://en.wikipedia.org/wiki/Larus_dominicanus) |  |
| ME | 0.5279 | [Fratercula arctica](https://en.wikipedia.org/wiki/Fratercula_arctica) |  |
| MI | 0.6334 | [Setophaga kirtlandii](https://en.wikipedia.org/wiki/Setophaga_kirtlandii) | Kirtland's Warbler |
| MN | 0.1151 | [Cygnus buccinator](https://en.wikipedia.org/wiki/Cygnus_buccinator) | Trumpeter Swan |
| MO | 0.5093 | [Passer montanus](https://en.wikipedia.org/wiki/Passer_montanus) | Eurasian Tree Sparrow |
| MS | 0.1435 | [Dendrocygna viduata](https://en.wikipedia.org/wiki/Dendrocygna_viduata) | White-faced Whistling-Duck |
| MT | 0.1975 | [Centronyx bairdii](https://en.wikipedia.org/wiki/Centronyx_bairdii) | Baird's Sparrow |
| NC | 0.9096 | [Hydrobates pelagicus](https://en.wikipedia.org/wiki/Hydrobates_pelagicus) |  |
| ND | 0.1474 | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse |
| NE | 0.1329 | [Lanius sp.](https://en.wikipedia.org/wiki/Lanius) |  |
| NH | 0.2412 | [Egretta gularis](https://en.wikipedia.org/wiki/Egretta_gularis) |  |
| NJ | 0.8225 | [Chlidonias hybrida](https://en.wikipedia.org/wiki/Chlidonias_hybrida) |  |
| NM | 0.4158 | [Pluvialis apricaria](https://en.wikipedia.org/wiki/Pluvialis_apricaria) |  |
| NV | 0.1529 | [Artemisiospiza nevadensis](https://en.wikipedia.org/wiki/Artemisiospiza_nevadensis) | Sagebrush Sparrow |
| NY | 0.9360 | [Chroicocephalus cirrocephalus](https://en.wikipedia.org/wiki/Chroicocephalus_cirrocephalus) |  |
| OH | 0.1042 | [Fringilla montifringilla](https://en.wikipedia.org/wiki/Fringilla_montifringilla) |  |
| OK | 0.4407 | [Tadorna ferruginea](https://en.wikipedia.org/wiki/Tadorna_ferruginea) |  |
| OR | 0.9727 | [Melanitta nigra](https://en.wikipedia.org/wiki/Melanitta_nigra) |  |
| PA | 0.3118 | [Anser serrirostris](https://en.wikipedia.org/wiki/Anser_serrirostris) |  |
| RI | 0.2711 | [Xenus cinereus](https://en.wikipedia.org/wiki/Xenus_cinereus) |  |
| SC | 0.1377 | [Dryobates borealis](https://en.wikipedia.org/wiki/Dryobates_borealis) | Red-cockaded Woodpecker |
| SD | 0.0381 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper |
| TN | 0.6266 | [Grus monacha](https://en.wikipedia.org/wiki/Grus_monacha) |  |
| TX | 0.9189 | [Baeolophus atricristatus](https://en.wikipedia.org/wiki/Baeolophus_atricristatus) | Black-crested Titmouse |
| UT | 0.1869 | [Psiloscops flammeolus](https://en.wikipedia.org/wiki/Psiloscops_flammeolus) | Flammulated Owl |
| VA | 0.5107 | [Anser indicus](https://en.wikipedia.org/wiki/Anser_indicus) |  |
| VT | 0.2150 | [Catharus bicknelli](https://en.wikipedia.org/wiki/Catharus_bicknelli) | Bicknell's Thrush |
| WA | 0.9451 | [Creagrus furcatus](https://en.wikipedia.org/wiki/Creagrus_furcatus) |  |
| WI | 0.1849 | [Tympanuchus cupido](https://en.wikipedia.org/wiki/Tympanuchus_cupido) | Greater Prairie-Chicken |
| WV | 0.0249 | [Setophaga cerulea](https://en.wikipedia.org/wiki/Setophaga_cerulea) | Cerulean Warbler |
| WY | 0.1964 | [Centrocercus urophasianus](https://en.wikipedia.org/wiki/Centrocercus_urophasianus) | Greater Sage-Grouse |





### Top Species for Alaska (AK)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.9934 | [Urile urile](https://en.wikipedia.org/wiki/Urile_urile) |  | 12099 |
| 0.9934 | [Onychoprion aleuticus](https://en.wikipedia.org/wiki/Onychoprion_aleuticus) | Aleutian Tern | 7065 |
| 0.9934 | [Aethia pygmaea](https://en.wikipedia.org/wiki/Aethia_pygmaea) |  | 669 |
| 0.9934 | [Muscicapa griseisticta](https://en.wikipedia.org/wiki/Muscicapa_griseisticta) |  | 281 |
| 0.9934 | [Phylloscopus collybita](https://en.wikipedia.org/wiki/Phylloscopus_collybita) | Common Chiffchaff | 205 |
| 0.9934 | [Anthus gustavi](https://en.wikipedia.org/wiki/Anthus_gustavi) |  | 140 |
| 0.9934 | [Cuculus optatus](https://en.wikipedia.org/wiki/Cuculus_optatus) | Oriental Cuckoo | 133 |
| 0.9934 | [Phylloscopus trochilus](https://en.wikipedia.org/wiki/Phylloscopus_trochilus) | Willow Warbler | 109 |
| 0.9932 | [Somateria fischeri](https://en.wikipedia.org/wiki/Somateria_fischeri) | Spectacled Eider | 5432 |
| 0.9932 | [Aethia pusilla](https://en.wikipedia.org/wiki/Aethia_pusilla) |  | 9479 |






### Top Species for Alabama (AL)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0607 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler | 2905 |
| 0.0606 | [Grus americana](https://en.wikipedia.org/wiki/Grus_americana) | Whooping Crane | 1504 |
| 0.0477 | [Sitta pusilla](https://en.wikipedia.org/wiki/Sitta_pusilla) | Brown-headed Nuthatch | 32313 |
| 0.0419 | [Lonchura punctulata](https://en.wikipedia.org/wiki/Lonchura_punctulata) | Scaly-breasted Munia | 1693 |
| 0.0418 | [Peucaea aestivalis](https://en.wikipedia.org/wiki/Peucaea_aestivalis) | Bachman's Sparrow | 1689 |
| 0.0327 | [Charadrius nivosus](https://en.wikipedia.org/wiki/Charadrius_nivosus) | Snowy Plover | 3533 |
| 0.0311 | [Caprimulgidae sp.](https://en.wikipedia.org/wiki/Caprimulgidae) |  | 31 |
| 0.0295 | [Geothlypis formosa](https://en.wikipedia.org/wiki/Geothlypis_formosa) | Kentucky Warbler | 6284 |
| 0.0274 | [Piranga rubra](https://en.wikipedia.org/wiki/Piranga_rubra) | Summer Tanager | 28464 |
| 0.0267 | [Thalasseus sandvicensis](https://en.wikipedia.org/wiki/Thalasseus_sandvicensis) | Sandwich Tern | 6175 |






### Top Species for Arkansas (AR)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0686 | [Antrostomus sp.](https://en.wikipedia.org/wiki/Antrostomus) |  | 8 |
| 0.0462 | [Calcarius pictus](https://en.wikipedia.org/wiki/Calcarius_pictus) | Smith's Longspur | 575 |
| 0.0372 | [Tyrannus forficatus](https://en.wikipedia.org/wiki/Tyrannus_forficatus)† | Scissor-tailed Flycatcher | 19125 |
| 0.0365 | [Geothlypis formosa](https://en.wikipedia.org/wiki/Geothlypis_formosa) | Kentucky Warbler | 7297 |
| 0.0324 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite | 10710 |
| 0.0260 | [Piranga rubra](https://en.wikipedia.org/wiki/Piranga_rubra) | Summer Tanager | 26191 |
| 0.0236 | [Dryobates borealis](https://en.wikipedia.org/wiki/Dryobates_borealis) | Red-cockaded Woodpecker | 970 |
| 0.0233 | [Antrostomus carolinensis](https://en.wikipedia.org/wiki/Antrostomus_carolinensis) | Chuck-will's-widow | 2627 |
| 0.0198 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel | 10491 |
| 0.0197 | [Ammospiza leconteii](https://en.wikipedia.org/wiki/Ammospiza_leconteii) | LeConte's Sparrow | 1422 |






### Top Species for Arizona (AZ)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.9691 | [Agapornis personatus](https://en.wikipedia.org/wiki/Agapornis_personatus) |  | 186 |
| 0.9357 | [Peucaea carpalis](https://en.wikipedia.org/wiki/Peucaea_carpalis) | Rufous-winged Sparrow | 73068 |
| 0.9136 | [Baeolophus wollweberi](https://en.wikipedia.org/wiki/Baeolophus_wollweberi) | Bridled Titmouse | 147289 |
| 0.9039 | [Agapornis roseicollis](https://en.wikipedia.org/wiki/Agapornis_roseicollis) |  | 23043 |
| 0.8973 | [Dryobates arizonae](https://en.wikipedia.org/wiki/Dryobates_arizonae) | Arizona Woodpecker | 47770 |
| 0.8901 | [Melanerpes uropygialis](https://en.wikipedia.org/wiki/Melanerpes_uropygialis) | Gila Woodpecker | 443649 |
| 0.8839 | [Melozone aberti](https://en.wikipedia.org/wiki/Melozone_aberti) | Abert's Towhee | 262829 |
| 0.8669 | [Amphispizopsis quinquestriata](https://en.wikipedia.org/wiki/Amphispizopsis_quinquestriata) | Five-striped Sparrow | 5685 |
| 0.8619 | [Megascops trichopsis](https://en.wikipedia.org/wiki/Megascops_trichopsis) | Whiskered Screech-Owl | 10842 |
| 0.8543 | [Aphelocoma wollweberi](https://en.wikipedia.org/wiki/Aphelocoma_wollweberi) | Mexican Jay | 130540 |






### Top Species for California (CA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.9851 | [Pica nuttalli](https://en.wikipedia.org/wiki/Pica_nuttalli) | Yellow-billed Magpie | 17869 |
| 0.9851 | [Aphelocoma insularis](https://en.wikipedia.org/wiki/Aphelocoma_insularis) | Island Scrub-Jay | 924 |
| 0.9625 | [Dryobates nuttallii](https://en.wikipedia.org/wiki/Dryobates_nuttallii) | Nuttall's Woodpecker | 74045 |
| 0.9206 | [Hydrobates homochroa](https://en.wikipedia.org/wiki/Hydrobates_homochroa) |  | 2162 |
| 0.9067 | [Toxostoma redivivum](https://en.wikipedia.org/wiki/Toxostoma_redivivum) | California Thrasher | 30314 |
| 0.8754 | [Melozone crissalis](https://en.wikipedia.org/wiki/Melozone_crissalis) | California Towhee | 124793 |
| 0.8726 | [Selasphorus sasin](https://en.wikipedia.org/wiki/Selasphorus_sasin) | Allen's Hummingbird | 37169 |
| 0.8058 | [Baeolophus inornatus](https://en.wikipedia.org/wiki/Baeolophus_inornatus) | Oak Titmouse | 64598 |
| 0.7647 | [Hydrobates socorroensis](https://en.wikipedia.org/wiki/Hydrobates_socorroensis) |  | 92 |
| 0.7206 | [Artemisiospiza belli](https://en.wikipedia.org/wiki/Artemisiospiza_belli) | Bell's Sparrow | 6672 |






### Top Species for Colorado (CO)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.7193 | [Leucosticte australis](https://en.wikipedia.org/wiki/Leucosticte_australis) | Brown-capped Rosy-Finch | 9642 |
| 0.6694 | [Sayornis sp.](https://en.wikipedia.org/wiki/Sayornis) |  | 177 |
| 0.6244 | [Streptopelia sp.](https://en.wikipedia.org/wiki/Streptopelia) |  | 272 |
| 0.4865 | [Lagopus leucura](https://en.wikipedia.org/wiki/Lagopus_leucura) | White-tailed Ptarmigan | 3927 |
| 0.4351 | [Selasphorus platycercus](https://en.wikipedia.org/wiki/Selasphorus_platycercus) | Broad-tailed Hummingbird | 174912 |
| 0.4322 | [Leucosticte sp.](https://en.wikipedia.org/wiki/Leucosticte) |  | 1152 |
| 0.3556 | [Streptopelia roseogrisea](https://en.wikipedia.org/wiki/Streptopelia_roseogrisea) | African Collared-Dove (a.k.a. Ringed Turtle-Dove) | 205 |
| 0.3094 | [Charadrius montanus](https://en.wikipedia.org/wiki/Charadrius_montanus) | Mountain Plover | 4008 |
| 0.3073 | [Empidonax occidentalis](https://en.wikipedia.org/wiki/Empidonax_occidentalis) | Cordilleran Flycatcher | 38951 |
| 0.2937 | [Spizella sp.](https://en.wikipedia.org/wiki/Spizella) |  | 4251 |






### Top Species for Connecticut (CT)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1904 | [Ammospiza sp.](https://en.wikipedia.org/wiki/Ammospiza) |  | 153 |
| 0.0910 | [Anser brachyrhynchus](https://en.wikipedia.org/wiki/Anser_brachyrhynchus) |  | 948 |
| 0.0818 | [Ammospiza caudacuta](https://en.wikipedia.org/wiki/Ammospiza_caudacuta) | Saltmarsh Sparrow | 5067 |
| 0.0811 | [Anser anser](https://en.wikipedia.org/wiki/Anser_anser) |  | 34 |
| 0.0782 | [Larus canus](https://en.wikipedia.org/wiki/Larus_canus) | Mew Gull | 240 |
| 0.0726 | [Calidris sp.](https://en.wikipedia.org/wiki/Calidris) | unid. small ''peep'' sandpiper | 627 |
| 0.0716 | [Branta bernicla](https://en.wikipedia.org/wiki/Branta_bernicla) | Brant | 34897 |
| 0.0668 | [Threskiornithidae sp. (ibis sp.)](https://en.wikipedia.org/wiki/Threskiornithidae) |  | 48 |
| 0.0639 | [Branta leucopsis](https://en.wikipedia.org/wiki/Branta_leucopsis) |  | 656 |
| 0.0527 | [Falco sp. (small falcon sp.)](https://en.wikipedia.org/wiki/Falcon) |  | 413 |






### Top Species for District of Columbia (DC)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1111 | [Larus michahellis](https://en.wikipedia.org/wiki/Larus_michahellis) |  | 33 |
| 0.0615 | [Branta leucopsis](https://en.wikipedia.org/wiki/Branta_leucopsis) |  | 536 |
| 0.0308 | [Corvus sp. (crow sp.)](https://en.wikipedia.org/wiki/Corvus) |  | 10911 |
| 0.0163 | [Melopsittacus undulatus (Domestic type)](https://en.wikipedia.org/wiki/Melopsittacus_undulatus_(Domestic_type)) |  | 15 |
| 0.0112 | [Corvus ossifragus](https://en.wikipedia.org/wiki/Corvus_ossifragus) | Fish Crow | 26969 |
| 0.0105 | [Melopsittacus undulatus](https://en.wikipedia.org/wiki/Melopsittacus_undulatus) | Budgerigar | 10 |
| 0.0076 | [Chaetura pelagica](https://en.wikipedia.org/wiki/Chaetura_pelagica) | Chimney Swift | 24475 |
| 0.0069 | [Antrostomus sp.](https://en.wikipedia.org/wiki/Antrostomus) |  | 1 |
| 0.0066 | [Empidonax virescens](https://en.wikipedia.org/wiki/Empidonax_virescens) | Acadian Flycatcher | 4171 |
| 0.0056 | [Fregata sp.](https://en.wikipedia.org/wiki/Fregata) |  | 1 |






### Top Species for Delaware (DE)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1686 | [Egretta garzetta](https://en.wikipedia.org/wiki/Egretta_garzetta)* | Little Egret | 503 |
| 0.1585 | [Chlidonias leucopterus](https://en.wikipedia.org/wiki/Chlidonias_leucopterus) | White-winged Tern | 186 |
| 0.1426 | [Chlidonias hybrida](https://en.wikipedia.org/wiki/Chlidonias_hybrida) |  | 95 |
| 0.0975 | [Ammospiza maritima](https://en.wikipedia.org/wiki/Ammospiza_maritima) | Seaside Sparrow | 9067 |
| 0.0533 | [Calidris ferruginea](https://en.wikipedia.org/wiki/Calidris_ferruginea) |  | 265 |
| 0.0483 | [Calidris pugnax](https://en.wikipedia.org/wiki/Calidris_pugnax) | Ruff | 841 |
| 0.0462 | [Threskiornithidae sp. (ibis sp.)](https://en.wikipedia.org/wiki/Threskiornithidae) |  | 31 |
| 0.0461 | [Rallus crepitans](https://en.wikipedia.org/wiki/Rallus_crepitans) | Clapper Rail | 12429 |
| 0.0351 | [Limosa limosa](https://en.wikipedia.org/wiki/Limosa_limosa) |  | 61 |
| 0.0339 | [Limnodromus griseus](https://en.wikipedia.org/wiki/Limnodromus_griseus) | Short-billed Dowitcher | 19031 |






### Top Species for Florida (FL)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.9494 | [Amazona amazonica](https://en.wikipedia.org/wiki/Amazona_amazonica) |  | 2592 |
| 0.9494 | [Myiarchus sagrae](https://en.wikipedia.org/wiki/Myiarchus_sagrae) |  | 1277 |
| 0.9494 | [Melanospiza bicolor](https://en.wikipedia.org/wiki/Melanospiza_bicolor) |  | 1164 |
| 0.9494 | [Mimus gundlachii](https://en.wikipedia.org/wiki/Mimus_gundlachii) | Bahama Mockingbird | 892 |
| 0.9494 | [Psittacara leucophthalmus](https://en.wikipedia.org/wiki/Psittacara_leucophthalmus) |  | 852 |
| 0.9494 | [Vireo crassirostris](https://en.wikipedia.org/wiki/Vireo_crassirostris) |  | 821 |
| 0.9494 | [Turdus plumbeus](https://en.wikipedia.org/wiki/Turdus_plumbeus) |  | 526 |
| 0.9494 | [Contopus caribaeus](https://en.wikipedia.org/wiki/Contopus_caribaeus) |  | 522 |
| 0.9494 | [Geotrygon chrysia](https://en.wikipedia.org/wiki/Geotrygon_chrysia) |  | 402 |
| 0.9494 | [Tachornis phoenicobia](https://en.wikipedia.org/wiki/Tachornis_phoenicobia) |  | 290 |






### Top Species for Georgia (GA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.2768 | [Sitta pusilla](https://en.wikipedia.org/wiki/Sitta_pusilla) | Brown-headed Nuthatch | 176715 |
| 0.0912 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler | 4722 |
| 0.0902 | [Peucaea aestivalis](https://en.wikipedia.org/wiki/Peucaea_aestivalis) | Bachman's Sparrow | 3798 |
| 0.0849 | [Setophaga pinus](https://en.wikipedia.org/wiki/Setophaga_pinus) | Pine Warbler | 176004 |
| 0.0648 | [Vanellus vanellus](https://en.wikipedia.org/wiki/Vanellus_vanellus) | Northern Lapwing | 167 |
| 0.0637 | [Dryobates borealis](https://en.wikipedia.org/wiki/Dryobates_borealis) | Red-cockaded Woodpecker | 2761 |
| 0.0628 | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum)‡ | Brown Thrasher | 179633 |
| 0.0625 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 264079 |
| 0.0586 | [Antrostomus carolinensis](https://en.wikipedia.org/wiki/Antrostomus_carolinensis) | Chuck-will's-widow | 7091 |
| 0.0558 | [Cairina moschata (Domestic type)](https://en.wikipedia.org/wiki/Cairina_moschata_(Domestic_type)) |  | 6376 |






### Top Species for Hawaii (HI)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.9981 | [Zosterops japonicus](https://en.wikipedia.org/wiki/Zosterops_japonicus)* |  | 82840 |
| 0.9981 | [Geopelia striata](https://en.wikipedia.org/wiki/Geopelia_striata)* |  | 78346 |
| 0.9980 | [Himatione sanguinea](https://en.wikipedia.org/wiki/Himatione_sanguinea) | Apapane | 35689 |
| 0.9980 | [Chlorodrepanis virens](https://en.wikipedia.org/wiki/Chlorodrepanis_virens) |  | 29234 |
| 0.9980 | [Fulica alai](https://en.wikipedia.org/wiki/Fulica_alai) |  | 22293 |
| 0.9980 | [Branta sandvicensis](https://en.wikipedia.org/wiki/Branta_sandvicensis)‡ |  | 18412 |
| 0.9980 | [Copsychus malabaricus](https://en.wikipedia.org/wiki/Copsychus_malabaricus) |  | 18329 |
| 0.9980 | [Leiothrix lutea](https://en.wikipedia.org/wiki/Leiothrix_lutea) |  | 17965 |
| 0.9980 | [Drepanis coccinea](https://en.wikipedia.org/wiki/Drepanis_coccinea) |  | 17194 |
| 0.9980 | [Paroaria capitata](https://en.wikipedia.org/wiki/Paroaria_capitata) |  | 17012 |






### Top Species for Iowa (IA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1470 | [Passer montanus](https://en.wikipedia.org/wiki/Passer_montanus) | Eurasian Tree Sparrow | 7675 |
| 0.0378 | [Larus crassirostris](https://en.wikipedia.org/wiki/Larus_crassirostris) | Black-tailed Gull | 47 |
| 0.0325 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel | 15850 |
| 0.0291 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus)†* | Ring-necked Pheasant | 21293 |
| 0.0266 | [Calcarius pictus](https://en.wikipedia.org/wiki/Calcarius_pictus) | Smith's Longspur | 353 |
| 0.0245 | [Rhodostethia rosea](https://en.wikipedia.org/wiki/Rhodostethia_rosea) | Ross's Gull | 76 |
| 0.0219 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow | 1960 |
| 0.0218 | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker | 24590 |
| 0.0210 | [Zonotrichia querula](https://en.wikipedia.org/wiki/Zonotrichia_querula) | Harris's Sparrow | 5050 |
| 0.0196 | [Cistothorus stellaris](https://en.wikipedia.org/wiki/Cistothorus_stellaris) | Sedge Wren | 5205 |






### Top Species for Idaho (ID)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.9937 | [Loxia sinesciuris](https://en.wikipedia.org/wiki/Loxia_sinesciuris) | Cassia Crossbill | 2084 |
| 0.2104 | [Tarsiger cyanurus](https://en.wikipedia.org/wiki/Tarsiger_cyanurus) |  | 156 |
| 0.1077 | [Centrocercus urophasianus](https://en.wikipedia.org/wiki/Centrocercus_urophasianus) | Greater Sage-Grouse | 1305 |
| 0.1072 | [Callipepla californica](https://en.wikipedia.org/wiki/Callipepla_californica)† | California Quail | 53065 |
| 0.0973 | [Alectoris chukar](https://en.wikipedia.org/wiki/Alectoris_chukar)* | Chukar | 3634 |
| 0.0891 | [Selasphorus calliope](https://en.wikipedia.org/wiki/Selasphorus_calliope) | Calliope Hummingbird | 10890 |
| 0.0778 | [Haemorhous cassinii](https://en.wikipedia.org/wiki/Haemorhous_cassinii) | Cassin's Finch | 20202 |
| 0.0769 | [Lanius sp.](https://en.wikipedia.org/wiki/Lanius) |  | 34 |
| 0.0726 | [Dendragapus obscurus](https://en.wikipedia.org/wiki/Dendragapus_obscurus) | Dusky Grouse | 1794 |
| 0.0693 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie | 118106 |






### Top Species for Illinois (IL)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.2943 | [Carduelis carduelis](https://en.wikipedia.org/wiki/Carduelis_carduelis)* | European Goldfinch | 1798 |
| 0.2550 | [Passer montanus](https://en.wikipedia.org/wiki/Passer_montanus) | Eurasian Tree Sparrow | 14313 |
| 0.2272 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow | 18756 |
| 0.1484 | [Streptopelia roseogrisea](https://en.wikipedia.org/wiki/Streptopelia_roseogrisea) | African Collared-Dove (a.k.a. Ringed Turtle-Dove) | 95 |
| 0.1000 | [Oporornis agilis](https://en.wikipedia.org/wiki/Oporornis_agilis) | Connecticut Warbler | 4029 |
| 0.0818 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel | 46626 |
| 0.0794 | [Catharus minimus](https://en.wikipedia.org/wiki/Catharus_minimus) | Gray-cheeked Thrush | 19054 |
| 0.0790 | [Vermivora chrysoptera](https://en.wikipedia.org/wiki/Vermivora_chrysoptera) | Golden-winged Warbler | 13460 |
| 0.0708 | [Larus crassirostris](https://en.wikipedia.org/wiki/Larus_crassirostris) | Black-tailed Gull | 109 |
| 0.0678 | [Myiopsitta monachus](https://en.wikipedia.org/wiki/Myiopsitta_monachus)* | Monk Parakeet | 11545 |






### Top Species for Indiana (IN)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.3219 | [Grus monacha](https://en.wikipedia.org/wiki/Grus_monacha) |  | 81 |
| 0.1326 | [Tringa erythropus](https://en.wikipedia.org/wiki/Tringa_erythropus) |  | 145 |
| 0.0893 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow | 7607 |
| 0.0819 | [Grus grus](https://en.wikipedia.org/wiki/Grus_grus) |  | 165 |
| 0.0700 | [Calcarius pictus](https://en.wikipedia.org/wiki/Calcarius_pictus) | Smith's Longspur | 949 |
| 0.0676 | [Limosa limosa](https://en.wikipedia.org/wiki/Limosa_limosa) |  | 121 |
| 0.0431 | [Geothlypis formosa](https://en.wikipedia.org/wiki/Geothlypis_formosa) | Kentucky Warbler | 10117 |
| 0.0399 | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker | 50156 |
| 0.0390 | [Setophaga cerulea](https://en.wikipedia.org/wiki/Setophaga_cerulea) | Cerulean Warbler | 6585 |
| 0.0300 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler | 15774 |






### Top Species for Kansas (KS)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.2114 | [Zonotrichia querula](https://en.wikipedia.org/wiki/Zonotrichia_querula) | Harris's Sparrow | 43167 |
| 0.1519 | [Limosa sp.](https://en.wikipedia.org/wiki/Limosa) |  | 64 |
| 0.1426 | [Tympanuchus cupido](https://en.wikipedia.org/wiki/Tympanuchus_cupido) | Greater Prairie-Chicken | 2429 |
| 0.0897 | [Calidris sp.](https://en.wikipedia.org/wiki/Calidris) | unid. small ''peep'' sandpiper | 710 |
| 0.0768 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel | 36284 |
| 0.0677 | [Leucophaeus pipixcan](https://en.wikipedia.org/wiki/Leucophaeus_pipixcan) | Franklin's Gull | 26149 |
| 0.0592 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite | 22554 |
| 0.0562 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper | 8401 |
| 0.0507 | [Calcarius pictus](https://en.wikipedia.org/wiki/Calcarius_pictus) | Smith's Longspur | 667 |
| 0.0506 | [Charadrius nivosus](https://en.wikipedia.org/wiki/Charadrius_nivosus) | Snowy Plover | 5380 |






### Top Species for Kentucky (KY)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0278 | [Geothlypis formosa](https://en.wikipedia.org/wiki/Geothlypis_formosa) | Kentucky Warbler | 5928 |
| 0.0242 | [Brachyramphus perdix](https://en.wikipedia.org/wiki/Brachyramphus_perdix) |  | 10 |
| 0.0192 | [Anser sp. (Domestic type)](https://en.wikipedia.org/wiki/Anser) |  | 1296 |
| 0.0185 | [Ectopistes migratorius](https://en.wikipedia.org/wiki/Ectopistes_migratorius) |  | 5 |
| 0.0170 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 113140 |
| 0.0169 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler | 8107 |
| 0.0163 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler | 959 |
| 0.0158 | [Setophaga dominica](https://en.wikipedia.org/wiki/Setophaga_dominica) | Yellow-throated Warbler | 11719 |
| 0.0157 | [Piranga rubra](https://en.wikipedia.org/wiki/Piranga_rubra) | Summer Tanager | 18248 |
| 0.0152 | [Piranga sp.](https://en.wikipedia.org/wiki/Piranga) |  | 69 |






### Top Species for Louisiana (LA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1090 | [Quiscalus sp.](https://en.wikipedia.org/wiki/Quiscalus) |  | 1442 |
| 0.1051 | [Rallus elegans](https://en.wikipedia.org/wiki/Rallus_elegans) | King Rail | 6306 |
| 0.0936 | [Ammospiza sp.](https://en.wikipedia.org/wiki/Ammospiza) |  | 77 |
| 0.0846 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite | 27044 |
| 0.0843 | [Dryobates borealis](https://en.wikipedia.org/wiki/Dryobates_borealis) | Red-cockaded Woodpecker | 3190 |
| 0.0824 | [Antrostomus sp.](https://en.wikipedia.org/wiki/Antrostomus) |  | 10 |
| 0.0794 | [Onychoprion anaethetus](https://en.wikipedia.org/wiki/Onychoprion_anaethetus) |  | 677 |
| 0.0779 | [Cairina moschata (Domestic type)](https://en.wikipedia.org/wiki/Cairina_moschata_(Domestic_type)) |  | 7608 |
| 0.0723 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler | 3553 |
| 0.0665 | [Coturnicops noveboracensis](https://en.wikipedia.org/wiki/Coturnicops_noveboracensis) | Yellow Rail | 942 |






### Top Species for Massachusetts (MA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.9674 | [Falco vespertinus](https://en.wikipedia.org/wiki/Falco_vespertinus) |  | 139 |
| 0.7511 | [Fringilla coelebs](https://en.wikipedia.org/wiki/Fringilla_coelebs) | Common Chaffinch | 116 |
| 0.5510 | [Pelagodroma marina](https://en.wikipedia.org/wiki/Pelagodroma_marina) |  | 1036 |
| 0.4568 | [Meleagris gallopavo (Domestic type)](https://en.wikipedia.org/wiki/Meleagris_gallopavo_(Domestic_type)) |  | 185 |
| 0.4424 | [Pterodroma cahow](https://en.wikipedia.org/wiki/Pterodroma_cahow) |  | 95 |
| 0.4409 | [Puffinus puffinus](https://en.wikipedia.org/wiki/Puffinus_puffinus) | Manx Shearwater | 9833 |
| 0.3483 | [Puffinus sp. (black-and-white shearwater sp.)](https://en.wikipedia.org/wiki/Puffinus) |  | 499 |
| 0.3438 | [Ardenna gravis](https://en.wikipedia.org/wiki/Ardenna_gravis) |  | 19121 |
| 0.3287 | [Sterna dougallii](https://en.wikipedia.org/wiki/Sterna_dougallii) | Roseate Tern | 14117 |
| 0.3149 | [Calonectris diomedea](https://en.wikipedia.org/wiki/Calonectris_diomedea) | Cory's Shearwater | 16342 |






### Top Species for Maryland (MD)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.4003 | [Larus dominicanus](https://en.wikipedia.org/wiki/Larus_dominicanus) |  | 333 |
| 0.1939 | [Anser cygnoides](https://en.wikipedia.org/wiki/Anser_cygnoides) |  | 30 |
| 0.1331 | [Corvus sp. (crow sp.)](https://en.wikipedia.org/wiki/Corvus) |  | 53171 |
| 0.1035 | [Empidonax virescens](https://en.wikipedia.org/wiki/Empidonax_virescens) | Acadian Flycatcher | 61388 |
| 0.0812 | [Hydrobates castro](https://en.wikipedia.org/wiki/Hydrobates_castro) |  | 1059 |
| 0.0734 | [Corvus ossifragus](https://en.wikipedia.org/wiki/Corvus_ossifragus) | Fish Crow | 203375 |
| 0.0657 | [Puffinus lherminieri](https://en.wikipedia.org/wiki/Puffinus_lherminieri) |  | 1684 |
| 0.0636 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 455890 |
| 0.0593 | [Cygnus columbianus](https://en.wikipedia.org/wiki/Cygnus_columbianus) | Tundra Swan | 36221 |
| 0.0541 | [Parkesia motacilla](https://en.wikipedia.org/wiki/Parkesia_motacilla) | Louisiana Waterthrush | 29442 |






### Top Species for Maine (ME)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.5279 | [Fratercula arctica](https://en.wikipedia.org/wiki/Fratercula_arctica) |  | 17498 |
| 0.4030 | [Turdus iliacus](https://en.wikipedia.org/wiki/Turdus_iliacus) |  | 600 |
| 0.3475 | [Cepphus grylle](https://en.wikipedia.org/wiki/Cepphus_grylle) | Black Guillemot | 58921 |
| 0.3373 | [Egretta garzetta](https://en.wikipedia.org/wiki/Egretta_garzetta)* | Little Egret | 1008 |
| 0.3335 | [Stercorarius skua](https://en.wikipedia.org/wiki/Stercorarius_skua) |  | 525 |
| 0.3307 | [Phaethon aethereus](https://en.wikipedia.org/wiki/Phaethon_aethereus) |  | 1364 |
| 0.2529 | [Sterna dougallii](https://en.wikipedia.org/wiki/Sterna_dougallii) | Roseate Tern | 10380 |
| 0.2129 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider | 126024 |
| 0.2098 | [Hydrobates leucorhous](https://en.wikipedia.org/wiki/Hydrobates_leucorhous) | Leach's Storm-Petrel | 7558 |
| 0.2004 | [Stercorarius sp. (skua sp.)](https://en.wikipedia.org/wiki/Stercorarius) |  | 145 |






### Top Species for Michigan (MI)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.6334 | [Setophaga kirtlandii](https://en.wikipedia.org/wiki/Setophaga_kirtlandii) | Kirtland's Warbler | 7644 |
| 0.4965 | [Tringa erythropus](https://en.wikipedia.org/wiki/Tringa_erythropus) |  | 521 |
| 0.1606 | [Cygnus sp.](https://en.wikipedia.org/wiki/Swan) |  | 3920 |
| 0.1267 | [Aythya sp.](https://en.wikipedia.org/wiki/Aythya) |  | 2875 |
| 0.1214 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan | 165631 |
| 0.0987 | [Larus sp. (white-winged gull sp.)](https://en.wikipedia.org/wiki/Larus) |  | 232 |
| 0.0985 | [Antigone canadensis](https://en.wikipedia.org/wiki/Antigone_canadensis) | Sandhill Crane | 176499 |
| 0.0834 | [Calidris sp.](https://en.wikipedia.org/wiki/Calidris) | unid. small ''peep'' sandpiper | 826 |
| 0.0760 | [Anas sp.](https://en.wikipedia.org/wiki/Anas) |  | 17 |
| 0.0608 | [Cygnus buccinator](https://en.wikipedia.org/wiki/Cygnus_buccinator) | Trumpeter Swan | 48981 |






### Top Species for Minnesota (MN)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1151 | [Cygnus buccinator](https://en.wikipedia.org/wiki/Cygnus_buccinator) | Trumpeter Swan | 69864 |
| 0.1065 | [Pagophila eburnea](https://en.wikipedia.org/wiki/Pagophila_eburnea) |  | 459 |
| 0.0987 | [Aegolius funereus](https://en.wikipedia.org/wiki/Aegolius_funereus) | Boreal Owl | 1218 |
| 0.0883 | [Cistothorus stellaris](https://en.wikipedia.org/wiki/Cistothorus_stellaris) | Sedge Wren | 22221 |
| 0.0879 | [Vermivora chrysoptera](https://en.wikipedia.org/wiki/Vermivora_chrysoptera) | Golden-winged Warbler | 13045 |
| 0.0877 | [Tympanuchus cupido](https://en.wikipedia.org/wiki/Tympanuchus_cupido) | Greater Prairie-Chicken | 1663 |
| 0.0836 | [Picoides arcticus](https://en.wikipedia.org/wiki/Picoides_arcticus) | Black-backed Woodpecker | 5030 |
| 0.0758 | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse | 3799 |
| 0.0753 | [Spizella pallida](https://en.wikipedia.org/wiki/Spizella_pallida) | Clay-colored Sparrow | 34266 |
| 0.0720 | [Fringillidae sp.](https://en.wikipedia.org/wiki/Fringillidae) |  | 2025 |






### Top Species for Missouri (MO)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.5093 | [Passer montanus](https://en.wikipedia.org/wiki/Passer_montanus) | Eurasian Tree Sparrow | 26402 |
| 0.1044 | [Mergellus albellus](https://en.wikipedia.org/wiki/Mergellus_albellus) |  | 109 |
| 0.0976 | [Antrostomus sp.](https://en.wikipedia.org/wiki/Antrostomus) |  | 12 |
| 0.0934 | [Geothlypis formosa](https://en.wikipedia.org/wiki/Geothlypis_formosa) | Kentucky Warbler | 18709 |
| 0.0679 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel | 34191 |
| 0.0508 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite | 21081 |
| 0.0481 | [Poecile sp.](https://en.wikipedia.org/wiki/Poecile)† | unid. western chickadee species | 1731 |
| 0.0476 | [Parkesia motacilla](https://en.wikipedia.org/wiki/Parkesia_motacilla) | Louisiana Waterthrush | 21483 |
| 0.0457 | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker | 53929 |
| 0.0431 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow | 4090 |






### Top Species for Mississippi (MS)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1435 | [Dendrocygna viduata](https://en.wikipedia.org/wiki/Dendrocygna_viduata) | White-faced Whistling-Duck | 30 |
| 0.0406 | [Rallus sp. (large Rallus sp.)](https://en.wikipedia.org/wiki/Rallus) |  | 8 |
| 0.0354 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler | 1697 |
| 0.0306 | [Gelochelidon nilotica](https://en.wikipedia.org/wiki/Gelochelidon_nilotica) | Gull-billed Tern | 3142 |
| 0.0278 | [Rallus crepitans](https://en.wikipedia.org/wiki/Rallus_crepitans) | Clapper Rail | 7469 |
| 0.0234 | [Rynchops niger](https://en.wikipedia.org/wiki/Rynchops_niger) | Black Skimmer | 8333 |
| 0.0227 | [Dryobates borealis](https://en.wikipedia.org/wiki/Dryobates_borealis) | Red-cockaded Woodpecker | 897 |
| 0.0217 | [Ammospiza maritima](https://en.wikipedia.org/wiki/Ammospiza_maritima) | Seaside Sparrow | 2211 |
| 0.0216 | [Anser anser](https://en.wikipedia.org/wiki/Anser_anser) |  | 9 |
| 0.0206 | [Cairina moschata (Domestic type)](https://en.wikipedia.org/wiki/Cairina_moschata_(Domestic_type)) |  | 2111 |






### Top Species for Montana (MT)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1975 | [Centronyx bairdii](https://en.wikipedia.org/wiki/Centronyx_bairdii) | Baird's Sparrow | 2510 |
| 0.1832 | [Rhynchophanes mccownii](https://en.wikipedia.org/wiki/Rhynchophanes_mccownii) | Thick-billed Longspur | 3501 |
| 0.1694 | [Haemorhous sp.](https://en.wikipedia.org/wiki/Haemorhous) |  | 124 |
| 0.1574 | [Calcarius ornatus](https://en.wikipedia.org/wiki/Calcarius_ornatus) | Chestnut-collared Longspur | 6066 |
| 0.1324 | [Sibirionetta formosa](https://en.wikipedia.org/wiki/Sibirionetta_formosa) |  | 43 |
| 0.1315 | [Nucifraga columbiana](https://en.wikipedia.org/wiki/Nucifraga_columbiana) | Clark's Nutcracker | 24361 |
| 0.1289 | [Perdix perdix](https://en.wikipedia.org/wiki/Perdix_perdix)* | Gray Partridge | 7149 |
| 0.1212 | [Dendragapus obscurus](https://en.wikipedia.org/wiki/Dendragapus_obscurus) | Dusky Grouse | 2920 |
| 0.1159 | [Selasphorus calliope](https://en.wikipedia.org/wiki/Selasphorus_calliope) | Calliope Hummingbird | 14066 |
| 0.1130 | [Centrocercus urophasianus](https://en.wikipedia.org/wiki/Centrocercus_urophasianus) | Greater Sage-Grouse | 1377 |






### Top Species for North Carolina (NC)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.9096 | [Hydrobates pelagicus](https://en.wikipedia.org/wiki/Hydrobates_pelagicus) |  | 107 |
| 0.8493 | [Pterodroma feae](https://en.wikipedia.org/wiki/Pterodroma_feae) |  | 496 |
| 0.8274 | [Pterodroma arminjoniana](https://en.wikipedia.org/wiki/Pterodroma_arminjoniana) |  | 682 |
| 0.5994 | [Pterodroma hasitata](https://en.wikipedia.org/wiki/Pterodroma_hasitata) |  | 6000 |
| 0.4791 | [Pterodroma cahow](https://en.wikipedia.org/wiki/Pterodroma_cahow) |  | 100 |
| 0.3751 | [Puffinus lherminieri](https://en.wikipedia.org/wiki/Puffinus_lherminieri) |  | 7090 |
| 0.3450 | [Hydrobates castro](https://en.wikipedia.org/wiki/Hydrobates_castro) |  | 3538 |
| 0.2608 | [Puffinus sp. (black-and-white shearwater sp.)](https://en.wikipedia.org/wiki/Puffinus) |  | 369 |
| 0.2549 | [Onychoprion anaethetus](https://en.wikipedia.org/wiki/Onychoprion_anaethetus) |  | 2104 |
| 0.2432 | [Calonectris diomedea](https://en.wikipedia.org/wiki/Calonectris_diomedea) | Cory's Shearwater | 12415 |






### Top Species for North Dakota (ND)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1591 | [Centronyx bairdii](https://en.wikipedia.org/wiki/Centronyx_bairdii) | Baird's Sparrow | 1986 |
| 0.1474 | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse | 6240 |
| 0.1260 | [Calcarius ornatus](https://en.wikipedia.org/wiki/Calcarius_ornatus) | Chestnut-collared Longspur | 4748 |
| 0.0652 | [Perdix perdix](https://en.wikipedia.org/wiki/Perdix_perdix)* | Gray Partridge | 3576 |
| 0.0573 | [Anthus spragueii](https://en.wikipedia.org/wiki/Anthus_spragueii) | Sprague's Pipit | 1636 |
| 0.0513 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper | 7042 |
| 0.0483 | [Spizella pallida](https://en.wikipedia.org/wiki/Spizella_pallida) | Clay-colored Sparrow | 19291 |
| 0.0389 | [Leucophaeus pipixcan](https://en.wikipedia.org/wiki/Leucophaeus_pipixcan) | Franklin's Gull | 14372 |
| 0.0352 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus)†* | Ring-necked Pheasant | 24049 |
| 0.0335 | [Ammospiza leconteii](https://en.wikipedia.org/wiki/Ammospiza_leconteii) | LeConte's Sparrow | 2114 |






### Top Species for Nebraska (NE)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1785 | [Tympanuchus cupido](https://en.wikipedia.org/wiki/Tympanuchus_cupido) | Greater Prairie-Chicken | 2934 |
| 0.1329 | [Lanius sp.](https://en.wikipedia.org/wiki/Lanius) |  | 56 |
| 0.0816 | [Grus grus](https://en.wikipedia.org/wiki/Grus_grus) |  | 147 |
| 0.0642 | [Zonotrichia querula](https://en.wikipedia.org/wiki/Zonotrichia_querula) | Harris's Sparrow | 13378 |
| 0.0528 | [Anser fabalis](https://en.wikipedia.org/wiki/Anser_fabalis) |  | 8 |
| 0.0423 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel | 19658 |
| 0.0365 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper | 5257 |
| 0.0319 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)‡ | Western Meadowlark | 42141 |
| 0.0268 | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse | 1279 |
| 0.0263 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite | 10081 |






### Top Species for New Hampshire (NH)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.3765 | [Tadorna tadorna](https://en.wikipedia.org/wiki/Tadorna_tadorna)* | Common Shelduck | 179 |
| 0.2412 | [Egretta gularis](https://en.wikipedia.org/wiki/Egretta_gularis) |  | 63 |
| 0.2373 | [Catharus bicknelli](https://en.wikipedia.org/wiki/Catharus_bicknelli) | Bicknell's Thrush | 3457 |
| 0.1201 | [Cygnus cygnus](https://en.wikipedia.org/wiki/Cygnus_cygnus) |  | 108 |
| 0.0331 | [Egretta garzetta](https://en.wikipedia.org/wiki/Egretta_garzetta)* | Little Egret | 115 |
| 0.0329 | [Empidonax flaviventris](https://en.wikipedia.org/wiki/Empidonax_flaviventris) | Yellow-bellied Flycatcher | 5766 |
| 0.0320 | [Turdus iliacus](https://en.wikipedia.org/wiki/Turdus_iliacus) |  | 56 |
| 0.0306 | [Calidris maritima](https://en.wikipedia.org/wiki/Calidris_maritima) | Purple Sandpiper | 2912 |
| 0.0275 | [Cuculidae sp.](https://en.wikipedia.org/wiki/Cuculidae) |  | 16 |
| 0.0270 | [Sterna dougallii](https://en.wikipedia.org/wiki/Sterna_dougallii) | Roseate Tern | 1322 |






### Top Species for New Jersey (NJ)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.8225 | [Chlidonias hybrida](https://en.wikipedia.org/wiki/Chlidonias_hybrida) |  | 544 |
| 0.5400 | [Progne tapera](https://en.wikipedia.org/wiki/Progne_tapera) | Brown-chested Martin | 62 |
| 0.3958 | [Rallus sp.](https://en.wikipedia.org/wiki/Rallus) |  | 76 |
| 0.2622 | [Tringa nebularia](https://en.wikipedia.org/wiki/Tringa_nebularia) | Common Greenshank | 325 |
| 0.2426 | [Vanellus vanellus](https://en.wikipedia.org/wiki/Vanellus_vanellus) | Northern Lapwing | 552 |
| 0.2163 | [Ammospiza maritima](https://en.wikipedia.org/wiki/Ammospiza_maritima) | Seaside Sparrow | 21461 |
| 0.1840 | [Calidris ferruginea](https://en.wikipedia.org/wiki/Calidris_ferruginea) |  | 950 |
| 0.1692 | [Haematopus palliatus](https://en.wikipedia.org/wiki/Haematopus_palliatus) | American Oystercatcher | 68430 |
| 0.1686 | [Cuculidae sp.](https://en.wikipedia.org/wiki/Cuculidae) |  | 92 |
| 0.1522 | [Branta bernicla](https://en.wikipedia.org/wiki/Branta_bernicla) | Brant | 73643 |






### Top Species for New Mexico (NM)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.4158 | [Pluvialis apricaria](https://en.wikipedia.org/wiki/Pluvialis_apricaria) |  | 341 |
| 0.3686 | [Baeolophus ridgwayi](https://en.wikipedia.org/wiki/Baeolophus_ridgwayi) | Juniper Titmouse | 31338 |
| 0.2965 | [Corvus sp. (raven sp.)](https://en.wikipedia.org/wiki/Corvus) |  | 13606 |
| 0.2709 | [Corvus cryptoleucus](https://en.wikipedia.org/wiki/Corvus_cryptoleucus) | Chihuahuan Raven | 26986 |
| 0.2584 | [Callipepla squamata](https://en.wikipedia.org/wiki/Callipepla_squamata) | Scaled Quail | 19220 |
| 0.2430 | [Leucosticte atrata](https://en.wikipedia.org/wiki/Leucosticte_atrata) | Black Rosy-Finch | 3183 |
| 0.2300 | [Leucosticte sp.](https://en.wikipedia.org/wiki/Leucosticte) |  | 606 |
| 0.2184 | [Leucosticte australis](https://en.wikipedia.org/wiki/Leucosticte_australis) | Brown-capped Rosy-Finch | 2965 |
| 0.2172 | [Gymnorhinus cyanocephalus](https://en.wikipedia.org/wiki/Gymnorhinus_cyanocephalus) | Pinyon Jay | 13673 |
| 0.2171 | [Melozone fusca](https://en.wikipedia.org/wiki/Melozone_fusca) | Canyon Towhee | 66423 |






### Top Species for Nevada (NV)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.9960 | [Tetraogallus himalayensis](https://en.wikipedia.org/wiki/Tetraogallus_himalayensis)* |  | 672 |
| 0.1529 | [Artemisiospiza nevadensis](https://en.wikipedia.org/wiki/Artemisiospiza_nevadensis) | Sagebrush Sparrow | 5068 |
| 0.1357 | [Toxostoma lecontei](https://en.wikipedia.org/wiki/Toxostoma_lecontei) | LeConte's Thrasher | 901 |
| 0.1303 | [Toxostoma crissale](https://en.wikipedia.org/wiki/Toxostoma_crissale) | Crissal Thrasher | 8275 |
| 0.0938 | [Dryobates albolarvatus](https://en.wikipedia.org/wiki/Dryobates_albolarvatus) | White-headed Woodpecker | 2560 |
| 0.0880 | [Polioptila melanura](https://en.wikipedia.org/wiki/Polioptila_melanura) | Black-tailed Gnatcatcher | 14326 |
| 0.0866 | [Gymnorhinus cyanocephalus](https://en.wikipedia.org/wiki/Gymnorhinus_cyanocephalus) | Pinyon Jay | 5444 |
| 0.0859 | [Calypte costae](https://en.wikipedia.org/wiki/Calypte_costae) | Costa's Hummingbird | 10397 |
| 0.0694 | [Empidonax wrightii](https://en.wikipedia.org/wiki/Empidonax_wrightii) | Gray Flycatcher | 6588 |
| 0.0662 | [Oreoscoptes montanus](https://en.wikipedia.org/wiki/Oreoscoptes_montanus) | Sage Thrasher | 6385 |






### Top Species for New York (NY)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.9360 | [Chroicocephalus cirrocephalus](https://en.wikipedia.org/wiki/Chroicocephalus_cirrocephalus) |  | 125 |
| 0.8710 | [Crex crex](https://en.wikipedia.org/wiki/Crex_crex) |  | 178 |
| 0.4780 | [Hydrobates sp.](https://en.wikipedia.org/wiki/Hydrobates) |  | 517 |
| 0.2971 | [Carduelis carduelis](https://en.wikipedia.org/wiki/Carduelis_carduelis)* | European Goldfinch | 1971 |
| 0.2352 | [Egretta gularis](https://en.wikipedia.org/wiki/Egretta_gularis) |  | 74 |
| 0.1864 | [Branta bernicla](https://en.wikipedia.org/wiki/Branta_bernicla) | Brant | 98677 |
| 0.1556 | [Catharus bicknelli](https://en.wikipedia.org/wiki/Catharus_bicknelli) | Bicknell's Thrush | 2999 |
| 0.1141 | [Ammospiza caudacuta](https://en.wikipedia.org/wiki/Ammospiza_caudacuta) | Saltmarsh Sparrow | 8990 |
| 0.1124 | [Aves sp.](https://en.wikipedia.org/wiki/Aves) |  | 3092 |
| 0.1050 | [Pelagodroma marina](https://en.wikipedia.org/wiki/Pelagodroma_marina) |  | 286 |






### Top Species for Ohio (OH)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1064 | [Larus dominicanus](https://en.wikipedia.org/wiki/Larus_dominicanus) |  | 109 |
| 0.1042 | [Fringilla montifringilla](https://en.wikipedia.org/wiki/Fringilla_montifringilla) |  | 632 |
| 0.1036 | [Larus crassirostris](https://en.wikipedia.org/wiki/Larus_crassirostris) | Black-tailed Gull | 152 |
| 0.0961 | [Setophaga kirtlandii](https://en.wikipedia.org/wiki/Setophaga_kirtlandii) | Kirtland's Warbler | 1496 |
| 0.0829 | [Setophaga castanea](https://en.wikipedia.org/wiki/Setophaga_castanea) | Bay-breasted Warbler | 41766 |
| 0.0818 | [Setophaga cerulea](https://en.wikipedia.org/wiki/Setophaga_cerulea) | Cerulean Warbler | 14331 |
| 0.0788 | [Cygnus sp.](https://en.wikipedia.org/wiki/Swan) |  | 2309 |
| 0.0783 | [Cygnus buccinator](https://en.wikipedia.org/wiki/Cygnus_buccinator) | Trumpeter Swan | 59931 |
| 0.0772 | [Calidris ferruginea](https://en.wikipedia.org/wiki/Calidris_ferruginea) |  | 496 |
| 0.0698 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow | 7628 |






### Top Species for Oklahoma (OK)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.4407 | [Tadorna ferruginea](https://en.wikipedia.org/wiki/Tadorna_ferruginea) |  | 114 |
| 0.1065 | [Anser cygnoides](https://en.wikipedia.org/wiki/Anser_cygnoides) |  | 15 |
| 0.0864 | [Vireo atricapilla](https://en.wikipedia.org/wiki/Vireo_atricapilla) | Black-capped Vireo | 1693 |
| 0.0848 | [Zonotrichia querula](https://en.wikipedia.org/wiki/Zonotrichia_querula) | Harris's Sparrow | 17544 |
| 0.0789 | [Tyrannus forficatus](https://en.wikipedia.org/wiki/Tyrannus_forficatus)‡ | Scissor-tailed Flycatcher | 37937 |
| 0.0743 | [Calcarius pictus](https://en.wikipedia.org/wiki/Calcarius_pictus) | Smith's Longspur | 889 |
| 0.0714 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite | 21873 |
| 0.0659 | [Streptopelia roseogrisea](https://en.wikipedia.org/wiki/Streptopelia_roseogrisea) | African Collared-Dove (a.k.a. Ringed Turtle-Dove) | 38 |
| 0.0517 | [Quiscalus sp.](https://en.wikipedia.org/wiki/Quiscalus) |  | 685 |
| 0.0358 | [Passerina ciris](https://en.wikipedia.org/wiki/Passerina_ciris) | Painted Bunting | 13547 |






### Top Species for Oregon (OR)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.9727 | [Melanitta nigra](https://en.wikipedia.org/wiki/Melanitta_nigra) |  | 285 |
| 0.6040 | [Pterodroma ultima](https://en.wikipedia.org/wiki/Pterodroma_ultima) |  | 589 |
| 0.5644 | [Aphelocoma californica](https://en.wikipedia.org/wiki/Aphelocoma_californica) | California Scrub-Jay | 374161 |
| 0.4319 | [Oreortyx pictus](https://en.wikipedia.org/wiki/Oreortyx_pictus) | Mountain Quail | 8746 |
| 0.3822 | [Chloris sinica](https://en.wikipedia.org/wiki/Chloris_sinica) |  | 43 |
| 0.3640 | [Setophaga occidentalis](https://en.wikipedia.org/wiki/Setophaga_occidentalis) | Hermit Warbler | 27518 |
| 0.3605 | [Chamaea fasciata](https://en.wikipedia.org/wiki/Chamaea_fasciata) | Wrentit | 38911 |
| 0.3525 | [Larus occidentalis](https://en.wikipedia.org/wiki/Larus_occidentalis) | Western Gull | 93667 |
| 0.3465 | [Chaetura vauxi](https://en.wikipedia.org/wiki/Chaetura_vauxi) | Vaux's Swift | 69677 |
| 0.3178 | [Sphyrapicus ruber](https://en.wikipedia.org/wiki/Sphyrapicus_ruber) | Red-breasted Sapsucker | 70159 |






### Top Species for Pennsylvania (PA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.3118 | [Anser serrirostris](https://en.wikipedia.org/wiki/Anser_serrirostris) |  | 733 |
| 0.2423 | [Chlidonias leucopterus](https://en.wikipedia.org/wiki/Chlidonias_leucopterus) | White-winged Tern | 317 |
| 0.1602 | [Poecile sp.](https://en.wikipedia.org/wiki/Poecile)† | unid. western chickadee species | 5671 |
| 0.0974 | [Aves sp.](https://en.wikipedia.org/wiki/Aves) |  | 2489 |
| 0.0882 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina)† | Wood Thrush | 171036 |
| 0.0820 | [Cuculidae sp.](https://en.wikipedia.org/wiki/Cuculidae) |  | 56 |
| 0.0701 | [Cathartidae sp.](https://en.wikipedia.org/wiki/Cathartidae) |  | 622 |
| 0.0653 | [Corvus sp. (crow sp.)](https://en.wikipedia.org/wiki/Corvus) |  | 34112 |
| 0.0625 | [Piranga olivacea](https://en.wikipedia.org/wiki/Piranga_olivacea) | Scarlet Tanager | 115306 |
| 0.0536 | [Setophaga citrina](https://en.wikipedia.org/wiki/Setophaga_citrina) | Hooded Warbler | 46535 |






### Top Species for Rhode Island (RI)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.6920 | [Cuculus canorus](https://en.wikipedia.org/wiki/Cuculus_canorus)* | Common Cuckoo | 672 |
| 0.2711 | [Xenus cinereus](https://en.wikipedia.org/wiki/Xenus_cinereus) |  | 194 |
| 0.2268 | [Anser anser](https://en.wikipedia.org/wiki/Anser_anser) |  | 82 |
| 0.1120 | [Calidris minuta](https://en.wikipedia.org/wiki/Calidris_minuta) |  | 179 |
| 0.0749 | [Brachyramphus perdix](https://en.wikipedia.org/wiki/Brachyramphus_perdix) |  | 26 |
| 0.0584 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant | 8422 |
| 0.0532 | [Ammospiza caudacuta](https://en.wikipedia.org/wiki/Ammospiza_caudacuta) | Saltmarsh Sparrow | 2966 |
| 0.0496 | [Calidris sp.](https://en.wikipedia.org/wiki/Calidris) | unid. small ''peep'' sandpiper | 380 |
| 0.0496 | [Larus crassirostris](https://en.wikipedia.org/wiki/Larus_crassirostris) | Black-tailed Gull | 58 |
| 0.0457 | [Tringa glareola](https://en.wikipedia.org/wiki/Tringa_glareola) |  | 154 |






### Top Species for South Carolina (SC)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1377 | [Dryobates borealis](https://en.wikipedia.org/wiki/Dryobates_borealis) | Red-cockaded Woodpecker | 5091 |
| 0.1131 | [Rallus crepitans](https://en.wikipedia.org/wiki/Rallus_crepitans) | Clapper Rail | 29691 |
| 0.1024 | [Sitta pusilla](https://en.wikipedia.org/wiki/Sitta_pusilla) | Brown-headed Nuthatch | 68558 |
| 0.1017 | [Passerina ciris](https://en.wikipedia.org/wiki/Passerina_ciris) | Painted Bunting | 38067 |
| 0.0872 | [Mycteria americana](https://en.wikipedia.org/wiki/Mycteria_americana) | Wood Stork | 40234 |
| 0.0716 | [Charadriidae sp.](https://en.wikipedia.org/wiki/Charadriidae) |  | 117 |
| 0.0674 | [Cathartidae sp.](https://en.wikipedia.org/wiki/Cathartidae) |  | 454 |
| 0.0669 | [Peucaea aestivalis](https://en.wikipedia.org/wiki/Peucaea_aestivalis) | Bachman's Sparrow | 2776 |
| 0.0598 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler | 3114 |
| 0.0588 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite | 20288 |






### Top Species for South Dakota (SD)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0592 | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse | 2538 |
| 0.0413 | [Tympanuchus cupido](https://en.wikipedia.org/wiki/Tympanuchus_cupido) | Greater Prairie-Chicken | 697 |
| 0.0381 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper | 5213 |
| 0.0314 | [Calcarius ornatus](https://en.wikipedia.org/wiki/Calcarius_ornatus) | Chestnut-collared Longspur | 1232 |
| 0.0313 | [Calamospiza melanocorys](https://en.wikipedia.org/wiki/Calamospiza_melanocorys)† | Lark Bunting | 3391 |
| 0.0222 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)† | Western Meadowlark | 28423 |
| 0.0219 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus)‡* | Ring-necked Pheasant | 15094 |
| 0.0187 | [Zonotrichia querula](https://en.wikipedia.org/wiki/Zonotrichia_querula) | Harris's Sparrow | 4057 |
| 0.0181 | [Athene cunicularia](https://en.wikipedia.org/wiki/Athene_cunicularia) | Burrowing Owl | 1976 |
| 0.0168 | [Leucophaeus pipixcan](https://en.wikipedia.org/wiki/Leucophaeus_pipixcan) | Franklin's Gull | 6443 |






### Top Species for Tennessee (TN)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.6266 | [Grus monacha](https://en.wikipedia.org/wiki/Grus_monacha) |  | 154 |
| 0.1358 | [Anser cygnoides](https://en.wikipedia.org/wiki/Anser_cygnoides) |  | 20 |
| 0.0604 | [Geothlypis formosa](https://en.wikipedia.org/wiki/Geothlypis_formosa) | Kentucky Warbler | 12863 |
| 0.0424 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler | 2385 |
| 0.0409 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 264148 |
| 0.0363 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 161073 |
| 0.0352 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler | 16980 |
| 0.0329 | [Setophaga citrina](https://en.wikipedia.org/wiki/Setophaga_citrina) | Hooded Warbler | 22961 |
| 0.0319 | [Spizella pusilla](https://en.wikipedia.org/wiki/Spizella_pusilla) | Field Sparrow | 83481 |
| 0.0313 | [Piranga rubra](https://en.wikipedia.org/wiki/Piranga_rubra) | Summer Tanager | 37115 |






### Top Species for Texas (TX)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.9189 | [Baeolophus atricristatus](https://en.wikipedia.org/wiki/Baeolophus_atricristatus) | Black-crested Titmouse | 365712 |
| 0.9136 | [Spermestes cucullata](https://en.wikipedia.org/wiki/Spermestes_cucullata) |  | 120 |
| 0.9092 | [Toxostoma longirostre](https://en.wikipedia.org/wiki/Toxostoma_longirostre) | Long-billed Thrasher | 118995 |
| 0.9036 | [Setophaga chrysoparia](https://en.wikipedia.org/wiki/Setophaga_chrysoparia) | Golden-cheeked Warbler | 21281 |
| 0.8348 | [Geranoaetus albicaudatus](https://en.wikipedia.org/wiki/Geranoaetus_albicaudatus) | White-tailed Hawk | 54492 |
| 0.7680 | [Arremonops rufivirgatus](https://en.wikipedia.org/wiki/Arremonops_rufivirgatus) | Olive Sparrow | 82550 |
| 0.7673 | [Dendrocygna sp.](https://en.wikipedia.org/wiki/Dendrocygna) |  | 345 |
| 0.7478 | [Leiothlypis crissalis](https://en.wikipedia.org/wiki/Leiothlypis_crissalis) | Colima Warbler | 3032 |
| 0.7431 | [Tyrannus couchii](https://en.wikipedia.org/wiki/Tyrannus_couchii) | Couch's Kingbird | 110055 |
| 0.7373 | [Cyanocorax yncas](https://en.wikipedia.org/wiki/Cyanocorax_yncas) | Green Jay | 150450 |






### Top Species for Utah (UT)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1930 | [Alectoris chukar](https://en.wikipedia.org/wiki/Alectoris_chukar)* | Chukar | 7064 |
| 0.1869 | [Psiloscops flammeolus](https://en.wikipedia.org/wiki/Psiloscops_flammeolus) | Flammulated Owl | 2119 |
| 0.1671 | [Gymnogyps californianus](https://en.wikipedia.org/wiki/Gymnogyps_californianus) | California Condor | 1515 |
| 0.1604 | [Leucosticte atrata](https://en.wikipedia.org/wiki/Leucosticte_atrata) | Black Rosy-Finch | 2119 |
| 0.1448 | [Aechmophorus clarkii](https://en.wikipedia.org/wiki/Aechmophorus_clarkii) | Clark's Grebe | 15670 |
| 0.1433 | [Vireo vicinior](https://en.wikipedia.org/wiki/Vireo_vicinior) | Gray Vireo | 2355 |
| 0.1345 | [Aphelocoma woodhouseii](https://en.wikipedia.org/wiki/Aphelocoma_woodhouseii) | Woodhouse's Scrub-Jay | 53017 |
| 0.1244 | [Gymnorhinus cyanocephalus](https://en.wikipedia.org/wiki/Gymnorhinus_cyanocephalus) | Pinyon Jay | 7974 |
| 0.1188 | [Centrocercus urophasianus](https://en.wikipedia.org/wiki/Centrocercus_urophasianus) | Greater Sage-Grouse | 1455 |
| 0.1137 | [Aix galericulata](https://en.wikipedia.org/wiki/Aix_galericulata) |  | 335 |






### Top Species for Virginia (VA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.5107 | [Anser indicus](https://en.wikipedia.org/wiki/Anser_indicus) |  | 152 |
| 0.1373 | [Limosa limosa](https://en.wikipedia.org/wiki/Limosa_limosa) |  | 245 |
| 0.1050 | [Corvus sp. (crow sp.)](https://en.wikipedia.org/wiki/Corvus) |  | 43910 |
| 0.0956 | [Numida meleagris (Domestic type)](https://en.wikipedia.org/wiki/Numida_meleagris_(Domestic_type)) |  | 229 |
| 0.0884 | [Empidonax virescens](https://en.wikipedia.org/wiki/Empidonax_virescens) | Acadian Flycatcher | 54363 |
| 0.0741 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 507768 |
| 0.0583 | [Corvus ossifragus](https://en.wikipedia.org/wiki/Corvus_ossifragus) | Fish Crow | 173005 |
| 0.0571 | [Helmitheros vermivorum](https://en.wikipedia.org/wiki/Helmitheros_vermivorum) | Worm-eating Warbler | 18144 |
| 0.0560 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 597727 |
| 0.0559 | [Larus crassirostris](https://en.wikipedia.org/wiki/Larus_crassirostris) | Black-tailed Gull | 93 |






### Top Species for Vermont (VT)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.2150 | [Catharus bicknelli](https://en.wikipedia.org/wiki/Catharus_bicknelli) | Bicknell's Thrush | 3176 |
| 0.0776 | [Larus crassirostris](https://en.wikipedia.org/wiki/Larus_crassirostris) | Black-tailed Gull | 96 |
| 0.0602 | [Aythya ferina](https://en.wikipedia.org/wiki/Aythya_ferina) |  | 47 |
| 0.0409 | [Spatula querquedula](https://en.wikipedia.org/wiki/Spatula_querquedula) |  | 90 |
| 0.0333 | [Empidonax alnorum](https://en.wikipedia.org/wiki/Empidonax_alnorum) | Alder Flycatcher | 15915 |
| 0.0319 | [Setophaga pensylvanica](https://en.wikipedia.org/wiki/Setophaga_pensylvanica) | Chestnut-sided Warbler | 44511 |
| 0.0297 | [Bonasa umbellus](https://en.wikipedia.org/wiki/Bonasa_umbellus)† | Ruffed Grouse | 16963 |
| 0.0294 | [Troglodytes hiemalis](https://en.wikipedia.org/wiki/Troglodytes_hiemalis) | Winter Wren | 27544 |
| 0.0293 | [Picoides arcticus](https://en.wikipedia.org/wiki/Picoides_arcticus) | Black-backed Woodpecker | 1953 |
| 0.0292 | [Catharus fuscescens](https://en.wikipedia.org/wiki/Catharus_fuscescens) | Veery | 35063 |






### Top Species for Washington (WA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.9451 | [Creagrus furcatus](https://en.wikipedia.org/wiki/Creagrus_furcatus) |  | 488 |
| 0.5293 | [Falco subbuteo](https://en.wikipedia.org/wiki/Falco_subbuteo) |  | 95 |
| 0.5010 | [Cerorhinca monocerata](https://en.wikipedia.org/wiki/Cerorhinca_monocerata) | Rhinoceros Auklet | 56517 |
| 0.4907 | [Prunella montanella](https://en.wikipedia.org/wiki/Prunella_montanella) |  | 589 |
| 0.4773 | [Zonotrichia sp.](https://en.wikipedia.org/wiki/Zonotrichia) |  | 754 |
| 0.4346 | [Cepphus columba](https://en.wikipedia.org/wiki/Cepphus_columba) | Pigeon Guillemot | 92260 |
| 0.3131 | [Poecile rufescens](https://en.wikipedia.org/wiki/Poecile_rufescens) | Chestnut-backed Chickadee | 268543 |
| 0.3079 | [Larus glaucescens](https://en.wikipedia.org/wiki/Larus_glaucescens) | Glaucous-winged Gull | 281727 |
| 0.3033 | [Ardenna carneipes](https://en.wikipedia.org/wiki/Ardenna_carneipes) |  | 935 |
| 0.2996 | [Phoebastria nigripes](https://en.wikipedia.org/wiki/Phoebastria_nigripes) |  | 7607 |






### Top Species for Wisconsin (WI)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.9598 | [Parus major](https://en.wikipedia.org/wiki/Parus_major)* | Great Tit | 729 |
| 0.1849 | [Tympanuchus cupido](https://en.wikipedia.org/wiki/Tympanuchus_cupido) | Greater Prairie-Chicken | 3424 |
| 0.1417 | [Antigone canadensis](https://en.wikipedia.org/wiki/Antigone_canadensis) | Sandhill Crane | 231517 |
| 0.1351 | [Anatidae sp.](https://en.wikipedia.org/wiki/Anatidae) |  | 1237 |
| 0.1237 | [Vermivora chrysoptera](https://en.wikipedia.org/wiki/Vermivora_chrysoptera) | Golden-winged Warbler | 19108 |
| 0.1097 | [Cistothorus stellaris](https://en.wikipedia.org/wiki/Cistothorus_stellaris) | Sedge Wren | 29448 |
| 0.1073 | [Carduelis carduelis](https://en.wikipedia.org/wiki/Carduelis_carduelis)* | European Goldfinch | 755 |
| 0.0861 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow | 8396 |
| 0.0798 | [Geothlypis philadelphia](https://en.wikipedia.org/wiki/Geothlypis_philadelphia) | Mourning Warbler | 21105 |
| 0.0637 | [Spizella pallida](https://en.wikipedia.org/wiki/Spizella_pallida) | Clay-colored Sparrow | 34542 |






### Top Species for West Virginia (WV)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0249 | [Setophaga cerulea](https://en.wikipedia.org/wiki/Setophaga_cerulea) | Cerulean Warbler | 3557 |
| 0.0246 | [Anser indicus](https://en.wikipedia.org/wiki/Anser_indicus) |  | 8 |
| 0.0157 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler | 850 |
| 0.0148 | [Parkesia motacilla](https://en.wikipedia.org/wiki/Parkesia_motacilla) | Louisiana Waterthrush | 6640 |
| 0.0145 | [Setophaga citrina](https://en.wikipedia.org/wiki/Setophaga_citrina) | Hooded Warbler | 9288 |
| 0.0137 | [Calidris tenuirostris](https://en.wikipedia.org/wiki/Calidris_tenuirostris) |  | 3 |
| 0.0134 | [Anas bahamensis](https://en.wikipedia.org/wiki/Anas_bahamensis) | White-cheeked Pintail | 18 |
| 0.0128 | [Piranga olivacea](https://en.wikipedia.org/wiki/Piranga_olivacea) | Scarlet Tanager | 19032 |
| 0.0128 | [Helmitheros vermivorum](https://en.wikipedia.org/wiki/Helmitheros_vermivorum) | Worm-eating Warbler | 3533 |
| 0.0125 | [Setophaga dominica](https://en.wikipedia.org/wiki/Setophaga_dominica) | Yellow-throated Warbler | 8854 |






### Top Species for Wyoming (WY)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1964 | [Centrocercus urophasianus](https://en.wikipedia.org/wiki/Centrocercus_urophasianus) | Greater Sage-Grouse | 2281 |
| 0.1465 | [Leucosticte atrata](https://en.wikipedia.org/wiki/Leucosticte_atrata) | Black Rosy-Finch | 1876 |
| 0.1183 | [Rhynchophanes mccownii](https://en.wikipedia.org/wiki/Rhynchophanes_mccownii) | Thick-billed Longspur | 2228 |
| 0.0956 | [Dendragapus obscurus](https://en.wikipedia.org/wiki/Dendragapus_obscurus) | Dusky Grouse | 2239 |
| 0.0784 | [Haemorhous sp.](https://en.wikipedia.org/wiki/Haemorhous) |  | 57 |
| 0.0773 | [Nucifraga columbiana](https://en.wikipedia.org/wiki/Nucifraga_columbiana) | Clark's Nutcracker | 14068 |
| 0.0735 | [Megascops sp.](https://en.wikipedia.org/wiki/Megascops) |  | 10 |
| 0.0612 | [Oreoscoptes montanus](https://en.wikipedia.org/wiki/Oreoscoptes_montanus) | Sage Thrasher | 5825 |
| 0.0601 | [Sialia currucoides](https://en.wikipedia.org/wiki/Sialia_currucoides)† | Mountain Bluebird | 21085 |
| 0.0525 | [Artemisiospiza nevadensis](https://en.wikipedia.org/wiki/Artemisiospiza_nevadensis) | Sagebrush Sparrow | 1788 |
















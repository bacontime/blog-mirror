
#%% Build the json from an (incomplete) markdown table

elementmd = '''|     | name          | symbol | pinyin | simp | trad | rad  | literal                      | etymology   | notes |
|-----|---------------|--------|--------|------|------|------|------------------------------|-------------|-------|
| 1   | Hydrogen      | H      | qīng   | 氢   | 氫   | 轻气 | lightweight gas              | ideographic |       |
| 2   | Helium        | He     | hài    | 氦   | 氦   | 亥气 | astrological pig gas         | loanword    |       |
| 3   | Lithium       | Li     | lǐ     | 锂   | 鋰   | 里金 | village metal                | loanword    |       |
| 4   | Beryllium     | Be     | pí     | 铍   | 鈹   | 皮金 | feather metal                | loanword    |       |
| 5   | Boron         | B      | péng   | 硼   | 硼   | 朋石 | friends stone                | classic     |       |
| 6   | Carbon        | C      | tàn    | 碳   | 碳   | 炭石 | coal stone                   | classic     |       |
| 7   | Nitrogen      | N      | dàn    | 氮   | 氮   | 淡气 | diluting gas                 | ideographic |       |
| 8   | Oxygen        | O      | yǎng   | 氧   | 氧   | 养气 | life-nurturing gas           | ideographic |       |
| 9   | Fluorine      | F      | fú     | 氟   | 氟   | 弗气 | negative gas                 | loanword    |       |
| 10  | Neon          | Ne     | nǎi    | 氖   | 氖   | 乃气 | indeed gas                   | loanword    |       |
| 11  | Sodium        | Na     | nà     | 钠   | 鈉   | 纳金 | offer metal                  | loanword    |       |
| 12  | Magnesium     | Mg     | měi    | 镁   | 鎂   | 美金 | beautiful metal              | loanword    |       |
| 13  | Aluminium     | Al     | lǚ     | 铝   | 鋁   | 吕金 | Lu metal (musical note/name) | loanword    |       |
| 14  | Silicon       | Si     | guī    | 硅   | 硅   | 圭石 | special jade stone           | loanword    |       |
| 15  | Phosphorus    | P      | lín    | 磷   | 磷   | 粦石 | phosphorus stone             | classic     |       |
| 16  | Sulfur        | S      | liú    | 硫   | 硫   | 荒石 | wasteland stone              | classic     |       |
| 17  | Chlorine      | Cl     | lǜ     | 氯   | 氯   | 绿气 | green gas                    | loanword    |       |
| 18  | Argon         | Ar     | yà     | 氩   | 氬   | 亚气 | next gas                     | loanword    |       |
| 19  | Potassium     | K      | jiǎ    | 钾   | 鉀   | 甲金 | shell metal                  | loanword    |       |
| 20  | Calcium       | Ca     | gài    | 钙   | 鈣   | 丐金 | beggar metal                 | loanword    |       |
| 21  | Scandium      | Sc     | kàng   | 钪   | 鈧   | 亢金 | proud metal                  | loanword    |       |
| 22  | Titanium      | Ti     | tài    | 钛   | 鈦   | 太金 | very big metal               | loanword    |       |
| 23  | Vanadium      | V      | fán    | 钒   | 釩   | 凡金 | mundane metal                | loanword    |       |
| 24  | Chromium      | Cr     | gè     | 铬   | 鉻   | 各金 | each metal                   | loanword    |       |
| 25  | Manganese     | Mn     | měng   | 锰   | 錳   | 猛金 | ferocious metal              | loanword    |       |
| 26  | Iron          | Fe     | tiě    | 铁   | 鐵   | ??   |                              | classic     |       |
| 27  | Cobalt        | Co     | gǔ     | 钴   | 鈷   | 古金 | ancient metal                | loanword    |       |
| 28  | Nickel        | Ni     | niè    | 镍   | 鎳   | 臬金 | benchmark metal              | loanword    |       |
| 29  | Copper        | Cu     | tóng   | 铜   | 銅   | ??   |                              | classic     |       |
| 30  | Zinc          | Zn     | xīn    | 锌   | 鋅   | 辛金 | acrid metal                  | loanword    |       |
| 31  | Gallium       | Ga     | jiā    | 镓   | 鎵   | 家金 | domestic metal               | loanword    |       |
| 32  | Germanium     | Ge     | zhě    | 锗   | 鍺   | 者金 | person of metal              | loanword    |       |
| 33  | Arsenic       | As     | shēn   | 砷   | 砷   | 申石 | explain metal                | loanword    |       |
| 34  | Selenium      | Se     | xī     | 硒   | 硒   | 西石 | west metal                   | loanword    |       |
| 35  | Bromine       | Br     | xiù    | 溴   | 溴   | 臭水 | stinky water                 | ideographic |       |
| 36  | Krypton       | Kr     | kè     | 氪   | 氪   | 克气 | conquering metal             | loanword    |       |
| 37  | Rubidium      | Rb     | rú     | 铷   | 銣   | 如金 | like such as metal           | loanword    |       |
| 38  | Strontium     | Sr     | sī     | 锶   | 鍶   | 思金 | ponder metal                 | loanword    |       |
| 39  | Yttrium       | Y      | yǐ     | 钇   | 釔   | 乙金 | 2nd metal                    | loanword    |       |
| 40  | Zirconium     | Zr     | gào    | 锆   | 鋯   | 告金 | sue metal                    | loanword    |       |
| 41  | Niobium       | Nb     | ní     | 铌   | 鈮   | 尼金 | nun metal                    | loanword    |       |
| 42  | Molybdenum    | Mo     | mù     | 钼   | 鉬   | 目金 | eye metal                    | loanword    |       |
| 43  | Technetium    | Tc     | dé     | 锝   | 鍀   | 得金 | get metal                    | loanword    |       |
| 44  | Ruthenium     | Ru     | liǎo   | 钌   | 釕   | 了金 | past-tense metal             | loanword    |       |
| 45  | Rhodium       | Rh     | lǎo    | 铑   | 銠   | 老金 | elderly metal                | loanword    |       |
| 46  | Palladium     | Pd     | bǎ     | 钯   | 鈀   | 把金 | cling to metal               | loanword    |       |
| 47  | Silver        | Ag     | yín    | 银   | 銀   | 艮金 |                              | classic     |       |
| 48  | Cadmium       | Cd     | gé     | 镉   | 鎘   | 鬲金 | Ge metal (name)              | loanword    |       |
| 49  | Indium        | In     | yīn    | 铟   | 銦   | 因金 | because of metal             | loanword    |       |
| 50  | Tin           | Sn     | xī     | 锡   | 錫   | 易金 |                              | classic     |       |
| 51  | Antimony      | Sb     | tī     | 锑   | 銻   | 悌金 | brotherly metal              | loanword    |       |
| 52  | Tellurium     | Te     | dì     | 碲   | 碲   | 帝石 | god emperor stone            | loanword    |       |
| 53  | Iodine        | I      | diǎn   | 碘   | 碘   | 典石 | classic stone                | loanword    |       |
| 54  | Xenon         | Xe     | xiān   | 氙   | 氙   | 仙气 | fairy gas                    | loanword    |       |
| 55  | Cesium        | Cs     | sè     | 铯   | 銫   | 色金 | tint metal                   | loanword    |       |
| 56  | Barium        | Ba     | bèi    | 钡   | 鋇   | 贝金 | cowry metal                  | loanword    |       |
| 57  | Lanthanum     | La     | lán    | 镧   | 鑭   | 阑金 | railing metal                | loanword    |       |
| 58  | Cerium        | Ce     | shì    | 铈   | 鈰   | 市金 | marketplace metal            | loanword    |       |
| 59  | Praseodymium  | Pr     | pǔ     | 镨   | 鐠   | 普金 | universal metal              | loanword    |       |
| 60  | Neodymium     | Nd     | nǚ     | 钕   | 釹   | 女金 | female metal                 | loanword    |       |
| 61  | Promethium    | Pm     | pǒ     | 钷   | 鉕   | 叵金 | improbable metal             | loanword    |       |
| 62  | Samarium      | Sm     | shān   | 钐   | 釤   | 彡金 | hair metal                   | loanword    |       |
| 63  | Europium      | Eu     | yǒu    | 铕   | 銪   | 有金 | have metal                   | loanword    |       |
| 64  | Gadolinium    | Gd     | gá     | 钆   | 釓   | 轧金 | squeeze metal                | loanword    |       |
| 65  | Terbium       | Tb     | tè     | 铽   | 鋱   | 忒金 | excessive metal              | loanword    |       |
| 66  | Dysprosium    | Dy     | dī     | 镝   | 鏑   | 滴金 | drip metal                   | loanword    |       |
| 67  | Holmium       | Ho     | huǒ    | 钬   | 鈥   | 火金 | fire metal                   | loanword    |       |
| 68  | Erbium        | Er     | ěr     | 铒   | 鉺   | 耳金 | ear metal                    | loanword    |       |
| 69  | Thulium       | Tm     | diū    | 铥   | 銩   | 丢金 | lost metal                   | loanword    |       |
| 70  | Ytterbium     | Yb     | yì     | 镱   | 鐿   | 意金 | intention metal              | loanword    |       |
| 71  | Lutetium      | Lu     | lǔ     | 镥   | 鑥   | 鲁金 | vulgar metal                 | loanword    |       |
| 72  | Hafnium       | Hf     | hā     | 铪   | 鉿   | 哈金 | ha! metal                    | loanword    |       |
| 73  | Tantalum      | Ta     | tǎn    | 钽   | 鉭   | 坦金 | composed metal               | loanword    |       |
| 74  | Tungsten      | W      | wū     | 钨   | 鎢   | 乌金 | raven metal                  | loanword    |       |
| 75  | Rhenium       | Re     | lái    | 铼   | 錸   | 来金 | incoming metal               | loanword    |       |
| 76  | Osmium        | Os     | é      | 锇   | 鋨   | 我金 | our metal                    | loanword    |       |
| 77  | Iridium       | Ir     | yī     | 铱   | 銥   | 衣金 | clothing metal               | loanword    |       |
| 78  | Platinum      | Pt     | bó     | 铂   | 鉑   | 白金 | white metal                  | loanword    |       |
| 79  | Gold          | Au     | jīn    | 金   | 金   | 金   | metal                        | classic     |       |
| 80  | Mercury       | Hg     | gǒng   | 工   | 汞   | 工水 | labor water                  | classic     |       |
| 81  | Thallium      | Tl     | tā     | 铊   | 鉈   | 它金 | it metal                     | loanword    |       |
| 82  | Lead          | Pb     | qiān   | 铅   | 鉛   | 㕣金 | marsh metal                  | classic     |       |
| 83  | Bismuth       | Bi     | bì     | 铋   | 鉍   | 必金 | necessarily metal            | loanword    |       |
| 84  | Polonium      | Po     | pō     | 钋   | 釙   | 卜金 |                              | loanword    |       |
| 85  | Astatine      | At     | ài     | 砹   | 砹   | 艾石 | mugwort stone                | loanword    |       |
| 86  | Radon         | Rn     | dōng   | 氡   | 氡   | 冬气 | winter gas                   | loanword    |       |
| 87  | Francium      | Fr     | fāng   | 钫   | 鈁   | 方金 | square metal                 | loanword    |       |
| 88  | Radium        | Ra     | léi    | 镭   | 鐳   | 雷金 | thunder metal                | loanword    |       |
| 89  | Actinium      | Ac     | ā      | 锕   | 錒   | 阿金 | āmetal (name prefix)         | loanword    |       |
| 90  | Thorium       | Th     | tǔ     | 钍   | 釷   | 土金 | earth metal                  | loanword    |       |
| 91  | Protactinium  | Pa     | pú     | 镤   | 鏷   | 菐金 | cumbersome metal             | loanword    |       |
| 92  | Uranium       | U      | yóu    | 铀   | 鈾   | 由金 | from metal                   | loanword    |       |
| 93  | Neptunium     | Np     | ná     | 镎   | 鎿   | 拿金 | seize metal                  | loanword    |       |
| 94  | Plutonium     | Pu     | bù     | 钚   | 鈈   | 不金 | not metal                    | loanword    |       |
| 95  | Americium     | Am     | méi    | 镅   | 鎇   | 眉金 | eyebrow metal                | loanword    |       |
| 96  | Curium        | Cm     | jú     | 锔   | 鋦   | 局金 | narrow metal                 | loanword    |       |
| 97  | Berkelium     | Bk     | péi    | 锫   | 錇   | 咅金 |                              | loanword    |       |
| 98  | Californium   | Cf     | kāi    | 锎   | 鐦   | 開金 | open metal                   | loanword    |       |
| 99  | Einsteinium   | Es     | āi     | 锿   | 鎄   | 哀金 | grief metal                  | loanword    |       |
| 100 | Fermium       | Fm     | fèi    | 镄   | 鐨   | 费金 | expenditure metal            | loanword    |       |
| 101 | Mendelevium   | Md     | mén    | 钔   | 鍆   | 门金 | door metal                   | loanword    |       |
| 102 | Nobelium      | No     | nuò    | 锘   | 鍩   | 诺金 | assent metal                 | loanword    |       |
| 103 | Lawrencium    | Lr     | láo    | 铹   | 鐒   | 劳金 | toil metal                   | loanword    |       |
| 104 | Rutherfordium | Rf     | lú     | 𬬻   | 鑪   | 卢金 | rice bowl metal              | loanword    |       |
| 105 | Dubnium       | Db     | dù     | 𬭊   | 𨧀   | 杜金 | stop metal                   | loanword    |       |
| 106 | Seaborgium    | Sg     | xǐ     | 𬭳   | 𨭎   | 喜金 | happy metal                  | loanword    |       |
| 107 | Bohrium       | Bh     | bō     | 𬭛   | 𨨏   | 波金 | wave metal                   | loanword    |       |
| 108 | Hassium       | Hs     | hēi    | 𬭶   | 𨭆   | 黑金 | black metal                  | loanword    |       |
| 109 | Meitnerium    | Mt     | mài    | 鿏   | 䥑   | 麦金 | wheat metal                  | loanword    |       |
| 110 | Darmstadtium  | Ds     | dá     | 𫟼   | 鐽   | 达金 | eminent metal                | loanword    |       |
| 111 | Roentgenium   | Rg     | lún    | 𬬭   | 錀   | 侖金 | orderly metal                | loanword    |       |
| 112 | Copernicium   | Cn     | gē     | 鿔   | 鎶   | 哥金 | older brother metal          | loanword    | Copernicus is transliterated as 哥白尼 (Gēbáiní)      |
| 113 | Nihonium      | Nh     | nǐ     | 鿭   | 鉨   | 你金 | thou metal                   | loanword    |       |
| 114 | Flerovium     | Fl     | fū     | 𫓧   | 鈇   | 夫金 | husband metal                | loanword    |       |
| 115 | Moscovium     | Mc     | mò     | 镆   | 镆   | 莫金 | don't metal                  | loanword    |       |
| 116 | Livermorium   | Lv     | lì     | 𫟷   | 鉝   | 立金 | erect metal                  | loanword    |       |
| 117 | Tennessine    | Ts     | tián   | 鿬   | 鿬   | 田石 | farm stone                   | loanword    |       |
| 118 | Oganesson     | Og     | ào     | 鿫   | 鿫   | 奥气 | mysterious gas               | loanword    |       |'''


# parse markdown table
elements = []

for line in elementmd.split('\n')[2:]:
    data = [entry.strip() for entry in line.strip('|').split('|')]
    element = dict()
    
    element["number"] = int(data[0])
    element["name"] = data[1]
    element["symbol"] = data[2]
    element["pinyin"] = data[3]
    element["hanzi_simp"] = data[4]
    element["hanzi_trad"] = data[5]
    element["etymology"] = data[8]
    
    radicals = data[6]
    element["radicals"] = radicals
    element["radical_phon"] = radicals[0]
    element["radical_sem"] = radicals[-1]
    element["radical_pinyin"] = radicals[-1]
    element["radical_meaning"] = data[7]

    element["notes"] = [data[9]]

    print(element)
    elements.append(element)

#"Copernicus" is transliterated as "哥白尼"


# %% Export the results to a json file for safe keeping.
import json

with open("hanzielements_generated.json", "w", encoding='UTF-8') as outfile:
    json.dump(elements, outfile, indent=4)






#%% Import and print source to put in markdown for GH pages.
# Two different files so that I have to manually merge them.
# Will change work flow in future commit.


def element_to_dlistmd(e):
    if e['hanzi_simp'] == e['hanzi_simp']:
        hanzi = e['hanzi_simp']
    else:
        hanzi = e['hanzi_simp'] + '/' + e['hanzi_trad']

    etymology = e['etymology']

    print(f"{e['symbol']} ({e['name']}) = {hanzi} ({e['pinyin']})")
    print(f": {etymology}")

    for note in e['notes']:
        if note:
            print(": "+note)

def element_to_ol(e):
    if e['hanzi_simp'] == e['hanzi_simp']:
        hanzi = e['hanzi_simp']
    else:
        hanzi = e['hanzi_simp'] + '/' + e['hanzi_trad']

    notes = ' '.join([note for note in e['notes'] if note])

    print(f"1. *{e['symbol']} ({e['name']}) = {hanzi} ({e['pinyin']})* -- {e['etymology']} {notes}")

elements = []
with open("hanzielements.json", "r", encoding='UTF-8') as f:
    elements = json.load(f)
for element in elements:
    #print()
    element_to_ol(element)
    

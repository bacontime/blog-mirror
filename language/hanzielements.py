
#%% Build the json from an (incomplete) markdown table

elementmd = '''|     | name          | symbol | pinyin | simp | trad | rad  | literal                      | etymology   | notes |
|-----|---------------|--------|--------|------|------|------|------------------------------|-------------|-------|
| 1   | Hydrogen      | H      | qīng   | 氢   | 氫   | 轻气 | lightweight gas              | ideographic |       |
| 2   | Helium        | He     | hài    | 氦   | 氦   | 亥气 | astrological pig gas         | pscompound    |       |
| 3   | Lithium       | Li     | lǐ     | 锂   | 鋰   | 里金 | village metal                | pscompound    |       |
| 4   | Beryllium     | Be     | pí     | 铍   | 鈹   | 皮金 | feather metal                | pscompound    |       |
| 5   | Boron         | B      | péng   | 硼   | 硼   | 朋石 | friends stone                | classic     |       |
| 6   | Carbon        | C      | tàn    | 碳   | 碳   | 炭石 | coal stone                   | classic     |       |
| 7   | Nitrogen      | N      | dàn    | 氮   | 氮   | 淡气 | diluting gas                 | ideographic |       |
| 8   | Oxygen        | O      | yǎng   | 氧   | 氧   | 养气 | life-nurturing gas           | ideographic |       |
| 9   | Fluorine      | F      | fú     | 氟   | 氟   | 弗气 | negative gas                 | pscompound    |       |
| 10  | Neon          | Ne     | nǎi    | 氖   | 氖   | 乃气 | indeed gas                   | pscompound    |       |
| 11  | Sodium        | Na     | nà     | 钠   | 鈉   | 纳金 | offer metal                  | pscompound    |       |
| 12  | Magnesium     | Mg     | měi    | 镁   | 鎂   | 美金 | beautiful metal              | pscompound    |       |
| 13  | Aluminium     | Al     | lǚ     | 铝   | 鋁   | 吕金 | Lu metal (musical note/name) | pscompound    |       |
| 14  | Silicon       | Si     | guī    | 硅   | 硅   | 圭石 | special jade stone           | pscompound    |       |
| 15  | Phosphorus    | P      | lín    | 磷   | 磷   | 粦石 | phosphorus stone             | classic     |       |
| 16  | Sulfur        | S      | liú    | 硫   | 硫   | 荒石 | wasteland stone              | classic     |       |
| 17  | Chlorine      | Cl     | lǜ     | 氯   | 氯   | 绿气 | green gas                    | pscompound    |       |
| 18  | Argon         | Ar     | yà     | 氩   | 氬   | 亚气 | next gas                     | pscompound    |       |
| 19  | Potassium     | K      | jiǎ    | 钾   | 鉀   | 甲金 | shell metal                  | pscompound    |       |
| 20  | Calcium       | Ca     | gài    | 钙   | 鈣   | 丐金 | beggar metal                 | pscompound    |       |
| 21  | Scandium      | Sc     | kàng   | 钪   | 鈧   | 亢金 | proud metal                  | pscompound    |       |
| 22  | Titanium      | Ti     | tài    | 钛   | 鈦   | 太金 | very big metal               | pscompound    |       |
| 23  | Vanadium      | V      | fán    | 钒   | 釩   | 凡金 | mundane metal                | pscompound    |       |
| 24  | Chromium      | Cr     | gè     | 铬   | 鉻   | 各金 | each metal                   | pscompound    |       |
| 25  | Manganese     | Mn     | měng   | 锰   | 錳   | 猛金 | ferocious metal              | pscompound    |       |
| 26  | Iron          | Fe     | tiě    | 铁   | 鐵   | ??   |                              | classic     |       |
| 27  | Cobalt        | Co     | gǔ     | 钴   | 鈷   | 古金 | ancient metal                | pscompound    |       |
| 28  | Nickel        | Ni     | niè    | 镍   | 鎳   | 臬金 | benchmark metal              | pscompound    |       |
| 29  | Copper        | Cu     | tóng   | 铜   | 銅   | ??   |                              | classic     |       |
| 30  | Zinc          | Zn     | xīn    | 锌   | 鋅   | 辛金 | acrid metal                  | pscompound    |       |
| 31  | Gallium       | Ga     | jiā    | 镓   | 鎵   | 家金 | domestic metal               | pscompound    |       |
| 32  | Germanium     | Ge     | zhě    | 锗   | 鍺   | 者金 | person of metal              | pscompound    |       |
| 33  | Arsenic       | As     | shēn   | 砷   | 砷   | 申石 | explain metal                | pscompound    |       |
| 34  | Selenium      | Se     | xī     | 硒   | 硒   | 西石 | west metal                   | pscompound    |       |
| 35  | Bromine       | Br     | xiù    | 溴   | 溴   | 臭水 | odor water                 | ideographic |       |
| 36  | Krypton       | Kr     | kè     | 氪   | 氪   | 克气 | conquering metal             | pscompound    |       |
| 37  | Rubidium      | Rb     | rú     | 铷   | 銣   | 如金 | like such as metal           | pscompound    |       |
| 38  | Strontium     | Sr     | sī     | 锶   | 鍶   | 思金 | ponder metal                 | pscompound    |       |
| 39  | Yttrium       | Y      | yǐ     | 钇   | 釔   | 乙金 | 2nd metal                    | pscompound    |       |
| 40  | Zirconium     | Zr     | gào    | 锆   | 鋯   | 告金 | sue metal                    | pscompound    |       |
| 41  | Niobium       | Nb     | ní     | 铌   | 鈮   | 尼金 | nun metal                    | pscompound    |       |
| 42  | Molybdenum    | Mo     | mù     | 钼   | 鉬   | 目金 | eye metal                    | pscompound    |       |
| 43  | Technetium    | Tc     | dé     | 锝   | 鍀   | 得金 | get metal                    | pscompound    |       |
| 44  | Ruthenium     | Ru     | liǎo   | 钌   | 釕   | 了金 | finish metal             | pscompound    |       |
| 45  | Rhodium       | Rh     | lǎo    | 铑   | 銠   | 老金 | elderly metal                | pscompound    |       |
| 46  | Palladium     | Pd     | bǎ     | 钯   | 鈀   | 把金 | cling to metal               | pscompound    |       |
| 47  | Silver        | Ag     | yín    | 银   | 銀   | 艮金 |                              | classic     |       |
| 48  | Cadmium       | Cd     | gé     | 镉   | 鎘   | 鬲金 | Ge metal (name)              | pscompound    |       |
| 49  | Indium        | In     | yīn    | 铟   | 銦   | 因金 | because of metal             | pscompound    |       |
| 50  | Tin           | Sn     | xī     | 锡   | 錫   | 易金 |                              | classic     |       |
| 51  | Antimony      | Sb     | tī     | 锑   | 銻   | 悌金 | brotherly metal              | pscompound    |       |
| 52  | Tellurium     | Te     | dì     | 碲   | 碲   | 帝石 | god emperor stone            | pscompound    |       |
| 53  | Iodine        | I      | diǎn   | 碘   | 碘   | 典石 | classic stone                | pscompound    |       |
| 54  | Xenon         | Xe     | xiān   | 氙   | 氙   | 仙气 | fairy gas                    | pscompound    |       |
| 55  | Cesium        | Cs     | sè     | 铯   | 銫   | 色金 | tint metal                   | pscompound    |       |
| 56  | Barium        | Ba     | bèi    | 钡   | 鋇   | 贝金 | cowry metal                  | pscompound    |       |
| 57  | Lanthanum     | La     | lán    | 镧   | 鑭   | 阑金 | railing metal                | pscompound    |       |
| 58  | Cerium        | Ce     | shì    | 铈   | 鈰   | 市金 | marketplace metal            | pscompound    |       |
| 59  | Praseodymium  | Pr     | pǔ     | 镨   | 鐠   | 普金 | universal metal              | pscompound    |       |
| 60  | Neodymium     | Nd     | nǚ     | 钕   | 釹   | 女金 | female metal                 | pscompound    |       |
| 61  | Promethium    | Pm     | pǒ     | 钷   | 鉕   | 叵金 | improbable metal             | pscompound    |       |
| 62  | Samarium      | Sm     | shān   | 钐   | 釤   | 彡金 | hair metal                   | pscompound    |       |
| 63  | Europium      | Eu     | yǒu    | 铕   | 銪   | 有金 | have metal                   | pscompound    |       |
| 64  | Gadolinium    | Gd     | gá     | 钆   | 釓   | 轧金 | squeeze metal                | pscompound    |       |
| 65  | Terbium       | Tb     | tè     | 铽   | 鋱   | 忒金 | excessive metal              | pscompound    |       |
| 66  | Dysprosium    | Dy     | dī     | 镝   | 鏑   | 滴金 | drip metal                   | pscompound    |       |
| 67  | Holmium       | Ho     | huǒ    | 钬   | 鈥   | 火金 | fire metal                   | pscompound    |       |
| 68  | Erbium        | Er     | ěr     | 铒   | 鉺   | 耳金 | ear metal                    | pscompound    |       |
| 69  | Thulium       | Tm     | diū    | 铥   | 銩   | 丢金 | lost metal                   | pscompound    |       |
| 70  | Ytterbium     | Yb     | yì     | 镱   | 鐿   | 意金 | intention metal              | pscompound    |       |
| 71  | Lutetium      | Lu     | lǔ     | 镥   | 鑥   | 鲁金 | vulgar metal                 | pscompound    |       |
| 72  | Hafnium       | Hf     | hā     | 铪   | 鉿   | 哈金 | ha! metal                    | pscompound    |       |
| 73  | Tantalum      | Ta     | tǎn    | 钽   | 鉭   | 坦金 | composed metal               | pscompound    |       |
| 74  | Tungsten      | W      | wū     | 钨   | 鎢   | 乌金 | raven metal                  | pscompound    |       |
| 75  | Rhenium       | Re     | lái    | 铼   | 錸   | 来金 | incoming metal               | pscompound    |       |
| 76  | Osmium        | Os     | é      | 锇   | 鋨   | 我金 | our metal                    | pscompound    |       |
| 77  | Iridium       | Ir     | yī     | 铱   | 銥   | 衣金 | clothing metal               | pscompound    |       |
| 78  | Platinum      | Pt     | bó     | 铂   | 鉑   | 白金 | white metal                  | pscompound    |       |
| 79  | Gold          | Au     | jīn    | 金   | 金   | 金   | metal                        | classic     |       |
| 80  | Mercury       | Hg     | gǒng   | 汞   | 汞   | 工水 | labor water                  | classic     |       |
| 81  | Thallium      | Tl     | tā     | 铊   | 鉈   | 它金 | it metal                     | pscompound    |       |
| 82  | Lead          | Pb     | qiān   | 铅   | 鉛   | 㕣金 | marsh metal                  | classic     |       |
| 83  | Bismuth       | Bi     | bì     | 铋   | 鉍   | 必金 | necessarily metal            | pscompound    |       |
| 84  | Polonium      | Po     | pō     | 钋   | 釙   | 卜金 |                              | pscompound    |       |
| 85  | Astatine      | At     | ài     | 砹   | 砹   | 艾石 | mugwort stone                | pscompound    |       |
| 86  | Radon         | Rn     | dōng   | 氡   | 氡   | 冬气 | winter gas                   | pscompound    |       |
| 87  | Francium      | Fr     | fāng   | 钫   | 鈁   | 方金 | square metal                 | pscompound    |       |
| 88  | Radium        | Ra     | léi    | 镭   | 鐳   | 雷金 | thunder metal                | pscompound    |       |
| 89  | Actinium      | Ac     | ā      | 锕   | 錒   | 阿金 | āmetal (name prefix)         | pscompound    |       |
| 90  | Thorium       | Th     | tǔ     | 钍   | 釷   | 土金 | earth metal                  | pscompound    |       |
| 91  | Protactinium  | Pa     | pú     | 镤   | 鏷   | 菐金 | cumbersome metal             | pscompound    |       |
| 92  | Uranium       | U      | yóu    | 铀   | 鈾   | 由金 | from metal                   | pscompound    |       |
| 93  | Neptunium     | Np     | ná     | 镎   | 鎿   | 拿金 | seize metal                  | pscompound    |       |
| 94  | Plutonium     | Pu     | bù     | 钚   | 鈈   | 不金 | not metal                    | pscompound    |       |
| 95  | Americium     | Am     | méi    | 镅   | 鎇   | 眉金 | eyebrow metal                | pscompound    |       |
| 96  | Curium        | Cm     | jú     | 锔   | 鋦   | 局金 | narrow metal                 | pscompound    |       |
| 97  | Berkelium     | Bk     | péi    | 锫   | 錇   | 咅金 |                              | pscompound    |       |
| 98  | Californium   | Cf     | kāi    | 锎   | 鐦   | 開金 | open metal                   | pscompound    |       |
| 99  | Einsteinium   | Es     | āi     | 锿   | 鎄   | 哀金 | grief metal                  | pscompound    |       |
| 100 | Fermium       | Fm     | fèi    | 镄   | 鐨   | 费金 | expenditure metal            | pscompound    |       |
| 101 | Mendelevium   | Md     | mén    | 钔   | 鍆   | 门金 | door metal                   | pscompound    |       |
| 102 | Nobelium      | No     | nuò    | 锘   | 鍩   | 诺金 | assent metal                 | pscompound    |       |
| 103 | Lawrencium    | Lr     | láo    | 铹   | 鐒   | 劳金 | toil metal                   | pscompound    |       |
| 104 | Rutherfordium | Rf     | lú     | 𬬻   | 鑪   | 卢金 | rice bowl metal              | pscompound    |       |
| 105 | Dubnium       | Db     | dù     | 𬭊   | 𨧀   | 杜金 | stop metal                   | pscompound    |       |
| 106 | Seaborgium    | Sg     | xǐ     | 𬭳   | 𨭎   | 喜金 | happy metal                  | pscompound    |       |
| 107 | Bohrium       | Bh     | bō     | 𬭛   | 𨨏   | 波金 | wave metal                   | pscompound    |       |
| 108 | Hassium       | Hs     | hēi    | 𬭶   | 𨭆   | 黑金 | black metal                  | pscompound    |       |
| 109 | Meitnerium    | Mt     | mài    | 鿏   | 䥑   | 麦金 | wheat metal                  | pscompound    |       |
| 110 | Darmstadtium  | Ds     | dá     | 𫟼   | 鐽   | 达金 | eminent metal                | pscompound    |       |
| 111 | Roentgenium   | Rg     | lún    | 𬬭   | 錀   | 侖金 | orderly metal                | pscompound    |       |
| 112 | Copernicium   | Cn     | gē     | 鿔   | 鎶   | 哥金 | older brother metal          | pscompound    | Copernicus is transliterated as 哥白尼 (Gēbáiní)      |
| 113 | Nihonium      | Nh     | nǐ     | 鿭   | 鉨   | 你金 | thou metal                   | pscompound    |       |
| 114 | Flerovium     | Fl     | fū     | 𫓧   | 鈇   | 夫金 | husband metal                | pscompound    |       |
| 115 | Moscovium     | Mc     | mò     | 镆   | 镆   | 莫金 | don't metal                  | pscompound    |       |
| 116 | Livermorium   | Lv     | lì     | 𫟷   | 鉝   | 立金 | erect metal                  | pscompound    |       |
| 117 | Tennessine    | Ts     | tián   | 鿬   | 鿬   | 田石 | farm stone                   | pscompound    |       |
| 118 | Oganesson     | Og     | ào     | 鿫   | 鿫   | 奥气 | mysterious gas               | pscompound    |       |'''


# parse markdown table
import xpinyin
pinyin = xpinyin.Pinyin()
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
    
    radicals = data[6]
    element["radicals"] = radicals
    element["radical_phon"] = radicals[0]
    element["radical_sem"] = radicals[-1]
    element["radical_pinyin"] = ""

    literal_meaning = data[7]
    literal_meaning = literal_meaning.replace('metal','')
    literal_meaning = literal_meaning.replace('gas','')
    literal_meaning = literal_meaning.replace('stone','')
    element["radical_meaning"] = literal_meaning.strip()

    element["etymology_type"] = data[8]
    element["etymology"] = ""
    if element["etymology_type"] == 'pscompound':
        radical_sound = pinyin.get_pinyin(element["radical_phon"], tone_marks='marks')
        element_sound = element["pinyin"]
        if element_sound == radical_sound:
            element["etymology"] = f'Loanword. Homophonic with {element["radical_phon"]}, meaning {element["radical_meaning"]!r}.'

    element["notes"] = [data[9]]


    print(element)
    elements.append(element)

#"Copernicus" is transliterated as "哥白尼"




#%% Same thing using a different library
for element in elements:
    rphon =  element["radical_phon"]
    rpin =  element["pinyin"]
    rphonpin = pinyin.get_pinyin(rphon, tone_marks='marks')
    if rpin != rphonpin:
        print(element['symbol'],element['hanzi_simp'],rphon, rpin,rphonpin)
        if element['etymology'] == 'classic':
            print(element['symbol'])

# Here are the results:
results = '''
P 磷 粦 lín lìn
S 硫 荒 liú huāng
Fe 铁 ? tiě ?
Cu 铜 ? tóng ?
Br 溴 臭 xiù chòu
Ru 钌 了 liǎo le
Ag 银 艮 yín gèn
Cd 镉 鬲 gé lì
Sn 锡 易 xī yì
Sb 锑 悌 tī tì
Gd 钆 轧 gá yà
Tb 铽 忒 tè tuī
Os 锇 我 é wǒ
Pt 铂 白 bó bái
Hg 汞 工 gǒng gōng
Pb 铅 㕣 qiān yǎn
Po 钋 卜 pō bǔ
Bk 锫 咅 péi pòu
'''

# These ones are fine:
r1 = '''
Ru 钌 了 liǎo le (mult pronunc)
P 磷 粦 lín lìn (xpinyin is wrong?)
Br 溴 臭 xiù chòu (mult pronunc)
Cd 镉 鬲 gé lì (mult pronunc)
Gd 钆 轧 gá yà (mult pronunc)
Tb 铽 忒 tè tuī (xpinyin is wrong?)

'''


# these ones are classic character
r2 = '''
S 硫 荒 liú huāng (mistake on my part, should be 旒)
Fe 铁 ? tiě ?
Cu 铜 ? tóng ?
Ag 银 艮 yín gèn
Pt 铂 白 bó bái (though platinum called 白金 báijīn as slang. yiru says is bou jin. dutch witgoud or platina)
Pb 铅 㕣 qiān yǎn (铅 only pronuc yan when used as proper noun)
Hg 汞 工 gǒng gōng
'''

# these ones are unexplained
r3 = '''
Sn 锡 易 xī yì
Sb 锑 悌 tī tì (genuinely just a different pronunciation)
Os 锇 我 é wǒ (originally 鐚惡è evil; 俄 is é, sudden/russian; 
    我 weapon ě; 哦 chanting é; 鹅 goose é, zh wiki cites goose 音同“鹅”)
Po 钋 卜 pō bǔ (???)
Bk 锫 咅 péi pòu (possibly from 培 or 赔)
'''


#%%
for element in elements:
    rphon =  element["radical_phon"]
    rpin =  element["pinyin"]
    rphonpin = p.get_pinyins(rphon, tone_marks='marks')
    if len(rphonpin) > 1:
        print(element['symbol'],element['hanzi_simp'],rphon, rpin,rphonpin)














# %% Export the results to a json file for safe keeping.
import json

with open("hanzielements_generated.json", "w", encoding='UTF-8') as outfile:
    json.dump(elements, outfile, indent=4)






#%% Import and print source to put in markdown for GH pages.
# Two different files so that I have to manually merge them.
# Will change work flow in future commit.


def element_to_dlistmd(e):
    if e['hanzi_simp'] == e['hanzi_trad']:
        hanzi = e['hanzi_simp']
    else:
        hanzi = e['hanzi_simp'] + '/' + e['hanzi_trad']

    print(f"{e['symbol']} ({e['name']}) = {hanzi} ({e['pinyin']})")
    print(f": {e['etymology']}")
    for note in e['notes']:
        if note:
            print(": "+note)

def element_to_ol(e):
    if e['hanzi_simp'] == e['hanzi_simp']:
        hanzi = e['hanzi_simp']
    else:
        hanzi = e['hanzi_simp'] + '/' + e['hanzi_trad']

    notes = ' '.join([note for note in e['notes'] if note])

    print(f"1. **{e['symbol']} ({e['name']}) = {hanzi} ({e['pinyin']})** -- {e['etymology']} {notes}")


with open("hanzielements.json", "r", encoding='UTF-8') as f:
    elementlist = json.load(f)
for element in elementlist:
    print()
    element_to_dlistmd(element)
    

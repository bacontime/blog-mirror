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
    

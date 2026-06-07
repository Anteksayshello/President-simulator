from pathlib import Path
import re

path = Path('game/script.rpy')
lines = path.read_text(encoding='utf-8').splitlines()

exact = {
    'AsSASSASsinate': 'assassinate',
    'asSASSASsinate': 'assassinate',
    'asSASsinate': 'assassinate',
    'AsSASSASsinated': 'assassinated',
    'asSASSASsinated': 'assassinated',
    'asSASsinated': 'assassinated',
    'Inveest': 'Invest',
    'Ingnore': 'Ignore',
    'Woould': 'Would',
    'Whatdo': 'What do',
    'resuls': 'results',
    'assasinate': 'assassinate',
    'assasinated': 'assassinated',
    'portugees': 'Portuguese',
    'demilitrize': 'demilitarize',
    'intropduce': 'introduce',
    'andora': 'Andorra',
    'presure': 'pressure',
    'stablize': 'stabilize',
    'reactrors': 'reactors',
    'rulling': 'ruling',
    'tule': 'rule',
    'airforce': 'air force',
    'ricardos': 'Ricardo',
    'france': 'France',
    'spanish': 'Spanish',
    'portugal': 'Portugal',
    'gibraltar': 'Gibraltar',
    'monaco': 'Monaco',
    'andorra': 'Andorra',
    'morocco': 'Morocco',
    'mossad': 'Mossad',
    'sas': 'SAS',
    'china': 'China',
    'iberia': 'Iberia',
    'listenbourg': 'Listenbourg',
    'socliast': 'socialist',
    'politcical': 'political',
    'diffrent': 'different',
    'goverment': 'government',
    'withold': 'withhold',
    'elecations': 'elections',
    'buisness': 'business',
    'ingnore': 'ignore',
    'proceerd': 'proceeded',
    'ccommunist': 'communist',
    'deicided': 'decided',
    'woould': 'would',
    'conspiritators': 'conspirators',
    'shoking': 'shocking',
    'dont': "don't",
    'aveonics': 'avionics',
    'manditory': 'mandatory',
}

for i, line in enumerate(lines):
    if re.search(r'^\s*(vc|n|p|na)\s+"', line):
        new_line = line
        for old, new in exact.items():
            new_line = new_line.replace(old, new)
        lines[i] = new_line

path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('Dialogue typo cleanup applied.')

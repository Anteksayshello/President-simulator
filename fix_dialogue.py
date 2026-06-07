from pathlib import Path
import re

path = Path('game/script.rpy')
text = path.read_text(encoding='utf-8')
lines = text.splitlines()

replacements = {
    'Assinate': 'Assassinate',
    'assinate': 'assassinate',
    'buisness': 'business',
    'ingnore': 'ignore',
    'inveest': 'invest',
    'withold': 'withhold',
    'elecations': 'elections',
    'goverment': 'government',
    'proceerd': 'proceeded',
    'ccommunist': 'communist',
    'deicided': 'decided',
    'woould': 'would',
    'assinated': 'assassinated',
    'conspiritators': 'conspirators',
    'shoking': 'shocking',
    'resuls': 'results',
    "dont": "don't",
    'assasinate': 'assassinate',
    'aveonics': 'avionics',
    'demilitrize': 'demilitarize',
    'whatdo': 'what do',
    'airforce': 'air force',
    'manditory': 'mandatory',
    'ricardos': 'Ricardo',
    'intropduce': 'introduce',
    'andora': 'Andorra',
    'presure': 'pressure',
    'stablize': 'stabilize',
    'reactrors': 'reactors',
    'rulling': 'ruling',
    'tule': 'rule',
    'politcical': 'political',
    'socliast': 'socialist',
    'diffrent': 'different',
    'assaninated': 'assassinated',
    'listenbourg': 'Listenbourg',
    'portugees': 'Portuguese',
    'portugese': 'Portuguese',
    'spain': 'Spain',
    'france': 'France',
    'uk': 'UK',
    'Uk': 'UK',
    'china': 'China',
    'iberia': 'Iberia',
    'andorra': 'Andorra',
    'gibraltar': 'Gibraltar',
    'monaco': 'Monaco',
    'morocco': 'Morocco',
    'mossad': 'Mossad',
    'sas': 'SAS',
}

for i, line in enumerate(lines):
    if re.search(r'^\s*(vc|n|p|na)\s+"', line):
        # Fix typo words in spoken dialogue lines only.
        new_line = line
        for old, new in replacements.items():
            new_line = new_line.replace(old, new)
        # Capitalize the first spoken character after the speaker tag if it starts lowercase.
        m = re.match(r'^(\s*(vc|n|p|na)\s+")([^"])(.*)"$', line)
        if m:
            prefix = m.group(1)
            first = m.group(3)
            rest = m.group(4)
            if first.islower():
                new_line = prefix + first.upper() + rest + '"'
        lines[i] = new_line

path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('Dialogue typo fixes applied.')

from pathlib import Path
import re

path = Path('game/script.rpy')
lines = path.read_text(encoding='utf-8').splitlines()

word_repls = [
    ('AsSASSASsinate', 'assassinate'),
    ('asSASSASsinate', 'assassinate'),
    ('asSASsinate', 'assassinate'),
    ('AsSASSASsinated', 'assassinated'),
    ('asSASSASsinated', 'assassinated'),
    ('asSASsinated', 'assassinated'),
    ('Assinate', 'Assassinate'),
    ('assinate', 'assassinate'),
    ('assinated', 'assassinated'),
    ('assasinate', 'assassinate'),
    ('assasinated', 'assassinated'),
    ('Inveest', 'Invest'),
    ('Ingnore', 'Ignore'),
    ('Woould', 'Would'),
    ('Whatdo', 'What do'),
    ('resuls', 'results'),
    ('demilitrize', 'demilitarize'),
    ('intropduce', 'introduce'),
    ('andora', 'Andorra'),
    ('presure', 'pressure'),
    ('stablize', 'stabilize'),
    ('reactrors', 'reactors'),
    ('rulling', 'ruling'),
    ('tule', 'rule'),
    ('airforce', 'air force'),
    ('ricardos', 'Ricardo'),
    ('portugees', 'Portuguese'),
    ('portugese', 'Portuguese'),
    ('listenbourg', 'Listenbourg'),
    ('socliast', 'socialist'),
    ('politcical', 'political'),
    ('diffrent', 'different'),
    ('goverment', 'government'),
    ('withold', 'withhold'),
    ('elecations', 'elections'),
    ('buisness', 'business'),
    ('ingnore', 'ignore'),
    ('proceerd', 'proceeded'),
    ('ccommunist', 'communist'),
    ('deicided', 'decided'),
    ('woould', 'would'),
    ('conspiritators', 'conspirators'),
    ('shoking', 'shocking'),
    ("dont", "don't"),
    ('aveonics', 'avionics'),
    ('manditory', 'mandatory'),
]

for i, line in enumerate(lines):
    if re.search(r'^\s*(vc|n|p|na)\s+"', line):
        new_line = line
        for old, new in word_repls:
            new_line = re.sub(r'\b' + re.escape(old) + r'\b', new, new_line)
        lines[i] = new_line

path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('Final dialogue cleanup applied.')

from spellchecker import SpellChecker
import re
import pathlib
text = pathlib.Path('game/script.rpy').read_text(encoding='utf-8')
lines = text.splitlines()
sc = SpellChecker()
ignore = {
 'rpy','renpy','listenbourg','iberia','portugal','spain','gibraltar','andorra','monaco','mossad','france','china','uk','sas','elections','parliament','government','military','militia','nuclear','welfare','education','budget','political','president','vice','fascism','communism','anarchist','monarchy','democracy','capitalist','socialism','socialist','national','coup','assassinate','assassination','assassinated','portuguese','portugees','french','spanish','europe','africa','militaristic','militarise','militarize','conscription','workcamps','resource','resources','recourses','infrastructure','corruption','transportation','homeless','shelters','radioactive','citizens','population','germany','britain','morocco','monaco','fascist','communist','uk','sas','portugese','throats'
}
bad=[]
pat = re.compile(r'^(\s*(vc|n|p|na)\s+"[^"]*"|\s*"[A-Za-z][^"]*"\s*:)')
for i,l in enumerate(lines,1):
    if pat.search(l):
        for w in re.findall(r"[A-Za-z']+", l):
            wl = w.lower()
            if wl not in sc.word_frequency and wl not in ignore and len(wl) > 2:
                bad.append((i, w, l.strip()))
print('BAD_COUNT', len(bad))
for item in bad[:500]:
    print(item)

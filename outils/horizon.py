# Que donne le modèle si on prolonge la boucle de tours au lieu d'extrapoler ?
T0, TCRE = 1.0, 0.00058
BDEF=[]
import re
src=open('HEAT_jeu_v0.4.html',encoding='utf-8').read()
m=re.search(r'const BDEF=\[(.*?)\n\];',src,re.S)
blk=m.group(1)
for b in re.finditer(r'\{k:"(\w+)".*?e:([\d.]+).*?g:(-?[\d.]+)',blk):
    BDEF.append({'k':b.group(1),'e':float(b.group(2)),'g':float(b.group(3))})
print("blocs:",[(b['k'],b['e'],b['g']) for b in BDEF])
def run(nturns,ypt,contr=0):
    bl=[dict(b) for b in BDEF]; cum=0
    for t in range(1,nturns+1):
        em=0
        for b in bl:
            g=b['g']*(0.90**(t-1))
            red=(min(contr,100)/100)**0.8*0.48
            nx=max(0.05,b['e']*(1+g)*(1-red))
            em+=(b['e']+nx)/2; b['e']=nx
        cum+=em*ypt
    return round(T0+TCRE*cum,3), round(sum(b['e'] for b in bl),1)
for lab,n,y in [("actuel 8x5 -> 2055",8,5),
                ("17x5 -> 2100",17,5),
                ("8x5 puis 4x10 (2100)",None,None),
                ("16x2.5 -> 2055",16,2.5),
                ("20x2.5 -> 2065",20,2.5)]:
    if n: print(lab, run(n,y))
# variante à pas variable
def run_var(pas,contr=0):
    bl=[dict(b) for b in BDEF]; cum=0
    for t,y in enumerate(pas,1):
        em=0
        for b in bl:
            g=b['g']*(0.90**(t-1))
            red=(min(contr,100)/100)**0.8*0.48
            nx=max(0.05,b['e']*(1+g)*(1-red))
            em+=(b['e']+nx)/2; b['e']=nx
        cum+=em*y
    return round(T0+TCRE*cum,3), round(sum(b['e'] for b in bl),1)
print("8x5 puis 5x9 (2015-2100, 13 tours)", run_var([5]*8+[9]*5))
print("12x5 puis 5x5 = 17x5", run_var([5]*17))
for c in (0,20,40,60,80):
    print("  contrainte figee",c,"-> 17x5:",run(17,5,c))

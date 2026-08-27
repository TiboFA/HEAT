import re
T0,TCRE=1.0,0.00058
src=open('HEAT_jeu_v0.4.html',encoding='utf-8').read()
BD=[]
m=re.search(r'const BDEF=\[(.*?)\n\];',src,re.S)
for b in re.finditer(r'\{k:"(\w+)".*?e:([\d.]+),g:(-?[\d.]+)',m.group(1)):
    BD.append({'k':b.group(1),'e':float(b.group(2)),'g':float(b.group(3))})
YPT=5; N=17
def sim(decay,rmax,contr=0,nt=N):
    bl=[dict(x) for x in BD]
    for b in bl: b['gy']=(1+b['g'])**(1/YPT)-1
    cum=0; traj=[]
    for t in range(1,nt+1):
        em=0
        for b in bl:
            gy=b['gy']*decay**((t-1)*YPT)
            ry=(min(contr,100)/100)**0.8*rmax
            nx=max(0.02,b['e']*((1+gy)*(1-ry))**YPT)
            em+=(b['e']+nx)/2; b['e']=nx
        cum+=em*YPT; traj.append((2015+t*YPT,round(sum(x['e'] for x in bl),1),round(T0+TCRE*cum,2)))
    return round(T0+TCRE*cum,3), traj
print("cible cum 2100 sans action :", round((3.48-1.0)/TCRE))
for d in (0.9791,0.96,0.95,0.945,0.94,0.93,0.92,0.90):
    T,_=sim(d,0)
    print(f"  decay/an {d}  ->  T2100 sans action {T}")

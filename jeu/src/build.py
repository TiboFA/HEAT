import sys
parts=[open(f,encoding='utf-8').read() for f in ['a_head.html','b_css.txt','c_body.html','d_js.txt','e_tail.html']]
h='\n'.join(parts)
open('HEAT_jeu_v0.10.html','w',encoding='utf-8').write(h)
print(len(h))

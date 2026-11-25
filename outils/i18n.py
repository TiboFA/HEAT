# Traduction anglaise de HEAT, au moment du build.
#
# Le jeu reste écrit en français dans jeu/src/. Ce module repère, sans rien
# exécuter, chaque morceau de texte destiné au joueur :
#   - dans le JS : le contenu des chaînes "…", '…', et les parties fixes des
#     gabarits `…${…}…` (les ${…} sont parcourus récursivement), plus les
#     expressions régulières qui portent du texte ;
#   - dans le HTML : les blocs de texte (avec leurs balises de mise en forme
#     <b>, <i>, <a>…) et les attributs lisibles (data-tip, title, aria-label…).
# Chaque morceau est cherché tel quel dans jeu/i18n/en.json (français → anglais)
# et remplacé. Les mêmes mots donnent toujours la même traduction : une chaîne
# comparée ailleurs dans le code (familles de leviers, raisons d'injouabilité)
# reste cohérente avec elle-même.
#
#   python3 outils/i18n.py extraire   met à jour en.json (nouvelles clés vides)
#                                     et liste ce qui manque
#   python3 outils/i18n.py manque     liste les morceaux sans traduction
import json, pathlib, re, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
SRC = RACINE / "jeu" / "src"
DICO = RACINE / "jeu" / "i18n" / "en.json"

ACC = "àâäçéèêëîïôöûùüÿœæÀÂÄÇÉÈÊËÎÏÔÖÛÙÜŸŒÆ«»"
MOTS = set("""le la les des du de un une et est sont pour sur par avec dans au aux en ce cette ces qui que ne pas plus
vous votre vos il elle ils elles son sa ses leur leurs tour tours bloc blocs levier leviers mais ou où si sans tout
toute tous rien chaque fois deux trois quatre jamais encore aussi comme entre moins après avant depuis quand""".split())
# mots isolés qui sont du code et non du texte
CODE = set("""actif att attr lev bloc glob blk hand mouse touch Enter Escape Tab ArrowLeft ArrowRight ArrowUp ArrowDown
auto demo hyb hasard histoire perdu contr reel percu fric fr tech prix alerte resol exode g r t a th sh adv h la de""".split())

# morceaux courts que la détection ne verrait pas, mais qui sont du texte
FORCE = {"Investissement d'infrastructure", "▾ replier", "▸ déplier", "▸ régler", "voir l'essentiel", "renforcé de", "réduit de", "Climato-actif", "climato-actif", "Climato-attentiste", "climato-attentiste", " à ", "AN", "AL", "Lanceur d'alerte", "afficher", "masquer", "replier", "attribuer", "jouer", "suivant", "tenu", "rempli", "gratuit", "mondial", "neutre", "jouable", "ouvert", "inconnue", "politique", "contrainte", "plafond", "sondage", "agences", "contraindre", "inciter", "aucune", "nier", "retarder", "attiser", "rassurer", "combinaison", "greenwashing", "agribashing", "whataboutisme", "sous ", "reste ", "maximum ", " et ", " ou ", " le ", " la ", " les ", " de ", " des ", " du ", " en ", " sur ", " d'avance"}
def francais(s):
    if s in FORCE: return True
    if s in CODE: return False
    t = s.strip()
    if not re.search(r"[A-Za-z%s]{2,}" % ACC, t): return False
    if t in CODE: return False
    if any(c in ACC for c in t): return True
    mots = re.findall(r"[A-Za-z%s']+" % ACC, t.lower())
    if any(m.split("'")[-1] in MOTS or m in MOTS for m in mots): return True
    # un mot seul avec majuscule : nom de bloc, de niveau, de famille
    if re.fullmatch(r"[A-Z][a-z]+(?: [A-Za-z][a-z]+)*", t) and t not in CODE: return True
    return False

# ---------------------------------------------------------------- JS
def scan_js(src, i=0, fin=None, prof=0):
    """Rend [(début, fin, nature, contenu)] pour chaque chaîne ou partie fixe
    de gabarit. Si fin vaut '}', s'arrête à l'accolade fermante de niveau 0."""
    out = []; n = len(src); acc = 0; dernier = ""
    while i < n:
        c = src[i]
        if c == "/" and src.startswith("//", i):
            i = src.index("\n", i) if "\n" in src[i:] else n; continue
        if c == "/" and src.startswith("/*", i):
            i = src.index("*/", i) + 2; continue
        if c in "\"'":
            j = i + 1
            while src[j] != c:
                j += 2 if src[j] == "\\" else 1
            out.append((i + 1, j, c, src[i + 1:j])); i = j + 1; dernier = "x"; continue
        if c == "`":
            j = i + 1; deb = j
            while True:
                if src[j] == "\\": j += 2; continue
                if src[j] == "`":
                    out.append((deb, j, "`", src[deb:j])); i = j + 1; break
                if src.startswith("${", j):
                    out.append((deb, j, "`", src[deb:j]))
                    sous, j = scan_js(src, j + 2, "}", prof + 1)
                    out += sous; deb = j; continue
                j += 1
            dernier = "x"; continue
        if c == "/" and (dernier in "(,=:[!&|?{};+-*%<>~^" or re.search(r"\b(return|typeof|case)\s*$", src[max(0, i - 8):i])):
            j = i + 1; cl = False; ok = True
            while True:
                if j >= n or src[j] == "\n": ok = False; break   # une division, pas une expression régulière
                if src[j] == "\\": j += 2; continue
                if src[j] == "[": cl = True
                elif src[j] == "]": cl = False
                elif src[j] == "/" and not cl: break
                j += 1
            if ok:
                out.append((i + 1, j, "/", src[i + 1:j])); i = j + 1
                while i < n and src[i].isalpha(): i += 1
                dernier = "x"; continue
        if fin == "}":
            if c == "{": acc += 1
            elif c == "}":
                if acc == 0: return out, i + 1
                acc -= 1
        if not c.isspace(): dernier = c
        i += 1
    return (out, i) if fin else out

def norm_js(raw, q):
    return raw.replace("\\" + q, q) if q in "\"'" else raw

def esc_js(txt, q):
    if q in "\"'": return re.sub(r"(?<!\\)" + re.escape(q), "\\" + q, txt)
    if q == "`": return txt.replace("`", "\\`")
    return txt

# ---------------------------------------------------------------- HTML
INLINE = "b|i|em|strong|u|a|br|small|kbd|sup|sub|code|span"
ATTRS = ("data-tip", "title", "aria-label", "alt", "placeholder", "content")
def scan_html(src):
    out = []
    # attributs lisibles
    for m in re.finditer(r'\b(%s)="([^"]*)"' % "|".join(ATTRS), src):
        out.append((m.start(2), m.end(2), "attr", m.group(2)))
    # blocs de texte : entre deux balises de bloc, balises en ligne comprises.
    # Les <svg> et <style>/<script> sont ignorés.
    masque = [False] * len(src)
    for m in re.finditer(r"<(svg|style|script)\b.*?</\1>", src, re.S):
        for k in range(m.start(), m.end()): masque[k] = True
    tags = [m for m in re.finditer(r"<[^>]+>", src)]
    def inline(t):
        return re.match(r"</?(%s)\b" % INLINE, t.group(0)) and "class=\"lnk\"" not in t.group(0) and " id=" not in t.group(0)
    k = 0; deb = None
    bornes = []
    pos = 0
    for t in tags + [None]:
        fin = t.start() if t else len(src)
        if t is None or not inline(t):
            # le segment [pos, fin) : du texte et des balises en ligne
            seg = src[pos:fin]
            if seg.strip() and not masque[pos] and re.search(r"[A-Za-z%s]" % ACC, re.sub(r"<[^>]+>", "", seg)):
                g = len(seg) - len(seg.lstrip()); d = len(seg.rstrip())
                out.append((pos + g, pos + d, "html", seg[g:d]))
            pos = t.end() if t else len(src)
    return out

def morceaux():
    """Tous les morceaux traduisibles, par fichier : {fichier: [(deb, fin, nature, clé)]}."""
    res = {}
    for f in ("a_head.html", "c_body.html"):
        src = (SRC / f).read_text(encoding="utf-8")
        res[f] = [(a, b, k, s) for a, b, k, s in scan_html(src) if francais(re.sub(r"<[^>]+>", " ", s) if k == "html" else s)]
    src = (SRC / "d_js.txt").read_text(encoding="utf-8")
    l = []
    for a, b, q, raw in scan_js(src):
        s = norm_js(raw, q)
        if francais(s): l.append((a, b, q, s))
    res["d_js.txt"] = l
    return res

VER = re.compile(r"v\d+(?:\.\d+)+")
def cle(s):
    """La clé du dictionnaire : le numéro de version est remplacé par {V}, pour
    qu'une nouvelle version ne rende pas la phrase orpheline."""
    return VER.sub("{V}", s)

def charger():
    return json.loads(DICO.read_text(encoding="utf-8")) if DICO.exists() else {}

PONCT = (("« ", "“"), (" »", "”"), ("«", "“"), ("»", "”"), (" :", ":"), (" ;", ";"), (" ?", "?"), (" !", "!"), (" %", "%"))
def ponctuation(s):
    """Un fragment sans lettres ne porte que de la typographie : on passe aux
    guillemets et aux espaces anglais. Rend None s'il n'y a rien à changer."""
    if re.search(r"[A-Za-z%s]" % ACC.replace("«", "").replace("»", ""), s): return None
    r = s
    for a, b in PONCT: r = r.replace(a, b)
    r = r.replace("“ ", "“").replace(" ”", "”")
    return r if r != s else None

def chercher(dico, s):
    en = dico.get(cle(s))
    if not en: return ponctuation(s)
    if en == "=": return s                      # identique en anglais
    v = VER.search(s)
    if v: en = en.replace("{V}", v.group(0))
    # les espaces en bord de morceau sont ceux du français : ils collent les
    # morceaux entre eux et aux valeurs calculées
    g = s[:len(s) - len(s.lstrip())]; d = s[len(s.rstrip()):]
    en = en.strip()
    if en[:1] in ":;?!%,." and g.endswith(" "): g = g[:-1]   # pas d'espace devant la ponctuation anglaise
    if en.endswith("“") and d.startswith(" "): d = d[1:]       # ni à l'intérieur des guillemets
    if en.startswith("”") and g.endswith(" "): g = g[:-1]
    return g + en + d

def traduire(f, src, dico, manque):
    """Le fichier f traduit. Les morceaux sans traduction restent en français
    et sont ajoutés à manque."""
    if f == "d_js.txt":
        ms = [(a, b, q, norm_js(raw, q)) for a, b, q, raw in scan_js(src)]
    else:
        # un bloc de texte peut contenir des attributs (data-tip d'un <span>) :
        # on garde le bloc entier, sa traduction porte aussi les attributs
        ms = sorted(scan_html(src), key=lambda m: (m[0], -m[1]))
    out = []; pos = 0
    for a, b, q, s in ms:
        if a < pos: continue                      # contenu dans un morceau déjà traité
        en = chercher(dico, s)
        if not en:
            if (f == "d_js.txt" and francais(s)) or (f != "d_js.txt" and francais(re.sub(r"<[^>]+>", " ", s) if q == "html" else s)):
                manque.append(s)
            continue
        out.append(src[pos:a]); out.append(esc_js(en, q) if f == "d_js.txt" else en); pos = b
    out.append(src[pos:])
    return "".join(out)

def construire_en(parts):
    """Les cinq morceaux, traduits. Rend (html, liste des morceaux manquants)."""
    dico = charger(); manque = []
    noms = ['a_head.html', 'b_css.txt', 'c_body.html', 'd_js.txt', 'e_tail.html']
    out = []
    for f, src in zip(noms, parts):
        if f in ("a_head.html", "c_body.html", "d_js.txt"): src = traduire(f, src, dico, manque)
        out.append(src)
    h = "\n".join(out)
    # ce qui n'est pas du texte mais dépend de la langue
    for a, b in (('<html lang="fr"', '<html lang="en"'),
                 ('const LANG="fr";', 'const LANG="en";'),
                 ('function fr(v,n){return v.toFixed(n).replace(".",",");}', 'function fr(v,n){return v.toFixed(n);}'),
                 ('function fmtP(p){ return (Math.round(p*10)/10).toString().replace(".",","); }', 'function fmtP(p){ return (Math.round(p*10)/10).toString(); }')):
        assert h.count(a) == 1, a
        h = h.replace(a, b)
    return h, sorted(set(manque))

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "manque"
    dico = charger()
    tout = morceaux()
    cles = []
    for f, l in tout.items():
        for *_, s in l:
            if cle(s) not in cles: cles.append(cle(s))
    if cmd == "extraire":
        neuf = {k: dico.get(k, "") for k in cles}
        # on garde les traductions de clés disparues : elles ne coûtent rien
        for k, v in dico.items():
            if k not in neuf and v: neuf[k] = v
        DICO.write_text(json.dumps(neuf, ensure_ascii=False, indent=1), encoding="utf-8")
        dico = neuf
    vides = [k for k in cles if not dico.get(k)]
    print("%d morceaux, %d traduits, %d à traduire, %d caractères à traduire"
          % (len(cles), len(cles) - len(vides), len(vides), sum(len(k) for k in vides)))

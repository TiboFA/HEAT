# HEAT — Note d'interface v2

**Objet :** écran de tour réorganisé autour d'une carte du monde
**Date :** 18 août 2026
**Accompagne :** `HEAT_interface_v2.html` — remplace `HEAT_interface_v1.html`

---

## 1. La disposition demandée, telle qu'elle est réalisée

```
┌──────────────────────────────────────────────────────────────┐
│ Tour · difficulté · fin de tour                              │
├──────────────────────────────────────────────────────────────┤
│ ÉVÉNEMENTS DU TOUR — trois cartes, attribution en un clic    │
├──────────────┬──────────────┬──────────────┬─────────────────┤
│ Votre        │ Vos moyens   │ Vos acquis   │ Le monde        │
│ position     │              │              │ (ou : dommages) │
├──────────────┴──────────────┴──────────────┴─────────────────┤
│ leviers │            CARTE DU MONDE              │ leviers   │
│ (2)     │   8 blocs, 3 barres verticales chacun  │ (2)       │
│ doctrine│                                        │trajectoire│
└─────────┴────────────────────────────────────────┴───────────┘
```

Tout est survolable. Les explications ne sont écrites nulle part à l'écran : elles sont dans les
infobulles. C'est ce qui permet à l'écran de rester dense sans être bavard.

## 2. La carte

Contours réels simplifiés (Natural Earth), agrégés en huit blocs, Antarctique retiré. Le fond reste
volontairement sourd — les terres sont grises, la couleur est réservée aux données. Survoler un bloc
l'éclaire ; le bloc sélectionné reste éclairci.

**Trois barres verticales par bloc**, sur un cartouche semi-opaque ancré au centre du bloc :

| Barre | Remplissage | Ce qu'elle dit |
|---|---|---|
| **R** — soutien réel | plein, vert d'eau | lent, insensible aux campagnes adverses ; détermine ce qui tiendra |
| **P** — soutien perçu | contour hachuré, jaune | volatile ; détermine ce que les décideurs osent faire ce tour-ci |
| **F** — friction | plein, ambre puis rouge | s'accumule à chaque mesure non compensée ; au-delà du seuil, retour de flamme |

Trois remplissages distincts, trois libellés : la lecture ne dépend jamais de la couleur seule. Le
bandeau **⚠ RETOUR DE FLAMME** apparaît sous le cartouche du bloc concerné — sobre, sans clignotement,
conformément au principe 6.

L'écart R/P se voit d'un coup d'œil sur les huit blocs simultanément. C'était impossible avec la liste
de la v1 : c'est le vrai gain de la carte.

## 3. Ce qui a changé par rapport à la v1

- La liste de blocs devient la carte, avec des barres verticales au lieu d'horizontales.
- Les événements passent en haut, en bandeau, et deviennent **trois** au lieu d'un — dont un événement
  favorable au camp actif (baisse du coût du solaire), pour que le bandeau ne soit pas un flux de mauvaises nouvelles.
- Le tableau de bord passe en quatre colonnes au-dessus de la carte. Sa quatrième colonne change selon
  le camp : *Le monde* pour l'actif, *Dommages subis* pour l'attentiste.
- Les leviers encadrent la carte, deux à gauche, deux à droite.
- La doctrine (couche 2) occupe le bas de la colonne gauche, la trajectoire avec ligne fantôme le bas de
  la colonne droite. Elle est réduite mais toujours présente : le principe 3 tient.
- Toutes les explications passent par des infobulles, y compris sur les tuiles du tableau de bord et sur
  la légende.

## 4. Points à trancher

**Le cartouche masque la carte.** Huit cartouches occupent une part réelle de la surface. Alternatives à
tester : les réduire à trois barres nues sans cadre, avec le nom du bloc seulement au survol ; ou les
sortir en couronne autour de la carte avec un trait de rappel. Je garderais le cartouche : lisible tout
de suite, et le nom du bloc compte.

**La friction sur la même échelle que l'opinion.** R, P et F sont sur 100, ce qui est commode
visuellement mais mélange deux natures. Si l'écart gêne au test, séparer F sous forme de jauge fine sous
le cartouche.

**Le fond de carte.** Il est neutre aujourd'hui. On pourrait le colorer par émissions par habitant, par
dépendance à la rente fossile ou par exposition aux dommages — mais toute couleur de fond entrera en
compétition avec les barres. À réserver à un mode d'affichage optionnel.

## 5. Prochaine étape

Le test reste le même : trois personnes extérieures au projet, une consigne — *« explique-moi ce que tu
peux faire ce tour-ci, et ce que ça va produire »*. Avec la carte, une question s'ajoute : *« quel bloc
te préoccupe le plus, et pourquoi ? »* Si la réponse ne mentionne ni l'écart R/P ni la friction, les
barres sont mal calibrées.

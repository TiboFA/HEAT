# HEAT — version jouable v0.16.2

## v0.16.2 — la fiche de levier passe au style filaire

- **Une carte filaire, pour un levier de bloc de votre camp**, en tête de « Si vous le jouez maintenant » :
  - les blocs où il est jouable sont en bleu, avec la probabilité de réussite si c'est un pari, ou « jouable » ;
  - les autres sont estompés, avec leur raison : « perçu 30 / 45 », « déjà appliqué », « trop cher »…
  - le tableau bloc par bloc reste en dessous.

  Les leviers mondiaux et les leviers adverses n'ont pas de carte : il n'y a rien à cibler.
- **Le reste de la fiche** reprend le langage du plateau : intitulés de section en vert d'eau, identifiant et famille en chasse fixe, valeurs des encadrés et pourcentages de réussite en chasse fixe, bordures teintées, encadré de doctrine bordé de vert d'eau, nom adverse marqué en orange.
- **Les étiquettes des cartes filaires** (fin de partie, bilan, fiche) ont un interligne proportionnel à leur taille : à grande taille, les deux lignes ne se touchent plus.

Aucune règle ne change ; `outils/verifier.py` passe.

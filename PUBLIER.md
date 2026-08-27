# Publier une version sur GitHub

Mémo pour ce dépôt, avec GitHub Desktop. À relire à chaque livraison — la
première fois pour la mise en place, ensuite seulement pour la boucle courante.

## La boucle courante, à chaque nouvelle version

1. Ouvrir **GitHub Desktop**. Le dépôt HEAT est déjà dans la liste à gauche.
2. Les fichiers modifiés apparaissent dans la colonne de gauche, cochés.
3. En bas à gauche, écrire un **résumé** — une ligne, à l'impératif, qui dit ce
   qui change : `v0.11 — la crédibilité devient un rapport entre les deux camps`.
   Le champ « Description » en dessous accepte le détail, il est facultatif.
4. Cliquer **Commit to main**.
5. Cliquer **Push origin** en haut. C'est cette étape qui envoie sur GitHub —
   sans elle, le commit reste sur le disque.

Un commit sans push n'existe que chez toi. Un push sans commit n'existe pas.

## Mise en place, une seule fois

### 1. Le compte

Créer un compte sur [github.com](https://github.com) si ce n'est pas fait.
Un dépôt **public** est visible de tous et gratuit ; un dépôt **privé** l'est
aussi, sur un compte personnel.

### 2. GitHub Desktop

Télécharger depuis [desktop.github.com](https://desktop.github.com/), installer,
puis se connecter : **File → Options → Accounts → Sign in**. L'authentification
passe par le navigateur — GitHub Desktop ouvre une page, on valide, la fenêtre se
referme toute seule. Il n'y a pas de mot de passe à saisir dans l'application, et
pas de jeton à fabriquer.

Dans **File → Options → Git**, vérifier que le nom et l'adresse e-mail sont ceux
du compte GitHub. C'est ce qui rattache les commits au profil.

### 3. Déclarer le dépôt

Le dossier de ce dépôt contient déjà un `.git` : il est un dépôt Git complet,
avec son historique. Il ne faut donc pas en créer un nouveau, mais déclarer
celui-ci.

**File → Add local repository…**, désigner le dossier, **Add repository**.

### 4. Le publier

Bouton **Publish repository** en haut de la fenêtre.

- **Name** : le nom qu'aura le dépôt sur GitHub. `heat` convient.
- **Description** : une ligne.
- **Keep this code private** : décoché pour un dépôt public.

**Publish repository**. Le dépôt est créé sur GitHub et le contenu envoyé dans
la foulée. Ensuite, **Repository → View on GitHub** ouvre la page.

## Reconstruire le jeu après avoir modifié les sources

```
cd jeu/src
python3 build.py
```

Le fichier produit est à déplacer dans `jeu/`. Avant de le publier, faire
tourner au minimum `outils/play3.py` et `outils/calib3.py` — voir le README.

## Ce qui ne doit pas entrer dans le dépôt

`.gitignore` écarte déjà les captures d'écran des harnais (41 Mo, régénérables),
les `__pycache__` et les fichiers de sauvegarde. Si GitHub Desktop propose de
commiter des centaines de `.png`, c'est que le `.gitignore` a été perdu — ne pas
commiter, le restaurer d'abord.

## Deux réglages qui comptent, et pourquoi

**`.gitattributes` désactive la normalisation des fins de ligne** (`* -text`).
Le projet vérifie ses livraisons au md5 : un HTML construit ici doit être bit à
bit identique à celui qui arrive ailleurs. Le réglage par défaut de Git sur
Windows réécrit les fins de ligne à l'extraction et casse cette garantie sans
rien dire. Ne pas le remettre.

**La branche s'appelle `main`.** C'est le nom par défaut sur GitHub depuis 2020 ;
les tutoriels plus anciens parlent de `master`.

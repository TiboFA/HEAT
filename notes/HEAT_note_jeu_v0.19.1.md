# HEAT v0.19.1 — la main ne se réordonne plus pendant le plan

Signalé : un levier de bloc appliqué une première fois, et encore jouable sur un autre bloc, remontait en tête de la main.

Cause : en tri « jouables d'abord », l'ordre était recalculé sur l'état prévisionnel à chaque levier ajouté au plan. Le budget restant baissant, les cartes devenues trop chères partaient en fin de liste ; celles qui restaient jouables — dont le levier de bloc déjà engagé — remontaient. Les cartes changeaient de place sous la souris.

Correction : l'ordre « jouables d'abord » est lu sur l'état du début du tour, sans le plan. Pendant la planification, les cartes ne bougent plus ; celles qui deviennent injouables se grisent sur place. Au tour suivant, l'ordre est recalculé. Les tris « par puissance » et « par famille » ne dépendaient déjà pas du plan.

Testé sur quatre parties, en remplissant le plan jusqu'à épuisement du budget : ordre identique du début à la fin. Aucune règle ni donnée modifiée.

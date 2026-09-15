# Ligne éditoriale du carnet technique

Ce dépôt héberge le carnet technique de Guilhem Lettron. Ces consignes guident la
rédaction et la révision des articles. Elles sont publiques, comme le dépôt.

## Ce qu'un article doit apporter

Écrire en français pour un lectorat technique, sans supposer qu'il connaît déjà
le sujet. Expliquer les notions nécessaires au raisonnement, sans reprendre tout
depuis les bases.

Partir d'une question précise : un mécanisme à comprendre, une décision à éclairer,
une idée reçue à examiner. Le lecteur doit repartir avec une compréhension ou un
critère de décision qu'il n'aurait pas trouvé dans une introduction au projet.
La profondeur vient de l'explication, pas de la longueur ni du jargon.

## Pour les articles sur les pratiques

- Revenir sur leur histoire : quel problème les a fait émerger, dans quelles
  contraintes techniques ou organisationnelles, et avec quelles alternatives ?
  Retenir les étapes qui éclairent le raisonnement, sans imposer une chronologie
  exhaustive à chaque article.
- Expliquer pourquoi ces choix étaient raisonnables dans leur contexte, puis ce
  qui a changé. Éviter de juger les décisions passées avec les seules possibilités
  d'aujourd'hui.
- Montrer comment la pratique agit sur le problème, ce qu'elle coûte et dans
  quelles conditions elle devient moins pertinente. Une recommandation doit
  permettre de décider quand l'appliquer et quand s'en passer.
- Dépasser les évidences telles que « il faut tester » ou « il faut communiquer » :
  décrire une situation, le mécanisme en jeu et ses conséquences observables.

## Pour les articles techniques

- Aller au-delà du README et du getting started : fonctionnement interne,
  interaction entre composants, diagnostic d'un comportement surprenant ou
  conséquences d'un choix d'implémentation. Choisir l'angle utile au sujet.
- Renvoyer à la documentation pour l'installation et l'usage courant. Garder les
  étapes nécessaires pour reproduire ou comprendre la démonstration ; une suite
  de commandes qui fonctionne ne suffit pas à constituer l'article.
- Relier le code au raisonnement : ce qu'on cherche à observer, pourquoi il se
  comporte ainsi et ce que le résultat permet de conclure. Un exemple court et
  expliqué vaut mieux qu'une application complète sans analyse.
- Préciser les versions, hypothèses et conditions d'exécution lorsqu'elles
  changent le résultat. Montrer les limites ou les cas d'échec qui éclairent
  réellement le mécanisme étudié.

## Voix et construction

Adopter un ton direct, posé et curieux, comme entre collègues qui cherchent à
comprendre. Employer des mots précis, des paragraphes reliés et des exemples
concrets. Expliquer un terme spécialisé à sa première utilisation si le lectorat
risque de ne pas le connaître.

Éviter les introductions passe-partout, les promesses marketing, les titres
racoleurs et les conclusions qui répètent simplement le texte. Les titres doivent
annoncer un sujet ou une tension réelle. Une prise de position est bienvenue si
elle est argumentée et si ses limites sont explicites.

Choisir le plan selon la question traitée. L'archétype du dépôt est un point de
départ, pas un sommaire obligatoire. L'histoire et les exemples doivent faire
avancer l'explication, plutôt que remplir des rubriques.

## Sources et honnêteté

- Étayer les faits historiques et les affirmations techniques déterminantes par
  des sources vérifiées, liées près du passage concerné. Privilégier les sources
  primaires : textes d'origine, RFC, documentation, code, discussions de conception
  ou publications de l'époque.
- Distinguer fait documenté, observation, interprétation et opinion. Signaler une
  origine incertaine ou discutée ; ne pas inventer une histoire plus nette que les
  sources ne le permettent.
- Vérifier les exemples exécutables lorsque c'est possible. Présenter les sorties
  illustratives comme telles et les mesures avec leurs conditions ; ne pas laisser
  croire à une exécution ou à une expérience de production qui n'a pas eu lieu.
- Ne pas inventer de vécu au nom de l'auteur. La première personne s'appuie sur
  des éléments qu'il a fournis. Utiliser des cas publics ou des exemples fictifs
  explicitement présentés comme tels, sans exposer de données privées.

## Relire avant de proposer un article

Vérifier que le texte répond à sa question, explique le pourquoi et apporte quelque
chose au-delà de la documentation de démarrage. Si un passage pourrait être repris
tel quel dans un article sur n'importe quel autre outil ou pratique, le préciser
ou le supprimer. Si l'angle manque de matière, le resserrer plutôt que le remplir
de généralités.

Les conventions de fichiers et les commandes de prévisualisation et de
vérification du site restent dans le [README](README.md).

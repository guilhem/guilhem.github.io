---
title: "Partager du code, sans perdre le contexte"
date: 2026-09-14T10:00:00+02:00
description: "Un exemple doit pouvoir se lire, se copier et se comprendre. Le contexte et les limites font partie du code."
tags: [Bash, Markdown, Documentation]
draft: true
---

> **Article de démonstration, à adapter avant publication.** Ce brouillon permet
> de découvrir la présentation d'un article technique : code, sommaire, tableaux
> et notes. Il n'apparaît pas sur le site publié.

Une commande sortie de son contexte peut être juste et pourtant inutilisable.
Avant le premier bloc de code, quelques lignes suffisent souvent : quel problème
on cherche à résoudre, dans quel environnement et avec quel résultat attendu.

## Commencer par une commande reproductible

Prenons un petit exemple : afficher les fichiers suivis par Git dont le nom
se termine par `.md`. Le point de départ est un dépôt Git ; la commande se lance
à sa racine.

```bash
git ls-files '*.md'
```

Les guillemets comptent : ils laissent Git interpréter le motif au lieu de le
faire développer par le shell. La liste contient les fichiers suivis, y compris
dans les sous-dossiers, et ignore les fichiers qui n'ont pas encore été ajoutés à Git.

Une sortie possible, dans ce dépôt :

```text
content/about.md
content/posts/partager-du-code/index.md
```

Une sortie d'exemple aide à se repérer. Elle ne remplace pas la description de ce
que fait la commande, et elle changera avec le contenu du dépôt.

## Montrer le piège, pas seulement le chemin heureux

Dans un pipeline Bash, le statut de la dernière commande peut masquer l'échec
d'une commande précédente. On peut l'observer sans toucher à aucun fichier :

```bash
bash -c 'false | cat'; printf 'Sans pipefail : %s\n' "$?"
bash -o pipefail -c 'false | cat'; printf 'Avec pipefail : %s\n' "$?"
```

```text
Sans pipefail : 0
Avec pipefail : 1
```

`pipefail` change la manière dont Bash détermine le statut du pipeline. Il ne
suffit pas, à lui seul, à arrêter un script ou à décider comment traiter l'erreur.
Cette décision dépend de la commande et de ce qu'on veut faire après son échec.

## Rendre la configuration lisible

Les fichiers de configuration méritent le même soin. Un exemple court peut être
accompagné d'un nom de fichier et d'une explication de chaque choix.

```yaml {title="article.md"}
---
title: "Une note de terrain"
description: "Le problème et l'idée à retenir."
tags: [Documentation]
draft: true
---
```

| Élément | Ce qu'il apporte |
| --- | --- |
| Un titre précis | Le lecteur sait ce qu'il va trouver. |
| Une description courte | Le sujet est compréhensible depuis la liste des articles. |
| Quelques tags | Les notes liées sont plus faciles à retrouver. |
| Un brouillon explicite | Le texte peut être relu avant publication. |

## Laisser une trace utile

Un bon partage de code donne au lecteur assez d'éléments pour décider s'il peut
l'utiliser dans son propre contexte :

- les prérequis et les versions qui changent le comportement ;
- une entrée et une sortie compréhensibles ;
- les limites connues ;
- un lien vers la documentation qui fait autorité.

Pour cet exemple, les références sont la documentation de
[`git ls-files`](https://git-scm.com/docs/git-ls-files) et celle des
[pipelines Bash](https://www.gnu.org/software/bash/manual/html_node/Pipelines.html).

Le code reste du texte. On peut le sélectionner, le copier avec le bouton du
bloc, le comparer et l'adapter. Et le contexte reste juste à côté.

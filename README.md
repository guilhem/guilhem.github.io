# Le carnet technique de Guilhem

Blog statique en français, construit avec **Hugo** et **PaperMod**. Les articles
restent en Markdown. La personnalisation est dans `layouts/` et
`assets/css/extended/notebook.css` ; le thème amont reste un sous-module non modifié.

## Démarrer

Installer la version de Hugo indiquée dans `.hugo-version`. Le binaire standard
suffit : aucun environnement Node ni gestionnaire de paquets n'est nécessaire.

```sh
git submodule update --init --recursive
hugo server --buildDrafts
```

L'adresse locale s'affiche dans le terminal. `--buildDrafts` rend visibles les
brouillons, dont l'article de démonstration livré avec cette refonte. Sans cette
option, Hugo ne les publie pas. Il n'y a pas encore d'article publié.

## Écrire un article

```sh
hugo new content posts/mon-sujet/index.md
```

Modifier le fichier créé et placer ses images ou fichiers téléchargeables dans
le même dossier. Utiliser les liens Markdown habituels :

````markdown
![Description de l'image](schema.png)
[Télécharger le script](exemple.sh)

```bash
git status --short
```
````

Le langage du bloc active la coloration et s'affiche dans son en-tête. La copie
est fournie par PaperMod. Les blocs sans langage restent utilisables. Hugo permet
également d'ajouter un titre facultatif : `bash {title="exemple.sh"}`.

Renseigner `title`, `date`, `description` et `tags`, puis passer `draft` à `false`
lorsque l'article est prêt. Le sommaire est généré à partir des titres Markdown.
Les tags, le flux RSS et l'index de recherche sont générés pendant la compilation.

## Vérifier et publier

```sh
hugo --gc --minify --panicOnWarning
python3 scripts/check_site.py public
```

Pour vérifier aussi la présentation de l'article de démonstration :

```sh
hugo --buildDrafts --destination /tmp/guilhem-blog-preview
python3 scripts/check_site.py /tmp/guilhem-blog-preview --drafts
```

GitHub Actions compile et vérifie les pull requests. La publication sur Pages
est réservée à `master` (push ou lancement manuel depuis cette branche).
Dans les paramètres du dépôt, la source de Pages doit être **GitHub Actions**.
L'adresse de publication est `https://guilhem.github.io/`.

Les actions sont épinglées par SHA ; Dependabot propose leurs mises à jour chaque
semaine. La compilation n'a qu'un accès en lecture au dépôt ; seuls les droits
Pages et OIDC sont accordés au job de publication. Les exécutions sont regroupées
par branche ou pull request : une nouvelle révision annule la vérification
précédente de sa PR, tandis qu'une publication en cours se termine normalement.

## Entretenir et personnaliser

- Identité, menus et options du thème : `hugo.yaml`.
- Accueil : `layouts/home.html`.
- À propos : `layouts/profile.html` affiche directement `profile/README.md`, sans
  réécriture. `profile/` est un sous-module du dépôt
  [guilhem/guilhem](https://github.com/guilhem/guilhem), récupéré par le checkout
  récursif déjà utilisé en CI. Pour reprendre une nouvelle version du profil,
  lancer `git submodule update --remote profile`, relancer Hugo pour vérifier le rendu, puis
  enregistrer le nouveau pointeur du sous-module dans un commit.
- Styles : `assets/css/extended/notebook.css`.
- Hugo : modifier `.hugo-version`, utiliser cette version localement et relancer les vérifications.
- PaperMod : `git -C themes/PaperMod fetch`, choisir un commit amont, puis
  `git -C themes/PaperMod checkout <commit>`. Vérifier le rendu avant d'enregistrer
  le nouveau pointeur du sous-module.

Le thème est sous licence MIT ; son texte de licence reste dans le sous-module.
La licence existante du dépôt est conservée dans `LICENSE`.

Les templates RSS et Open Graph utilisent l'API `Locale` de Hugo actuel. Le flux
RSS est limité aux articles ; les pages de navigation et la biographie en sont exclues.

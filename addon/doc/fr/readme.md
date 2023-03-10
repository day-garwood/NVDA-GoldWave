# Goldwave #

* Auteurs : Joseph Lee, contributeurs de NVDA.
* Télécharger [version stable][1]
* NVDA compatibility: 2022.4 and later

Cette extension améliore l'accès et l'utilisation de l'éditeur audio
Goldwave.

## Raccourcis ##

* NVDA+Maj+C : Bascule l'annonce des commandes lors de l'édition audio.
* Contrôle+Maj+P : Annonce la position courante de la piste.
* NVDA+Maj+R: Annonce le temps restant pour la piste en cours d'édition.
* Contrôle+NVDA+1 : Annonce le canal en cours d'édition.
* Contrôle+NVDA+2 : Annonce la longueur totale du fichier audio.
* Contrôle+NVDA+3 : annonce un résumé des informations relatives à la
  sélection audio.
* Contrôle+NVDA+4 : Annonce le niveau de zoom.

Pour plus d'informations sur Goldwave et les commandes clavier,
reportez-vous au manuel de Goldwave.

Remarque : Nécessite GoldWave 6 ou version ultérieure.

## Version 23.02

* NVDA 2022.4 or later is required.
* Windows 10 21H2 (November 2021 Update/build 19044) or later is required.

## Version 23.01

* NVDA 2022.3 or later is required.
* Windows 10 or later is required as Windows 7, 8, and 8.1 are no longer
  supported by Microsoft as of January 2023.

## Version 22.03

* Nécessite 3 ou ultérieur.
* Un message d'avertissement s'affichera si vous installez l'extension sur
  Windows 7, 8 et 8.1.

## Version 21.10

* NVDA 2021.2 ou version ultérieure est requis en raison des modifications
  apportées à NVDA qui affectent cette extension.
* Dans GoldWave 6.57 et versions ultérieures, NVDA ne répétera plus le nom
  du fichier chargé lors de l'appui sur les touches lecture/retour
  arrière/arrêt.

## Version 21.06

* Résolution de problèmes de style de code supplémentaires et de bugs
  potentiels avec Flake8.

## Version 20.06

* Résolution de nombreux problèmes de style de code et de bugs potentiels
  avec Flake8.

## Version 20.04

* Ajout de messages d'aide pour la commande de temps restant (NVDA+Maj+R).
* La commande permettant de basculer l'annonce des commandes ((NVDA+Maj+C)
  se trouve désormais dans les gestes de commande de NVDA sous la catégorie
  Goldwave.

## Version 20.01

* Nécessite NVDA 2019.3 et supérieures.

## Version 19.11

* Windows 7 SP1, Goldwave 6.x et NVDA 2019.1 ou supérieures sont requis.
* Ajout d'un message d'aide pour la fenêtre son, (seulement accessible si
  l'extension Control Usage Assistant est installée)

## Version 18.12

* NVDA ne semblera plus ne rien faire ou n'émettra plus des sons d'erreur
  lors de l'exécution de certaines commandes GoldWave avec l'annonce de la
  commande désactivée (cela peut entraîner des comportements étranges dans
  certains cas).
* Changements internes permettant la prise en charge de futures versions de
  NVDA.

## Version 18.07

* Correction d'un problème où les zéros initiaux ne s'affichaient pas
  lorsque vous essayiez d'obtenir le temps restant pour une piste.

## Version 17.05

* Ajout de la possibilité de fournir des informations de débogage lorsque
  NVDA est en cours d'exécution avec le journal activé en mode débogage
  (NVDA 2017.1 ou version ultérieure).
* Traductions mises à jour.

## Version 16.12

* La nomenclature de version est désormais année.mois au lieu de
  majeure.mineure.

## Changements pour la version 4.0

* Le dépôt pour l'extension a été déplacé sur GitHub (se trouve désormais
  sur https://github.com/josephsl/goldwave).
* Amélioration des performances lorsque vous cherchez des informations comme
  le nom du canal et d'autres informations de statut.

## Changements pour la version 3.0

* Ajout d'une commande pour annoncer le temps restant sur la piste courante
  (NVDA+Maj+R).
* Légère amélioration dans l'annonce d'informations de statut  telles que
  les informations du canal.

## Changements pour la version 2.0

* Support pour GoldWave 6, y compris la version 64-bit de GoldWave (voir la
  note ci-dessus).
* L'aide de l'extension est désormais accessible à partir du Gestionnaire
  d'extensions (NVDA 2014.3 et versions ultérieur).
* NVDA annonce maintenant le canal sélectionné si vous appuyez sur les
  commandes de sélection de canaux tels que Ctrl+Maj+L pour le canal gauche.
* Divers problèmes avec les zones d'édition numérique comme le détecteur de
  zone et le sélecteur de temps dans la boîte de dialogue du mélangeur a été
  corrigé, y compris la sélection de texte, mise à jour des valeurs et ainsi
  de suite.
* Le paramètre d'annonce de commande sera mémorisé lors du basculement vers
  d'autres programmes.

## Changements pour la version 1.2

* Correction d'un problème où NVDA avait des Difficultés à annoncer
  certaines zones d'édition.
* Traductions nouvelles et mises à jour.
* Veuillez noter qu'en raison de changements récents dans NVDA, la sélection
  audio et le statut d'autres commandes peuvent ne pas fonctionner comme
  prévu sur certains systèmes.

## Changements pour la version 1.1

* Prise en charge des annonces de message en braille.
* Le résumé de la Sélection audio est présentée dans les langues autres que
  l'anglais.
* Autres annonces de commande ajoutés y compris le mouvement de la position
  du point de repère et les opérations supprimer/couper.
* Correction d'un problème dans les zones d'édition numérique comme les
  divers effets  des boîtes de dialogues où rien ou le mauvais nom de la
  zone était annoncé.
* Traductions nouvelles et mises à jour.

## Changements pour la version 1.0

* Première version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=goldwave

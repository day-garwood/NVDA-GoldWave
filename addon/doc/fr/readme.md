# GoldWave #

* Auteurs : Joseph Lee, contributeurs de NVDA.
* Télécharger [version stable][1]
* Télécharger [version de développement][2]
* NVDA compatibility: 2019.3 to 2020.3

This app module enhances access and usage of GoldWave audio editor.

## Raccourcis ##

* NVDA+Shift+C: Toggles speaking of commands during audio editing.
* Contrôle+Maj+P : Annonce la position actuelle de la piste.
* NVDA+Maj+R: Annonce le temps restant de la piste que vous êtes
  actuellement en train de modifier.
* Contrôle+NVDA+1 : Annonce le canal que vous êtes en train de modifier.
* Contrôle+NVDA+2 : Annonce la longueur totale du fichier audio.
* Control+NVDA+3: announces a summary on audio selection information.
* Contrôle+NVDA+4 : Annonce le niveau de zoom.

For more information about GoldWave and keyboard commands, refer to GoldWave
Manual.

Note: GoldWave 6 requires 64-bit version of Windows 7 or later. To use this
add-on, NVDA 2019.3 or later is required.

## Version 20.06

* Resolved many coding style issues and potential bugs with Flake8.

## Version 20.04

* Added input help messages for remainig time command (NVDA+Shift+R).
* Toggle command announcement command (NVDA+Shift+C) will now show up under
  "GoldWave" category in NVDA's input gestures dialog.

## Version 20.01

* Requires NVDA 2019.3 or later.

## Version 19.11

* Windows 7 SP1, GoldWave 6.x, and NVDA 2019.1 or later is required.
* Added help message for sound window (accessible if Control Usage Assistant
  add-on is installed).

## Version 18.12

* NVDA will no longer appear to do nothing or play error tones when
  performing certain GoldWave commands with command announcement set to off
  (this may result in odd behaviors in some cases).
* Internal changes to support future NVDA releases.

## Version 18.07

* Fixed an issue where leading zeroes would not be displayed when trying to
  obtain remaining time for a trakc.

## Version 17.05

* Ajout de la possibilité de fournir des informations de débogage lorsque
  NVDA est en cours d'exécution avec le journal activé en mode débogage
  (NVDA 2017.1 ou version ultérieure).
* Traductions mises à jour.

## Version 16.12

* La version système est maintenant year.month au lieu de major.minor.

## Changements pour la version 4.0

* Le référentiel de l'extension a été déplacé à GitHub (maintenant localisé
  à https://github.com/josephsl/goldwave).
* Amélioration des performances lorsque vous cherchez des informations comme
  le nom du canal et d'autres informations du statut.

## Changements pour la version 3.0

* Added a command to announce remaining time for the current track
  (NVDA+Shift+R).
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

* prise en charge des annonces de message en braille.
* le résumé de la Sélection audio est présentée dans des langues autres que
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

[1]: https://addons.nvda-project.org/files/get.php?file=gwv

[2]: https://addons.nvda-project.org/files/get.php?file=gwv-dev

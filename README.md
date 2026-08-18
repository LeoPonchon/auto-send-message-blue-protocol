# Blue Protocol — Guild Invite Auto Sender

Petit outil d'automatisation Windows en Python pour envoyer un message de recrutement de guilde dans **Blue Protocol: Star Resonance** en parcourant plusieurs mondes/canaux via l'interface du jeu.

Le script pilote l'interface avec `pyautogui`, détecte les boutons à partir des captures d'écran stockées dans le dépôt, colle le texte via le presse-papiers et ajoute des délais/offsets légers entre les actions.

> **Important :** l'automatisation d'un client de jeu peut être interdite ou limitée par les règles du jeu. Vérifiez les conditions d'utilisation applicables avant de l'utiliser.

## Fonctionnement

Le script :

1. recherche la fenêtre `Blue Protocol: Star Resonance` ;
2. ouvre l'interface ciblée avec la touche `J` ;
3. détecte les boutons de monde à partir des fichiers `WORLD_*.png` ;
4. sélectionne successivement les mondes configurés ;
5. colle le message de recrutement ;
6. valide l'envoi puis passe au monde suivant.

## Prérequis

- Windows
- Python 3
- le jeu lancé en mode/fenêtre compatible avec les captures d'écran du dépôt
- une interface suffisamment proche de celle utilisée lors de la création des images de référence

Installez les dépendances :

```bash
pip install pyautogui keyboard pyperclip pygetwindow pillow
```

## Utilisation

Clonez le dépôt :

```bash
git clone https://github.com/LeoPonchon/auto-send-message-blue-protocol.git
cd auto-send-message-blue-protocol
```

Avant de lancer le script, vérifiez le message à envoyer et les paramètres directement dans `auto_send_guild_invite.py`.

Puis :

```bash
python auto_send_guild_invite.py
```

Gardez la fenêtre du jeu accessible pendant l'exécution et évitez d'utiliser souris/clavier en parallèle.

## Images de référence

Les fichiers `WORLD_0.png` à `WORLD_9.png`, ainsi que `WORLD_BUTTON.png`, `WORLD_OK.png`, `WORLD_DEL.png` et `WORLD_PLEASE_ENTER_TEXT.png`, servent à la reconnaissance visuelle de l'interface.

Si l'UI du jeu, la langue, la résolution ou l'échelle Windows change, il peut être nécessaire de refaire ces captures.

## Limites

- automatisation basée sur la position et la reconnaissance d'images ;
- sensible aux changements d'interface ;
- conçu pour Windows ;
- ne fournit aucune garantie contre les limitations anti-spam ou les règles du jeu.

import pyautogui
import keyboard
import pyperclip
import time
import pygetwindow as gw
import random
import math

# Temps d'attente pour laisser respirer le script entre les actions
DELAY = 0.4

# Message à envoyer dans chaque canal
GUILD_MESSAGE = "✦ A S T R A L I S ✧ [EU] ✦ Guilde Lv.3 ✧ 18+ ✦ ID : 3469010 ✧ Discord : 9k9JfWhhnq ✦ Rejoins nous pour accomplir donjons et raids !"


def switch_to_blue_protocol():
    """Trouve et active la fenêtre Blue Protocol: Star Resonance"""
    # Recherche exacte du titre
    exact_title = "Blue Protocol: Star Resonance"

    windows = gw.getWindowsWithTitle(exact_title)
    if windows:
        window = windows[0]
        window.activate()
        time.sleep(0.2)
        print(f"✅ Fenêtre trouvée et activée : {window.title}")
        return True

    # Si aucune fenêtre trouvée par titre exact, chercher dans toutes les fenêtres
    try:
        all_windows = gw.getAllWindows()
        for window in all_windows:
            if window.title and window.title == exact_title:
                window.activate()
                time.sleep(0.2)
                print(f"✅ Fenêtre trouvée et activée : {window.title}")
                return True
    except Exception as e:
        print(f"[!] Erreur lors de la recherche de fenêtre : {e}")

    print(f"[!] Fenêtre '{exact_title}' non trouvée. Arrêt du script.")
    return False


def human_like_mouse_move(x, y, duration=None):
    """Déplace la souris de manière naturelle avec une courbe fluide et rapide"""
    current_x, current_y = pyautogui.position()

    if duration is None:
        # Durée aléatoire basée sur la distance (plus rapide)
        distance = math.sqrt((x - current_x) ** 2 + (y - current_y) ** 2)
        duration = random.uniform(0.15, 0.4) + (distance / 2000) * random.uniform(
            0.3, 0.8
        )

    # Mouvement direct fluide avec pyautogui (gère déjà l'easing naturel)
    pyautogui.moveTo(x, y, duration=duration)

    # Délai minimal après le mouvement
    time.sleep(random.uniform(0.02, 0.05))


def random_delay(min_seconds, max_seconds):
    """Attend un délai aléatoire entre min et max secondes"""
    delay = random.uniform(min_seconds, max_seconds)
    time.sleep(delay)
    return delay


def click_image(image_name, confidence=1):
    """Trouve une image à l'écran et clique dessus avec mouvement naturel"""
    pos = pyautogui.locateCenterOnScreen(image_name, confidence=confidence)
    if pos:
        # Ajouter un petit offset aléatoire pour ne pas cliquer exactement au centre
        offset_x = random.randint(-3, 3)
        offset_y = random.randint(-3, 3)
        target_x = pos[0] + offset_x
        target_y = pos[1] + offset_y

        # Déplacer la souris de manière naturelle
        human_like_mouse_move(target_x, target_y)

        # Petit délai avant le clic (réduit)
        random_delay(0.03, 0.1)

        # Clic avec durée aléatoire (plus rapide)
        click_duration = random.uniform(0.03, 0.08)
        pyautogui.click(target_x, target_y, duration=click_duration)

        # Délai aléatoire après le clic (réduit)
        random_delay(DELAY * 0.5, DELAY * 0.8)
        return True
    else:
        print(f"[!] Image non trouvée : {image_name}")
        return False


def main():
    print("Démarrage du script dans 3 secondes...")
    time.sleep(3)

    # Basculement vers la fenêtre Blue Protocol
    print("Basculement vers Blue Protocol...")
    if not switch_to_blue_protocol():
        print("❌ Impossible de trouver la fenêtre Blue Protocol. Script annulé.")
        return

    # Appuie sur J pour ouvrir le menu
    random_delay(0.1, 0.3)
    keyboard.press_and_release("j")
    random_delay(DELAY * 0.5, DELAY * 0.8)

    # Pour chaque monde de 1 à 9
    for i in range(1, 10):
        print(f"--- Monde {i} ---")

        # Délai aléatoire avant chaque changement de monde (entre 1.0 et 1.8 secondes)
        delay_before_world = random.uniform(1.0, 1.8)
        print(
            f"Attente de {delay_before_world:.1f} secondes avant le changement de monde..."
        )
        time.sleep(delay_before_world)

        if not click_image("WORLD_BUTTON.png"):
            continue
        if not click_image(f"WORLD_{i}.png"):
            continue
        if not click_image("WORLD_OK.png"):
            continue
        if not click_image("WORLD_PLEASE_ENTER_TEXT.png"):
            continue

        # Copie le message dans le presse-papiers et le colle
        pyperclip.copy(GUILD_MESSAGE)
        random_delay(0.1, 0.2)  # Délai aléatoire pour s'assurer que le texte est copié

        # Collage avec délai aléatoire entre les touches
        pyautogui.keyDown("ctrl")
        random_delay(0.02, 0.08)
        pyautogui.press("v")
        random_delay(0.02, 0.08)
        pyautogui.keyUp("ctrl")

        # Délai aléatoire après le collage
        random_delay(DELAY * 0.5, DELAY * 0.8)

        # Appuie sur Entrée avec délai aléatoire
        random_delay(0.15, 0.3)
        keyboard.press_and_release("enter")
        random_delay(DELAY * 0.5, DELAY * 0.8)

    # Ferme le menu à la fin
    random_delay(0.1, 0.3)
    keyboard.press_and_release("j")
    print("✅ Script terminé")


if __name__ == "__main__":
    main()

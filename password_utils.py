import re

MIN_LENGTH = 8

def check_password_strength(password: str):
    score = 0
    reasons = []

    if len(password) >= MIN_LENGTH:
        score += 1
    else:
        reasons.append(f"Longueur insuffisante minimum {MIN_LENGTH} caracteres")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        reasons.append("Aucune lettre minuscule")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        reasons.append("Aucune lettre majuscule")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        reasons.append("Aucun chiffre")

    if re.search(r"[^a-zA-Z0-9]", password):
        score += 1
    else:
        reasons.append("Aucun caractere special")

    common_weak = [
        "password",
        "123456",
        "admin",
        "azerty",
        "qwerty",
        "motdepasse",
    ]
    if password.lower() in common_weak:
        reasons.append("Mot de passe tres commun")
        score = 0

    if score >= 4:
        level = "Fort"
    elif score >= 2:
        level = "Moyen"
    else:
        level = "Faible"

    return level, score, reasons

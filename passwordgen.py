import random
import string

def generate_password(length=12, lowercase=True, uppercase=True, numbers=True, symbols=True):
    pools = []
    if lowercase:
        pools.append(string.ascii_lowercase)
    if uppercase:
        pools.append(string.ascii_uppercase)
    if numbers:
        pools.append(string.digits)
    if symbols:
        pools.append("!@#$%^&*()-_=+[]{};:,.<>?/|")

    if not pools:
        return "Please select at least one option!"

    # guarantee at least one from each selected pool
    password_chars = [random.choice(pool) for pool in pools]

    # fill the rest from all pools combined
    all_chars = "".join(pools)
    remaining = length - len(password_chars)
    password_chars += random.choices(all_chars, k=remaining)

    # shuffle to avoid predictable order
    random.shuffle(password_chars)

    return "".join(password_chars)

def rate_password(password: str):
    has_lower = any(c in string.ascii_lowercase for c in password)
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_num   = any(c.isdigit() for c in password)
    has_sym   = any(c in "!@#$%^&*()-_=+[]{};:,.<>?/|" for c in password)

    # Check strength
    if has_lower and has_upper and has_num and has_sym and len(password) >= 12:
        return "Strong Password", "strong"
    elif (has_lower and has_upper and has_num) or (has_upper and has_num and has_sym):
        return "Moderate Password", "moderate"
    else:
        return "Weak Password", "weak"

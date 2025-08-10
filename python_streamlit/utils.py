def format_number(value, prefix=''):
    for unit in["", "mil"]:
        if abs(value) < 1000:
            return f"{prefix}{value:.2f}{unit}"
        value /= 1000
    return f"{prefix}{value:.2f}Millhões"
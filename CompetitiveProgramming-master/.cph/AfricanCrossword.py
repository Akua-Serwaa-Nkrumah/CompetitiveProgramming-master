def is_valid(unit):
    seen = set()
    for letter in unit:
        if letter in seen:
            unit.pop()
        else: 
            seen.add(letter)
    
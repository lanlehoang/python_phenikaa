import unicodedata

# Vietnamese character and accent order
CHARACTER_ORDER = [
    'a', 'ă', 'â', 'b', 'c', 'd', 'đ', 'e', 'ê', 'g', 'h', 'i',
    'k', 'l', 'm', 'n', 'o', 'ô', 'ơ', 'p', 'q', 'r', 's', 't',
    'u', 'ư', 'v', 'x', 'y'
]
ACCENTS = ['', '̀', '́', '̉', '̃', '̣']

# Maps for special Vietnamese characters
DIACRITIC_MAP = {
    ('a', '̂'): 'â',
    ('a', '̆'): 'ă',
    ('e', '̂'): 'ê',
    ('o', '̂'): 'ô',
    ('o', '̛'): 'ơ',
    ('u', '̛'): 'ư',
}


def get_vi_name_key(name):
    return get_vi_key(westernize_and_lower(name))


def westernize_and_lower(name):
    words = [word.lower() for word in name.split()]
    return words[-1] + " " + " ".join(words[:-1])


def get_vi_key(s):
    s = unicodedata.normalize('NFD', s.lower())
    result = []
    # Iterate over each character
    i = 0
    while i < len(s):
        # Skip if it's a standalone diacritic
        if unicodedata.category(s[i]) == 'Mn':
            i += 1
            continue
        # Get the base character
        base = s[i]
        i += 1
        # Check if the next characters are a diacritic and a tone
        char_diacritic = None
        tone = None
        if i < len(s) and unicodedata.category(s[i]) == 'Mn':
            # Check diacritic
            if s[i] not in ACCENTS:
                char_diacritic = s[i]
                i += 1
            # Check tone (regardless of whether the diacritic exists or not)
            if i < len(s) and unicodedata.category(s[i]) == 'Mn':
                tone = s[i]
                i += 1
        if char_diacritic and (base, char_diacritic) in DIACRITIC_MAP:
            base = DIACRITIC_MAP[(base, char_diacritic)]

        result.append((
            CHARACTER_ORDER.index(base) if base in CHARACTER_ORDER else 100,
            ACCENTS.index(tone) if tone in ACCENTS else 0,
        ))
    return result

import unicodedata

# Vietnamese character and accent order
CHARACTER_ORDER = [
    'a', 'ă', 'â', 'b', 'c', 'd', 'đ', 'e', 'ê', 'g', 'h', 'i',
    'k', 'l', 'm', 'n', 'o', 'ô', 'ơ', 'p', 'q', 'r', 's', 't',
    'u', 'ư', 'v', 'x', 'y'
]
ACCENTS = ['', '̀', '́', '̉', '̃', '̣']

def get_vi_name_key(name):
    return get_vi_key(westernize_and_lower(name))

def westernize_and_lower(name):
    words = [word.lower() for word in name.split()]
    return words[-1] + " " + " ".join(words[:-1])

def get_vi_key(s):
    s = unicodedata.normalize('NFD', s.lower())
    result = []
    for c in s:
        if unicodedata.category(c) == 'Mn':
            continue  # skip, handled as tone
        base = c
        tone = ''
        # get tone mark (if any)
        decomposed = unicodedata.normalize('NFD', c)
        for d in decomposed:
            if unicodedata.category(d) == 'Mn' and d in ACCENTS:
                tone = d
        result.append((
            CHARACTER_ORDER.index(base) if base in CHARACTER_ORDER else 100,
            ACCENTS.index(tone) if tone in ACCENTS else 0,
            base
        ))
    return result

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
    normalized = unicodedata.normalize('NFD', s.lower())
    result = []
    
    # Process each word separately
    for word in normalized.split():
        word_result = []
        word_tone = 0  # Default: no tone
        
        # First pass: extract tone if present
        for c in word:
            if unicodedata.category(c) == 'Mn' and c in ACCENTS:
                word_tone = ACCENTS.index(c)
                break
        
        # Second pass: process characters properly
        i = 0
        while i < len(word):
            # Skip standalone diacritics
            if unicodedata.category(word[i]) == 'Mn':
                i += 1
                continue
                
            # Process base character
            base = word[i]
            i += 1
            
            # Check for character-forming diacritic
            if i < len(word) and unicodedata.category(word[i]) == 'Mn' and word[i] not in ACCENTS:
                if (base, word[i]) in DIACRITIC_MAP:
                    base = DIACRITIC_MAP[(base, word[i])]
                i += 1
            
            # Add character to word result
            char_index = CHARACTER_ORDER.index(base) if base in CHARACTER_ORDER else 100
            word_result.append(char_index)
        
        # Add word result with tone at a different level
        result.append((word_result, word_tone))
    
    return result

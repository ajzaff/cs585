# -*- coding: utf-8 -*-

import json


topic_refs = {
    'Piano': ['piano', 'pianos', 'it', 'instrument'],
    'Violin': ['violin', 'violins', 'it', 'instrument'],
    'Trumpet': ['trumpet', 'trumpets', 'it', 'instrument'],
    'Drum': ['drum', 'drums', 'it', 'instrument'],
    'Flute': ['flute', 'flutes', 'it', 'instrument'],
    'Cymbal': ['cymbal', 'cymbals', 'it', 'instrument'],
    'Guitar': ['guitar', 'guitars', 'it', 'instrument'],
    'Xylophone': ['xylophone', 'xylophones', 'it', 'instrument'],
    'Cello': ['cello', 'cellos', 'it', 'instrument'],
    'Lyre': ['lyre', 'lyres', 'it', 'instrument']
}

if __name__ == '__main__':
    dp_pairs = json.load(open('data/alldppairs.json'))

    # LEARNING STEP ALGORITHM
    # 1. Identify the question type T, or None.
    # 2. Identify the sentence referent f(X), or None.
    # 3. Mark the unidentified term with the greatest height h(Y).
    # 4. Mark the answer referent g(X), or None.
    # 5. The mapping pair is T -> (h, g).

    # 1. For all QA pairs:
    #   2. 

    # MAPPING ALGORITHM

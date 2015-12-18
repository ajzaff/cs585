# -*- coding: utf-8 -*-

import collections
import parser
import json
import re


r_qtype = re.compile(r'\b(who|what|where|why|when|which|how|many|can|is|'
                                 r'are|do|does|did|were|was|will|has|have|had)\b')

top_rels = [
    'nsubj', 'nsubjpass', 'csubj',
    'csubjpass', 'dobj', 'ccomp',
    'xcomp', 'iobj'
]

topic_refs = {
    'Alessandro_Volta': ['volta', 'he'],
    'Amedeo_Avogadro': ['avogadro', 'he'],
    'Ant': ['ant', 'ants', 'it', 'they'],
    'Antwerp': ['antwerp', 'it'],
    'Arabic_language': ['arabic', 'it'],
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
    topics = ['Piano', 'Violin', 'Trumpet', 'Drum', 'Flute', 'Cymbal', 'Guitar', 'Xylophone', 'Cello', 'Lyre']
    dp_pairs = json.load(open('data/alldppairs.json'))
    dp_map = collections.defaultdict(list)


    # LEARNING STEP
    # 1. Identify the question type T, or None.
    # 2. Identify the answer referent f(X), or None.
    # 4. Identify the answer relation g(Y), g!=f, or None.
    # 5. The mapping pair is T -> (f, g).
    def learn(pair):
        #  [ topic, question_dp, answer_dp ]
        global topics
        try:
            topic = pair[0]
            qdp = pair[1]
            adp = pair[2]

            qtype = []
            for dp in qdp:
                dep = parser.deptoken(dp)
                res = r_qtype.findall(dep['word'])
                qtype.append(res)

            g_top = float('inf')
            g_word = None
            g_rel = None
            h_top = float('inf')
            h_word = None
            h_rel = None
            for dp in adp:
                dep = parser.deptoken(dp)
                if dep['word'].lower() in topics:
                    if dep['root'] < g_top:
                        g_top = dep['root']
                        g_word = dep['word'].lower()
                        g_rel = dep['rel']
                elif dep['root'] < h_top:
                    h_top = dep['root']
                    h_word = dep['word'].lower()
                    h_rel = dep['rel']

        except IndexError:
            pass



    # LEARNING ALGORITHM
    # 1. For all QA pairs:
    #   2. Learn the weights for each pair mapping T -> (f, g)



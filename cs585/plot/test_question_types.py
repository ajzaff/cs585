# -*- coding: utf-8 -*-

import plotly.plotly as py
import plotly.graph_objs as go
import collections
import json
import re


if __name__ == '__main__':
    r_question_type = re.compile(r'\b(who|what|where|why|when|which|how|many|can|is|'
                                 r'are|do|does|did|were|was|will|has|have|had)\b')

    qa_pairs = json.load(open('data/allpairs.json'))
    items = []

    topics = ['Piano', 'Violin', 'Trumpet', 'Drum', 'Flute', 'Cymbal', 'Guitar', 'Xylophone', 'Cello', 'Lyre']
    examples = collections.defaultdict(list)
    counts = collections.defaultdict(int)

    for q in qa_pairs:
        if not q:
            continue
        if q[0][0] in topics:
            index = topics.index(q[0][0])
            q = q[0][1].lower()
            q_words = r_question_type.findall(q)[:2]
            if q_words:
                tqw = tuple(q_words)
                items.append(' '.join(tqw))
                counts[' '.join(tqw)] += 1
                examples[' '.join(tqw)].append(q)

    counts = counts.items()
    print(counts)
    counts = sorted(counts, key=lambda e: -e[1])
    common = counts[:40]

    for k,v in common:
        print(k, v)
        print('')
        for e in examples[k]:
            print(e)
        print('====')

    labels = list(map(lambda e: e[0], common))
    values = list(map(lambda e: e[1], common))

    data = [
        go.Bar(
            x=labels,
            y=values
        )
    ]
    settings = json.load(open('settings.json'))
    py.sign_in(settings['plotly-api-user'], settings['plotly-api-key'])
    plot_url = py.plot(data, filename='basic-bar')

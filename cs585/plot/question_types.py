# -*- coding: utf-8 -*-

import re
import nltk
import collections



if __name__ == '__main__':
    f = open('question_answer_pairs.txt')
    lines = f.readlines()

    r_question_type = re.compile(r'\b(who|what|where|why|when|which|how|many|can|is|'
                                 r'are|do|does|did|were|was|will|has|have|had)\b')

    r_level = r'NULL|easy|medium|hard'
    r_pair = r'^(.*?)\s+(.*?\?)\s+(.*?)\s+(%s)\s+(%s)\s+(.*?)\s*$' % (r_level, r_level)
    qa_pairs = [re.findall(r_pair, line.strip()) for line in lines]
    items = []

    examples = collections.defaultdict(list)

    for q in qa_pairs:
        if not q:
            continue
        q = q[0][1].lower()
        q_words = r_question_type.findall(q)
        tqw = tuple(q_words)
        items.append(' '.join(tqw))
        examples[' '.join(tqw)].append(q)

    fd = nltk.FreqDist(items)
    common =  fd.most_common(10)
    for k,v in common:
        print(k, v)
        print('')
        for e in examples[k]:
            print(e)
        print('====')

    items = []
    for e, v in common:
        for i in range(v):
            items.append(e)

    fdc = nltk.FreqDist(items)
    fdc.plot()
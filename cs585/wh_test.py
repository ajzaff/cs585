# -*- coding: utf-8 -*-
import re
import collections
import nltk

f = open('question_answer_pairs.txt')
lines = f.readlines()

inst = ['Piano', 'Lyre', 'Violin', 'Trumpet', 'Drum', 'Flute', 'Cymbal', 'Guitar', 'Xylophone', 'Cello']

r_question_type = re.compile(r'\b(who|what|where|why|when|which|how|many|can|is|are|do|does|did|were|was|will|has|have|had)\b')

r_level = r'NULL|easy|medium|hard'
r_pair = r'^(.*?)\s+(.*?\?)\s+(.*?)\s+(%s)\s+(%s)\s+(.*?)\s*$' % (r_level, r_level)
re_pair = re.compile(r_pair)
qa_pairs = [re_pair.findall(line.strip()) for line in lines]


items = []

for q in qa_pairs:
    if q == []:
        continue
    q = q[0]
    q_words = r_question_type.findall(q[1].lower())
    if q[0] in inst:
        if len(q_words) > 1:
            if q_words[0] == 'what' and q_words[1] == 'is':
                items.append(q)
                print q[0], ';;;', q[1], ';;;', q[2]
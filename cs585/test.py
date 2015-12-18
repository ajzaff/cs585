# -*- coding: utf-8 -*-

from nltk.stem import PorterStemmer
import parser
import json
import re


rules = getattr(__import__('rules'), 'rules')


# MAPPING ALGORITHM
# 1. Identify the question type T, or None.
# 2. While can select next mapping:
#   3. Select the next argmax(h, g) [ T -> (h, g) ]
#   4. If extracted from data set, from h(Y) return Y.
# 5. Return None

stemmer = PorterStemmer()
r_qtype = re.compile(r'\b(who|what|where|why|when|which|how|many|can|is|'
                             r'are|do|does|did|were|was|will|has|have|had)\b')
topics = ['Piano', 'Violin', 'Trumpet', 'Drum', 'Flute', 'Cymbal', 'Guitar', 'Xylophone', 'Cello', 'Lyre']
alldppairs = json.load(open('data/alldppairs.json'))

wikis = {topic.lower(): json.load(
        open('data/deps/%s.json' % topic)) for
        topic in topics}

subjs = [
    'nsubj', 'nsubjpass', 'csubj', 'csubjpass'
]

objs = [
    'dobj', 'ccomp', 'xcomp', 'iobj', 'case', 'nmod', 'acl', 'root'
]


def determine_qtype(deps):
    qtype = []
    for dep in deps:
        res = r_qtype.findall(dep['word'].lower())
        qtype.extend(res)
    return ' '.join(qtype)


def get_root(deps, stem=True):
    for dep in question:
        if dep['root'] == 0:
            if stem:
                return stemmer.stem(dep['word'])
            else:
                return dep['word']


def get_rel(deps, rel):
    for dep in question:
        if rel in dep['rel']:
            return dep


def collect_subtree(deps, index):
    """
    collects subtree of X in place.
    :param deps:
    :return:
    """

n = 1
for i, e in enumerate(alldppairs):
    if not e:
        continue

    topic = e[0]
    if topic not in topics:
        continue

    question = map(parser.deptoken, e[1])
    answer = map(parser.deptoken, e[2])
    qtype = determine_qtype(question)
    if qtype:
        if qtype in rules:

            ruleset = rules[qtype]

            # Subject
            q_subj = None
            for rel in subjs:
                q_subj = get_rel(question, rel=rel)
                if q_subj:
                    break

            # Object
            q_obj = None
            for rel in objs:
                q_obj = get_rel(question, rel=rel)
                if q_obj:
                    break

            # Root
            q_root = get_root(question)

            if q_subj and q_root and q_obj:

                print(n)
                print(qtype)
                for e in question:
                    print(e)
                print('---')

                for e in answer:
                    print(e)
                print('---')

                print(q_subj, q_root, q_obj)

                # print('---')
                # print('Rules:')
                # for rule in ruleset:
                #     print(rule['subj'])
                #     print(rule['obj'])
                #     print(rule['answer'])
                #     print('-')

                wiki = wikis[topic.lower()]
                answers = []
                for sent in wiki:
                    for rule in ruleset:
                        for dep in sent:
                            pass

                print('---------------')
                n += 1

            else:
                pass  # print('ERROR NONE')
        else:
            pass
            # print('QTYPE NOT IN RULES')
            # print(qtype)
            # for e in question:
            #     print(e)
    else:
        pass
        # print('NO QTYPE')
        # for e in question:
        #         print(e)

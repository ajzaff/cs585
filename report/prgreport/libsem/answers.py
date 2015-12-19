# -*- coding: utf-8 -*-
"""Extract question forms from question-answers corpus. """
import nltk, parser, questions
from graph import FreqGraph
import re
import json
import pickle

if __name__ == '__main__':
    """cougar_pairs = filter(lambda e: False if len(e) == 0 else (e[0][0] == 'Cougar'), questions.qa_pairs)
    f = cougar_pairs[0][0][-1]
    raw = open('qa_data/%s.txt.clean' % f, 'rb').read()
    raw = raw[raw.index('\n')+1:]
    sents = nltk.sent_tokenize(raw.decode('utf-8'))
    G = FreqGraph()
    i = 0
    for s in sents:
        s = s.strip().encode('ascii', 'ignore')
        s = re.sub('\n+', ' ', s)
        if s == '' or s.startswith('*'):
            continue
        splits = s.split(';')
        for split in splits:
            try:
                print '[%d] %s' % (i, split)
                deps = parser.cp.parse_trees(split, transform=parser.to_deps).next()
                G.ingest(deps)
                i += 1
            except KeyboardInterrupt as e:
                import sys
                sys.exit()
            except StopIteration:
                pass
            except Exception as e:
                print 'error:', e.message, e.args, '@', split"""

    cougar_pairs = filter(lambda e: False if len(e) == 0 else (e[0][0] == 'Cymbal'), questions.qa_pairs)
    things = []
    raw = open('qa_data/data/set2/a2.txt.clean', 'rb').read()
    raw = raw[raw.index('\n')+1:]
    sents = nltk.sent_tokenize(raw.decode('utf-8'))
    #G = FreqGraph()
    i = 0
    for s in sents:
        s = s.strip().encode('ascii', 'ignore')
        s = re.sub('\n+', ' ', s)
        if s == '' or s.startswith('*'):
            continue
        splits = s.split(';')
        for split in splits:
            try:
                print '[%d] %s' % (i, split)
                deps = parser.cp.parse_trees(split, transform=parser.to_deps).next()
                things.append(deps)
                #G.ingest(deps)
                i += 1
            except KeyboardInterrupt as e:
                import sys
                sys.exit()
            except StopIteration:
                pass
            except Exception as e:
                print 'error:', e.message, e.args, '@', split

    pickle.dump(things, open('qa_data/a2.json', 'wb'))

    #G = FreqGraph.load(open('cougar.json', 'rb'))

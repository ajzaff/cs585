# -*- coding: utf-8 -*-

import re
import json
import parser


if __name__ == '__main__':

    f = open('data/allpairs.txt')
    lines = f.readlines()

    r_question_type = re.compile(r'\b(who|what|where|why|when|which|how|many|can|is|'
                                 r'are|do|does|did|were|was|will|has|have|had)\b')

    r_level = r'NULL|easy|medium|hard'
    r_pair = r'^(.*?)\s+(.*?\?)\s+(.*?)\s+(%s)\s+(%s)\s+(.*?)\s*$' % (r_level, r_level)
    qa_pairs = [re.findall(r_pair, line.strip()) for line in lines]

    json.dump(qa_pairs, open('data/allpairs.json', 'w'))

    qa_cp = []
    qa_dp = []

    for e in qa_pairs:
        try:
            e = e[0]
            que = next(parser.cp.parse_trees(e[1]))
            ans = next(parser.cp.parse_trees(e[2]))
            qa_cp.append([e[0], que, ans])
            qa_dp.append([e[0], parser.to_deps(que), parser.to_deps(ans)])
            print(e)
        except StopIteration:
            print('STOP ITERATION')
        except IndexError:
            print('INDEX ERROR')
        except:
            print('UNKNOWN ERROR')

    json.dump(qa_cp, open('data/allcppairs.json', 'w'))
    json.dump(qa_dp, open('data/alldppairs.json', 'w'))

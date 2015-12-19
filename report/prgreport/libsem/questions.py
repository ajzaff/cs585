"""Extract question forms from question-answers corpus. """
from graph import FreqGraph
import parser
import re

lines = open('qa_data/question_answer_pairs.txt').readlines()[1:]
# subject (question)? (answer)	(NULL|easy|medium|hard)	(NULL|easy|medium|hard)	(data)
r_level = r'NULL|easy|medium|hard'
r_pair = r'^(.*?)\s+(.*?\?)\s+(.*?)\s+(%s)\s+(%s)\s+(.*?)\s*$' % (r_level, r_level)
re_pair = re.compile(r_pair)
qa_pairs = [re_pair.findall(line) for line in lines]

if __name__ == '__main__':
    G = FreqGraph()
    for pair in qa_pairs:
        try:
            print pair[0][0], pair[0][1]
            deps = parser.cp.parse_trees(pair[0][1], transform=parser.to_deps).next()
            G.ingest(deps)
        except KeyboardInterrupt:
            import sys
            sys.exit(0)
        except:
            pass
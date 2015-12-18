# -*- coding: utf-8 -*-

import parser
import json
import nltk
import sys
import re


def tokenize(text):
    topic = str(text)[:text.index('\n')].strip().lower()
    yield topic
    text = str(text).decode('ascii', 'ignore')[text.index('\n')+1:].strip()
    text = re.sub(r'[\s\n]+', ' ', text)
    for sent in nltk.sent_tokenize(text):
        yield sent


def process(topic):
    topic = topic.strip().lower()

    f = open('data/raw/%s.txt' % topic)  # open resources
    tokenizer = tokenize(f.read())
    topic = next(tokenizer)
    cpf = open('data/cp/%s.json' % topic, 'w')
    dpf = open('data/dp/%s.json' % topic, 'w')
    cp = []
    dp = []
    i = 1

    for sent in tokenizer:
        try:
            cp.extend(parser.cp.parse_trees(sent))
            dp.extend(parser.cp.parse_trees(sent, transform=parser.to_deps))
            print("[%s %d] %s" % (topic, i, sent))
        except ValueError:
            print("[%s %d] TIMED OUT: %s" % (topic, i, sent))
        except:
            print("[%s %d] UNKNOWN ERROR: %s" % (topic, i, sent))
        i += 1

    json.dump(cp, cpf)
    json.dump(dp, dpf)


if __name__ == '__main__':

    if len(sys.argv) < 2:  # test arguments
        topics = open('data/topics.txt').readlines()
        for topic in topics:
            process(topic)
        sys.exit(0)
    else:
        process(sys.argv[1])

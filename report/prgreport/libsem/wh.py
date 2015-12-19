"""Wh- inference. Alan J. Zaffetti. 2015 """
import parser

wh_words = {
    'what', 'which', 'where', 'when', 'who'
}

tenses = {
    'is', 'are', 'was', 'were', 'will'
}


if __name__ == '__main__':
    while True:
        query = raw_input('?: ')
        deps = parser.cp.parse_trees(query, transform=parser.to_deps).next()
        for dep in deps:
            print dep


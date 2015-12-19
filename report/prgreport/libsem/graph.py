# -*- coding: utf-8 -*-

from collections import defaultdict
import logic, json

ROOT = 'ROOT'
TERMINAL = 'TERMINAL'
CLIQUE = '&'


def default_freq_dict():
    return defaultdict(int)


class SkolemKeyGenerator(object):

    def __init__(self, n=None):
        self.n = n if n else 0

    def next(self):
        i = self.n
        self.n += 1
        return i


class FreqGraph(defaultdict):
    """Represents a graph as a default dictionary of (int) default dictionaries. """

    def __init__(self, default_factory=None):
        """
        :param default_factory: unused
        :return:
        """
        defaultdict.__init__(self, default_freq_dict)
        self._sid_gen = SkolemKeyGenerator()
        self._sk = defaultdict(self._sid_gen.next)
        self._sids = {}
        self._skolem(ROOT)
        self._pos = set()

    def _skolem(self, term):
        sid = self._sk[term]
        self._sids[sid] = term
        if hasattr(term, 'pos'):
            self._pos.add(term.pos)
        return sid

    def lookup(self, e):
        try:
            return self._sids[e]
        except:
            if isinstance(e, basestring):
                e = e.lower()
                return [(self._sk[(e, p)], p) for p in self._pos if (e, p) in self._sk]
            elif e in self._sk:
                return self._sk[e]
        return None

    def ingest(self, deps):
        """Ingests a list of dependency relations.

        :param deps: (list[Token]) dependency relations
        """
        terms = map(logic.Term, deps)
        for i, dep in enumerate(deps):
            term = terms[i]
            head = dep.head - 1
            if head == -1:
                self.add_edge('root', ROOT, term)
            else:
                self.add_edge(dep.deprel, terms[head], term)

    def clique(self, deps):
        """Ingests the ``CLIQUE'' relation.
        :param deps: (list[Token]) dependency relations
        """
        raise ValueError('clique not implemented')
        # terms = map(logic.Term, deps)
        # for i, p in enumerate(terms):
        #     for j, q in enumerate(terms):
        #         if i != j:
        #             self.add_edge(CLIQUE, p, q)

    def add_edge(self, label, head, child):
        """Adds an observation of the edge ``head -> child''.

        :param label: (str) the edge relation.
        :param head: a head element
        :param child: a child element
        """
        h = self._skolem(head)
        c = self._skolem(child)
        self[c] = self[c]
        for r in label.split(':'):
            self[h][Edge((r, c))] += 1

    def dumps(self):

        dd = {}
        for k in self:
            dv = {}
            for r, o in self[k]:
                dv['%s,%s' % (r, o)] = self[k][(r, o)]
            dd[k] = dv

        obj = {
            'sid': self._sid_gen.n,
            'skolem': self._sids,
            'graph': dd,
            'pos': list(self._pos)
        }
        return json.dumps(obj)

    def dump(self, file):
        s = self.dumps()
        file.write(s)

    @classmethod
    def load(cls, file):
        obj = json.load(file)
        sid = obj['sid']
        sid_gen = SkolemKeyGenerator(sid)
        sk = {}
        sids = {}
        graph = {}

        # Decode skolem dictionary
        for k in obj['skolem']:
            if obj['skolem'][k] == ROOT:
                term = ROOT
            else:
                term = logic.Term.from_iterable(obj['skolem'][k])
            sids[int(k)] = term
            sk[term] = int(k)

        # Decode graph
        for v in obj['graph']:
            es = {}
            for e in obj['graph'][v]:
                dep, skid = e.split(',')
                es[(dep, int(skid))] = obj['graph'][v][e]
            graph[int(v)] = defaultdict(int)
            graph[int(v)].update(es)

        # Build the object
        fg = FreqGraph()
        fg._sid_gen = SkolemKeyGenerator(sid)
        fg._sk = defaultdict(sid_gen.next)
        fg._sk.update(sk)
        fg._sids = sids
        fg._pos = set(obj['pos'])
        fg.update(graph)
        return fg

    def query(self, *args):
        """Query this frequency graph.

        :param args: (list) the query as a list of Edges
        :return: tuples of cliques which satisfy the query
            mapped to confidence levels.
        """
        pass


class Edge(tuple):

    def __init__(self, iterable):
        assert len(iterable) == 2
        tuple.__init__(self, iterable)
        self.label = iterable[0]
        self.child = iterable[1]

    def __new__(cls, *args, **kwargs):
        assert len(args) == 1
        assert len(args[0]) == 2
        return tuple.__new__(cls, args[0])


if __name__ == '__main__':
    import nltk
    from nltk.corpus import gutenberg
    import parser

    def get_deps(s):
        return parser.cp.parse_trees(s, transform=parser.to_deps)


    G = FreqGraph()
    alice_sents = gutenberg.sents(fileids='carroll-alice.txt')
    for sent in alice_sents:
        dep = get_deps(' '.join(sent))
        try:
            term = logic.Term(dep.next())
            G.clique(term)
        except:
            pass
    #G.ingest(get_deps('Barack is president'))
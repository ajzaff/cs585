import StanfordDependencies
import simplejson
import sys
import json

dp = StanfordDependencies.get_instance(backend='subprocess')


def to_nltk_tree(sent):
    """Transforms a sentence to an NLTK tree.
    :param sent: (str) a bracketed parse
    :return: (nltk.Tree) an NLTK ``Tree'' instance
    """
    import nltk
    return nltk.Tree.fromstring(sent)


def to_cnf(sent):
    """Transforms a parsed sentence to a parsed sentence in CNF.
    :param sent: (str) a bracketed parse
    :return: (str) a bracketed parse in Chomsky Normal Form
    """
    import nltk
    tree = nltk.Tree.fromstring(sent)
    tree.chomsky_normal_form()
    return str(tree)


def to_deps(sent):
    """Transforms a parsed sentence to raw universal dependencies.
    :param sent: (str) a bracketed parse
    :return: (list[Token]) a list of Tokens representing a dependency tree
    """
    global dp
    return dp.convert_tree(sent)


def dep_find_index(i, dp):
    for d in dp:
        if d.index == i:
            return d
    raise ValueError('index %d not in dependency tree' % i)


class Parser:
    """The core NLP parser server. """

    def __init__(self, path_to_parser=None):
        """Creates a new Core NLP parser.

        :param path_to_parser: (str) the path to the source code of Core NLP.
        :return: (Parser) a Core NLP parser
        """
        self._server = None
        self._invoked = False
        self.invoke(path_to_parser)

    def invoke(self, path_to_parser=None):
        if path_to_parser:
            try:
                sys.path.append(path_to_parser)
                jsonrpc = __import__('jsonrpc')
                self._server = jsonrpc.ServerProxy(
                    jsonrpc.JsonRpc20(),
                    jsonrpc.TransportTcpIp(
                        addr=("127.0.0.1", 8080),
                        timeout=200))
            finally:
                self._invoked = True
                return self

    def parse_trees(self, sents, transform=lambda s: s, filter=lambda s: True):
        """Parse a sentence into bracket notation.

        :param sents: (str) raw sentences to parse as a string.
        :param transform: (function) applied when yielding each parse,
            default => lambda s: s
            option  => transform_nltk_tree
            option  => transform_cnf
        :param filter: (function) returns ``True'' or ``False'' whether to include the element.
        :return: (iterable[?]) bracketed parse trees for each sent in ``sents'',
            default => (iterable[str])
        """
        data = self._server.parse(sents)
        result = simplejson.loads(data)
        try:
            for sent in result['sentences']:
                ts = transform(sent['parsetree'])
                if filter(ts):
                    yield ts
        except:
            if 'error' in result:
                raise ValueError(result['error'])


cp = Parser().invoke(json.load('../settings.json')['parserpath'])
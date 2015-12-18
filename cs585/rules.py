# -*- coding: utf-8 -*-

# rule based system for IR
# key format:
# {
#   subj   => DR to match (subject).
#   obj    => DR to match (object).
#   answer => DR where answer is found.
# }
rules = {
    # Is questions are mapped to TRUE or FALSE
    # Based on match frequency ratio <> 1/2
    'is': [
        {
            'subj': 'nsubjpass',
            'obj': 'nmod',
            'answer': 'obj'
        },
        {
            'subj': 'csubj',
            'obj': 'dobj',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'nmod',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        }
    ],
    'what is': [
        {
            'subj': 'nsubjpass',
            'obj': 'dobj',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'acl',
            'answer': 'subj'
        },
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'ccomp',
            'answer': 'obj'
        }
    ],
    'how has': [
        {
            'subj': 'nsubjpass',
            'obj': 'dobj',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'acl',
            'answer': 'subj'
        },
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'root'
        },
        {
            'subj': 'nsubj',
            'obj': 'ccomp',
            'answer': 'obj'
        }
    ],
    'how was': [
        {
            'subj': 'nsubjpass',
            'obj': 'dobj',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'acl',
            'answer': 'subj'
        },
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'ccomp',
            'answer': 'obj'
        }
    ],
    'how is': [
        {
            'subj': 'nsubjpass',
            'obj': 'dobj',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'acl',
            'answer': 'subj'
        },
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'ccomp',
            'answer': 'obj'
        }
    ],
    'how do': [
        {
            'subj': 'nsubjpass',
            'obj': 'dobj',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'acl',
            'answer': 'subj'
        },
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'ccomp',
            'answer': 'obj'
        }
    ],
    'are': [
        {
            'subj': 'nsubjpass',
            'obj': 'nmod',
            'answer': 'obj'
        },
        {
            'subj': 'csubj',
            'obj': 'dobj',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'nmod',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        }
    ],
    'what are': [
        {
            'subj': 'nsubjpass',
            'obj': 'dobj',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'acl',
            'answer': 'subj'
        },
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'ccomp',
            'answer': 'obj'
        }
    ],
    'what can': [
        {
            'subj': 'nsubjpass',
            'obj': 'dobj',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'acl',
            'answer': 'subj'
        },
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'ccomp',
            'answer': 'obj'
        }
    ],
    'how many': [
        {
            'subj': ['nsubj', 'nummod'],
            'obj': 'ccomp',
            'answer': 'subj'
        },
        {
            'subj': ['nsubjpass', 'nummod'],
            'obj': 'root',
            'answer': 'subj'
        },
        {
            'subj': 'nsubj',
            'obj': ['dobj', 'nummod'],
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'ccomp',
            'answer': 'obj'
        }
    ],
    'do many': [
        {
            'subj': ['nsubj', 'nummod'],
            'obj': 'ccomp',
            'answer': 'subj'
        },
        {
            'subj': ['nsubjpass', 'nummod'],
            'obj': 'root',
            'answer': 'subj'
        },
        {
            'subj': 'nsubj',
            'obj': ['dobj', 'nummod'],
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'ccomp',
            'answer': 'obj'
        }
    ],
    'what was': [
        {
            'subj': 'nsubjpass',
            'obj': 'dobj',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'acl',
            'answer': 'subj'
        },
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'ccomp',
            'answer': 'obj'
        }
    ],
    'what did': [
        {
            'subj': 'nsubjpass',
            'obj': 'dobj',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'acl',
            'answer': 'subj'
        },
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'ccomp',
            'answer': 'obj'
        }
    ],
    'does': [
        {
            'subj': 'nsubjpass',
            'obj': 'nmod',
            'answer': 'obj'
        },
        {
            'subj': 'csubj',
            'obj': 'dobj',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'nmod',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        }
    ],
    'do': [
        {
            'subj': 'nsubjpass',
            'obj': 'nmod',
            'answer': 'obj'
        },
        {
            'subj': 'csubj',
            'obj': 'dobj',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'nmod',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        }
    ],
    'did': [
        {
            'subj': 'nsubjpass',
            'obj': 'nmod',
            'answer': 'obj'
        },
        {
            'subj': 'csubj',
            'obj': 'dobj',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'nmod',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        }
    ],
    'has': [
        {
            'subj': 'nsubjpass',
            'obj': 'nmod',
            'answer': 'obj'
        },
        {
            'subj': 'csubj',
            'obj': 'dobj',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'nmod',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        }
    ],
    'have': [
        {
            'subj': 'nsubjpass',
            'obj': 'nmod',
            'answer': 'obj'
        },
        {
            'subj': 'csubj',
            'obj': 'dobj',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'nmod',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        }
    ],
    'can': [
        {
            'subj': 'nsubjpass',
            'obj': 'nmod',
            'answer': 'obj'
        },
        {
            'subj': 'csubj',
            'obj': 'dobj',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'nmod',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        }
    ],
    'can have': [
        {
            'subj': 'nsubjpass',
            'obj': 'nmod',
            'answer': 'obj'
        },
        {
            'subj': 'csubj',
            'obj': 'dobj',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'nmod',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        }
    ],
    'what': [
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'nmod',
            'answer': 'subj'
        }
    ],
    'which': [
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'nmod',
            'answer': 'subj'
        }
    ],
    'who': [
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'nmod',
            'answer': 'subj'
        }
    ],
    'who was': [
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'nmod',
            'answer': 'subj'
        }
    ],
    'when does': [
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'nmod',
            'answer': 'subj'
        }
    ],
    'when was': [
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'nmod',
            'answer': 'subj'
        }
    ],
    'when is': [
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'nmod',
            'answer': 'subj'
        }
    ],
    'when do': [
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'nmod',
            'answer': 'subj'
        }
    ],
    'where is': [
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'nmod',
            'answer': 'subj'
        }
    ],
    'where was': [
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'nmod',
            'answer': 'subj'
        }
    ],
    'was': [
        {
            'subj': 'nsubjpass',
            'obj': 'nmod',
            'answer': 'obj'
        },
        {
            'subj': 'csubj',
            'obj': 'dobj',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'nmod',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        }
    ],
    'were': [
        {
            'subj': 'nsubjpass',
            'obj': 'nmod',
            'answer': 'obj'
        },
        {
            'subj': 'csubj',
            'obj': 'dobj',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'nmod',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        }
    ],
    'what were': [
        {
            'subj': 'nsubjpass',
            'obj': 'dobj',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'acl',
            'answer': 'subj'
        },
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'ccomp',
            'answer': 'obj'
        }
    ],
    'does have': [
        {
            'subj': 'nsubjpass',
            'obj': 'nmod',
            'answer': 'obj'
        },
        {
            'subj': 'csubj',
            'obj': 'dobj',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'nmod',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        }
    ],
    'what does': [
        {
            'subj': 'nsubjpass',
            'obj': 'dobj',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'acl',
            'answer': 'subj'
        },
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'ccomp',
            'answer': 'obj'
        }
    ],
    'what has': [
        {
            'subj': 'nsubjpass',
            'obj': 'dobj',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'acl',
            'answer': 'subj'
        },
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'ccomp',
            'answer': 'obj'
        }
    ],
    'why do': [
        {
            'subj': 'nsubjpass',
            'obj': 'nmod',
            'answer': 'obj'
        },
        {
            'subj': 'csubj',
            'obj': 'dobj',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'nmod',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        }
    ],
    'why are': [
        {
            'subj': 'nsubjpass',
            'obj': 'nmod',
            'answer': 'obj'
        },
        {
            'subj': 'csubj',
            'obj': 'dobj',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'nmod',
            'answer': 'obj'
        },
        {
            'subj': 'nsubj',
            'obj': 'root',
            'answer': 'obj'
        }
    ],
}
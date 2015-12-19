import pickle

if __name__ == '__main__':
    all_deps = pickle.load(open('a1.pickle'))
    
    def in_dep(dep, req):
        """
        reqs = [(rel, form), ...]
        """
        if dep.form.lower() == req[1].lower():
            if dep.deprel == req[0]:
                return True
        return False
    
    results = []
    
    for deps in all_deps:
        reqs = [('dep', 'sustain'), ('nsubj', 'pedal'), ('dep', 'the')]
        for dep in deps:
            found = False
            for i, req in enumerate(reqs):
                if in_dep(dep, req):
                    found = True
                    break
            if found:
                del reqs[i]
        if reqs == []:
            results.append(deps)
            
    for res in results:
        for r in res:
            print r
        print '==='
                
            
            
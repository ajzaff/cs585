def get_question_type(deps):
    qw = []
    for dep in deps:
        if dep['word'] in question_types:
            qw.append(dep['word'])
        if len(qw) > 1:
            break
    return ' '.join(qw)
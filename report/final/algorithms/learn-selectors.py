def get_selectors(deps, agent):
    qtype = get_question_type(deps)
    ref = get_question_referent(deps, agent)
    patient = get_question_patient(deps)
    root = get_root_theme(deps)
    return qtype, ref, root patient
    
for deps, topic in dataset:
    sel = get_selectors(deps, topic)
    # TODO: count the selector
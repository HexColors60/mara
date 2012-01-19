"""
Social command management
"""

def social(cmd, *preps):
    """
    Build and register a social command, with optional prepositions
    """
    def closure(e):
        prep = ''
        target = e.args.target
        if target and preps:
            prep = '%s %s' % (e.args.prep or preps[0], target.name)
        
        verb_third = English_verb_present(cmd, person=3)
        
        if target:
            write(e.user, "You %s %s" % (cmd, prep))
            write_except(e.user, "%s %s %s" % (e.user.name, verb_third, prep))
        else:
            write(e.user, "You %s" % cmd)
            write_except(e.user, "%s %s" % (e.user.name, verb_third))
    
    # Build argument list
    args = []
    if preps:
        regex = '|'.join(preps)
        args.append(Arg(
            name = 'prep',
            match = preps[0] if len(preps) == 1 else '(?:' + regex + ')',
            syntax = regex,
            optional = True
        ))
    # ++ Add support for multiple users
    # ++ Add support for User or str
    args.append(Arg('target', User, optional=True))
    
    commands[cmd] = Command(cmd, closure, args=args)

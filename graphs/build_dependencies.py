'''
Track which build components may be built when.
'''


def build_order(dependencies):
    '''
    Given a list of (component, dependency) pairs, return a list of lists of
    components which can be built in parallel.
    '''

    ref_counts = {}
    deps = {}

    next_build_round = set()
    build_order = []

    for comp, upstream in dependencies:

        # Handle upstream component
        if upstream not in deps:
            deps[upstream] = []
            ref_counts[upstream] = 0
            next_build_round.add(upstream)
        deps[upstream].append(comp)

        # Handle current component
        if comp not in deps:
            deps[comp] = []
            ref_counts[comp] = 0
        ref_counts[comp] += 1
        if comp in next_build_round:
            next_build_round.remove(comp)

    # Calculate the build rounds.
    while next_build_round:
        current_build_round = list(next_build_round)
        build_order.append(current_build_round)
        next_build_round = set()
        for component in current_build_round:
            # Decrement reference count. If a count reaches 0, we add
            # that component to the next build round.
            for upstream in deps[component]:
                ref_counts[upstream] -= 1
                if ref_counts[upstream] == 0:
                    next_build_round.add(upstream)

    return build_order


for order in build_order([('a', 'b'), ('c', 'b'), ('d', 'b'), ('b', 'e')]):
    print order

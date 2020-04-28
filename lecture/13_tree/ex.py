"""Tree
2 different metaform for a tree

Recursive description: A tree has a root label and a list of branches. Each branch is a tree.
A tree with zero branches is called leaf.

Relative description: Each location in a tree is called a node. Each node ahs a label that can be any value. One node can be the parent/child of another.

People oftne refer to lebels by their locations: each parent is the sum of its children

tree implement
tree(3, [tree(1),
         tree(2, [tree(1),
                  tree(1)])])
"""

# Trees

def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

# Tree Processing
def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(label(left) + label(right), [left, right])

def count_leaves(t):
    """Count the leaves of a tree."""
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(t)])

def leaves(tree):
    """Return a list containing the leaf labels of tree."""
    if is_leaf(tree):
        return [label(tree)]
    return sum([leaves(b) for b in branches(tree)], [])

def invrement_leaves(t):

    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t), bs)

def increment(t):
    """Return a tree like t btu with all labels incremented."""
    return tree(label(t) + 1, [increment(b) for b in branches(t)])

def print_tree(t, indent=0):
    print(' ' * indent, str(label(t)))
    for b in branches(t):
        print_tree(b, indent+1)

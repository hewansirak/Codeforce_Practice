import sys

sys.setrecursionlimit(2000)

# Segment tree node structure
class Node:
    def __init__(self, balance=0, suffix_stack=None):
        self.balance = balance
        self.suffix_stack = suffix_stack if suffix_stack is not None else []

# Merge function for segment tree nodes
def merge_nodes(left_node, right_node):
    bal_l = left_node.balance
    suf_l = left_node.suffix_stack
    bal_r = right_node.balance
    suf_r = right_node.suffix_stack

    # Number of pops from the right segment that hit the left segment's effective stack.
    # These are the pops in the right segment that are not absorbed by pushes within the right segment.
    # The number of such "unabsorbed" pops in the right segment is max(0, -bal_r), assuming an empty incoming stack.
    # If a stack of size len(suf_l) comes into the right segment, these pops will remove min(len(suf_l), max(0, -bal_r))
    # elements from the end of suf_l.
    num_popped_from_left = min(len(suf_l), max(0, -bal_r))

    new_balance = bal_l + bal_r
    # The new suffix stack is the remainder of the left suffix stack (after being popped by the right)
    # followed by the right suffix stack.
    # Slicing suf_l[:len(suf_l) - num_popped_from_left] efficiently gets the required prefix.
    # This slice handles cases where num_popped_from_left is 0 or >= len(suf_l).
    new_suffix_stack = suf_l[:len(suf_l) - num_popped_from_left] + suf_r

    return Node(new_balance, new_suffix_stack)

# Global array to store details of original operations
# Index i stores details of original operation i+1 (0-indexed)
# This array is populated as operations are revealed step by step.
original_ops_details = [] # List of (type, value) tuples, value is None for pop

# Segment tree array
tree = []
M = 0 # Number of operations

# Segment tree build function (initial state: all original operations are inactive)
# This function builds the initial segment tree representing the state before any operations are remembered.
# v: current node index in the tree (1-based)
# tl, tr: range covered by node v (0-based original operation indices, inclusive)
def build(v, tl, tr):
    if tl == tr:
        # Leaf node corresponds to a single original operation.
        # Initially, all operations are inactive, so their state is (balance=0, empty stack).
        tree[v] = Node(0, [])
    else:
        tm = (tl + tr) // 2 # Midpoint of the range
        # Recursively build left and right children
        build(2*v, tl, tm)
        build(2*v+1, tm+1, tr)
        # Internal nodes initially represent the merge of inactive children.
        tree[v] = merge_nodes(tree[2*v], tree[2*v+1])

# Segment tree update function (activates the original operation at index pos)
# When an operation is remembered, we update the segment tree to include its effect.
# v: current node index in the tree (1-based)
# tl, tr: range covered by node v (0-based original operation indices, inclusive)
# pos: index of the original operation being activated (0-based)
def update(v, tl, tr, pos):
    if tl == tr:
        # We found the leaf node corresponding to the original operation at index 'pos'.
        # Retrieve its details from the global array (which were stored when it was remembered).
        op_type, op_value = original_ops_details[pos]
        if op_type == 1: # Push operation
            # When a push operation is active, it adds 1 to the balance and its value to the suffix stack.
            tree[v] = Node(1, [op_value])
        else: # Pop operation
            # When a pop operation is active, it subtracts 1 from the balance and adds no elements to the suffix stack.
            tree[v] = Node(-1, [])
    else:
        tm = (tl + tr) // 2 # Midpoint of the range
        if pos <= tm:
            # The operation to activate is in the left child's range. Recurse left.
            update(2*v, tl, tm, pos)
        else:
            # The operation to activate is in the right child's range. Recurse right.
            update(2*v+1, tm+1, tr, pos)
        # After updating the relevant child node, merge the children's states to update the parent's state.
        tree[v] = merge_nodes(tree[2*v], tree[2*v+1])

def solve():
    global M, original_ops_details, tree
    M = int(sys.stdin.readline())

    # Store the input operations as they are remembered (permuted order).
    # We need this list to process the operations step by step.
    remembered_operations_input = []
    for _ in range(M):
        line = list(map(int, sys.stdin.readline().split()))
        p_i = line[0] # Original index of this operation (1-based)
        t_i = line[1] # Type of operation (0 for pop, 1 for push)
        x_i = line[2] if t_i == 1 else None # Value for push (if type is 1)
        remembered_operations_input.append((p_i, t_i, x_i))

    # Initialize the array to store the details of all M original operations.
    # original_ops_details[i] will store the details of the (i+1)-th original operation (0-indexed).
    # We populate this array as operations are remembered.
    original_ops_details = [None] * M

    # Initialize the segment tree.
    # The tree covers the range of original operation indices [0, M-1].
    # A size of 4*M is typically sufficient for a segment tree using 1-based indexing for nodes.
    tree = [None] * (4 * M)
    build(1, 0, M-1) # Build the initial tree with all operations inactive.

    # Process the remembered operations step by step.
    # At each step (from 1 to M), one original operation's details are revealed.
    for step in range(M):
        # Get the details of the original operation revealed at this step.
        p_i, t_i, x_i = remembered_operations_input[step]
        original_index = p_i - 1 # Convert the 1-based original index to 0-based.

        # Store the details of this original operation in the global array.
        # This makes the details available for the update function.
        original_ops_details[original_index] = (t_i, x_i)

        # Activate this operation in the segment tree by updating the corresponding leaf node.
        # The update function will automatically propagate the changes up the tree by merging node states.
        update(1, 0, M-1, original_index)

        # After activating the operation, the state of the stack after considering
        # all operations remembered so far (which are original ops p_1, ..., p_{step}
        # applied in their original order) is represented by the root node of the segment tree (tree[1]).

        root_node = tree[1]

        # The final effective stack after applying all active operations in original order
        # is given by the suffix_stack of the root node.
        final_stack = root_node.suffix_stack

        # The top of the stack is the last element of the final effective stack.
        # If the stack is empty, the suffix_stack will be an empty list.
        # Print -1 if the stack is empty, otherwise print the top element.
        if not final_stack:
            print(-1)
        else:
            print(final_stack[-1])

solve()
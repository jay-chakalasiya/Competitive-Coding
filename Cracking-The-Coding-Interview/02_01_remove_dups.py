
class listnode:
    def __init__(self, val):
        self.val = val
        self.next = None
    def print_list(self):
        ls_string=str(self.val)+' -> '
        cur_node = self
        while cur_node.next:
            cur_node = cur_node.next
            ls_string+=str(cur_node.val)+' -> '
        return ls_string+'#'

def make_linked_list(ls):
    nodes = [listnode(l) for l in ls]
    for i in range(0, len(nodes)-1, 1):
        nodes[i].next = nodes[i+1]
    return nodes[0]


def remove_dups(start_node):
    if start_node is None:
        return start_node
    current = start_node
    travelled = set([current.val])
    while current.next:
        if current.next.val in travelled:
            current.next = current.next.next
        else:
            travelled.add(current.next.val)
            current = current.next
    return start_node


def remove_dups_followup(start_node):
    if start_node is None:
        return start_node
    current = start_node
    while current:
        runner = current
        while runner.next:
            if runner.next.val == current.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    return start_node



if __name__ == "__main__":
    start_node = make_linked_list([2,2,3,4,4,6,7,8,4,10])
    start_node = remove_dups_followup(start_node)#remove_dups(start_node)
    print(start_node.print_list())
    #print(remove_dups(start_node))

        
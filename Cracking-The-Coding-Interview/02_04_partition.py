# 

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


def partition(start_node, value):
    less_current_node = None
    more_start_node = None
    more_current_node = None


    current_node = start_node


    while current_node:
        if current_node.val>=value:
            if more_start_node is None:
                more_start_node = current_node
                more_current_node = more_start_node
            else:
                more_current_node.next=current_node
                more_current_node = more_current_node.next

        elif current_node.val<value:
            if less_current_node is None:
                less_current_node = current_node
            else:
                less_current_node.next=current_node
                less_current_node = less_current_node.next
        current_node = current_node.next
    less_current_node.next = more_start_node
    return start_node

    

if __name__ == "__main__":
    start_node = make_linked_list([2,2,3,4,34,6,7,8,4,10])
    print(start_node.print_list())
    start_node = partition(start_node, 8)
    print(start_node.print_list())

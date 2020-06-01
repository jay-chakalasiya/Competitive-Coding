# Implement algorthm to find kth to the last element in singly linked list

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


def return_kth_to_last(start_node, k):
    distance=0
    distant_node=start_node
    while distance<k and distant_node.next:
        distant_node = distant_node.next
        distance+=1
    if distance!=k:
        return start_node
    current_node = start_node
    while distant_node:
        distant_node = distant_node.next
        current_node = current_node.next
    return current_node

if __name__ == "__main__":
    start_node = make_linked_list([2,2,3,4,4,6,7,8,4,10])
    kth_to_last_node = return_kth_to_last(start_node, 2)#remove_dups(start_node)
    print(start_node.print_list(),'\n',kth_to_last_node.print_list())

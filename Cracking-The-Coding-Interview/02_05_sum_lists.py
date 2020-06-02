# Sum two linked lists
# Example input - (7->1->6) & (5->9->2) = 617+295
# Output = (2->1->9) = 912


# Implement other function which looks like this
# Example input - (6->1->7) & (2->9->5) = 617+295
# Output = (9->1->2) = 912

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


def sum_lists(l1, l2):
    start=l1
    carry=0
    while l1 and l2:
        sum_ = l1.val+l2.val+carry
        l1.val = sum_%10
        carry = int(sum_/10)
        if l1.next is None:
            l1.next, l2.next = l2.next, l1.next
        l1, l2 = l1.next, l2.next

    while l1:
        sum_ = l1.val+carry
        l1.val = sum_%10
        carry = int(sum_/10)
        l1 = l1.next
    return start

def sum_lists_reverse(l1, l2):
    start_l1 = l1
    start_l2 = l2
    while l1 and l2:
        l1 = l1.next
        l2 = l2.next

    if l1 is None:
        start_l1, start_l2, l1, l2 = start_l2, start_l1, l2, l1
    while l1:
        l1 = l1.next
        new_node = listnode(0)
        new_node.next = start_l2
        start_l2 = new_node
    
    print(start_l1.print_list())
    print(start_l2.print_list())

    

if __name__ == "__main__":
    l1 = make_linked_list([7,1,6]) # 617
    l2 = make_linked_list([5,9,5,1]) # 1595
    print(l1.print_list(), l2.print_list())
    start_node = sum_lists(l1, l2)
    print(start_node.print_list())

    l1 = make_linked_list([7,1,6]) # 617
    l2 = make_linked_list([5,9,5,1]) # 1595
    sum_lists_reverse(l2, l1)
# Given only access to some node excluding start and end remove that node
# Example : Linked list: 1->2->3->4->5->6->7->8->9
# Access is given to 4
# Result : 1->2->3->5->6->7->8->9

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


def delete_middle_node(middle_node):
    next_node = middle_node.next
    middle_node.val = next_node.val
    middle_node.next = next_node.next

if __name__ == "__main__":
    start_node = make_linked_list([2,2,3,4,34,6,7,8,4,10])
    print(start_node.print_list())
    delete_middle_node(start_node.next.next.next.next)
    print(start_node.print_list())

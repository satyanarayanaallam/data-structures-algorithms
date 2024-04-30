''' Write code to remove duplicates from an unsorted linked list. '''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node
        return self.head

    def print(self):
        temp = self.head
        while temp:
            print(temp.data , " ")
            temp = temp.next


def remove_duplicates(root):
    temp = root
    previous = None
    my_set = set()
    while temp != None:
        if temp.data in my_set:
            previous.next = temp.next
        else:
            my_set.add(temp.data)
            previous = temp
        temp = temp.next


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)
    linked_list.add(4)
    linked_list.add(2)
    linked_list.add(1)
    linked_list.print()
    remove_duplicates(linked_list.head)
    print("-----------")
    linked_list.print()

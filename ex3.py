from week4_DLL import DNode, DoubleLinkedList


def reverse_merge(ML, NL):
    '''(LLNode, LLNode) -> LLNode
    This function take in  two double linked lists as its input parameters.
    It merge these two lists to one list
    that contains all the student’s surname sorted ascendingly.
    REQ: the input must be two DLL
    '''
    DL = Node()
    curr = DL
    Mcurr = ML.head
    Ncurr = ML.tail
    while Mcurr or Ncurr:
        if ncurr is None or (Mcurr and Mcurr.data < Ncurr.data):
            if mcurr.data != curr.data:
                curr.next = Node(Mcurr.data)
                curr.next.prev = curr
                curr = curr.next
            Mcurr = Mcurr.next
        else:
            if ncurr.data != curr.data:
                curr.next = Node(Ncurr.data)
                curr.next.prev = curr
                curr = curr.next
            Ncurr = Ncurr.prev
    return DL.next


def allocate_room(Sname, Room, Capacity, Index):
    '''(LLNode, string, int, int) -> String
    This function takes four parameters
    a dll containing students’ surnames,
    a string representing room name and number,
    an int representing the capacity of the room,
    an int representing the index of the node
    that contains the surname of the first person assigned to this room
    This function return a string that shows:
    two first letters of surnames of the first and last person
    that should attend the given room.
    >>> allocate_room(csca48_list, “SW319”, 80, 150)
    SW319 JU-MO
    '''
    start_name = ""
    end_name = ""
    position = 0
    curr = Sname.head
    if position != Index:
        curr = curr.next
        position += 1
    start_name = curr.data[:2]
    if position != (Index + Capacity):
        if curr.next is None:
            position = Index + Capacity
        else:
            curr = curr.next
            position += 1
    end_name = curr.data[:2]
    return Room + " " + start_name + "-" + end_name

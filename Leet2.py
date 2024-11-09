class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def count_nodes(head):
    count = 0
    curr = head
    while curr is not None:
        count += 1
        curr = curr.next
    return count


def addTwoNumbers(l1, l2):
    muisti = 0
    lenl1 = count_nodes(l1)
    lenl2 = count_nodes(l2)
    head = ListNode()
    valmis = head
    currentl1 = l1
    currentl2 = l2

    for k in range(max(lenl1,lenl2)):
        val1 = currentl1.val if currentl1 else 0
        val2 = currentl2.val if currentl2 else 0

        sum = val1 + val2 + muisti
        if sum > 9:
            valmis.next = ListNode(sum - 10)
            muisti = 1
        else:
            valmis.next = ListNode(sum)
            muisti = 0
        
        valmis = valmis.next   
        if currentl1: currentl1 = currentl1.next
        if currentl2: currentl2 = currentl2.next

    if muisti > 0: 
        valmis.next = ListNode(muisti)
    
    return head.next


def main():
    i = ListNode(2)
    i.next = ListNode(5)
    i.next.next = ListNode(9)
    i.next.next.next = ListNode(1)

    j = ListNode(9)
    j.next = ListNode(8)
    j.next.next = ListNode(1)

    summa = addTwoNumbers(i, j)

    print(summa.val)
    print(summa.next.val)
    print(summa.next.next.val)
    print(summa.next.next.next.val)


if __name__ == "__main__":
    main()
        
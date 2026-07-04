class llnode:
    def __init__(self,val:int,next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = llnode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        temp = llnode(val)
        temp.next = self.head.next
        self.head.next = temp
        if not temp.next:
            self.tail = temp

    def insertTail(self, val: int) -> None:
        temp = llnode(val)
        self.tail.next = temp
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0
        while curr and i < index:
            i += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        ans = []
        curr = self.head.next

        while curr:
            ans.append(curr.val)
            curr = curr.next
        return ans


        

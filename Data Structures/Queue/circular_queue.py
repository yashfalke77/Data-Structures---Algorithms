class Circular_Queue:
    def __init__(self, size) -> None:
        self.size = size
        self.cqueue = [None] * size
        self.front = self.rear = size - 1

    def empty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def full(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def insert(self, value):
        self.rear = (self.rear + 1) % self.size
        if self.full():
            print("Circular Queue is Full")
        else:
            self.cqueue[self.rear] = value

    def remove(self):
        if self.empty():
            return False
        else:
            self.front = (self.front+1) % self.size
            return self.cqueue[self.front]

    def show(self):
        if self.empty():
            print("Circular Queue is Empty")
        else:
            if self.front < self.rear:
                for i in range(self.front + 1, self.rear + 1):
                    print(self.cqueue[i], end=" ")
            else:
                for j in range(self.front + 1, self.size):
                    print(self.cqueue[j], end=" ")
                for k in range(0, self.rear + 1):
                    print(self.cqueue[k], end=" ")


circular_queue = Circular_Queue(4)
circular_queue.insert(10)
circular_queue.insert(20)
circular_queue.insert(30)

circular_queue.show()


# Major disadvantage of circular queue is we cant insert the element at the last position of circular queue
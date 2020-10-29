class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def remove_node(self):
        if self.next:
            self.next.previous = self.previous

        if self.previous:
            self.previous.next = self.next

        self.next = None
        self.previous = None
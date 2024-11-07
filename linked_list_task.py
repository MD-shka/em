class ObjList:
    def __init__(self, data, __next=None, prev=None):
        self.__data = data
        self.__next = __next
        self.__prev = prev

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def get_next(self):
        return self.__next

    def set_prev(self, obj):
        self.__prev = obj

    def get_prev(self):
        return self.__prev


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_obj(self, obj):
        if self.head is None:
            self.head = obj
            self.tail = obj
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj

    def remove_obj(self):
        if self.tail is None:
            return
        if self.tail.get_prev() is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)

    def get_data(self):
        current = self.head
        result = []
        while current:
            result.append(current.get_data())
            current = current.get_next()
        return result

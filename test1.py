from dataclasses import dataclass


class MagicList(list):
    def __init__(self, cls_type=None):
        self.cls_type = cls_type
        self.my_list = []

    def __str__(self):
        return '[{}]'.format(', '.join(str(i) for i in self.my_list))

    def __len__(self):
        return len(self.my_list)

    def extend(self, new_length):
        self.my_list.extend([0] * (new_length - len(self)))

    def __setitem__(self, key, item):
        if key >= len(self):
            self.extend(key + 1)
        self.my_list[key] = item

    def __getitem__(self, item):
        if len(self) == item and self.cls_type is not None:
            self[item] = self.cls_type()
        return self.my_list[item]


@dataclass
class Person:
    age: int = 1


a = MagicList(cls_type=Person)
a[0].age = 5
print(a)
a[1].age = 6
print(a)

# if we will run the next line, we will get error because the index:
# a[4].age = 7
# print(a)


list1 = MagicList()

list1[0] = 5
list1[1] = "hello"
list1[0] = 2
list1[10] = 22
list1[5] = "hey"

print(list1)

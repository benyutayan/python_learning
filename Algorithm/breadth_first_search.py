from collections import deque


class Node(object):
    def __init__(self, value, prev=None, next=None):
        self.value = value
        # 前驱区
        self.prev = prev
        # 后继区
        self.next = next


node1 = Node("lishuo", "you", "lilaoda")
graph = {"you": {"lishuo", "madan", "tangjie"},
         "lishuo": {"lilaoda", "xuejianfen", "lizhen"},
         "madan": {"tianhaixiao", "tianduoduo", "grandatian"},
         "tangjie": {"tagnjieba", "tangjiema", "tangjiejiem"},
         "lilaoda": [],
         "xuejianfen": [],
         "lizhen": [],
         "tianhaixiao": [],
         "tianduoduo": [],
         "grandatian": [],
         "tagnjieba": [],
         "tangjiema": [],
         "tangjiejiem": []}


def search(name):
    path = ""

    search_queue = deque()
    for i in graph[name]:
        search_queue.append(i)

    print(name)
    searched = []

    while search_queue:
        person = search_queue.popleft()
        #print(person + "--->")
        if person not in searched:

            if person_is_seller(person):
                print(person + " is a mango seller! ")
                return True
            else:
                path += person + "--->"
                print(path)
                for i in graph[person]:
                    search_queue.append(i)
                searched.append(person)

    return False


def person_is_seller(person):
    return person[-1] == 'm'


search("you")

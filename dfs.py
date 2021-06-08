class Node:
    def __init__(self,name):
        self.children = []
        self.name = name
    
    def addchild(self,name):
        self.children.append(Node(name))
        return self

    def dfs(self,array):
        array.append(self.name)
        for child in self.children:
            child.dfs(array)
        return array


{
  "nodes": [
    {"children": ["B", "C", "D"], "id": "A", "value": "A"},
    {"children": ["E", "F"], "id": "B", "value": "B"},
    {"children": [], "id": "C", "value": "C"},
    {"children": ["G", "H"], "id": "D", "value": "D"},
    {"children": [], "id": "E", "value": "E"},
    {"children": ["I", "J"], "id": "F", "value": "F"},
    {"children": ["K"], "id": "G", "value": "G"},
    {"children": [], "id": "H", "value": "H"},
    {"children": [], "id": "I", "value": "I"},
    {"children": [], "id": "J", "value": "J"},
    {"children": [], "id": "K", "value": "K"}
  ],
  "startNode": "A"
}



node = Node()
node.dfs(nodes)
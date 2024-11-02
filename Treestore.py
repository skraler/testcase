class Treestore():
    def __init__(self, items):
        self.items= items
        self.items_dict = {item['id']: item for item in items}

    def getAll(self) -> list:
        return self.items

    def getItem(self, id: int) -> dict:
        return self.items_dict.get(id)

    def getChildren(self, id: int) -> list:
        return [item for item in self.items if item['parent'] == id]

    def getAllParents(self, id: int) -> list:
        parents = []
        while id != "root":
            parent = self.items_dict[id]
            parents.append(parent)
            id = parent['parent']
        return parents

ts = Treestore([
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
])

# Test getALL
assert ts.getAll() == [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]

# Test getItem
assert ts.getItem(4) == {"id": 4, "parent": 2, "type": "test"}

# Test getChildren
assert ts.getChildren(4) == [
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]

assert ts.getChildren(5) == []

# Test getAllParents
assert ts.getAllParents(4) == [
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 1, "parent": "root"}
]

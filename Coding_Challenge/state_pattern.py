class Node:
    """
    Represents a tree of Node objectst
    Contains the name of the tag it is parsing, and since it's a tree,
    it should maintain a pointer to the parent node and a list of the node's children in order.
    Some nodes have a text value, but not all of them.
    """
    def __init__(self, tag_name, parent=None):
        self.parent = parent
        self.tag_name = tag_name
        self.children = []
        self.text = ""

    def __str__(self):
        if self.text:
            return self.tag_name + ": " + self.text
        else:
            return self.tag_name


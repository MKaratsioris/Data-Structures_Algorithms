from __future__ import annotations
from typing import Optional
from collections import deque

from definitions import DataTypes

"""
TODO    Implement   getters/setters for Node class

TODO    Implement   logging functionality.
TODO    Implement   unit tests.
"""

class TreeNode:
    """
    A Node class representation, used in Tree.
    
    Attributes
    ----------
    data : DataTypes
        Data to be saved in the node
    children : list[TreeNode]
        A list with all the nodes with one level down
    parent : TreeNode
        The node with one level up
    level : int
        Level of the node in the Tree
    
    Methods
    -------
    add_child(self, child: TreeNode) -> None

    show(self, depth: int = None) -> None

    depth_first_search(self, node: TreeNode = None) -> None

    breadth_first_search(self, node: TreeNode = None) -> None

    it_has(self, data, node: TreeNode = None) -> bool

    """
    def __init__(self, data: DataTypes) -> None:
        self.data: DataTypes = data
        self.children: list[TreeNode] = []
        self.parent: TreeNode = None
        self.level: int = 0
        self.depth: int = 0
    
    def add_child(self, child: TreeNode) -> None:
        """_summary_

        Parameters
        ----------
        child : TreeNode
            _description_
        """
        child.parent = self
        self.children.append(child)
        child.level = self.level + 1
        child.parent.depth += 1
    
    def show(self, depth: int = None) -> None:
        """_summary_

        Parameters
        ----------
        depth : int, optional
            _description_, by default None
        """
        if depth is None:
            depth = self.level
        elif self.level > depth:
            return
        spaces: str = ' ' * self.level * 3
        prefix: str = spaces + '|__' if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.show(depth=depth)
    
    def depth_first_search(self, node: TreeNode = None) -> None:
        """_summary_

        Parameters
        ----------
        node : TreeNode, optional
            _description_, by default None
        """
        if node is None:
            node = self
        print(node.data)
        for child in node.children:
            self.depth_first_search(node=child)
    
    def breadth_first_search(self, node: TreeNode = None) -> None:
        """_summary_

        Parameters
        ----------
        node : TreeNode, optional
            _description_, by default None
        """
        if node is None:
            node = self
        queue: deque = deque([node])
        
        while queue:
            current_node: TreeNode = queue.popleft()
            print(current_node.data)
            queue.extend(current_node.children)
    
    def it_has(self, data, node: TreeNode = None) -> bool:
        """_summary_

        Parameters
        ----------
        data : _type_
            _description_
        node : TreeNode, optional
            _description_, by default None

        Returns
        -------
        bool
            _description_
        """
        if node is None:
            node = self
        if node.data == data:
            return True
        for child in node.children:
            result = self.it_has(data=data, node=child)
            if result:
                return result
        return False

if __name__ == '__main__':
    print("\n=========== TREE NODE ===========")
    print("\n1. add_child")
    root = TreeNode(data='Electronics')
    laptop = TreeNode(data='Laptop')
    cellphone = TreeNode(data='Cellphone')
    tv = TreeNode(data='TV')
    root.add_child(child=laptop)
    root.add_child(child=cellphone)
    root.add_child(child=tv)
    print(f"{len(root.children)=}")
    print(f"{root.data=}")
    print(f"{root.children[0].parent.data=}")
    print(f"{root.children[0].data=}")
    print(f"{len(root.children[0].children)=}")
    
    print("\n2. show")
    laptop.add_child(child=TreeNode(data='Macbook Pro'))
    laptop.add_child(child=TreeNode(data='Surface'))
    laptop.add_child(child=TreeNode(data='Thinkpad'))
    cellphone.add_child(child=TreeNode(data='iPhone'))
    cellphone.add_child(child=TreeNode(data='Google Pixel'))
    cellphone.add_child(child=TreeNode(data='Vivo'))
    tv.add_child(child=TreeNode(data='LG'))
    tv.add_child(child=TreeNode(data='Samsung'))
    for level in range(3):
        print(f"\n----- {level=} -----")
        root.show(depth=level)
        
    print("\n3. depth_first_search")
    root.depth_first_search()
    
    print("\n4. breadth_first_search")
    root.breadth_first_search()
    
    print("\n5. it_has")
    print(f"{root.it_has(data='LG')=}")
    print(f"{root.it_has(data='LGI')=}")
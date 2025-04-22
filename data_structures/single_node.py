from __future__ import annotations
from typing import Optional
from collections import deque

from definitions import DataTypes

"""
TODO    Implement   getters/setters for Node class

TODO    Implement   logging functionality.
TODO    Implement   unit tests.
"""

class SingleNode:
    """
    A Node class representation, used in Single Linked List.
    
    Attributes
    ----------
    data : DataTypes
        Data to be saved in the node
    next_node : SingleNode
        The next node
    """
    def __init__(self, data: DataTypes, next_node: Optional[SingleNode] = None) -> None: # type: ignore
        self.data: DataTypes = data # type: ignore
        self.next_node: SingleNode = next_node
    
    def __str__(self) -> str:
        return f"SingleNode(data={self.data}, next_node={self.next_node})"
    
    def __repr__(self) -> str:
        return f"SingleNode(data={self.data}, next_node={self.next_node})"

if __name__ == '__main__':
    print("\n=========== SINGLE NODE ===========\n")
    print("Saving integer in the node.")
    first_node: SingleNode = SingleNode(data=1)
    print(f"{first_node.data=}")
    print(f"{first_node.next_node=}")
    second_node: SingleNode = SingleNode(data=2)
    third_node: SingleNode = SingleNode(data=4)
    
    
    first_node.next_node = second_node
    second_node.next_node = third_node
    print(f"{first_node.data=}")
    print(f"{first_node.next_node=}")
    print(f"{second_node.data=}")
    print(f"{second_node.next_node=}")
    print(f"{third_node.data=}")
    print(f"{third_node.next_node=}")
    new_node = SingleNode(data=3)
    new_node.next_node = third_node
    second_node.next_node = new_node
    print(f"\n{first_node.data=}")
    print(f"{first_node.next_node=}")
    print(f"{second_node.data=}")
    print(f"{second_node.next_node=}")
    print(f"{new_node.data=}")
    print(f"{new_node.next_node=}")
    print(f"{third_node.data=}")
    print(f"{third_node.next_node=}")
    
    
    print("\nSaving string in the node.")
    first_node: SingleNode = SingleNode(data="1")
    print(f"{first_node.data=}")
    print(f"{first_node.next_node=}")
    second_node: SingleNode = SingleNode(data="2")
    third_node: SingleNode = SingleNode(data="4")
    
    
    first_node.next_node = second_node
    second_node.next_node = third_node
    print(f"{first_node.data=}")
    print(f"{first_node.next_node=}")
    print(f"{second_node.data=}")
    print(f"{second_node.next_node=}")
    print(f"{third_node.data=}")
    print(f"{third_node.next_node=}")
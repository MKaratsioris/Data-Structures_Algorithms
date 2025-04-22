from __future__ import annotations
from typing import Optional
from collections import deque

from definitions import DataTypes

"""
TODO    Implement   getters/setters for Node class

TODO    Implement   logging functionality.
TODO    Implement   unit tests.
"""
class DoubleNode:
    """
    A Node class representation, used in Double Linked List.
    
    Attributes
    ----------
    data : DataTypes
        Data to be saved in the node
    previous_node : DoubleNode
        The previous node
    next_node : DoubleNode
        The next node
    """
    def __init__(self, data: DataTypes, previous_node: Optional[DoubleNode] = None, next_node: Optional[DoubleNode] = None) -> None: # type: ignore
        self.data: DataTypes = data # type: ignore
        self.previous_node: DoubleNode = previous_node
        self.next_node: DoubleNode = next_node
    
    def __str__(self) -> str:
        return f"DoubleNode(data={self.data})"
    
    def __repr__(self) -> str:
        return f"DoubleNode(data={self.data})"


if __name__ == '__main__':
    print("\n=========== DOUBLE NODE ===========\n")
    print("Saving integer in the node.")
    first_node: DoubleNode = DoubleNode(data=1)
    second_node: DoubleNode = DoubleNode(data=2)
    third_node: DoubleNode = DoubleNode(data=4)
    print("\nFirst Node:")
    print(f"{first_node.data=}")
    print(f"{first_node.next_node=}")
    print(f"{first_node.previous_node=}")
    print("\nSecond Node:")
    print(f"{second_node.data=}")
    print(f"{second_node.next_node=}")
    print(f"{second_node.previous_node=}")
    print("\nThird Node:")
    print(f"{third_node.data=}")
    print(f"{third_node.next_node=}")
    print(f"{third_node.previous_node=}")
    print("\n---------------------")
    first_node.next_node = second_node
    second_node.previous_node = first_node
    second_node.next_node = third_node
    third_node.previous_node = second_node
    print("\nFirst Node:")
    print(f"{first_node.data=}")
    print(f"{first_node.next_node=}")
    print(f"{first_node.previous_node=}")
    print("\nSecond Node:")
    print(f"{second_node.data=}")
    print(f"{second_node.next_node=}")
    print(f"{second_node.previous_node=}")
    print("\nThird Node:")
    print(f"{third_node.data=}")
    print(f"{third_node.next_node=}")
    print(f"{third_node.previous_node=}")
    new_node = DoubleNode(data=3)
    new_node.next_node = third_node
    new_node.previous_node = second_node
    second_node.next_node = new_node
    third_node.previous_node = new_node
    print("\n---------------------")
    print("\nFirst Node:")
    print(f"{first_node.data=}")
    print(f"{first_node.next_node=}")
    print(f"{first_node.previous_node=}")
    print("\nSecond Node:")
    print(f"{second_node.data=}")
    print(f"{second_node.next_node=}")
    print(f"{second_node.previous_node=}")
    print("\nThird Node:")
    print(f"{new_node.data=}")
    print(f"{new_node.next_node=}")
    print(f"{new_node.previous_node=}")
    print("\nFourth Node:")
    print(f"{third_node.data=}")
    print(f"{third_node.next_node=}")
    print(f"{third_node.previous_node=}")
    
    
    print("\nSaving string in the node.")
    first_node: DoubleNode = DoubleNode(data="1")
    second_node: DoubleNode = DoubleNode(data="2")
    third_node: DoubleNode = DoubleNode(data="4")
    print("\nFirst Node:")
    print(f"{first_node.data=}")
    print(f"{first_node.next_node=}")
    print(f"{first_node.previous_node=}")
    print("\nSecond Node:")
    print(f"{second_node.data=}")
    print(f"{second_node.next_node=}")
    print(f"{second_node.previous_node=}")
    print("\nThird Node:")
    print(f"{third_node.data=}")
    print(f"{third_node.next_node=}")
    print(f"{third_node.previous_node=}")
    print("\n---------------------")
    first_node.next_node = second_node
    second_node.previous_node = first_node
    second_node.next_node = third_node
    third_node.previous_node = second_node
    print("\nFirst Node:")
    print(f"{first_node.data=}")
    print(f"{first_node.next_node=}")
    print(f"{first_node.previous_node=}")
    print("\nSecond Node:")
    print(f"{second_node.data=}")
    print(f"{second_node.next_node=}")
    print(f"{second_node.previous_node=}")
    print("\nThird Node:")
    print(f"{third_node.data=}")
    print(f"{third_node.next_node=}")
    print(f"{third_node.previous_node=}")
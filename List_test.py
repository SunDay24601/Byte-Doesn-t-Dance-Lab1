import unittest
from hypothesis import given, strategies
from list import UnrolledLinkedList


class Test(unittest.TestCase):

    def test_size(self) -> None:
        self.assertEqual(UnrolledLinkedList().size(), 0)
        self.assertEqual(UnrolledLinkedList(0).size(), 0)
        lst1: UnrolledLinkedList = UnrolledLinkedList(3)
        lst1.add(1)
        self.assertEqual(lst1.size(), 1)
        lst2: UnrolledLinkedList = UnrolledLinkedList(3)
        lst2.add(1)
        lst2.add(2)
        lst2.add(3)
        self.assertEqual(lst2.size(), 3)

    def test_add(self) -> None:
        lst1: UnrolledLinkedList = UnrolledLinkedList(3)
        lst1.add(1)
        self.assertEqual(lst1.to_list(), [1])

        lst2: UnrolledLinkedList = UnrolledLinkedList(3)
        lst2.from_list([1, 2, 3])
        lst2.add(4)
        self.assertEqual(lst2.to_list(), [1, 2, 3, 4])

        lst3: UnrolledLinkedList = UnrolledLinkedList(3)
        for i in range(1, 10):
            lst3.add(i)
        self.assertEqual(lst3.to_list(), list(range(1, 10)))

    def test_get(self) -> None:
        # Test getting elements from an empty list
        lst1: UnrolledLinkedList = UnrolledLinkedList(3)
        self.assertRaises(IndexError, lst1.get, 0)

        # Test getting elements from a list with one node
        lst2: UnrolledLinkedList = UnrolledLinkedList(3)
        lst2.add(1)
        self.assertEqual(lst2.get(0), 1)
        self.assertRaises(IndexError, lst2.get, 1)

        # Test getting elements from a list with multiple nodes
        lst3: UnrolledLinkedList = UnrolledLinkedList(3)
        lst3.from_list([1, 2, 3, 4])
        self.assertEqual(lst3.get(0), 1)
        self.assertEqual(lst3.get(1), 2)
        self.assertEqual(lst3.get(2), 3)
        self.assertEqual(lst3.get(3), 4)
        self.assertRaises(IndexError, lst3.get, 4)

    def test_set(self) -> None:
        # Test setting elements in an empty list
        lst1: UnrolledLinkedList = UnrolledLinkedList(3)
        self.assertRaises(IndexError, lst1.set, 0, 1)

        # Test setting elements in a list with multiple nodes
        lst3: UnrolledLinkedList = UnrolledLinkedList(2)
        lst3.from_list([1, 2, 3])
        lst3.set(1, 5)
        self.assertEqual(lst3.to_list(), [1, 5, 3])
        self.assertRaises(IndexError, lst3.set, 3, 4)

    def test_remove(self) -> None:
        # Test removing elements from an empty list
        lst1: UnrolledLinkedList = UnrolledLinkedList(3)
        self.assertRaises(ValueError, lst1.remove, 1)

        # Test removing an element from a single-node list
        lst2: UnrolledLinkedList = UnrolledLinkedList(3)
        lst2.from_list([1, 2, 3])
        lst2.remove(2)
        self.assertEqual(lst2.to_list(), [1, 3])

        # Test removing elements from a multi-node list
        lst3: UnrolledLinkedList = UnrolledLinkedList(3)
        lst3.from_list([1, 2, 2, 3, 4, 2, 5])
        lst3.remove(2)
        self.assertEqual(lst3.to_list(), [1, 3, 4, 5])

        # Test automatic merging of nodes after removing elements
        lst4: UnrolledLinkedList = UnrolledLinkedList(2)
        lst4.from_list([1, 2, 3, 4, 5])
        lst4.remove(2)
        lst4.remove(3)
        lst4.remove(4)
        self.assertEqual(lst4.to_list(), [1, 5])

    def test_is_member(self) -> None:
        # Test whether an element exists in an empty list
        lst1: UnrolledLinkedList = UnrolledLinkedList(3)
        self.assertFalse(lst1.isMember(1))

        # Test whether an element exists in a single-node list
        lst2: UnrolledLinkedList = UnrolledLinkedList(3)
        lst2.add(1)
        self.assertTrue(lst2.isMember(1))
        self.assertFalse(lst2.isMember(2))

    def test_reverse(self) -> None:
        # Test reversing an empty list
        lst1: UnrolledLinkedList = UnrolledLinkedList()
        lst1.reverse()
        self.assertEqual(lst1.to_list(), [])

        # Test reversing a single-node list
        lst2: UnrolledLinkedList = UnrolledLinkedList(3)
        lst2.add(1)
        lst2.reverse()
        self.assertEqual(lst2.to_list(), [1])

        # Test reversing a multi-node list
        lst3: UnrolledLinkedList = UnrolledLinkedList(3)
        lst3.from_list([1, 2, 3, 4])
        lst3.reverse()
        self.assertEqual(lst3.to_list(), [4, 3, 2, 1])

    def test_filter(self) -> None:
        # Test filtering an empty list
        lst1: UnrolledLinkedList = UnrolledLinkedList(0)
        lst1.filter(lambda x: x % 2 == 0)
        self.assertEqual(lst1.to_list(), [])

        # Test filtering a single-node list
        lst2: UnrolledLinkedList = UnrolledLinkedList(3)
        lst2.add(1)
        lst2.filter(lambda x: x % 2 == 0)
        self.assertEqual(lst2.to_list(), [])

        # Test filtering a multi-node list
        lst3: UnrolledLinkedList = UnrolledLinkedList(3)
        lst3.from_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
        lst3.filter(lambda x: x % 2 == 0)
        self.assertEqual(lst3.to_list(), [2, 4, 6, 8])

    def test_map(self) -> None:
        # Test mapping an empty list
        lst1: UnrolledLinkedList = UnrolledLinkedList()
        lst1.map(lambda x: x * 2)
        self.assertEqual(lst1.to_list(), [])

        # Test mapping a list with elements
        lst2: UnrolledLinkedList = UnrolledLinkedList(3)
        lst2.from_list([1, 2])
        lst2.map(str)
        self.assertEqual(lst2.to_list(), ["1", "2"])

        # Test mapping a multi-node list
        lst3: UnrolledLinkedList = UnrolledLinkedList(3)
        lst3.from_list([1, 2, 3, 4, 5])
        lst3.map(lambda x: x * 2)
        self.assertEqual(lst3.to_list(), [2, 4, 6, 8, 10])

    def test_reduce(self) -> None:
        # Test reducing an empty list
        lst1: UnrolledLinkedList = UnrolledLinkedList()
        self.assertRaises(ValueError, lst1.reduce, lambda x, y: x + y, None)

        # Test reducing a single-node list
        lst2: UnrolledLinkedList = UnrolledLinkedList(3)
        lst2.add(1)
        self.assertEqual(lst2.reduce(lambda x, y: x + y, 0), 1)

        # Test reducing a multi-node list
        lst3: UnrolledLinkedList = UnrolledLinkedList(3)
        lst3.from_list([1, 2, 3, 4, 5])
        self.assertEqual(lst3.reduce(lambda x, y: x + y, 0), 15)

    def test_from_list(self) -> None:
        test_data: list[list[int]] = [[], [1], [1, 2, 3, 4, 5]]
        for e in test_data:
            lst: UnrolledLinkedList = UnrolledLinkedList(3)
            lst.from_list(e)
            self.assertEqual(lst.to_list(), e)

    def test_to_list(self) -> None:
        self.assertEqual(UnrolledLinkedList(3).to_list(), [])

        lst1: UnrolledLinkedList = UnrolledLinkedList(3)
        lst1.add(1)
        self.assertEqual(lst1.to_list(), [1])

        lst2: UnrolledLinkedList = UnrolledLinkedList(3)
        lst2.add(1)
        lst2.add(2)
        lst2.add(3)
        self.assertEqual(lst2.to_list(), [1, 2, 3])

    def test_str(self) -> None:
        # Test string representation of an empty list
        lst1: UnrolledLinkedList = UnrolledLinkedList()
        self.assertEqual(str(lst1), "")

        # Test string representation of a single-node list
        lst2: UnrolledLinkedList = UnrolledLinkedList(3)
        lst2.add(1)
        self.assertEqual(str(lst2), "1")

        # Test string representation of a multi-node list
        lst3: UnrolledLinkedList = UnrolledLinkedList(3)
        lst3.from_list([1, 2, 3, 4, 5])
        self.assertEqual(str(lst3), "1 : 2 : 3 : 4 : 5")

    def test_iter(self) -> None:
        # Test iteration over an empty list
        lst1: UnrolledLinkedList = UnrolledLinkedList(3)
        i = iter(lst1)
        self.assertRaises(StopIteration, lambda: next(i))

        # Test iteration over a non-empty list
        x: list[int] = [1, 2, 3]
        lst2: UnrolledLinkedList = UnrolledLinkedList(3)
        lst2.from_list(x)
        tmp: list[int] = []
        for e in lst2:
            tmp.append(e)
        self.assertEqual(x, tmp)
        self.assertEqual(lst2.to_list(), tmp)

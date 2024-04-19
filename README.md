# Byte Doesn't Dance - lab 1 - variant 1

Unrolled linked list is a variant of linked list data structure. Its 
main purpose is to reduce pointer overhead and improve cache hit rate.

In this program, we implement a data structure based on Unrolled Linked List. 
This data structure provides common linked list operations, including adding, 
getting, setting, and removing elements, as well as other advanced operations 
such as inversion, filtering, mapping, reduction, etc. Through these operations, 
we can store and operate elements of integer type in unrolled Linked List.

## Project structure

- `list.py` -- implementation of `UnrolledNode` class and `UnrolledLinkedList` class 
- with multiple functions, including adding, getting, setting, and removing elements, 
- as well as other advanced operations
   Stateless.
- `List_test.py` -- unit and PBT tests for `unrolled linked list`.

## Features

- PBT: `test_add_commutative`

## Contribution

- `Hu Jinghao` (1206041060@qq.com) 
  - Add all type annotations.
  - Implement most functions.
  - Implement most of the test.

- `Meng Chenxu` (xxx@qq.com) edited by `Hu Jinghao`. It still needs to be edited.
  - Implement all function.
  - Implement all test.

## Changelog

- 19.04.2024 - 3
  - Add type annotations.
- 19.04.2024 - 2
  - Add test coverage.
- 19.04.2024 - 1
  - Update README. Add formal sections.
- 18.04.2024 - 0
  - Initial

## Design notes

- Compared with traditional singly linked lists, unrolled linked lists store multiple 
- elements in one node instead of one element corresponding to one node. This allows 
- us to focus on storing multiple elements in a single node to reduce memory overhead 
- and improve cache hits. It has advantages of efficiency. When the number of elements 
- is large, unrolled linked list can improve memory utilization and access efficiency.

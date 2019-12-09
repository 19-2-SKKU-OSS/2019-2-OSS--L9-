# Bitonic-Sort

Bitonic mergesort is a parallel algorithm for sorting. It is also used as a construction method for building a sorting network. 
The algorithm was devised by Ken Batcher. The resulting sorting networks consist of 
{\displaystyle O(n\log ^{2}(n))}O(n\log ^{2}(n)) comparators and have a delay of 
{\displaystyle O(\log ^{2}(n))}O(\log ^{2}(n)), where {\displaystyle n}n is the number of items to be sorted.[1]

A sorted sequence is a monotonically non-decreasing (or non-increasing) sequence. A bitonic sequence is a sequence with {\displaystyle x_{0}\leq \cdots \leq x_{k}\geq \cdots \geq x_{n-1}}x_{0}\leq \cdots \leq x_{k}\geq \cdots \geq x_{n-1} for some {\displaystyle k,0\leq k<n}k,0\leq k<n, or a circular shift of such a sequence.

## Sorting bitonic sequences

Implemented in bitonic.cpp.

![alt text](https://raw.githubusercontent.com/AntoinePassemiers/Bitonic-Sort/master/doc/imgs/bitonic.png)

## Sorting arbitrary sequences

Implemented in arbitrary.cpp.

![alt text](https://raw.githubusercontent.com/AntoinePassemiers/Bitonic-Sort/master/doc/imgs/arbitrary.png)

## Complexity

| Name                  | Best            | Average             | Worst               | Memory    | Stable    | Comments  |
| --------------------- | :-------------: | :-----------------: | :-----------------: | :-------: | :-------: | :-------- |
| **Bitonic sort**       | n               | n<sup>2</sup>       | n<sup>2</sup>       | 1         | No       |           |

## References
 - [Wikipedia](https://en.wikipedia.org/wiki/Bitonic_sorter)

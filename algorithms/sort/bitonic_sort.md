# Bitonic Sort

Bitonic mergesort is a parallel algorithm for sorting. It is also used as a construction method for building a sorting network. 
The algorithm was devised by Ken Batcher. The resulting sorting networks consist of 
 `O(n log² n)` comparators and have a delay of 
`O(log² n)`, where n is the number of items to be sorted.

A sorted sequence is a monotonically non-decreasing (or non-increasing) sequence. 
A bitonic sequence is a sequence with x0 for some k, 0<=k<n, or a circular shift of such a sequence.

## Sorting bitonic sequences

![alt text](https://raw.githubusercontent.com/AntoinePassemiers/Bitonic-Sort/master/doc/imgs/bitonic.png)

## Sorting arbitrary sequences

![alt text](https://raw.githubusercontent.com/AntoinePassemiers/Bitonic-Sort/master/doc/imgs/arbitrary.png)

## Complexity

| Name                  | Best            | Average             | Worst               | Memory    | Stable    | Comments  |
| --------------------- | :-------------: | :-----------------: | :-----------------: | :-------: | :-------: | :-------- |
| **Bitonic sort**       | log²n               | log<sup>2</sup>n       | log<sup>2</sup>n      |nlog²n         | No       | parellel time      |

## References
 - [Wikipedia](https://en.wikipedia.org/wiki/Bitonic_sorter)
 - [Youtube](https://www.youtube.com/watch?v=GEQ8y26blEY)

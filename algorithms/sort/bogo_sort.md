# Bogo Sort

In computer science, BogoSort also known as permutation sort, stupid sort, slow sort, shotgun sort or monkey sort is 
a particularly ineffective algorithm based on generate and test paradigm. The algorithm successively 
generates permutations of its input until it finds one that is sorted.
For example, if bogosort is used to sort a deck of cards, it would consist of checking if the deck were in order, 
and if it were not, one would throw the deck into the air, pick the cards up at random, 
and repeat the process until the deck is sorted.

![Algorithm Visualization](https://idea-instructions.com/bogo-sort.png)
![Time complexity by n times](https://raw.githubusercontent.com/joscha0/ExoticAlgorithms/master/img/bogoSort.png)

## Complexity

| Name                  | Best            | Average             | Worst               | Memory    | Stable    | Comments  |
| --------------------- | :-------------: | :-----------------: | :-----------------: | :-------: | :-------: | :-------- |
| **Bogo Sort**         | n               | n!                  | ∞                   |  1        | Yes       |           |

## References

- [Wikipedia](https://en.wikipedia.org/wiki/Bogosort)
- [YouTube](https://www.youtube.com/watch?v=eU4CQ_kA22g)
- [Rosetta Code](https://rosettacode.org/wiki/Sorting_algorithms/Bogosort)

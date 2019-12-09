---
title: 'Project Overview'

layout: nil
---

Fork한 Repository 주소: https://github.com/keon/algorithms
<br>
<p align="center"><img src="https://raw.githubusercontent.com/keon/algorithms/master/docs/source/_static/logo/logotype1blue.png"></p>

# Pythonic Data Structures and Algorithms

Minimal and clean example implementations of data structures and algorithms in Python 3.

## Tests

### Use unittest
For running all tests write down:

    $ python3 -m unittest discover tests

For running some specific tests you can do this as following (Ex: sort):

    $ python3 -m unittest tests.test_sort

### Use pytest
For running all tests write down:

    $ python3 -m pytest tests

## Install
If you want to use the API algorithms in your code, it is as simple as:

    $ pip3 install algorithms

You can test by creating a python file: (Ex: use `merge_sort` in `sort`)

```python3
from algorithms.sort import merge_sort

if __name__ == "__main__":
    my_list = [1, 8, 3, 5, 6]
    my_list = merge_sort(my_list)
    print(my_list)
```

## Uninstall
If you want to uninstall algorithms, it is as simple as:

    $ pip3 uninstall -y algorithms

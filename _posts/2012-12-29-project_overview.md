---
title: '프로젝트 개요'

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

You can test by creating a python file: (Ex: use 'merge_sort' in 'sort')

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

## Contribute
If you want to contribute this project, click <a href="https://github.com/keon/algorithms/blob/master/CONTRIBUTING.md">this</a>

<hr>
# 프로젝트 활동 내용 요약
1. 프로젝트의 오타 수정
2. 원 repository의 issue를 받아서 코드 추가 및 수정
3. 프로젝트 모듈에 더욱 추가하고 싶은 알고리즘 코드 추가

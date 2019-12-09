---
title: '프로젝트 개요'

layout: nil
---

Fork한 Repository 주소: https://github.com/keon/algorithms
<br>
<p align="center"><img src="https://raw.githubusercontent.com/keon/algorithms/master/docs/source/_static/logo/logotype1blue.png"></p>

# 파이썬으로 자료구조 및 알고리즘 구현

Python3에서 자료구조와 알고리즘의 최소한의 깔끔한 구현을 목표로 하는 프로젝트.

## 테스트

### unittest 이용
작성된 모든 테스트를 수행하기 위해서:

    $ python3 -m unittest discover tests

몇 가지 특정 테스트를 실행하기 위해서는 다음과 같이 수행해야 한다. (예: sort):

    $ python3 -m unittest tests.test_sort

### pytest 이용
작성된 모든 테스트를 수행하기 위해서:

    $ python3 -m pytest tests

## 설치
만약 여러분의 코드에 이 프로젝트에서의 알고리즘 API를 적용하고 :

    $ pip3 install algorithms

파이썬 파일을 만들어서 검사할 수 있습니다: (예: use 'merge_sort' in 'sort')

```python3
from algorithms.sort import merge_sort

if __name__ == "__main__":
    my_list = [1, 8, 3, 5, 6]
    my_list = merge_sort(my_list)
    print(my_list)
```

## 제거
만약 알고리즘 모듈을 제거하고 싶다면:

    $ pip3 uninstall -y algorithms

## 프로젝트 기여
만약 여러분이 이 프로젝트에 기여하고 싶으시다면, 다음 <a href="https://github.com/keon/algorithms/blob/master/CONTRIBUTING.md">링크</a>를 클릭해주세요.

<hr>
# 프로젝트 활동 내용 요약
1. 프로젝트의 오타 수정
2. 원 repository의 issue를 받아서 코드 추가 및 수정
3. 프로젝트 모듈에 더욱 추가하고 싶은 알고리즘 코드 추가

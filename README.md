# 2019-2-OSS-L9

## Original Project
https://github.com/keon/algorithms
<br>
<p align="center"><img src="https://raw.githubusercontent.com/keon/algorithms/master/docs/source/_static/logo/logotype1blue.png"></p>

### Pythonic Data Structures and Algorithms

Minimal and clean example implementations of data structures and algorithms in Python 3.

### Tests

#### Use unittest
For running all tests write down:

    $ python3 -m unittest discover tests

For running some specific tests you can do this as following (Ex: sort):

    $ python3 -m unittest tests.test_sort

#### Use pytest
For running all tests write down:

    $ python3 -m pytest tests

### Install
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

### Uninstall
If you want to uninstall algorithms, it is as simple as:

    $ pip3 uninstall -y algorithms

## Members

**이창원 Lee ChangWon `lcw921`**
- Student ID : 2015313527
- E-mail : leechangwon921@gmail.com
- Static Page : https://lcw921.github.io/static_page/

**한영진 Han YoungJin `skkuYJ`**
- Student ID : 2016314770
- E-mail : soulstory24@naver.com
- Static Page : https://skkuYJ.github.io/static_page/

**안현준 Ahn HyunJun `NthreeAhn`**
- Student ID : 2018310737
- E-mail : a.hyunjun1999@gmail.com
- Static Page : https://nthreeahn.github.io/static_page/

**강민우 Kang MinWoo `r0ya1je11y`**
- Student ID : 2018311929
- E-mail : skydnk4332@gmail.com
- Static Page : https://r0ya1je11y.github.io/static_page/

**금상인 Geum SangIn `sangingeum`**
- Student ID : 2018311642
- E-mail : sangingeum@gmail.com
- Static Page : https://sangingeum.github.io/static_page/FirstPost/

## Contribution

1. 프로젝트의 오타 수정
2. 원 repository의 issue를 받아서 코드 추가 및 수정
3. 프로젝트 모듈에 더욱 추가하고 싶은 알고리즘 코드 추가
> 프로젝트에 관해 자세한 내용은 <a href="https://19-2-skku-oss.github.io/2019-2-OSS-L9/">Team GitHub Page</a>에서 확인하실 수 있습니다.

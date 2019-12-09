---
title: '프로젝트 개요'

layout: nil
---

Fork한 Repository 주소: https://github.com/keon/algorithms
<br>
<p align="center"><img src="https://raw.githubusercontent.com/keon/algorithms/master/docs/source/_static/logo/logotype1blue.png"></p>

# 파이썬으로 자료구조 및 알고리즘 구현

<p>이 프로젝트는 Python3 언어에서 자료구조와 알고리즘의 직접적인 구현과 모듈화를 주 목표로 하고 있습니다. 또한, 자료구조와 알고리즘의 이해를 돕는 테스트 예제도 포함하고 있습니다.</p>
<p>Python3 코드 안에서 이 알고리즘 모듈을 불러오게 하여, 사용자로 하여금 자신의 프로그램에서 간단하게 자료구조 및 알고리즘을 사용할 수 있도록 하고 있습니다.
    이 프로젝트에서 구현한 모듈의 설치 방법에는 아래에 더욱 자세하게 설명을 해 놓았습니다.</p>

## 설치
만약 여러분의 코드에 이 프로젝트에서의 알고리즘 API를 적용하고 싶다면, 다음과 같이 작성하세요:

    $ pip3 install algorithms

정상적으로 설치되었는지는 파이썬 파일을 만들어서 검사할 수 있습니다: (예: use 'merge_sort' in 'sort')

```python3
from algorithms.sort import merge_sort

if __name__ == "__main__":
    my_list = [1, 8, 3, 5, 6]
    my_list = merge_sort(my_list)
    print(my_list)
```

## 프로젝트 기여
만약 여러분이 이 프로젝트에 기여하고 싶으시다면, 다음 <a href="https://github.com/keon/algorithms/blob/master/CONTRIBUTING.md">링크</a>를 클릭해주세요.

# 팀 활동 
<p>저희는 이 프로젝트에 기여하기 위해서, Issue를 통해 적극적으로 토의하고, 각자 관심 있는 부분을 선택해서 코드를 작성하고 수정하는 등의 과정을 거쳤습니다. 자세한 내용은 이어지는 문단에서 설명하고 있습니다.</p>

## 프로젝트 활동 내용 요약
1. 프로젝트의 오타 수정
2. 원 repository의 issue를 받아서 코드 추가 및 수정
3. 프로젝트 모듈에 더욱 추가하고 싶은 알고리즘 코드 추가

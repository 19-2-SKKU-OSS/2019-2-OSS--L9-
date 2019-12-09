---
category: 팀 활동
path: '/stuff/'
title: '주요 커밋 및 풀리퀘스트 활동'


layout: nil
---
### 주요 커밋 활동
- Path_from_unweighted_graph(skkuYJ)
    - 11월 27일 Path_from_unweighted_graph.py 추가
<br>    
- all pairs shortest path(lcw921)
    - 12월 1일 all_pairs_shortest_path.py 추가
    <br>all_pairs_shortest_path의 구현은 floyd-warshall algorithm을 사용하였다. 
    <br>시간 복잡도는 O(E^3)이며, 기존에 자주 사용하던 알고리즘이기 때문에, 큰 어려움을 겪지 않고 빠르게 개발에 착수, 완료할 수 있었다.
    <br>
    - 12월 6일 unittest 추가 요청
    <br>
    - 12월 7일 unittest 추가 완료
    <br>단위테스트를 추가해달라는 요청을 받았다. 단위테스트에 대한 자료를 찾아보며, 단위테스트의 중요성을 알게 되었고, 파이썬에서는 단위테스트를 간편하게 수행할 수 있다는 것을 알게되어 이를 추가하였다.
    <br>
    - 12월 9일 새로운 conflict 해결 요청
    <br>
    - 12월 9일 conflict 해결 완료
    <br>master 브랜치에 다른 풀 리퀘스트가 추가됨에 따라, 기존의 코드로 작성하였던, 내 코드가 충돌이 발생하였고, 이를 해결해달라는 요청을 받았다.
    <br>수정해야할 부분을 깃허브를 통해 빠른 시간내에 수정할 수 있었다.
- maximum flow(lcw921)
    - 12월 3일 maximum_flow_bfs.py 추가
    <br>
    - 12월 4일 maximum_flow_dfs.py 추가
    <br>maximum flow를 Ford Fulkerson 알고리즘을 통해 구하는 모듈을 작성해달라는 issue를 확인하여, 이를 구현하려 시도하였다.
    <br>bfs와 dfs를 사용한 모든 방법을 추가해달라고 요구하였기 때문에, 두 방법 모두 추가하였다.
    <br>두 방법은 큰 차이 없이, 자료구조를 queue를 사용하느냐, stack을 사용하느냐의 차이만을 통해 구현하였기 때문에, 큰 어려움을 겪지 않았다.
    <br>
    - 12월 6일 unittest 추가 요청
    <br>
    - 12월 7일 unittest 추가 완료
    <br>마찬가지로 단위테스트를 추가해달라는 요청을 받았다. 
    <br>파이썬에서는 단위테스트를 간편하게 수행할 수 있었기 때문에 이를 간편히 추가하였다.
    <br>
    - 12월 9일 새로운 conflict 해결 요청
    <br>
    - 12월 9일 conflict 해결
    <br>마찬가지로 master 브랜치에 다른 풀 리퀘스트가 추가됨에 따라, 기존의 코드로 작성하였던, 내 코드가 충돌이 발생하였고, 이를 해결해달라는 요청을 받았다.
    <br>수정해야할 부분을 깃허브를 통해 빠른 시간내에 수정할 수 있었다.
    <br>코드의 가독성을 위해 example로 되어있는 배열등을 좀 더 가독성이 나은 방식으로 수정해주기를 요청받았기에 이를 수정하였다.
- blocking_virus(skkuYJ)
    - 12월 3일 blocking_viurs.py 추가
    <br>
    - 12월 8일 blocking_virus.py 테스트케이스 추가
    - 12월 9일 blocking_virus.py 테스트케이츠 추가
- bellman_ford(NthreeAhn)
    - 12월 3일 bellman_ford.py 알고리즘 추가:
    <br> Bellman-Ford 알고리즘을 이용해 Shortest Path 문제 해결 가능 여부 판단 
    <br>
    - 12월 6일 unittest 형태로 테스트케이스 추가 요청
    <br> test case 형식을 unittest로 작성할 것을 요청받음
    <br>
    - 12월 8일 unittest 추가 완료
    <br> 음수 값을 가진 path가 있으면서 shortest path가 존재하는 경우
    <br>
    - 12월 9일 pull request 승인 완료
- dfa(NthreeAhn)
    - 12월 5일 dfa.py 및 automata 하위 범주 추가:
    <br>새로운 알고리즘 범주 추가 & DFA acceptance 여부 판단 알고리즘 작성
    <br>
    - 12월 6일 unittest 추가 요청:
    <br> test case 형식을 unittest로 작성해 줄 것을 요청받음
    <br>
    - 12월 8일 unittest 추가 완료:
    <br> 0과 1로 이루어진 문자열 중 0의 개수가 짝수개인 DFA 승인 케이스
    <br>
    - 12월 9일 테스트케이스 추가 요청:
    <br> 추가적인 테스트케이스 요청받음
    <br>
    - 12월 9일 테스트케이스 추가 완료:
    <br> 0과 1로 이루어진 문자열 중 001을 포함하지 않는 경우 DFA 케이스 추가
    <br> a와 b로 이루어진 문자열 중 bba를 포함하는 경우 DFA 케이스 추가
- Sort Description(skkuYJ)
    - 12월 9일 counting_sort.md 추가 (정의, 이미지, 복잡도, 참고 링크)
    - 12월 9일 merge_sort.md 추가 (정의, 이미지, 복잡도, 참고 링크)
    - 12월 9일 bubble_sort.md 추가 (정의, 이미지, 복잡도, 참고 링크)
    - 12월 9일 heap_sort.md 추가 (정의, 이미지, 복잡도, 참고 링크)
    - 12월 9일 insertion_sort.md 추가 (정의, 이미지, 복잡도, 참고 링크)
    - 12월 9일 quick_sort.md 추가 (정의, 이미지, 복잡도, 참고 링크)
    - 12월 9일 radix_sort.md 추가 (정의, 이미지, 복잡도, 참고 링크)
    - 12월 9일 selection_sort.md 추가 (정의, 이미지, 복잡도, 참고 링크)
    - 12월 9일 radix_sort.md 추가 (정의, 이미지, 복잡도, 참고 링크)
    - 12월 10일 bitonic_sort.md 추가 (정의, 이미지, 복잡도, 참고 링크)
    - 12월 10일 bogo_sort.md 추가 (정의, 이미지, 복잡도, 참고 링크)

### 풀리퀘스트 활동

- 풀리퀘스트 시도 중
    - all_pairs_shortest_path<br>
    <img width="300" alt="all_pairs_shortest_path" src="https://github.com/19-2-SKKU-OSS/2019-2-OSS-L9/blob/gh-pages/images/allpairs.PNG?raw=true"> <br>
    - maximum_flows_bfs & maximum_flows_dfs<br>
    <img width="300" alt="maximum_flows" src="https://github.com/19-2-SKKU-OSS/2019-2-OSS-L9/blob/gh-pages/images/maximum_flow.PNG?raw=true"> <br>
    - dfa<br>
    <img width="300" alt="dfa" src="https://github.com/19-2-SKKU-OSS/2019-2-OSS-L9/blob/gh-pages/images/dfa.PNG?raw=true"> <br>
    - path_from_unweighted_graph<br>
    <img width="300" alt="path_from_unweighted_graph" src="https://github.com/19-2-SKKU-OSS/2019-2-OSS-L9/blob/gh-pages/images/path_from_unweighted_graph_pull_request.PNG?raw=true"> <br>
- 풀리퀘스트 승인 완료
    - bellman_ford<br>
    <img width="300" alt="주제 선별 스크린샷3" src="https://github.com/19-2-SKKU-OSS/2019-2-OSS-L9/blob/gh-pages/images/bellman.PNG?raw=true"> <br>

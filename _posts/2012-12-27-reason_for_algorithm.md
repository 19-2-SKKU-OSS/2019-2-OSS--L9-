---
category: Stuff
path: '/stuff'
title: '프로젝트 선정 과정 '


layout: nil
---

### 팀 주제 의견 수합

<img width="814" alt="주제 선별 스크린샷" src="https://github.com/19-2-SKKU-OSS/2019-2-OSS-L9/blob/gh-pages/images/%EC%BA%A1%EC%B2%98.PNG?raw=true"> <br>

* The headers must include a **valid authentication token**.

### Response

Sends back a collection of things.

```Status: 200 OK```
```{
    {
        id: thing_1,
        name: 'My first thing'
    },
    {
        id: thing_2,
        name: 'My second thing'
    }
}```

For errors responses, see the [response status codes documentation](#response-status-codes).

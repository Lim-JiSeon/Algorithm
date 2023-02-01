# 숫자 비교하기(비교연산)

## 문제 설명
정수 num1과 num2가 매개변수로 주어집니다. 두 수가 같으면 1 다르면 -1을 retrun하도록 solution 함수를 완성해주세요.

## 문제 풀이
- SAME_NUMBER/DIFFERENT_NUMBER 변수 만들기<br>
*SAME_NUMBER/DIFFERENT_NUMBER : num1과 num2가 같으면 1, 다르면 -1을 리턴하는 역할 제공*
```python
SAME_NUMBER = 1
DIFFERENT_NUMBER = -1
```
```javascript
const SAME_NUMBER = 1;
const DIFFERENT_NUMBER = -1;
```

## 코드
### Python 코드
```python
SAME_NUMBER = 1
DIFFERENT_NUMBER = -1

def solution(num1, num2):
    if num1 == num2:
        return SAME_NUMBER
    return DIFFERENT_NUMBER
```

### JavaScript 코드
```javascript
const SAME_NUMBER = 1;
const DIFFERENT_NUMBER = -1;

function solution(num1, num2) {
    if (num1 === num2)
        return SAME_NUMBER;
    return DIFFERENT_NUMBER;
}
```

# 몫 구하기(사칙연산)

## 문제 설명
정수 num1, num2가 매개변수로 주어질 때, num1을 num2로 나눈 몫을 return 하도록 solution 함수를 완성해주세요.

## 문제 풀이
- get_quotient/getQuotient 함수 만들기<br>
*get_quotient/getQuotient(num1, num2) : num1을 num2로 나눈 몫을 구하는 기능 제공*
```python
def get_quotient(num1, num2):
    return num1//num2
```
```javascript
function divide(num1, num2) {
    return num1/num2;
}

function getQuotient(num1, num2) {
    return parseInt(divide(num1, num2));
}
```

## 코드
### Python 코드
```python
def get_quotient(num1, num2):
    return num1//num2

def solution(num1, num2):
    return get_quotient(num1, num2)
```

### JavaScript 코드
```javascript
function divide(num1, num2) {
    return num1/num2;
}

function getQuotient(num1, num2) {
    return parseInt(divide(num1, num2));
}

function solution(num1, num2) {
    return getQuotient(num1, num2);
}
```

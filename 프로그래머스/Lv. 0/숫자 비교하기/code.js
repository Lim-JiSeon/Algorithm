const SAME_NUMBER = 1;
const DIFFERENT_NUMBER = -1;

function solution(num1, num2) {
    if (num1 === num2)
        return SAME_NUMBER;
    return DIFFERENT_NUMBER;
}

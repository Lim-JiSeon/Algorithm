function solution(n,a,b)
{
    var answer = 0;

    while (a !== b) {
        answer += 1;
        a = Math.round(a / 2)
        b = Math.round(b / 2)
    }

    return answer;
}
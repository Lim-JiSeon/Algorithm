function sum(n) {
    return n * (n + 1) / 2;
}

function solution(n) {
    let num = 1;
    let count = 0;
    while (n > sum(num - 1)) {
        if ((n - sum(num - 1)) % num === 0) count += 1;
        num += 1;
    }
    return count;
}
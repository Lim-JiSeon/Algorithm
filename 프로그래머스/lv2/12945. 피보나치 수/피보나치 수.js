function solution(n) {
    let fib1 = 0;
    let fib2 = 1;
    for (let i = 2; i <= n; i++) {
        const newFib = (fib1 + fib2) % 1234567;
        fib1 = fib2;
        fib2 = newFib;
    }
    return fib2;
}
function solution(s) {
    const stack = [];
    for (const item of s) {
        if (!stack || stack[stack.length - 1] !== item)
            stack.push(item);
        else
            stack.pop();
    }
    return stack.length ? 0 : 1;
}
function solution(brown, yellow) {
    const mulValue = brown + yellow;
    const plusValue = (mulValue - yellow + 4) / 2;
    const row = (plusValue + Math.sqrt(plusValue**2 - 4*mulValue)) / 2;
    const col = plusValue - row;
    return [row, col];
}
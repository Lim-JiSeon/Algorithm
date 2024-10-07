function solution(diffs, times, limit) {
    var answer = 0;
    
    // level의 범위는 1 ~ diffs의 최대값 사이로 정의
    // 반복문을 모두 탐색할 시 시간초과, 이진탐색 사용
    let left = 1;
    // js는 약 10000~20000의 크기를 갖는 자바스크립트의 호출 스택 범위를 넘어가는 경우 RangeError: Maximum call stack size exceeded 란 런타임에러를 발생시키기 때문에 Math.max(...diffs) 대신 아래 코드 사용
    let right = diffs.reduce((acc, cur) => Math.max(acc, cur), 1);
    let middle = Math.floor((right + left) / 2);
    
    while(left <= right) {
        let total_limit = calculate(diffs, times, middle);
        
        // limit 보다 작거나 같으면 level의 값을 작게 함으로써 total_limit의 값이 크게 나오게 시도
        if (total_limit <= limit) {
            right = middle - 1;
        } else {
            // limit 보다 크면 level의 값을 크게 함으로써 total_limit의 값이 작게 나오게 설정
            left = middle + 1;
        }
        
        middle = Math.floor((right + left) / 2);
    }
    
    answer = left;
    return answer;
}

// 모든 퍼즐 해결 시간 계산 함수
function calculate(diffs, times, level) {
    let total_time = 0;
    
    for (let index in diffs) {
        if (level >= diffs[index]) {
            total_time += times[index];
        } else {
            total_time += (times[index] + times[index - 1])*(diffs[index] - level) + times[index];
        }
    }
    
    return total_time;
}


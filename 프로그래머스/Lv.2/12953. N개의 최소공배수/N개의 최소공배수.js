function findLCM(a, b) {
    var lcm = a > b ? a : b
    while (true) {
        if (lcm % a === 0 && lcm % b === 0) break
        lcm += 1
    }
    return lcm
}

function solution(arr) {
    var answer = 0
    
    var prev = arr[0]
    for (let i = 1; i < arr.length; i++) {
        answer = findLCM(prev, arr[i])
        prev = answer
    }
    return answer
}
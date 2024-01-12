function findDuplicates(arr) {
  return arr.filter(function(item, index) { return arr.indexOf(item) !== index })
}

function solution(n, words) {
    var answer = [0,0];
    
    const duplicates = findDuplicates(words)
    
    if (duplicates.length) {
        const duplicateIndex = words.lastIndexOf(duplicates[0]);
        
        const user = (duplicateIndex % n) + 1;
        const number = parseInt(duplicateIndex / n) + 1;
        
        answer = [user, number]
    } else {
        var alpha = words[0];
        
        for(let i = 1; i < words.length; i++) {
            if (alpha[alpha.length - 1] !== words[i][0]) {
                const index = words.indexOf(words[i]);

                const user = (index % n) + 1;
                const number = parseInt(index / n) + 1;

                answer = [user, number];
                break;
            }
            else {
                alpha = words[i]; 
            }
        }
    }

    return answer;
}
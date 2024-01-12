function solution(n)
{
    var ans = n % 2 ? 1 : 0;

    while(n > 1) {
        n = parseInt(n / 2)
        
        if (n % 2) {
            ans += 1
            n -= 1
        }
    }

    return ans;
}

function solution(s) {
    return s.toLowerCase().split(" ")
        .map(str => {
            if(str) return str.replace(str[0], str[0].toUpperCase())
            else return ""
        })
        .join(" ")
}
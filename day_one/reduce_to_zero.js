/**
 * @param {number} num
 * @return {number}
 */
var numberOfSteps  = function(num) {
    let answer = 0
    while (num !== 0){
        if (num % 2 === 0){
            num = num / 2
            answer = answer + 1
        }
        else if (num > 0){
            num = num -1
            answer = answer + 1
        }
    }
    return answer
};

function power_two(x){
    if(x > 0){
        let ln = Math.log(x) / Math.log(2)
        if(Number.isInteger(ln)){
            return  true
        }
        else{
            return false
        }
    }
    return 'Number has to be greater than 0'
}

console.log(power_two(8))//true
console.log(power_two(6))//false
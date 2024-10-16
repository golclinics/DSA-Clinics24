const reverse_integer = (num) => {

    num_string = num.toString()

    if (num<0) {
        num_reversed = '-' + num_string.slice(0).split('').reverse().join('')

    }else {
        num_reversed = num_string.split('').reverse().join('')
    } 

    return parseInt(num_reversed)
}

console.log(reverse_integer(21));   
console.log(reverse_integer(-56));   
console.log(reverse_integer(500));   
console.log(reverse_integer(-90)); 
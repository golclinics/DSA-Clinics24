<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<script>
 /*Write a program that prints the numbers from 1 to 100. For multiples of 3, print Fizz; for
multiples of 5, print Buzz; and for numbers that are multiples of both 3 and 5, print FizzBuzz.*/

/**/
    const final=[];
    let num = 1;
    console.log(num);
    while (num<=100){
        if (num%3==0 && num%5==0){
            final.push("FIZZBUZZ");
        }
        else if(num%3==0){
            final.push("FIZZ");
        }
        else if (num%5==0){
            final.push("BUZZ");
        }
        else{
            final.push(num);
        }
    num++;
    }
    console.log(final);

</script>
</body>
</html>

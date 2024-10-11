for (g=0; g <= 100; g++) {

    if (g % 3 === 0 && g % 5 === 0) {
        console.log("fizzbuzz");
    } else if (g % 3 === 0) {
        console.log("fizz");
    } else if (g % 5 === 0) {
        console.log("buzz");
    } else {
        console.log((g));
    }
}
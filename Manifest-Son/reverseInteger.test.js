const reverse = require('./reverseInteger'); 

describe('Reversing an integer', () => {
    // Test for positive integers
    test('reverses positive integers', () => {
        expect(reverse(123)).toBe(321); 
        expect(reverse(91)).toBe(19);   
        expect(reverse(500)).toBe(5);   
        expect(reverse(1)).toBe(1);     
    });

    // Test for negative integers
    test('reverses negative integers', () => {
        expect(reverse(-56)).toBe(-65);   
        expect(reverse(-90)).toBe(-9);    
        expect(reverse(-1234)).toBe(-4321); 
    });

    // Test for edge cases
    test('handles edge cases', () => {
        expect(reverse(0)).toBe(0);        
        expect(reverse(100000)).toBe(1);   
        expect(reverse(-100000)).toBe(-1); 
    });
});

const isPowerOfTwo = require('../DSA-Clinics24/ItotiaHarrison/power_of_two');

test('8 should be a power of two', () => {
    expect(isPowerOfTwo(8)).toBe(true);
});

test('6 should not be a power of two', () => {
    expect(isPowerOfTwo(6)).toBe(false);
});

test('1 should be a power of two', () => {
    expect(isPowerOfTwo(1)).toBe(true);
});

test('0 should not be a power of two', () => {
    expect(isPowerOfTwo(0)).toBe(false);
});

test('Negative numbers should not be powers of two', () => {
    expect(isPowerOfTwo(-2)).toBe(false);
    expect(isPowerOfTwo(-16)).toBe(false);
});
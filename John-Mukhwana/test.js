const assert = require('assert');
const reverseInteger = require('./Reverse_Zeros');

// Test cases
function runTests() {
    console.log('Running tests for reverseInteger function...');

    // Test case 1: Positive number
    assert.strictEqual(reverseInteger(500), 5, 'Test case 1 failed: 500 should reverse to 5');

    // Test case 2: Negative number
    assert.strictEqual(reverseInteger(-56), -65, 'Test case 2 failed: -56 should reverse to -65');

    // Test case 3: Number ending with zero
    assert.strictEqual(reverseInteger(-90), -9, 'Test case 3 failed: -90 should reverse to -9');

    // Test case 4: Two-digit number
    assert.strictEqual(reverseInteger(91), 19, 'Test case 4 failed: 91 should reverse to 19');

    // Test case 5: Single-digit number
    assert.strictEqual(reverseInteger(7), 7, 'Test case 5 failed: 7 should reverse to 7');

    // Test case 6: Zero
    assert.strictEqual(reverseInteger(0), 0, 'Test case 6 failed: 0 should reverse to 0');

    // Test case 7: Large number
    assert.strictEqual(reverseInteger(1234567), 7654321, 'Test case 7 failed: 1234567 should reverse to 7654321');

    console.log('All tests passed successfully!');
}

runTests();
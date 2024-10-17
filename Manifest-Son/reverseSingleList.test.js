const { reverseLinkedList, createLinkedList, linkedListToArray } = require('./reverseSingleList');

describe('Linked List Reversal', () => {
  test('reverses an array list', () => {
    const originalList = [1, 2, 3, 4, 5];
    const expected = [5, 4, 3, 2, 1];
    
    const head = createLinkedList(originalList);
    const reversedHead = reverseLinkedList(head);
    const result = linkedListToArray(reversedHead);
    
    expect(result).toEqual(expected);
  });

})
#include <iostream>
using namespace std;

class Node {
  public:
    int data;
    Node* next;
  // constructor that initializes data to 0 and next pointer to NULL
    Node() {
      data = 0;
      next = NULL;
    }
    Node(int data) {
      this->data = data;
      this->next = NULL;
    }
};

int main() {
  Node* first = new Node(20);
  Node* second = new Node(30);
  Node* third = new Node(40);

  Node* head = first;
  first->next = second;
  second->next = third;
  Node* temp;

  cout << "List befor reversing: " << endl;
  temp = head;
  while (temp != NULL) {
    cout << temp->data << "->";
    temp = temp->next;
  }
  cout << "NULL" << endl;
  Node* current = head;
  Node* previous = NULL;
  Node* nextNode = NULL;

  while (current != NULL) {
    nextNode = current->next; // store the address of the next node
    current->next = previous; // point to the previous node
    previous = current; // store the address of the current node

    current = nextNode;
  }
  head = previous;

  cout << "List after reversing: " << endl;
  temp = head;
  while (temp != NULL) {
    cout << temp->data << "->";
    temp = temp->next;
  }
  cout << "NULL" << endl;
  return 0;
}

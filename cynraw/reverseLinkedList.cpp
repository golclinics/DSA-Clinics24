#include<iostream>
using namespace std;


class node{
    public:
        int data;
        node *next;
    // constructor for a node
    node(int value){
        data = value;
        next = nullptr;
    }
};
class reversedLinkedList{
    private:
    node * head;

    public:
    reversedLinkedList(){
        head = nullptr;
    }

    void reverse(){
        node * current = head;
        node * next = nullptr;
        node * prev = nullptr;

        while(current != nullptr){
            next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        }
        head = prev;
    }
    //inserting at the head
    void insert(int value){
        node *newnode = new node(value);
        newnode->data = value;
        newnode->next = head;
        head = newnode;
    }
    void printList(){
        node *current = head;
        while(current != nullptr){
            cout << current->data << "->";
            current = current->next;
        }
        cout<< "Null";
    }

};

int main(){
    reversedLinkedList list;

    list.insert(5);
    list.insert(4);
    list.insert(3);
    list.insert(2);
    list.insert(1);

    cout<< "Original List"<< endl;
    list.printList();
    cout<<endl;

    list.reverse();

    cout<< "Reversed List";
    list.printList();


    return 0;
}
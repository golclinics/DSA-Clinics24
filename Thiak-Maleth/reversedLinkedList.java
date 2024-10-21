public class ReversedLinkedList {

    static class Node {
        int data;
        Node next;
    
        Node(int data) {
            this.data = data;
        }
    }

    public static Node reverseList(Node head) {
        Node prev = null;
        Node curr = head;
        Node next = null;

        while (curr != null) {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }

    public static void main(String[] args) {
        Node head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(3);
        head.next.next.next = new Node(4);
        head.next.next.next.next = new Node(5);

         Node result = reverseList(head);

        while (result != null) {
            if (result.next != null) {
                System.out.print(result.data + " -> ");
            } else {
                System.out.print( result.data + " ");
            }
            result = result.next;
        }
    }
}



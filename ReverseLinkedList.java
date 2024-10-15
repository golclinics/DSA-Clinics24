
public class ReverseLinkedList {

    public static void main(String[] args) {
        Node head = new Node(1);
        head.next = new Node(2);
        head =  reverseLinkedList(head);
    }

    private static Node reverseLinkedList(Node head) {
        Node previous = null, next =null , currNode = head;

        while(currNode.next != null){
            next = currNode.next;

            currNode.next = previous;

            previous = currNode;
            currNode = next;

        }

        return previous;
    }
        
}


    

    
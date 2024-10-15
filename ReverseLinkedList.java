
public class ReverseLinkedList {

    public static void main(String[] args) {
        Node head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(3);
     
        
        head =  reverseLinkedList(head);
        System.out.println("Reversed Order Linked List");
        while (head != null) {
            
            System.out.println(head.nodeData);
            head = head.next;
        }
       
    }

    private static Node reverseLinkedList(Node head) {
        Node previous = null, next = null, currNode = head;

        while(currNode != null){
            
            next = currNode.next;

            currNode.next = previous;
            previous = currNode;
            currNode = next;

        }

        return previous;
    }
        
}


    

    
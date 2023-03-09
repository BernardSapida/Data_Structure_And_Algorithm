public class SinglyLinkedList {
    Node head;
    Node tail;
    int length;

    SinglyLinkedList() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    public void push(int value) {
        Node newNode = new Node(value);

        if(this.head == null) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            this.tail.next = newNode;
            this.tail = newNode;
        }

        this.length++;
    }

    public void printList() {
        Node currentNode = this.head;
        String result = "";

        while(currentNode != null) {
            result += (currentNode.value + " -> ");
            currentNode = currentNode.next;
        }

        result += "NULL";
        System.out.println(result);
    }
}
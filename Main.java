class Main {
    public static void main(String[] args) {
        SinglyLinkedList linkedList = new SinglyLinkedList();

        linkedList.push(6);
        linkedList.push(2);
        linkedList.push(17);
        linkedList.push(4);
        linkedList.push(0);

        linkedList.printList();
        System.out.println(linkedList.head.value);
        System.out.println(linkedList.tail.value);
    }
}

/*
 *
 * [1, 2, 3, 4, 5, ...] -> Overflow
 * 
 * Linked List -> different memory location
 * 1 -> 2 -> 3 -> 4 -> null
 * head           tail
 *                     currentNode
 * 
 * Proceedure (Pust Method):
 * this.tail.next = newNode(2)
 * this.tail = newNode(2)
 * 
 * Proceedure (Pop method):
 * 
 * newNode.value = 1
 * newNode.next = null
 * 
 * visual representation:
 * 1 -> null
 * 
 * Java -> Class
 * C -> struct
 */
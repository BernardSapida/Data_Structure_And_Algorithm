/*
    Singly Linked List methods:
    1) Push
    2) Pop
    3) Shift
    4) Unshift
    5) Get
    6) Set
    7) Insert
    8) Remove
    9) Reverse
*/

class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

class SinglyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    push(value) {
        let newNode = new Node(value);

        if(this.head == null) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            this.tail.next = newNode;
            this.tail = newNode;
        }

        this.length++;
        return true;
    }

    pop() {
        if(!this.head) return undefined;

        let beforeNode = this.head;
        let afterNode = beforeNode;

        while(afterNode.next) {
            beforeNode = afterNode;
            afterNode = afterNode.next;
        }

        beforeNode.next = null;
        this.tail = beforeNode;
        this.length--;

        if(this.length === 0) {
            this.head = null;
            this.tail = null;
        }

        return afterNode;
    }

    shift() {
        if(!this.head) return undefined;
        
        let firstNode = this.head;
        this.head = firstNode.next;
        this.length--;
        return firstNode;
    }

    unshift(value) {
        let newNode = new Node(value);
        
        newNode.next = this.head;
        this.head = newNode;
        return true;
    }

    get(index) {
        let currentNode = this.head;
        let position = 0;

        if(index < 0 || index > this.length-1) return undefined;
        if(index === this.length-1) return this.tail;

        while(position !== index) {
            currentNode = currentNode.next;
            position++;
        }

        return currentNode;
    }

    set(index, value) {
        let foundNode = this.get(index);
        
        if(foundNode) {
            foundNode.val = value;
            return true;
        }

        return false;
    }

    insert(index, value) {
        if(index < 0 || index > this.length) return false;
        else if(index === 0) return this.unshift(value);
        else if(index === this.length) return this.push(value);

        let newNode = new Node(value);
        let beforeNode = this.get(index-1);
        let afterNode = beforeNode.next;

        beforeNode.next = newNode;
        newNode.next = afterNode;

        return true;
    }

    remove(index) {
        if(index < 0 || index > this.length) return false;
        else if(index === 0) return this.shift();
        else if(index === this.length) return this.pop();

        let beforeNode = this.get(index-1);
        let removeNode = beforeNode.next;
        let afterNode = removeNode.next;

        beforeNode.next = afterNode;

        return removeNode;
    }

    reverse() {
        let node = this.head;
        this.head = this.tail;
        this.tail = node;
        let next;
        let prev = null;

        for(let i = 0; i < this.length; i++) {
            next = node.next; // 2, 3
            node.next = prev; // null, 1, 
            prev = node; // 1, 2
            node = next; // 2, 3
        }
    }

    printList() {
        let currentNode = this.head;
        let result = "";

        while(currentNode != null) {
            result += `${currentNode.val} -> `;
            currentNode = currentNode.next;
        }

        result += "NULL";
        return result;
    }
}

let SLL = new SinglyLinkedList();
// SLL.push(1);
// SLL.push(2);
// SLL.push(3);
// SLL.push(4);
// SLL.push(5);
// console.log(SLL.pop());
// console.log(SLL.shift());
// console.log(SLL.set(0, 11));
// console.log(SLL.set(-1, 1));
// console.log(SLL.insert(4, 17));
// console.log(SLL.length);
// console.log(SLL.get(6));

// console.log(SLL.remove(8).val);
// console.log(SLL.printList());
// console.log(SLL.reverse());
SLL.push(4);
SLL.push(6);
SLL.push(8);
SLL.push(2);
console.log(SLL.printList());
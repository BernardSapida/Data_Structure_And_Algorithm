class Node{
    constructor(val){
        this.val = val;
        this.next = null;      
        this.prev = null;      
    }
}

class DoublyLinkedList{
    constructor(){
        this.head = null;
        this.tail = null;      
        this.length = 0;      
    }

    push(val){
        let newNode = new Node(val);

        if(!this.head) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            this.tail.next = newNode;
            newNode.prev = this.tail;
            this.tail = newNode;
        }

        this.length++;
        return this;
    }

    pop() {
        let removedNode = this.tail;

        if(this.length === 0) return undefined;
        if(this.length === 1) {
            this.head = null;
            this.tail = null;
        } else {
            let prevNode = removedNode.prev;
            prevNode.next = null;
            removedNode.prev = null;
            this.tail = prevNode;
        }
        
        this.length--;
        return removedNode;
    }

    unshift(val) {
        let newNode = new Node(val);

        if(this.length === 0) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            newNode.next = this.head;
            this.head.prev = newNode;
            this.head = newNode;
        }

        this.length++;
        return this;
    }

    shift() {
        if(this.length === 0) return undefined;

        let removedNode = this.head;

        if(this.length == 1) return this.pop();
        else {
            let nextNode = removedNode.next;
            this.head.next = null;
            nextNode.prev = null;
            this.head = nextNode;
        }

        this.length--;
        return removedNode;
    }

    get(index) {
        if(index < 0 || index > this.length-1) return null;
        else if(index === 0) return this.head;
        else if(index === this.length-1) return this.tail;

        let currentNode = this.head;
        let currentIndex = 0;

        while(currentIndex != index) {
            currentNode = currentNode.next;
            currentIndex++;
        }

        return currentNode;
    }

    set(index, val) {
        if(index > this.length-1) return false;

        let foundNode = this.get(index);

        if(!foundNode) return false;

        foundNode.val = val;
        return true;
    }

    remove(index) {
        if(index < 0 || index >= this.length) return undefined;
        else if(index == 0) return this.shift();
        else if(index == this.length-1) return this.pop();

        let removedNode = this.get(index);
        let beforeNode = removedNode.prev;
        let afterNode = removedNode.next;

        beforeNode.next = afterNode;
        afterNode.prev = beforeNode;

        removedNode.prev = null;
        removedNode.next = null;
        
        this.length--;
        return removedNode;
    }

    reverse() {
        let node = this.head;
        this.head = this.tail;
        this.tail = node;

        let prev = null;
        let next = null;

        for(let i = 0; i < this.length; i++) {
            next = node.next;
            node.next = prev;
            node.prev = next;
            prev = node;
            node = next;
        }

        return this;
    }
}

let doublyLinkedList = new DoublyLinkedList;
doublyLinkedList.push(5).push(10).push(15).push(20)
console.log(doublyLinkedList.reverse()); // singlyLinkedList;
console.log(doublyLinkedList.length); // 4
console.log(doublyLinkedList.head.val); // 20
console.log(doublyLinkedList.head.next.val); // 15
console.log(doublyLinkedList.head.next.next.val); // 10
console.log(doublyLinkedList.head.next.next.next.val); // 5
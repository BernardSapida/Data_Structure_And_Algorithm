class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

class Queue {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    enqueue(val) {
        let newNode = new Node(val);

        if(!this.head) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            this.tail.next = newNode;
            this.tail = newNode;
        }
    }

    dequeue() {
        let firstNode = this.head;
        this.head = this.head.next;
        return firstNode;
    }
}

class Vertex {
    constructor(val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

class BinarySearchTree {
    constructor() {
        this.root = null;
    }

    insert(val) {
        let newVertex = new Vertex(val);
        
        if(!this.root) this.root = newVertex;
        else {
            let currentNode = this.root;

            while(true) {
                if(val > currentNode.val) {
                    if(currentNode.right == null) {
                        currentNode.right = newVertex;
                        break;
                    }
                    else currentNode = currentNode.right;
                } else {
                    if(currentNode.left == null) {
                        currentNode.left = newVertex;
                        break;
                    }
                    else currentNode = currentNode.left; 
                }
            }
        }

        return true;
    }

    search(val, parent = this.root) {
        if(!parent) return false;
        
        if(val > parent.val) return this.search(val, parent.right);
        else if(val < parent.val) return this.search(val, parent.left);
        else return parent;
    }

    remove(val, parent = this.root) {
        if(val > parent.val) parent.right = this.remove(val, parent.right);
        else if(val < parent.val) parent.left = this.remove(val, parent.left);
        else {
            if(parent.right == null && parent.left == null) return null;
            else if(parent.left == null) return parent.right;
            else if(parent.right == null) return parent.left;
            else {
                let minimumVal = this.findMinimum(parent.right);
                this.remove(minimumVal.val, parent.right);
                parent.val = minimumVal.val;
                return parent;
            }
        }
    }

    findMinimum(node) {
        if(node.left == null) return node;
        return this.findMinimum(node.left);
    }

    breathFirstSearh() {
        if(!this.root) return false;

        let queue = new Queue();
        let arr = [];

        queue.enqueue(this.root);

        while(queue.head) {
            let dequeueNode = queue.dequeue().val;
            arr.push(dequeueNode.val);
            if(dequeueNode.left) queue.enqueue(dequeueNode.left);
            if(dequeueNode.right) queue.enqueue(dequeueNode.right);
        }

        return arr;
    }

    preorder() {
        let arr = [];
    
        (function traverse(node) {
            if(!node) return;
            arr.push(node.val);
            traverse(node.left);
            traverse(node.right);
        })(this.root);
        
        return arr;
    }

    postorder() {
        let arr = [];
        
        (function traverse(node) {
            if(!node) return;
            traverse(node.left);
            traverse(node.right);
            arr.push(node.val);
        })(this.root);
        
        return arr;
    }

    inorder() {
        let arr = [];
        
        (function traverse(node) {
            if(!node) return;
            traverse(node.left);
            arr.push(node.val);
            traverse(node.right);
        })(this.root);
        
        return arr;
    }

    getSuccessor(val) {
        
    }

    getPredecessor(val) {
    
    }
}

let bst = new BinarySearchTree();
bst.insert(41);
bst.insert(20);
bst.insert(11);
bst.insert(29);
bst.insert(32);
bst.insert(65);
bst.insert(50);
bst.insert(91);
bst.insert(72);
bst.insert(99);
// console.log(bst);
// console.log(bst.findMinimum(bst.root));
// console.log(bst.search(65).right);
// console.log(bst.search(41));
// console.log(bst.remove(65));
// console.log(bst.search(41));
console.log(bst.preorder());
console.log(bst.postorder());
console.log(bst.inorder());
console.log(bst.breathFirstSearh());
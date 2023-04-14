class BinaryHeap {
    constructor() {
        this.length = 0;
        this.tree = [];
    }

    insert(val) {
        this.tree.push(val);

        if(++this.length === 1) return true;

        let newNodePos = this.length-1;
        let parentPos = Math.floor(Math.abs((newNodePos-1)/2));

        while(true) {
            if(this.tree[newNodePos] > this.tree[parentPos]) {
                [this.tree[parentPos], this.tree[newNodePos]] = [this.tree[newNodePos], this.tree[parentPos]];
                newNodePos = parentPos;
                parentPos = Math.floor(Math.abs(newNodePos-1/2));
            } else break;
        }

        return true;
    }

    extractMax() {
        if(this.length == 0) return false;

        let currentPosition = 0;
        let last = this.tree.pop()

        if(this.length > 1) this.tree[0] = last;

        while(true) {
            let leftVal = this.tree[currentPosition*2+1];
            let rightVal = this.tree[currentPosition*2+2];

            if(leftVal > rightVal && leftVal > this.tree[currentPosition]) {
                [this.tree[currentPosition], this.tree[currentPosition*2+1]] = [this.tree[currentPosition*2+1], this.tree[currentPosition]];
                currentPosition = currentPosition*2+1;
            } else if(rightVal > leftVal && rightVal > this.tree[currentPosition]) {
                [this.tree[currentPosition], this.tree[currentPosition*2+2]] = [this.tree[currentPosition*2+2], this.tree[currentPosition]];
                currentPosition = currentPosition*2+2;
            } else break;
        }

        this.length--;
    }

    search(val) {
        if(this.length == 0) return undefined;
        else {
            for(let n of this.tree) {
                if(val == n) return true;
            }
        }
    }
}

let heap = new BinaryHeap;
console.log(heap.insert(92));
console.log(heap.insert(79));
console.log(heap.insert(74));
console.log(heap.insert(58));
console.log(heap.insert(55));
console.log(heap.insert(53));
console.log(heap.insert(42));
console.log(heap.insert(38));
console.log(heap.insert(25));
console.log(heap.insert(35));
console.log(heap.insert(20));
console.log(heap.insert(24));
console.log(heap.insert(29));
console.log(heap.insert(21));
console.log(heap.tree);
console.log(heap.extractMax());
console.log(heap.extractMax());
console.log(heap.extractMax());
console.log(heap.tree);
console.log(heap.search(20));
console.log(heap.length);
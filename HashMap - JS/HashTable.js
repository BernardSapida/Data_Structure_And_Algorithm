/* 
    Problem with this hash:
    1) Numbers on keys produce negative index in hash function.
    2) Capital letters produce negative index in hash function.
*/
class HashTable {
    constructor(size = 53) {
        this.length = size;
        this.hashTable = new Array(size);
    }

    _hash(key) {
        let total = 0;
        let prime = 13;

        for(let i = 0; i < Math.min(key.length, 100); i++) {
            let value = key[i].charCodeAt(0) - 96;
            total = (total * prime + value) % this.length;
        }

        return total;
    }

    set(key, value) {
        let idx = this._hash(key);
        if(this.hashTable[idx]) this.hashTable[idx].push([key, value]);
        else this.hashTable[idx] = [[key, value]];
    }
    
    get(key) {
        let idx = this._hash(key);
        let map = this.hashTable;

        if(map[idx]) {
            if(map[idx].length == 1) {
                if(map[idx][0][0] == key) return map[idx];
            } else {
                for(let arr of map[idx]) {
                    if(arr[0] == key) return arr;
                }
            }
        }
    }
}

let hashTable = new HashTable();
hashTable.set("hello world", "goodbye!!");
hashTable.set("dogs", "are cool");
hashTable.set("cats", "are fine");
hashTable.set("i love", "pizza");
console.log(hashTable.get("hello world"));
console.log(hashTable.get("dogs"));
console.log(hashTable.get("cats"));
console.log(hashTable.get("i love"));
console.log(hashTable.hashTable);
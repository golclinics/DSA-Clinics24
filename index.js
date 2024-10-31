class HashMap {
  constructor() {
    this._buckets = [];
  }
  _hash(key) {
    let hash = "";
    for (let i = 0; i < key.length; i++) {
      hash += (hash + key.charCodeAt(i)) % this._buckets.length;
    }
    return hash;
  }
  insert(key, value) {
    const index = this._hash(key);
    if (!this._buckets[index]) {
      this._buckets[index] = [];
    }
    const bucket = this._buckets[index];
    for (let i = 0; i < bucket.length; i++) {
      if (bucket[i][0] === key) {
        bucket[i][1] = value;
        return;
      }
    }
    bucket.push([key, value]);
  }
  search(key) {
    const index = this._hash(key);
    const bucket = this._buckets[index];

    if (!bucket) {
      return undefined;
    }

    for (let i = 0; i < bucket.length; i++) {
      if (bucket[i][0] === key) {
        return bucket[i][1];
      }
    }
    return undefined;
  }
  delete(key) {
    const index = this._hash(key);
    const bucket = this._buckets[index];
    if (!bucket) {
      return;
    }
    for (let i = 0; i < bucket.length; i++) {
      if (bucket[i][0] === key) {
        bucket.splice(i, 1);
        return;
      }
    }
  }
}

const hashMap = new HashMap();

hashMap.insert("name", "Nicholas");
hashMap.insert("mane", "Mane...");
hashMap.insert("occupation", "Software Engineer");
hashMap.delete("mane");

console.log("====================================");
console.log(hashMap.search("mane")); //undefined since it has been deleted
console.log("====================================");

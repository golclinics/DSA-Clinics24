using System;
using System.Collections.Generic;
public class HashMap<K, V>
{
    private int size;
    private List<KeyValuePair<K, V>>[] map;

    public HashMap(int size)
    {
        this.size = size;
        map = new List<KeyValuePair<K, V>>[size];
        for (int i = 0; i < size; i++)
        {
            map[i] = new List<KeyValuePair<K, V>>();
        }
    }

    private int GetIndex(K key)
    {
        return key.GetHashCode() % size;
    }

    public void Add(K key, V value)
    {
        int index = GetIndex(key);
        var bucket = map[index];
        foreach (var pair in bucket)
        {
            if (pair.Key.Equals(key))
            {
                throw new ArgumentException("Key already exists");
            }
        }
        bucket.Add(new KeyValuePair<K, V>(key, value));
    }

    public V Get(K key)
    {
        int index = GetIndex(key);
        var bucket = map[index];
        foreach (var pair in bucket)
        {
            if (pair.Key.Equals(key))
            {
                return pair.Value;
            }
        }
        throw new KeyNotFoundException("Key not found");
    }

    public bool Remove(K key)
    {
        int index = GetIndex(key);
        var bucket = map[index];
        for (int i = 0; i < bucket.Count; i++)
        {
            if (bucket[i].Key.Equals(key))
            {
                bucket.RemoveAt(i);
                return true;
            }
        }
        return false;
    }

    public void PrintAll()
    {
        foreach (var bucket in map)
        {
            foreach (var pair in bucket)
            {
                Console.WriteLine($"Key: {pair.Key}, Value: {pair.Value}");
            }
        }
    }
}

public class Program
{
    public static void Main()
    {
        var hashMap = new HashMap<int, string>(10);
        hashMap.Add(1, "one");
        hashMap.Add(2, "two");
        hashMap.Add(3, "three");

        Console.WriteLine(hashMap.Get(1)); 
        Console.WriteLine(hashMap.Get(2));
        Console.WriteLine(hashMap.Get(3)); 

        hashMap.PrintAll();
    }
}

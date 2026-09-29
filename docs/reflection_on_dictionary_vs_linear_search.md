# Reflection on Dictionary Lookup and Linear Search

## Why is dictionary lookup faster?

In this project, transactions are stored in two ways:

- `transactions` stores them in a list.
- `transaction_dictionary` stores each transaction using its ID as the key.

Linear search checks the list from the beginning, one item at a time. If there are many transactions, it may need to check all of them. This gives linear search a time complexity of $O(n)$.

A dictionary can find a transaction using its ID directly. This is because Python uses a hash table to store dictionary values. On average, dictionary lookup takes $O(1)$ time, which means it stays fast even when the number of transactions increases.

Dictionary lookup can sometimes be slower because of hash collisions, but this is uncommon. Dictionaries also use more memory than lists and need unique keys.

## How this applies to our project

The API already creates `transaction_dictionary`. The DELETE endpoint uses it to find transactions, but the GET-by-ID endpoint still uses linear search:

```python
transaction = linear_search(transactions, transaction_id)
```

The GET endpoint could use the dictionary instead:

```python
transaction = transaction_dictionary.get(str(transaction_id))
```

This would make ID searches faster, especially when the project has many transactions. The dictionary must be kept updated when transactions are added, changed, or deleted.

## Another possible solution

Binary search could also improve search speed. It works on a list that is sorted by transaction ID. Instead of checking every item, it checks the middle item and removes half of the remaining list each time. Its time complexity is $O(\log n)$, which is faster than linear search.

The disadvantage is that the list must stay sorted. Adding or deleting transactions may also require the list to be rearranged.

For this project, a dictionary is the best choice for quick searches by transaction ID because the IDs are unique. If the project stores the transactions in a database later, adding an index to the transaction ID column would also make searches faster.

## Conclusion

Linear search is simple and is suitable for a small list. However, its search time increases as more transactions are added. Dictionary lookup is faster for this API because it can find a transaction directly by its ID. Binary search and database indexes are other useful options, depending on how the data is stored.
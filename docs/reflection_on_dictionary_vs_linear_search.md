# Reflection on Dictionary Lookup vs Linear Search

## Why dictionary lookup is faster

The API stores transactions in two forms:

- `transactions` is a list of transaction records.
- `transaction_dictionary` maps each transaction ID to its record.

The `linear_search` function checks list items one at a time until it finds the requested ID. If there are `n` transactions, it may inspect every item, giving it a time complexity of $O(n)$. A transaction near the beginning may be found quickly, but a transaction near the end, or an ID that does not exist, requires a full scan.

A Python dictionary uses a hash table. The transaction ID is converted into a hash that identifies where the corresponding record should be stored. This allows the dictionary to locate a record directly instead of comparing it with every other record. Dictionary lookup has an average time complexity of $O(1)$, so the lookup time generally remains almost constant as the number of transactions grows.

Dictionary lookup is not guaranteed to be $O(1)$ in every situation. Hash collisions can require additional comparisons, making the worst case $O(n)$. In practice, Python manages its hash table to keep collisions low. The trade-off is that a dictionary uses more memory than a list and requires unique, hashable keys.

## Application to this project

The API already creates `transaction_dictionary`, and the DELETE endpoint uses it to find a transaction by ID. The GET-by-ID endpoint currently calls `linear_search(transactions, transaction_id)`, so it does not benefit from the dictionary that has already been prepared. For consistent performance, GET-by-ID could use:

```python
transaction = transaction_dictionary.get(str(transaction_id))
```

This is especially useful when the SMS dataset becomes large or when the endpoint receives many ID-based requests. The dictionary must also be updated whenever a transaction is added, modified, or deleted, which the current POST and DELETE logic already partially handles.

## Another data structure or algorithm

Binary search is another option when transactions are kept in a list sorted by numeric ID. It repeatedly compares the target ID with the middle item and discards half of the remaining list. Its time complexity is $O(\log n)$, which is much faster than linear search for large datasets. However, the list must remain sorted, and inserting or deleting items may require shifting records. Binary search is therefore most suitable for mostly static data or data that is periodically sorted.

For this API, a dictionary is the better in-memory structure for direct ID lookups because IDs are unique and requests do not require sorted order. If the project moves to persistent database storage, an indexed database column such as `transaction_id` would be the stronger long-term choice. A B-tree database index also provides approximately $O(\log n)$ lookup while supporting durable storage, filtering, and range queries.

## Conclusion

Linear search is simple and works well for small lists, but its cost grows directly with the number of transactions. Dictionary lookup is faster on average because hashing provides direct access to a record. The current API should use `transaction_dictionary` consistently for ID-based lookups, while a database index would provide an efficient and scalable solution once transactions are stored in the database.
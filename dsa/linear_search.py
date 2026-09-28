def linear_search(transactions, target_id):
    for transaction in transactions:
        if transaction['id'] == target_id:
            return transaction
    return None


if __name__ == '__main__':
    sample_transactions = [
        {'id': 1, 'amount': 2000},
        {'id': 2, 'amount': 5000},
        {'id': 3, 'amount': 1000},
    ]

    result = linear_search(sample_transactions, 2)
    print(result)

    missing = linear_search(sample_transactions, 99)
    print(missing)
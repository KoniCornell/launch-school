def transactions_for(id: int, all_transactions: list):
    return [element for element in all_transactions
                    if element['id'] == id]

def is_item_available(id: int, all_transactions: list):
    transactions_for_id = transactions_for(id, all_transactions)
    total_inventory = sum([transaction['quantity'] * -1
                           if transaction['movement'] == 'out'
                           else transaction['quantity']
                           for transaction in transactions_for_id])
    
    if total_inventory <= 0:
        return False
    
    return True
    



transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True
items = {
    "121": {
        "name": "item1",
        "price": 100
    },
    "122": {
        "name": "item2",
        "price": 103
    },
    "123": {
        "name": "item3",
        "price": 102
    }
}

def addNewReceipt():
    receipts = []
    
    while True:
        b = input('Barcode? ')
        
        getItem = items.get(b)
        if getItem:
            q = int(input('Quantity? '))     

            receipts.append({"barcode": b, "name": getItem['name'], "quantity": q,
                        "unit_price": getItem['price'], "total_price": (q * getItem['price'])})   
            
            print(receipts)
            print('Another Item ? (yes / no)')
            i = input().strip().lower()

            while i not in ['yes', 'no']:
                i = input('Please choose yes or no: ')
            
            if i == 'no':
                break 
        else:
            print('Item not found. Other barcode ? (yes / no)')
            b = input().strip().lower()

            while b not in ['yes', 'no']:
                b = input('Please choose yes or no: ')
        
            if b == 'yes':
                addNewReceipt()
            else:
                startReceipt()

    return receipts

def printReceipt(receipts):
    print("\n--- Receipt ---")
    total = 0
    for item in receipts:
        print('hana')
        print(item['total_price'])
        total += item['total_price']
        print(f"Item Name: {item['name']} ({item['barcode']}): {item['quantity']} x {item['unit_price']} = {item['total_price']} ")

    print(f'Total amount is: {total}')

def startReceipt():
    newReceipt = input("Start a new receipt ? (yes / no): ").strip().lower()

    while newReceipt not in ['yes', 'no']:
        newReceipt = input('Please choose yes or no: ')

    if newReceipt == 'no':
        print('Thank you.')
    else: 
        receipts = addNewReceipt()
        printReceipt(receipts)
        startReceipt()

startReceipt()


# def check_correctness(c):
#     while c != '1' and c != '0':
#         print("Not get it, please choose 1 for yes, 0 for no")
#         c = input()
#     return c

# def check_barcode_exists(b):
#     for i in items:
#         if i['barcode'] == b:
#             return True
#     return False


# print("Add new Receipt ? 1 for yes, 0 for no")
# c = input()

# c = check_correctness(c)

# while c == '1':
#     print('ds')
#     #add
#     b = input('Barcode: ')
#     be = False
#     while not check_barcode_exists(b):
#         print("Barcode not exists in our dekene. Try another one or press 0 to exit")
#         b = input('Barcode: ')
#         if b == '0':
#             break
    


#     print("Add other receipt ? 1 for yes, 0 for no")
#     e = input()
#     check_correctness(e)

#if c != '1':
    #print
    










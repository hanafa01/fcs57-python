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

            alreadyIndex = -1
            for r in range(0, len(receipts)):
                if b == receipts[r]['barcode']:
                    alreadyIndex = r
                    break

            if alreadyIndex != -1:
                print('Item already exists... updating quantity and total price')
                receipts[r]['quantity'] = receipts[r]['quantity'] + q
                receipts[r]['total_price'] = receipts[r]['quantity'] * receipts[r]['unit_price'] 
            else:
                receipts.append({"barcode": b, "name": getItem['name'], "quantity": q,
                        "unit_price": getItem['price'], "total_price": (q * getItem['price'])})  
            
            i = input('Another Item ? (yes / no): ').strip().lower()

            while i not in ['yes', 'no']:
                i = input('Please choose yes or no: ')
            
            if i == 'no':
                break 
        else:
            b = input('Item not found. Other barcode ? (yes / no): ').strip().lower()

            while b not in ['yes', 'no']:
                b = input('Please choose yes or no: ')
            #########3
            if b == 'yes':
                continue
                # addNewReceipt()
            else:
                break

    return receipts

def printReceipt(receipts):
    print("\n--- Receipt ---")
    total = 0
    for item in receipts:
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
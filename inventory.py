def menu():
    print("\tDashboard\n")
    print("Number of items in stock: " + str(len(Items)))
    print("Number of ordered Items : " + str(len(orderedItems)))

    print("\tMENU ITEMS\n")
    print("1.Display items in stock")
    print("2.Update items in stock")
    print("3.Add items to stock")
    print("4.Order items from stock\n")
    choice = int(input("Choose the option you want: "))
    if choice == 1:
        print (f"{'id':<5} {'name':<20} {'price':<10} {'supplier':<10}")
        for i in range (len(Items)):
            print (f"{Items[i]["id"]: <5} {Items[i]["name"]: <20} {Items[i]["price"]: <10} {Items[i]["supplier"]: <10}")
        menu()
    elif choice == 2:
        chosenId = int (input("Enter the id of the item to update: "))
        for i in range (len(Items)):
            if Items[i]["id"] == chosenId:
                k = i
                break
            k = len(Items)
        if k != len(Items):
            choiceUpdate=int(input("What do want to update?\n1.id \n2.Name \n3.Price \n4.Supplier\nChoice: "))
            if choiceUpdate == 1:
                newId = int (input("Enter the new id: "))
                Items[k]["id"] = newId
                menu()
            elif choiceUpdate == 2:
                newName = input("Enter the new name: ")
                Items[k]["name"] = newName
                menu()
            elif choiceUpdate == 3:
                newPrice= int (input("Enter the new price: "))
                Items[k]["price"] = newPrice
                menu()
            elif choiceUpdate == 4:
                newSupplier= int (input("Enter the new supplier: "))
                Items[k]["supplier"] = newSupplier
                ()
            else:
                print("Wrong choice....")
                menu()
    elif choice == 3:
        
        addId = int(input("Enter new item's id: "))
        addName = (input("Enter new item's name: "))
        addPrice= int(input("Enter new item's price: "))
        addSupplier = (input("Enter new item's supplier: "))
        dict  = {
            "id":addId,
            "name":addName,
            "price":addPrice,
            "supplier":addSupplier
        }
        Items.append(dict)
        menu()
    
    elif choice == 4:
        orderID = int(input("Enter the Id for the item to be ordered: "))
        for i in range (len(Items)):
            if orderID == Items[i]["id"]:
                j = i
                break
            j = len(Items)
        if j != len(Items):
            dict2 ={
                "id": Items[j]["id"],
                "name": Items[j]["name"],
                "price": Items[j]["price"],
                "supplier": Items[j]["supplier"]
            } 
            orderedItems.append(dict2)
            del Items[j]
        else:
            print("Item is out of stock.")
    menu()           
print("Inventory Management System\n".upper())
Items = list(
    ({"id": 101, "name": "LED Light Bulb", "price": 5.99, "supplier": "BrightTech Ltd."},
    {"id": 102, "name": "Smart Plug", "price": 14.49, "supplier": "HomeSmart Inc."},
    {"id": 103, "name": "Motion Sensor", "price": 22.75, "supplier": "SecureHome Co."},
    {"id": 104, "name": "Thermostat V2", "price": 89.99, "supplier": "EcoLiving Corp."},
    {"id": 105, "name": "Door Lock Pro", "price": 129.50, "supplier": "LockIt Systems"})
    )
orderedItems = []
menu()

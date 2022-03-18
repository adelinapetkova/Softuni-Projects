from collections import deque


def stock_availability(boxes, action, *args):
    if action=='delivery':
        for cupcake in args:
            boxes.append(cupcake)
        return boxes
    elif action=='sell':
        boxes=deque(boxes)
        if len(args)==1 and str(args[0]).isnumeric():
            for i in range(int(args[0])):
                boxes.popleft()
        elif args:
            for product in args:
                while product in boxes:
                    boxes.remove(product)
        else:
            boxes.popleft()

        return list(boxes)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
#Quiz 8

iterator = iter(["apple", "banana", "cherry"])

def next_item(iterator):
    try:
        return next(iterator)
    
    except StopIteration:
        
        return None

print(next_item(iterator))
print(next_item(iterator))
print(next_item(iterator))
print(next_item(iterator))
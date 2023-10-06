class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __lt__(self, other):
        return self.value / self.weight < other.value / other.weight


def cmp(items, capacity):
    items.sort(reverse=True)
    total_value = 0
    total_weight = 0
    for item in items:
        if total_weight + item.weight <= capacity:
            total_value += item.value
            total_weight += item.weight
        else:
            break
    return total_value


def kp(items, capacity):
    items.sort(reverse=True)
    total_value = 0
    for item in items:
        if item.weight <= capacity:
            total_value += item.value
            capacity -= item.weight
        else:
            break
    return total_value


if __name__ == "__main__":
    items = [Item(10, 2), Item(5, 1), Item(2, 1)]
    capacity = 6

    print("CMP:", cmp(items.copy(), capacity))
    print("KP:", kp(items.copy(), capacity))

# Task 03 - JSON Path Explorer
def find_paths(data, target, path=""):
    found = []
    if isinstance(data, dict):
        for key in data:
            found += find_paths(data[key], target, path + "." + key if path else key)
    elif isinstance(data, list):
        for i in range(len(data)):
            found += find_paths(data[i], target, path + "[" + str(i) + "]")
    elif data == target and type(data) == type(target):   # True is not 1
        found.append(path)
    return found

print(find_paths({"a": [{"x": 5}, 5], "b": {"y": 5}}, 5))   # ['a[0].x', 'a[1]', 'b.y']

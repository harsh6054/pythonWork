def flatten_list(nested_list):
    flattened_list = []
    for sublist in nested_list:
        for item in sublist:
            flattened_list.append(item)
    return flattened_list

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print("Flattened list:", flatten_list(nested_list))

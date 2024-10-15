def count_occurrences(lst: list):
    dict_lst = {element: lst.count(element) for element in lst}

    for key, value in dict_lst.items():
        print(f'{key} => {value}')

    

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)
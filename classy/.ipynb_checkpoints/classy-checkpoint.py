n = int(input())

    
def calculate_people_worth(class_list, max_depth):
    mapping = {'upper': 3, 'middle': 2, 'lower':1}
    # print("B4",class_list)
    class_list += ['middle'] * (max_depth - len(class_list))
    # print("AF", class_list)
    #print(tuple(mapping[p] for p in class_list))
    return tuple(mapping[p] for p in class_list)

    
for _ in range(n):
    people = []
    max_depth = 0
    for _ in range(int(input())):
        name, class_info = input().split(': ')
        class_levels = class_info.replace(' class', '').split('-')
        
        max_depth = max(max_depth, len(class_levels))
        
        people.append((name, class_levels))

    
    sortable = [
        (calculate_people_worth(levels, max_depth), name)
        for name, levels in people
    ]

    #print(sortable)

    for _, name in reversed(sorted(sortable, key=lambda x:  x[0])):
        print(name)
    print('=' * 30)
    # sortable = [(class_to_tuple('-'.join(levels), max_depth), name) for name, levels in people]




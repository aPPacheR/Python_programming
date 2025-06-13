
height = 3
root = 5

def gen_bin_tree(height, root):
    if height == 0:
        return None
    # Создаем наше дерево через рекурсию
    tree = {
        'root': root,
        'left': gen_bin_tree(height - 1, root * 2),
        'right': gen_bin_tree(height - 1, root + 3)
    }

    return tree

print(gen_bin_tree(height, root))

height = 3
root = 5

def gen_nobin_tree(height, root):
    # Создаем массив значений нашего дерева
    array = [{
        'value': root,
        'left': None,
        'right': None
    }]
    for i in range(2 ** (height - 1)):
        # Создаем значения для левого и правого потомка
        left_value = array[i]['value'] * 2
        right_value = array[i]['value'] + 3

        # Создаем левый и правый потомков
        left_node = {'value': left_value, 'left': None, 'right': None}
        right_node = {'value': right_value, 'left': None, 'right': None}

        # Связываем потомков
        array[i]['left'] = left_node
        array[i]['right'] = right_node

        # Добавляем потомков в массив
        array.append(left_node)
        array.append(right_node)

    # Возвращаем корень дерева
    return array[0]

print(gen_nobin_tree(height, root))
"""


"""
Реализовать нерекурсивный вариант функции для построения бинарного дерева.

Можно разбить данную задачу на 2 этапа: 
1) построение корней дерева полностью (список списков, в котором, каждый "уровень" дерева - это список) (roots)

2) итерация по этому списку списков (roots) с выборкой элементов оттуда и помещением их в "правильное" место нашего дерева


def gen_bin_tree(height: int, root: int, left_leaf, right_leaf) -> dict:
    roots = [[root]]

    for leaf in range(height - 1):
        if (len(roots) == 1):
            r = roots[0]  # помнить про тип данных
        else:
            r = [item for s in roots[-1] for item in s]
        leaves = list(
            map(
                lambda root_value:
                [left_leaf(root_value),
                 right_leaf(root_value)], r))

        roots.append(leaves)

    roots.reverse()

    roots[-1] = [roots[-1]]
    roots[0] = list(map(lambda x: [{
        str(x[0]): []
    }, {
        str(x[1]): []
    }], roots[0]))

    for i in range(height - 1):
        sublist = roots[i]
        for j in range(len(sublist)):
            x = sublist.pop()
            roots[i + 1][j // 2][j % 2] = {str(roots[i + 1][j // 2][j % 2]): x}
    tree = roots[-1][0][0]

    return tree


if __name__ == '__main__':
    print(gen_bin_tree(2, 5, lambda x: x + 3, lambda x: x * 2))






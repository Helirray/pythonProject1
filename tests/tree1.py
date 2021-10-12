import hexlet.fs
import copy
import os

def find_files_by_name(tree, substr):
    def walk(node, ancestry):
        name = hexlet.fs.get_name(node)
        new_ancestry = os.path.join(ancestry, name)
        if hexlet.fs.is_file(node):
            return [] if name.find(substr) < 0 else new_ancestry
        children = hexlet.fs.get_children(node)
        paths = map(lambda child: walk(child, new_ancestry), children)
        return hexlet.fs.flatten(paths)
    return walk(tree, '')



def count_size(node):
    if hexlet.fs.is_file(node):
        new_meta = copy.deepcopy(hexlet.fs.get_meta(node))
        return new_meta['size']
    children = hexlet.fs.get_children(node)
    size_counts = list(map(count_size, children))
    return sum(size_counts)


def du(node):
    children = hexlet.fs.get_children(node)
    result = map(lambda child: (hexlet.fs.get_name(child), count_size(child)), children)
    return sorted(list(result), key= lambda value: value[1], reverse=True)


def get_hidden_files_count(node):
    name = hexlet.fs.get_name(node)
    if hexlet.fs.is_file(node) and name.startswith('.'):
        return 1
    children = hexlet.fs.get_children(node)
    if children is None:
        return 0
    counts = list(map(get_hidden_files_count, children))
    return sum(counts)


def downcase_file_names(node):
    name = hexlet.fs.get_name(node)
    new_meta = copy.deepcopy(hexlet.fs.get_meta(node))
    if hexlet.fs.is_file(node):
        new_name = name.lower()
        return hexlet.fs.mkfile(new_name, new_meta)
    children = hexlet.fs.get_children(node)
    new_children = list(map(lambda child: downcase_file_names(child), children))
    new_tree = hexlet.fs.mkdir(name, new_children, new_meta)
    return new_tree


def get_nodes_count(node):
    if hexlet.fs.is_file(node):
        # Возвращаем 1 для учёта текущего файла
        return 1
    # Если узел — директория, получаем его детей
    children = hexlet.fs.get_children(node)
    # Самая сложная часть
    # Считаем количество потомков для каждого из детей,
    # вызывая рекурсивно нашу функцию get_nodes_count
    descendant_counts = list(map(get_nodes_count, children))
    # Возвращаем 1 (текущая директория) + общее количество потомков
    return 1 + sum(descendant_counts)


def generate():
    return mkdir(
        'python-package',
        [
            mkfile('Makefile'),
            mkfile('README.md'),
            mkdir('dist'),
            mkdir('test', [
                mkfile('test_solution.py'),
            ]),
            mkfile('pyproject.toml'),
            mkdir(
                '.venv',
                [
                    mkdir('lib', [
                        mkdir('python3.6', [
                            mkdir('site-packages', [
                                mkfile('hexlet-python-package.egg-link'),
                            ]),
                        ]),
                    ]),
                ],
                {'owner': 'root', 'hidden': False}
            ),
        ],
        {'hidden': True}
    )


def compress_images(node):
    children = hexlet.fs.get_children(node)
    new_meta = copy.deepcopy(hexlet.fs.get_meta(node))
    name = hexlet.fs.get_name(node)
    for d in children:
        if d['name'].endswith(".jpg") and {'size'} in d:
            d['meta']['size'] //= 2
    return hexlet.fs.mkdir(name, children, new_meta)


def compress_images1(tree):
    children = hexlet.fs.get_children(tree)

    def reduce_image_size(node):
        name = hexlet.fs.get_name(node)
        if not hexlet.fs.is_file(node) or not name.endswith('.jpg'):
            return node
        meta = hexlet.fs.get_meta(node)
        new_meta = copy.deepcopy(meta)
        new_meta['size'] //= 2
        return hexlet.fs.mkfile(name, new_meta)

    new_children = map(reduce_image_size, children)
    new_meta = copy.deepcopy(hexlet.fs.get_meta(tree))
    return hexlet.fs.mkdir(hexlet.fs.get_name(tree), list(new_children), new_meta)


tree = hexlet.fs.mkdir('/', [
    hexlet.fs.mkdir('etc', [
        hexlet.fs.mkdir('apache'),
        hexlet.fs.mkdir('nginx', [
            hexlet.fs.mkfile('.nginx.conf', {'size': 800}),
        ]),
        hexlet.fs.mkdir('.consul', [
            hexlet.fs.mkfile('.config.json', {'size': 1200}),
            hexlet.fs.mkfile('data', {'size': 8200}),
            hexlet.fs.mkfile('raft', {'size': 80}),
        ]),
     ]),
     hexlet.fs.mkfile('.hosts', {'size': 3500}),
     hexlet.fs.mkfile('resolve', {'size': 1000}),
])

tree2 = hexlet.fs.mkdir('/', [
    hexlet.fs.mkdir('etc', [
        hexlet.fs.mkdir('apache'),
        hexlet.fs.mkdir('nginx', [
            hexlet.fs.mkfile('nginx.conf', {'size': 800}),
        ]),
        hexlet.fs.mkdir('consul', [
            hexlet.fs.mkfile('.config.json', {'size': 1200}),
           hexlet.fs.mkfile('data', {'size': 8200}),
            hexlet.fs.mkfile('raft', {'size': 80}),
        ]),
    ]),
    hexlet.fs.mkfile('hosts', {'size': 3500}),
    hexlet.fs.mkfile('resolve', {'size': 1000}),
])

new_tree = downcase_file_names(tree)
print(du(tree2))

list_ = ['/', 'user', 'huy']
print(os.path.join(*list_))
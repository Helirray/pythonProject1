from capitalize import capitalize

assert capitalize('hello') == 'Hello'

assert capitalize('') == ''

def fill(coll, value, begin=0, end=None):
    chunk = [value for _ in coll[begin:end]]
    coll[begin:end] = chunk

def test_fill_default(collection, fill):
    fill(collection, '*')
    assert collection == ['*', '*', '*', '*']


def test_fill_start_ge_length(collection, fill):
    fill(collection, '*', 10, 12)
    assert collection == [1, 2, 3, 4]


def test_fill_start_ge_end(collection, fill):
    fill(collection, '*', 2, 2)
    assert collection == [1, 2, 3, 4]


def test_fill_end_ge_length(collection, fill):
    fill(collection, '*', 0, 10)
    assert collection == ['*', '*', '*', '*']

# if get({'hello': 'world'}, 'hello') != 'world':
#     raise Exception('wrong!!!')
#
# if get({}, 'hello', 'kitty') != 'kitty':
#     raise Exception('wrong!!!')
#
# if get({"hello": "world"}, "hello", "kitty") != 'world':
#     raise Exception('wrong!!!')
print('Все тесты пройдены!')

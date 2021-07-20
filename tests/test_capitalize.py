from capitalize import capitalize

assert capitalize('hello') == 'Hello'

assert capitalize('') == ''


# if get({'hello': 'world'}, 'hello') != 'world':
#     raise Exception('wrong!!!')
#
# if get({}, 'hello', 'kitty') != 'kitty':
#     raise Exception('wrong!!!')
#
# if get({"hello": "world"}, "hello", "kitty") != 'world':
#     raise Exception('wrong!!!')
print('Все тесты пройдены!')

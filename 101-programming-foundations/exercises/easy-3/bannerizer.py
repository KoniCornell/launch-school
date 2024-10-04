def print_in_box(text):
    length = len(text)
    top = '+-' + ('-' * length) + '-+'
    side = '| ' + (' ' * length) +' |'
    side_w_text = '| ' + (text) +' |'
    print(top)
    print(side)
    print(side_w_text)
    print(side)
    print(top)

print_in_box('Hello Sadness my old friend...')
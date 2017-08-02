flat_list = ['hi', 'test', 'of', 'list', 'of', 'of']
word_quantity = {}

final_list = list(filter(lambda a: a != '', flat_list))

print("final_list: ", final_list)

for pick in final_list:
    if pick not in word_quantity:
        word_quantity[pick] = 1
        print(word_quantity)
    else:
        word_quantity[pick] = word_quantity[pick] + 1
        print(word_quantity)

print("=" * 10)
print(word_quantity)

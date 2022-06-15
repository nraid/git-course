products = {
    'vegetables': ['tomato', 'cucumber', 'carrot'],
    'fruits': ['orange', 'apple', 'strawberry'],
    'snacks': ['chips', 'crackers', 'popcorn'],
    'water': ['soda', 'mineral water', 'juice']
}


def tags():
    for key in products[guess]:
        with open('text.txt', 'a') as f:
            f.write(f'{key}\n')
    print('Product found. The tags are in file tags.txt.')


while products:
    guess = input('Guess a product to take it home xD: ')
    if guess in products:
        tags()
        products.pop(guess)
    if not products:
        print('All products are gone.')






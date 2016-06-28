inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'arrow']

def display_inventory(inventory):
    print('Inventory:')
    for i,u in inventory.items():
        print(u, i)
    print('Total number of items: ', sum(inventory.values()))

def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i in inventory:
            inventory[i] += 1
        elif i not in inventory:
             inventory.update({i:1})

def print_table(inventory):
    w = max(len(x) for x in inventory)
    line_w = (w * 2)+8
    print('{0:>{w}}\t{1:>{w}} '.format( 'COUNT', 'ITEM NAME', w = w))
    print('-' * line_w)
    for i,u in inventory.items():
        print('{0:>{w}}\t{1:>{w}}'.format(u,i, w = w))
    print('-' * line_w)
    print('Total number of items: ', sum(inventory.values()))

def import_inventory(filename = 'import_inventory.csv'):
    line_counter = 0
    with open(filename, 'r') as f:
        for line in f:
            line_counter +=1
            if line_counter > 1:      #we don't want header
                word = line.strip().split(',')
                if word[0] in inventory:
                    inventory[word[0]] += int(word[1])
                elif word[0] not in inventory:
                    inventory.update({word[0]:int(word[1])})

def export_inventory(filename = 'export_inventory.csv'):
    with open(filename, 'w') as f:
        [f.write('item_name,count\n')]
        [f.write('{0},{1}\n'.format(key, value)) for key, value in inventory.items()]







import_inventory()
display_inventory(inventory)
print_table(inventory)
export_inventory()

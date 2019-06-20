# dictionaries allow to maps keys to values {}

apples = {'cox': 17,
          'braeburn': 21,
          'pink lady': 7,
          'royal garla': 12,
          'fuji': 1}

cox_stock = apples['cox']
print(f'we have {cox_stock} cox apples')

for apple in apples.keys():
    print(apple)

for apple, stock_count in apples.items():
    print(f'we have {stock_count} {apple} apples')

# get retrieves a value, if the value does not exist, a default value can be assigned
mac_apples = apples.get('macintosh', 0)
print(f'we have {mac_apples} macintosh apples')

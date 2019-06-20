# lists can contain repeated items []
# sets can only contain unique items

available_apples = ['cox', 'pink lady', 'braeburn']
available_apples.append('royal garla')
available_apples.remove('braeburn')

new_apples = ['pink lady', 'empire', 'mutsu', 'red delicious', 'cox']
available_apples.extend(new_apples)
print(available_apples)

unique_apples = set(available_apples)
available_apples = list(unique_apples)
print(unique_apples)
print(available_apples)

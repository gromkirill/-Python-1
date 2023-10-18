users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
user = {
    'Общее количество':0,
    'Уникальные посещения':0
}
count = len(users)
user['Общее количество'] = count
user_set = set(users)
count_user = len(user_set)
user['Уникальные посещения'] = count_user

print(user)
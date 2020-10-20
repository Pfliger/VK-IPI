
import requests

TOKEN = '' # Место ввода токена
app_id = ''


class UsersVK:
    API_BASE_URL = 'https://api.vk.com/method/'

    def __init__(self, token, user_id, version='5.124'):
        self.vksite = 'https://vk.com/'
        self.token = token
        self.version = version
        self.user_id = user_id
        response = requests.get(self.API_BASE_URL + 'users.get', params={'user_ids': self.user_id, 'fields': 'domain',
                                'access_token': token, 'v': 5.124})
        user = response.json()
        self.domain = user['response'][0]['domain']
        self.friend_list = self.get_friends_list()

    def get_friends_list(self):
        response = requests.get(self.API_BASE_URL + 'friends.get', params={'user_id': self.user_id,
                                'access_token': self.token, 'v': 5.124})
        friends = response.json()['response']['items']
        return friends

    def __and__(self, other):
        result = []
        for friend in self.friend_list:
            if friend not in other.friend_list:
                continue
            result.append(friend)
        return result

    def __str__(self):
        return self.vksite + self.domain


user_1 = UsersVK(TOKEN, 7)
user_2 = UsersVK(TOKEN, 22)

print('Ссылки на страницы пользователей: ')
print(user_1)
print(user_2)

print('Список общих друзей: ')
print(user_1 & user_2)

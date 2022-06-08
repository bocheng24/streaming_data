from faker import Faker
from datetime import datetime
from random import randint, uniform

faker = Faker()

def get_user(id):

    profile = faker.simple_profile()

    user = {
        'id': id,
        'username': profile['username'],
        'email': profile['mail'],
        'create_time': datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    }

    return user

def get_shop():

    shop = {
        'userId': randint(1, 15),
        'quantity': randint(1, 10),
        'price': round(randint(1, 10) * uniform(0, 1), 2)
    }

    return shop

if __name__ == '__main__':

    for i in range(10):
        user = get_user(i + 1)
        print(get_shop())
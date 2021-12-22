from faker import Faker
from datetime import datetime

faker = Faker()

def get_user():

    profile = faker.simple_profile()

    user = {
        'username': profile['username'],
        'email': profile['mail'],
        'create_time': datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    }

    return user

if __name__ == '__main__':

    print(get_user())
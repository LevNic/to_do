import random

from mimesis import Person
from mimesis.enums import Gender
from collections import OrderedDict
from pprint import pprint


def get_user(number):
    """
    Creates random user data
    :param number: number of users
    :return: user data list
    """
    data = []
    for i in range(number):
        user_gender = random.sample([Gender.MALE, Gender.FEMALE], 1)[0]
        person = Person('ru')
        data.append(OrderedDict(first_name=person.first_name(gender=user_gender),
                                last_name=person.last_name(gender=user_gender),
                                age=person.age(minimum=18, maximum=66),
                                email=person.email(domains=('yandex.ru', 'gmail.com')),
                                username=person.username(template='UU_d'))
                    )
    return data


if __name__ == '__main__':
    pprint(get_user(5))

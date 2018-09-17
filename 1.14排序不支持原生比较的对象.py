class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def sort_notcompare():
    users = [User(23), User(3), User(99)]
    print(users)
    print(sorted(users, key=lambda u: u.user_id))

sort_notcompare()


users = [User(23), User(3), User(99)]
from operator import attrgetter
print(sorted(users, key=attrgetter('user_id')))


# by_name = sorted(users, key=attrgetter('last_name', 'first_name'))


min(users, key=attrgetter('user_id'))
max(users, key=attrgetter('user_id'))

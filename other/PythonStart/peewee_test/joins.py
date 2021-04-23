import datetime

from peewee import *
import logging

logger = logging.getLogger("peewee")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

db = MySQLDatabase('peewee', host='127.0.0.1', user='root', passwd='root')


class BaseModel(Model):
    class Meta:
        database = db  # 这里是数据库链接，为了方便建立多个表，可以把这个部分提炼出来形成一个新的类


class User(BaseModel):
    username = TextField()

    class Meta:
        table_name = 'user2'


class Tweet(BaseModel):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)
    user = ForeignKeyField(User, backref="tweets")

    class Meta:
        table_name = 'tweet2'


class Favorite(BaseModel):
    user = ForeignKeyField(User, backref="favorites")
    tweet = ForeignKeyField(Tweet, backref="favorites")


def populate_test_data():
    data = (
        ('huey', ('meow', 'hiss', 'purr')),
        ('mickey', ('woof', 'whine')),
        ('zaizee', ()))
    for username, tweets in data:
        user = User.create(username=username)
        for tweet in tweets:
            Tweet.create(user=user, content=tweet)

    # Populate a few favorites for our users, such that:
    favorite_data = (
        ('huey', ['whine']),
        ('mickey', ['purr']),
        ('zaizee', ['meow', 'purr']))
    for username, favorites in favorite_data:
        user = User.get(User.username == username)
        for content in favorites:
            tweet = Tweet.get(Tweet.content == content)
            Favorite.create(user=user, tweet=tweet)


if __name__ == "__main__":
    # db.connect()
    # db.create_tables([User, Tweet, Favorite])

    #正向
    # for tweet in Tweet.select():
    #     print(tweet.content, tweet.user.username)

    # populate_test_data()

    # 使用表连接 能减少网络传输
    # query = Tweet.select(Tweet, User.username).join(User).where(User.username=="mickey")
    # for q in query:
    #     print(q.user.username, q.content)

    # query = Tweet.select(Tweet, User.username).join(User, on=(Tweet.user==User.id)).where(User.username=="mickey")
    # for q in query:
    #     print(q.user.username, q.content)

    #反向
    # user = User.get(User.username=="mickey")
    # tweets = Tweet.select().where(Tweet.user==user)
    # for tweet in tweets:
    #     print(user.username, tweet.content)

    #反向2
    # tweets = User.get(User.username == "mickey").tweets
    # # tweets = Tweet.select().where(Tweet.user == user)
    # for tweet in tweets:
    #     print(tweet.content)
    #想得到5个数据， 会发起5次请求 + 1 -> n+1查询
    # for tweet in Tweet.select():
    #     print(tweet.content, tweet.user.username)
    #什么时候sql会发起请求，以及会发起多少次请求， 开发人员来说 很重要 很多sql高手不会喜欢用orm
    query = Tweet.select(Tweet, User.username).join(User).where(User.username == "mickey")
    for q in query:
        print(q.user.username, q.content)
import factory

from . import models


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User

    username = factory.Sequence(lambda n: "User %03d" % n)
    password = factory.Faker('password')

import factory
from django.contrib.auth.models import User

class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model= User

    username = factory.Sequence(lambda n: 'username{0}'.format(n))
    first_name = factory.Sequence(lambda n: 'first_name{0}'.format(n))
    last_name = factory.Sequence(lambda n: 'last_name{0}'.format(n))
    email = factory.Sequence(lambda n: 'email{0}@gmail.com'.format(n))
    password = "Passw0rd"

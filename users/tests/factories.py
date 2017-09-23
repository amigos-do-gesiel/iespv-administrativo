import factory
from users.models import Secretary, Administrator
from django.contrib.auth.models import User

class SecretaryFactory(factory.DjangoModelFactory):
    class Meta:
        model= Secretary

    first_name = factory.Sequence(lambda n: 'first_name{0}'.format(n))
    phone_number = factory.Sequence(lambda n: '{0}'.format(n))
    username = factory.Sequence(lambda n: 'secretary{0}'.format(n))
    email = factory.Sequence(lambda n: 'secretary{0}@gmail.com'.format(n))
    password = "1234"

class AdministratorFactory(factory.DjangoModelFactory):
    class Meta:
        model= Administrator

    first_name = factory.Sequence(lambda n: 'first_name{0}'.format(n))
    phone_number = factory.Sequence(lambda n: '{0}'.format(n))
    username = factory.Sequence(lambda n: 'admin{0}'.format(n))
    email = factory.Sequence(lambda n: 'admin{0}@gmail.com'.format(n))
    password = "1234"

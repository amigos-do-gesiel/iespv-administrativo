import factory
from users.models import Secretary, Administrator
from django.contrib.auth.models import User

class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model= User

    username = factory.Sequence(lambda n: 'username{0}'.format(n))
    first_name = factory.Sequence(lambda n: 'first_name{0}'.format(n))
    last_name = factory.Sequence(lambda n: 'last_name{0}'.format(n))
    email = factory.Sequence(lambda n: 'email{0}@gmail.com'.format(n))
    password = factory.PostGenerationMethodCall('set_password', 'test_password')



class SecretaryFactory(factory.DjangoModelFactory):
    class Meta:
        model= Secretary

    phone_number = factory.Sequence(lambda n: '{0}'.format(n))
    user = factory.SubFactory(UserFactory)

class AdministratorFactory(factory.DjangoModelFactory):
    class Meta:
        model= Administrator

    phone_number = factory.Sequence(lambda n: '{0}'.format(n))
    user = factory.SubFactory(UserFactory)
    

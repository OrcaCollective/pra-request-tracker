import factory
from factory import Faker
from factory.django import DjangoModelFactory

from ..models import Agency, Correspondence, RecordRequest, RecordRequestFile


class AgencyFactory(DjangoModelFactory):
    class Meta:
        model = Agency

    name = Faker("company")


class RecordRequestFactory(DjangoModelFactory):
    class Meta:
        model = RecordRequest

    agency = factory.SubFactory(AgencyFactory)


class CorrespondenceFactory(DjangoModelFactory):
    class Meta:
        model = Correspondence

    to_address = factory.Faker("email")
    from_address = factory.Faker("email")
    request = factory.SubFactory(RecordRequestFactory)


class RecordRequestFileFactory(DjangoModelFactory):
    class Meta:
        model = RecordRequestFile

    request = factory.SubFactory(RecordRequestFactory)
    title = Faker("file_name")
    file = factory.django.FileField()

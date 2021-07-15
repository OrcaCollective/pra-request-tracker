import factory
from factory import Faker
from factory.django import DjangoModelFactory

from ..models import Agency, RecordRequest, RecordRequestFile


class AgencyFactory(DjangoModelFactory):
    class Meta:
        model = Agency

    name = Faker("company")


class RecordRequestFactory(DjangoModelFactory):
    class Meta:
        model = RecordRequest

    agency = factory.SubFactory(AgencyFactory)


class RecordRequestFileFactory(DjangoModelFactory):
    class Meta:
        model = RecordRequestFile

    request = factory.SubFactory(RecordRequestFactory)
    title = Faker("file_name")
    file = factory.django.FileField()

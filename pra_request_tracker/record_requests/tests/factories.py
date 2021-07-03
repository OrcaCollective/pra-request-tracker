from factory import Faker
import factory
from factory.django import DjangoModelFactory

from ..models import Agency
from ..models import RecordRequest
from ..models import RecordRequestFile


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

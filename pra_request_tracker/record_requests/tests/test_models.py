import pytest
from .factories import AgencyFactory
from .factories import RecordRequestFactory
from .factories import RecordRequestFileFactory

from ..models import Agency, RecordRequestFile
from ..models import RecordRequest


@pytest.mark.django_db(transaction=True)
def test_agency_request_count():
    agency = AgencyFactory.create()

    for _ in range(2):
        RecordRequestFactory.create(agency=agency)

    assert agency.request_count == 2


@pytest.mark.django_db(transaction=True)
def test_agency_delete():
    agency = AgencyFactory.create()
    pk = agency.pk
    with pytest.raises(NotImplementedError):
        agency.delete()

    assert Agency.objects.filter(pk=pk).first() is not None


@pytest.mark.django_db(transaction=True)
def test_record_request_status_label():
    status = RecordRequest.Status.INSTALLMENTS
    record_request = RecordRequestFactory.create(status=str(status))

    assert record_request.status_label == status.label


@pytest.mark.django_db(transaction=True)
def test_record_requeset_delete():
    record_request = RecordRequestFactory.create()
    pk = record_request.pk

    with pytest.raises(NotImplementedError):
        record_request.delete()

    assert RecordRequest.objects.filter(pk=pk).first() is not None


@pytest.mark.django_db(transaction=True)
def test_record_request_files():
    record_request = RecordRequestFactory.create()

    files = []
    for _ in range(3):
        files.append(RecordRequestFileFactory.create(request=record_request))

    assert files == list(record_request.files)


@pytest.mark.django_db(transaction=True)
def test_record_request_file_delete():
    file = RecordRequestFileFactory.create()
    pk = file.pk
    file.delete()

    assert RecordRequestFile.objects.filter(pk=pk).first() is None

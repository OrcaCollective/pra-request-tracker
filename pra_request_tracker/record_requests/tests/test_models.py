from django.test import TestCase

from .factories import AgencyFactory
from .factories import RecordRequestFactory
from .factories import RecordRequestFileFactory

from ..models import Agency, RecordRequestFile
from ..models import RecordRequest


class AgencyTestCase(TestCase):
    def test_agency_request_count(self):
        agency = AgencyFactory.create()

        for _ in range(2):
            RecordRequestFactory.create(agency=agency)

        self.assertEqual(agency.request_count, 2)

    def test_agency_delete(self):
        agency = AgencyFactory.create()
        pk = agency.pk
        with self.assertRaises(NotImplementedError):
            agency.delete()

        self.assertIsNotNone(Agency.objects.filter(pk=pk).first())


class RecordRequestTestCase(TestCase):
    def test_record_request_status_label(self):
        status = RecordRequest.Status.INSTALLMENTS
        record_request = RecordRequestFactory.create(status=str(status))

        self.assertEqual(record_request.status_label, status.label)

    def test_record_requeset_delete(self):
        record_request = RecordRequestFactory.create()
        pk = record_request.pk

        with self.assertRaises(NotImplementedError):
            record_request.delete()

        self.assertIsNotNone(RecordRequest.objects.filter(pk=pk).first())

    def test_record_request_files(self):
        record_request = RecordRequestFactory.create()

        files = []
        for _ in range(3):
            files.append(RecordRequestFileFactory.create(request=record_request))

        self.assertEqual(files, list(record_request.files))


class RecordRequestFileTestCase(TestCase):
    def test_record_request_file_delete(self):
        file = RecordRequestFileFactory.create()
        pk = file.pk
        file.delete()

        self.assertIsNone(RecordRequestFile.objects.filter(pk=pk).first())

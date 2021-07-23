from django.test import TestCase

from ..models import Agency, RecordRequest, RecordRequestFile
from .factories import (
    AgencyFactory,
    CorrespondenceFactory,
    RecordRequestFactory,
    RecordRequestFileFactory,
)


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

    def test_record_request_correspondences(self):
        record_request = RecordRequestFactory.create()

        correspondences = []
        for _ in range(3):
            correspondences.append(CorrespondenceFactory.create(request=record_request))

        self.assertEqual(correspondences, list(record_request.correspondences))

    def test_record_request_correspondences_prefetch_files(self):
        record_request = RecordRequestFactory.create()

        for _ in range(3):
            correspondence = CorrespondenceFactory.create(request=record_request)
            for _ in range(2):
                RecordRequestFileFactory.create(correspondence=correspondence)

        with self.assertNumQueries(2):
            record_request.correspondences[0].recordrequestfile_set.all()
            record_request.correspondences[1].recordrequestfile_set.all()
            record_request.correspondences[2].recordrequestfile_set.all()


class RecordRequestFileTestCase(TestCase):
    def test_record_request_file_delete(self):
        file = RecordRequestFileFactory.create()
        pk = file.pk
        file.delete()

        self.assertIsNone(RecordRequestFile.objects.filter(pk=pk).first())

    def test_auto_name(self):
        file = RecordRequestFileFactory.create()
        file.title = None
        file.save()

        self.assertEqual(file.file.name, file.title)

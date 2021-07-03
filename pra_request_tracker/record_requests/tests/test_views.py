from django.test import TestCase
from django.test import RequestFactory

from .factories import AgencyFactory
from .factories import RecordRequestFactory

from ..views import AgencyListView


class ViewTestCase(TestCase):
    view_cls = None

    def setUp(self):
        super().setUp()
        self.request_factory = RequestFactory()

    def get(self, *args, **kwargs):
        self.request = self.request_factory.get(*args, **kwargs)
        self.view = self.view_cls()
        self.view.setup(self.request)
        return self.view


class AgencyListViewTestCase(ViewTestCase):
    view_cls = AgencyListView

    def test_prefetches_record_requests(self):
        for _ in range(3):
            agency = AgencyFactory.create()
            for _ in range(4):
                RecordRequestFactory.create(agency=agency)

        view = self.get("/")
        with self.assertNumQueries(2):
            objects = list(view.get_queryset())
            for object in objects:
                self.assertEqual(object.request_count, 4)

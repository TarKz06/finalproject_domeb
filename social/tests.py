from django.test import TestCase
from social.views import PostListView
from social.views import PostDetailView
from social.views import PostEditView
from social.views import PostDeleteView
from social.views import AddNoiser
from social.views import RemoveNoiser
from social.views import AddServicer
from social.views import RemoveServicer
from social.views import AddRepairer
from social.views import RemoveRepairer
from social.views import AddParceler
from social.views import RemoveParceler
from social.views import UserSearch
from social.views import ListNoisers
from social.views import ListServicers
from social.views import ListRepairers
from social.views import Listparcelers
from social.views import PostNotification
from social.views import NoiseNotification
from social.views import ServiceNotification
from social.views import RepairNotification
from social.views import ParcelNotification
from social.views import ThreadNotification
from social.views import RemoveNotification
from social.views import ListThreads
from social.views import CreateThread
from social.views import ThreadView
from social.views import CreateMessage
# Create your tests here.

class PostListViewTestcase(TestCase):
    def setUp(self):
        PostListView

    def test_postlistview(self):


class PostDetailViewTestcase(TestCase):
    def setUp(self):
        PostDetailView

    def test_postdetailview(self):


class PostEditViewTestcase(TestCase):
    def setUp(self):
        PostEditView

    def test_posteditview(self):


class PostDeleteViewTestcase(TestCase):
    def setUp(self):
        PostDeleteView

    def test_postdeleteview(self):



class AddNoiserTestcase(TestCase):
    def setUp(self):
        AddNoiser

    def test_addnoiser(self):


class RemoveNoiserTestcase(TestCase):
    def setUp(self):
        RemoveNoiser

    def test_removenoiser(self):


class AddServicerTestcase(TestCase):
    def setUp(self):
        AddServicer

    def test_addservicer(self):


class RemoveServicerTestcase(TestCase):
    def setUp(self):
        RemoveServicer

    def test_removeservicer(self):



class AddRepairerTestcase(TestCase):
    def setUp(self):
        AddRepairer

    def test_addrepairer(self):



class RemoveRepairerTestcase(TestCase):
    def setUp(self):
        RemoveRepairer

    def test_removerepairer(self):



class AddParcelerTestcase(TestCase):
    def setUp(self):
        AddParceler

    def test_addparceler(self):



class RemoveParcelerTestcase(TestCase):
    def setUp(self):
        RemoveParceler

    def test_removeparceler(self):


class UserSearchTestcase(TestCase):
    def setUp(self):
        UserSearch

    def test_usersearch(self):


class ListNoisersTestcase(TestCase):
    def setUp(self):
        ListNoisers

    def test_listnoiser(self):



class ListServicersTestcase(TestCase):
    def setUp(self):
        ListServicers

    def test_listservicer(self):


class ListRepairersTestcase(TestCase):
    def setUp(self):
        ListRepairers

    def test_listrepairer(self):


class ListparcelersTestcase(TestCase):
    def setUp(self):
        Listparcelers

    def test_listparceler(self):


class PostNotificationTestcase(TestCase):
    def setUp(self):
        PostNotification

    def test_postnotification(self):



class NoiseNotificationTestcase(TestCase):
    def setUp(self):
        NoiseNotification

    def test_noisenotification(self):


class ServiceNotificationTestcase(TestCase):
    def setUp(self):
        ServiceNotification

    def test_servicenotification(self):



class RepairNotificationTestcase(TestCase):
    def setUp(self):
        RepairNotification

    def test_repairnotification(self):



class ParcelNotificationTestcase(TestCase):
    def setUp(self):
        ParcelNotification

    def test_parcelnotification(self):


class ThreadNotificationTestcase(TestCase):
    def setUp(self):
        ThreadNotification

    def test_threadnotification(self):



class RemoveNotificationTestcase(TestCase):
    def setUp(self):
        RemoveNotification

    def test_removenotification(self):



class ListThreadsTestcase(TestCase):
    def setUp(self):
        ListThreads

    def test_listthread(self):


#     From this to continue.

class CreateThreadTestcase(TestCase):
    def setUp(self):
        CreateThread

    def test_createthread(self):


class ThreadViewTestcase(TestCase):
    def setUp(self):
        ThreadView

    def test_threadview(self):


class CreateMessageTestcase(TestCase):
    def setUp(self):
        CreateMessage

    def test_createmessage(self):



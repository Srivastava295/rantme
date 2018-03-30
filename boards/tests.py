"""import required modules."""
from django.urls import reverse, resolve
from django.test import TestCase
from .views import index
# Create your tests here.


class IndexTests(TestCase):
    """Index tests."""

    def test_index_view_status_code(self):
        """Test index view."""
        url = reverse('index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_index_url_resolves_index_view(self):
        """Test index view."""
        view = resolve('/')
        self.assertEquals(view.func, index)


# class BoardTopicsTests(TestCase):
#    """Board tests."""

#    def setUp(self):
#        """Set up."""
#        Board.objects.create(name='Django', description='Django board.')
#
#    def test_board_topics_view_success_status_code(self):
#        """Test board topic success."""
#        url = reverse('board_topics', kwargs={'pk': 1})
#        response = self.client.get(url)
#        self.assertEquals(response.status_code, 200)
#
#    def test_board_topics_view_not_found_status_code(self):
#        """Test board no view."""
#        url = reverse('board_topics', kwargs={'pk': 99})
#        response = self.client.get(url)
#        self.assertEquals(response.status_code, 404)
#
#    def test_board_topics_url_resolves_board_topics_view(self):
#        """Test board url resolve."""
#        self.assertEquals(view.func, board_topics)
#

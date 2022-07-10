from django.test import TestCase
from .views import delete_review


class TestDeleteReviewView(TestCase):

    def test_can_delete_review(self):
        review = Review.objects(body='Test Review')
        response = self.client.get(f'delete/{review.id}/')
        self.assertRedirects(response, '/')
        updated_review = Review.objects.get(id=review.id)
        self.assertFalse(updated_review.done)

from django.test import TestCase
from .forms import ReviewForm

# Test if form will submit without an
#  names field populated (Author field is hidden)

class TestReviewForm(TestCase):

    def test_submit_review_name_is_required(self):
        form = ReviewForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())

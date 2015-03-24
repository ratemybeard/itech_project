from django.test import TestCase
from RMB.models import Categories, Comments, Ratings
from django.core.urlresolvers import reverse


class CategoriesTest (TestCase):

	def create_category(self, cat_descr="black beards"):
		return Categories.objects.create(cat_descr=cat_descr)
	def test_category_creation(self):
		testCategory = self.create_category()
		self.assertTrue(isinstance(testCategory, Categories))
		self.assertEqual(testCategory.__unicode__(), testCategory.cat_descr)

	def test_rmb_view(self):
		testCategory = self.create_category()
		url = reverse("RMB.views")
		resp = self.client.get(url)

		self.assertEqual(resp.status_code, 200)
		self.assertIn(testCategory.title, resp.content)

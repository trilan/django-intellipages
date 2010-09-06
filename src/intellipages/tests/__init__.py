from django.core.paginator import Paginator
from django.template import Context, Template
from django.test import TestCase


class IntellipagesFilterTestCase(TestCase):

    def setUp(self):
        self.paginator = Paginator(range(11), 1)

    def render(self, template, **context_dict):
        context = Context(context_dict)
        return Template('{% load intellipages %}' + template).render(context)

    def test_bad_context(self):
        result = self.render(
            '{% for p in page|intellipages %} {{ p }}{% endfor %}')

    def test_first_page(self):
        result = self.render(
            '{% for p in page|intellipages %} {{ p }}{% endfor %}',
            page=self.paginator.page(1))
        self.assertEqual(result, ' 1 2 3 0 11')

    def test_last_page(self):
        result = self.render(
            '{% for p in page|intellipages %} {{ p }}{% endfor %}',
            page=self.paginator.page(11))
        self.assertEqual(result, ' 1 0 9 10 11')

    def test_middle_page(self):
        result = self.render(
            '{% for p in page|intellipages %} {{ p }}{% endfor %}',
            page=self.paginator.page(6))
        self.assertEqual(result, ' 1 0 4 5 6 7 8 0 11')

    def test_not_far_from_start(self):
        result = self.render(
            '{% for p in page|intellipages %} {{ p }}{% endfor %}',
            page=self.paginator.page(5))
        self.assertEqual(result, ' 1 2 3 4 5 6 7 0 11')

    def test_not_far_from_end(self):
        result = self.render(
            '{% for p in page|intellipages %} {{ p }}{% endfor %}',
            page=self.paginator.page(7))
        self.assertEqual(result, ' 1 0 5 6 7 8 9 10 11')

    def test_page_number_as_argument(self):
        result = self.render(
            '{% for p in page.paginator|intellipages:page.number %} {{ p }}{% endfor %}',
            page=self.paginator.page(6))
        self.assertEqual(result, ' 1 0 4 5 6 7 8 0 11')

    def test_empty_page(self):
        result = self.render(
            '{% for p in paginator|intellipages:12 %} {{ p }}{% endfor %}',
            paginator=self.paginator)
        self.assertEqual(result, '')
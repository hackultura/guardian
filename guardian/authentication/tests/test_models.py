# -*- coding: utf-8 -*-

from django.test import TestCase
from django.db import models

from guardian.authentication.models import User


class UserTest(TestCase):
    def test_should_have_email_field(self):
        """Should have a email field"""
        field = User._meta.get_field('email')
        self.assertIsInstance(field, models.EmailField)

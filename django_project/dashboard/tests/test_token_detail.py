from rest_framework.test import APIRequestFactory
from django.contrib.auth.models import AnonymousUser
from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from core.models.token_detail import CustomApiKey
from dashboard.api_views.users import TokenDetail
from georepo.tests.model_factories import (
    UserF
)


class TestTokenDetail(TestCase):

    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.superuser = UserF.create(is_superuser=True)
        self.token_payload = {
            'platform': 'Test',
            'owner': 'Test'
        }
        self.user_1 = UserF.create()
        self.token_1 = Token.objects.create(user=self.user_1)
        self.user_2 = UserF.create()

    def create_token(self, token_ptr):
        key = CustomApiKey(
            token_ptr=token_ptr,
            user=token_ptr.user,
            **self.token_payload
        )
        key.save_base(raw=True)

    def test_token_access(self):
        self.create_token(self.token_1)
        # forbidden without user
        kwargs = {
            'id': self.user_1.id
        }
        request = self.factory.get(
            reverse('token-detail', kwargs=kwargs)
        )
        request.user = AnonymousUser()
        view = TokenDetail.as_view()
        response = view(request, **kwargs)
        self.assertEqual(response.status_code, 403)
        # user 2 cannot access user 1
        request.user = self.user_2
        response = view(request, **kwargs)
        self.assertEqual(response.status_code, 403)
        # superuser can access any token
        request.user = self.superuser
        response = view(request, **kwargs)
        self.assertEqual(response.status_code, 200)

    def test_token_get_list(self):
        self.create_token(self.token_1)
        kwargs = {
            'id': self.user_1.id
        }
        request = self.factory.get(
            reverse('token-detail', kwargs=kwargs)
        )
        request.user = self.user_1
        view = TokenDetail.as_view()
        response = view(request, **kwargs)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_token_create(self):
        kwargs = {
            'id': self.user_2.id
        }
        request = self.factory.post(
            reverse('token-detail', kwargs=kwargs),
            self.token_payload
        )
        request.user = self.user_2
        view = TokenDetail.as_view()
        response = view(request, **kwargs)
        self.assertEqual(response.status_code, 201)
        token = Token.objects.filter(user=self.user_2).first()
        self.assertTrue(token)
        key = CustomApiKey.objects.filter(
            token_ptr=token
        ).first()
        self.assertTrue(key)
        self.assertEqual(key.platform, self.token_payload['platform'])
        # cannot create for existing token
        response = view(request, **kwargs)
        self.assertEqual(response.status_code, 400)

    def test_token_update(self):
        self.create_token(self.token_1)
        kwargs = {
            'id': self.user_1.id
        }
        request = self.factory.put(
            reverse('token-detail', kwargs=kwargs),
            {
                'is_active': False
            }
        )
        request.user = self.user_1
        view = TokenDetail.as_view()
        response = view(request, **kwargs)
        self.assertEqual(response.status_code, 204)
        token = Token.objects.filter(user=self.user_1).first()
        self.assertTrue(token)
        key = CustomApiKey.objects.filter(
            token_ptr=token
        ).first()
        self.assertTrue(key)
        self.assertFalse(key.is_active)

    def test_token_delete(self):
        self.create_token(self.token_1)
        kwargs = {
            'id': self.user_1.id
        }
        request = self.factory.delete(
            reverse('token-detail', kwargs=kwargs)
        )
        request.user = self.user_1
        view = TokenDetail.as_view()
        response = view(request, **kwargs)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(CustomApiKey.objects.filter(
            user=self.user_1
        ).exists())

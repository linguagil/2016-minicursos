from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from ..factories import UserFactory


class AuthTests(APITestCase):
    def test_authenticate_user(self):
        self.given_i_am_an_user()
        # self.when_i_post_to_api_token()
        # self.then_i_should_get_my_token()

    def given_i_am_an_user(self):
        # given
        user = self.user = UserFactory()
        self.data = {'username': user.username, 'password': user.password}

    # def when_i_post_to_api_token(self):
    #     pass

    # def _when_i_post_to_api_token(self):
    #     # when
    #     url = reverse('api-token')
    #     self.response = self.client.post(url, self.data, format='json')

    # def then_i_should_get_my_token(self):
    #     pass

    # def _then_i_should_get_my_token(self):
    #     # then
    #     expected_response = {"token": self.user.auth_token}
    #     self.assertEqual(self.response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(self.response.content, expected_response)



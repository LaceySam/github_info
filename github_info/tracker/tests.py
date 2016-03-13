from django.core.cache import cache
from django.test import TestCase

from mock import MagicMock, patch

from models import Repo


class RepoTestCase(TestCase):
    test_name = 'baboon'
    zero_hash = '5961a8eab1dc2946ffae1a27203e81b6df5a3fa6'
    one_hash = 'dba1e4e775e91d47a6ca7b69ac2eb325b1411a9c'

    test_cache_value = 'potato'

    req_mock = MagicMock()
    req_mock.json = MagicMock(return_value=test_cache_value)
    req_mock.status_code = 200

    def setUp(self):
        Repo.objects.create(repo_name=self.test_name)

    def test_issue_cache_key(self):
        """
        Should generate hex hashes that has combo of repo_name and page number
        """
        repo = Repo.objects.get(repo_name=self.test_name)
        hashA = repo.get_issue_cache_key(1)
        self.assertEqual(hashA, self.zero_hash)

        hashB = repo.get_issue_cache_key(2)
        self.assertEqual(hashB, self.one_hash)

    @patch('requests.get', return_value=req_mock)
    def test_get_issues_caches(self, patch1):
        """
        Should verfiy that Repo.get_issues is using the cache
        """
        repo = Repo.objects.get(repo_name=self.test_name)
        repo.get_issues()

        test_cache = cache.get(self.zero_hash)

        self.assertEqual(test_cache, self.test_cache_value)

    @patch('django.core.cache.cache.get', return_value=test_cache_value)
    def test_get_issues_uses_cache(self, patch1):
        """
        Should verfiy that Repo.get_issues will retrive something from the
        cache
        """
        repo = Repo.objects.get(repo_name=self.test_name)
        got, _ = repo.get_issues()

        self.assertEqual(got, self.test_cache_value)

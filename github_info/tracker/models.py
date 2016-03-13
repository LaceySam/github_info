from __future__ import unicode_literals

from django.conf import settings
from django.core.cache import cache
from django.db import models

import sha
import urllib
import urlparse

import requests


class Repo(models.Model):
    repo_name = models.CharField(
        max_length=settings.DEFAULT_FORM_CHAR_LIMIT,
    )

    def get_issue_cache_key(self, page):
        return sha.new(self.repo_name + str(page)).hexdigest()

    def get_issues(self, page=1):
        url = urlparse.urlunparse((
            'https',
            settings.GITHUB_API_URI,
            urlparse.urljoin(
                settings.GITHUB_API_REPO_URI,
                self.repo_name + settings.GITHUB_API_ISSUES_URL,
            ),
            '',
            urllib.urlencode(
                {'page': page, 'per_page': settings.DEFAULT_PAGE_SIZE}
            ),
            ''
        ))

        # Check cache to see if we already have got this data locally
        cache_key = self.get_issue_cache_key(page)
        cached_resp = cache.get(cache_key)
        if cached_resp is not None:
            return cached_resp

        resp = requests.get(url)
        payload = resp.json()

        cache.set(cache_key, payload, settings.CACHE_LIFE_SPAN)

        return payload

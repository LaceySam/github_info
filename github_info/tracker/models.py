from __future__ import unicode_literals

from django.conf import settings
from django.db import models

import urllib
import urlparse

import requests


class Repo(models.Model):
    repo_name = models.CharField(
        max_length=settings.DEFAULT_FORM_CHAR_LIMIT,
    )

    def get_issues(self, page=0):
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

        resp = requests.get(url)

        return resp.json()

# Intro

A small django project that produces a webpage that will show the latest issues
on a github repo.

The project uses caching to avoid repeated requests to the github api, ajax
queries to load additional issues (also cached) and can view any public repo on
github.

## Setup

git clone https://github.com/Laceysam/github_info.git <br />
virtualenv env <br />
source env/bin/activate <br />
pip install -r requirements.txt <br />
cd github_info <br />
python manage.py migrate <br />
python manage.py test <br />
python manage.py runserver <br />

Then navigate to localhost:8000 and play around!

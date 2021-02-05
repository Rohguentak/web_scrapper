import requests
from bs4 import BeautifulSoup
from indeed import get_jobs as get_indeed_jobs
from stackoverflow import get_jobs as get_SO_jobs


indeed_jobs = get_indeed_jobs()
SO_jobs = get_SO_jobs()

jobs = indeed_jobs + SO_jobs

print(jobs)
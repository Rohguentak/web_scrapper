import requests
from bs4 import BeautifulSoup
from indeed import extract_indeed_pages,extract_indeed_jobs

last_indeed_pages=extract_indeed_pages()
print(last_indeed_pages)
#extract_indeed_jobs(last_indeed_pages)
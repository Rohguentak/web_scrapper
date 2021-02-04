import requests
from bs4 import BeautifulSoup

JOB_NUM_LIMIT = 50
INDEED_URL=f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={JOB_NUM_LIMIT}"

def extract_indeed_pages():
  result = requests.get(INDEED_URL)
  soup = BeautifulSoup(result.text, 'html.parser')

  pagination = soup.find("div", {"class":"pagination"})
  links = pagination.find_all('a')
  pages = []
  for link in links[0:-1]:
    pages.append(int(link.string))

  max_page = pages[-1]
  return max_page


def extract_indeed_jobs(last_page):
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{INDEED_URL}&start={page*JOB_NUM_LIMIT}")
    print(result.status_code)
  return jobs
    
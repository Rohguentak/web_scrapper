import requests
from bs4 import BeautifulSoup

JOB_NUM_LIMIT = 50
INDEED_URL=f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={JOB_NUM_LIMIT}"

def extract_indeed_pages():
  i = 1
  temp=0
  while(i == 1):
    result = requests.get(f"{INDEED_URL}&start={temp*JOB_NUM_LIMIT}")
    soup = BeautifulSoup(result.text, 'html.parser')

    pagination = soup.find("div", {"class":"pagination"})
    links = pagination.find_all('a')
    
    for l in links:
      if (l.get('aria-label') == '다음'):
        i = 1 
        print(i)
        print(l.get('aria-label'))
        print(temp)
      else :
        i = 0
    temp = temp + 1

  return temp + 1
  #pages = []
  #for link in links[0:-1]:
  #  pages.append(int(link.string))

  #max_page = pages[-1]
  #return max_page


def extract_indeed_jobs(last_page):
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{INDEED_URL}&start={page*JOB_NUM_LIMIT}")
    print(result.status_code)
  return jobs
    
import requests
from bs4 import BeautifulSoup

JOB_NUM_LIMIT = 50
INDEED_URL=f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={JOB_NUM_LIMIT}"

def extract_indeed_pages():
  i = 1
  temp=1
  while(i == 1):
    result = requests.get(f"{INDEED_URL}&start={temp*JOB_NUM_LIMIT}")
    soup = BeautifulSoup(result.text, 'html.parser')

    pagination = soup.find("div", {"class":"pagination"})
    links = pagination.find_all('a')
    
    for l in links:
      if (l.get('aria-label') == '다음'):
        i = 1 
      else :
        i = 0
    temp = temp + 1

  return temp
  #pages = []
  #for link in links[0:-1]:
  #  pages.append(int(link.string))

  #max_page = pages[-1]
  #return max_page


def extract_indeed_jobs(last_page):
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{INDEED_URL}&start={page*JOB_NUM_LIMIT}")
    soup = BeautifulSoup(result.text, 'html.parser')
    job_div = soup.find_all("div",{"class": "jobsearch-SerpJobCard"})
 
    for d in job_div:
      title = d.find("h2",{"class":"title"}).find("a")["title"]
      company = d.find("span",{"class":"company"})
      company_anchor = company.find("a")
      if company_anchor is not None:
        company = str(company_anchor.string) 
      else:
        company = str(company.string)
      company = company.strip()
      print("job title : " + title)
      print("company : " + company)
      print("===============================")
    print(result.status_code)
  return jobs
    
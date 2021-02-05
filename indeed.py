import requests
from bs4 import BeautifulSoup

JOB_NUM_LIMIT = 50
INDEED_URL=f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={JOB_NUM_LIMIT}"
INDEED_MAIN_URL = "https://kr.indeed.com"
def get_last_page_num():
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

def extract_job(html):
    job_title = html.find("h2",{"class":"title"})
    title = job_title.find("a")["title"]
    link = job_title.find("a")["href"]
    company = html.find("span",{"class":"company"})
    company_anchor = company.find("a")
    location = html.find("div",{"class":"recJobLoc"})["data-rc-loc"]
    if company_anchor is not None:
      company = str(company_anchor.string) 
    else:
      company = str(company.string)
    company = company.strip()
    return {'TITLE': title,'COMPANY': company,'LOCATION': location,'Link':f"{INDEED_MAIN_URL}{link}"}

def extract_jobs_from_html(last_page):
  jobs = []
  for page in range(last_page):
    print("==============================")
    print(f"Scrapping indeed {page} page ")
    result = requests.get(f"{INDEED_URL}&start={page*JOB_NUM_LIMIT}")
    soup = BeautifulSoup(result.text, 'html.parser')
    job_div = soup.find_all("div",{"class": "jobsearch-SerpJobCard"})
    for html in job_div:
      job_info = extract_job(html)
      jobs.append(job_info)
  return jobs
  

def get_jobs():
  last_pages=get_last_page_num()
  indeed_jobs = extract_jobs_from_html(last_pages)
  return indeed_jobs
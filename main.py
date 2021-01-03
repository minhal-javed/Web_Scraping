# importing the required moules
from bs4 import BeautifulSoup;
import requests;
import time

print('Put some skill that you dont know!')
unfam_skill=input('>')
print(f"Filtering out {unfam_skill}")

def find_jobs():
    # website
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
    soup=BeautifulSoup(html_text,'lxml')
    jobs=soup.find_all('li',class_="clearfix job-bx wht-shd-bx")
    for index,job in enumerate(jobs):
        date_pub=job.find('span',class_='sim-posted').span.text
        if 'few' in date_pub:
            company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            skills=job.find('span',class_='srp-skills').text.replace(' ','')
            more_info=job.header.h2.a['href']
            if unfam_skill not in skills:
                with open(f'posts/{index}.txt','w')as f:
                    f.write(f'Company Name: {company_name.strip()} \n')
                    f.write(f'Required Skills: {skills.strip()} \n')
                    f.write(f'More Info: {more_info.strip()} \n')
                print(f'File Saved {index}')

if __name__=='__main__':
    while True:
        find_jobs()
        # 5 minutes time break the rerun
        time_wait=5;
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait*60)

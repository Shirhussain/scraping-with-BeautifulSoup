from bs4 import BeautifulSoup 
import requests 
import time

print("Put some skill that you are not familiars with and don't wnat to show it here ")
unfamiliar_skills = input('> ')

def find_jobs():
    url = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
    soup = BeautifulSoup(url, 'lxml')
    # jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    # print(jobs)
    jobs = soup.find_all('li', class_ = "clearfix job-bx wht-shd-bx")
    # now if i wanna find some tags inside the <li> tags i don't need to find from all the website
    # just like soup.find i can implement for job.find
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_ = "sim-posted").span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_ = "joblist-comp-name").text.replace(' ', '')
            skills = job.find('span', class_ = "srp-skills").text.replace(' ', '')
            link = job.header.h2.a['href']
            if unfamiliar_skills not in skills:
                with open(f'posts/{index}.txt', 'w') as file: 
                    #if you have problem with spaces you need to use 'strip()'
                    file.write(f'Company name is 😍 : {company_name.strip()} \n') 
                    file.write(f'skills required are 👍 : {skills.strip()} \n')
                    file.write(f'More info: {link} \n')
                print(f"File saved: {index}")

if __name__=="__main__":
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting for {time_wait} minutes ....')
        time.sleep(30*time_wait)


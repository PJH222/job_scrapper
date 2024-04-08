from bs4 import BeautifulSoup
import requests
import re
import webbrowser

def extract_wwr2_jobs(keyword):
    url = f"https://remoteok.com/remote-{keyword}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    results = []
    
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        jobs = soup.find_all("tr", class_="job")        
        
        for job in jobs:
            company = job.find("h3", itemprop="name")
            position = job.find("h2", itemprop="title")
            location = job.find("div", class_="location")
            link = job.find("a", itemprop="url")
            
            if company:
                company = company.string.strip().replace(",", "")
            if position:
                position = position.string.strip().replace(",", "")
            if location:
                location = location.string.strip().replace(",", "") #for loc in location[:-2] if loc.string.strip() != "⏰ Contractor"]  # 마지막 2개 데이터는 제외하고 "⏰ Contractor" 데이터도 제외
                #location = ", ".join(location)  # 리스트를 문자열로 변환
            if link:
                href = link["href"]
                absolute_link = "https://remoteok.com" + href
                job_data = {'company': company, 'position': position, 'location': location, 'link': absolute_link}
                results.append(job_data)
    else:
        print("Can't get jobs.")
    
    return results

#keyword = input("May I help you?\n")
#print(extract_wwr_jobs(keyword))

from bs4 import BeautifulSoup
import requests
import re
import webbrowser

def extract_wwr_jobs(keyword):
    url = f"https://weworkremotely.com/remote-jobs/search?term={keyword}"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    results = []
    
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        jobs = soup.find_all("li", class_="feature")

        for job in jobs:
            company = job.find("span", class_="company")
            position = job.find("span", class_="title")
            location = job.find("span", class_="region")
            link = job.find("a", href=re.compile("/remote-jobs/"))
            
            if company:
                company = company.get_text(strip=True).replace(",", "")
            if position:
                position = position.get_text(strip=True).replace(",", "")
            if location:
                location = location.get_text(strip=True).replace(",", "")

            if link:
                href = link["href"]
                absolute_link = "https://weworkremotely.com" + href
                job_data = {'company': company, 'position': position, 'location': location, 'link': absolute_link}
                results.append(job_data)
    else:
        print("Can't get jobs.")
    
    return results

#keyword = input("Can I help you?\n")
#print(extract_wwr_jobs(keyword))

import requests
from bs4 import BeautifulSoup

data=requests.get("https://www.timesjobs.com/jobskill/python-jobs").text

p_data=BeautifulSoup(data,"html.parser")
p1=p_data.find('section',class_="lhs")
cp_data=p_data.find_all('li',class_="clearfix joblistli")
for c_data in cp_data:
    comp_data=c_data.find('h3',class_="joblist-comp-name").text.replace('(More Jobs)','')
    skills=c_data.find('ul',class_="job-dtl clearfix")
    skills_=skills.find('span',class_="srp-skills").text

    with open("big.txt",'a') as file:
        file.write(comp_data.strip())
        file.write(skills_.strip())
        file.write("\n")
        file.write("\n")
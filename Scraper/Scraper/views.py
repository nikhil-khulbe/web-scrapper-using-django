from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def scrape_view(request):
  if request.method == 'POST':
    url = request.POST.get('url')
    scraped_data = scrape_data(url)
    
    
    return render(request,'results.html',{'combined_data':scraped_data,})
  return render(request,'index.html')




def scrape_data(url):
  response = requests.get(url)
  if response.status_code == 200:
    soup = BeautifulSoup(response.content,'html.parser')
    title = soup.find('title').text
    headings = soup.find_all(['h1','h2','h3','h4','h5','h6'])
    combined_data=[]
    for heading in headings:
            next_sibling = heading.find_next('p')
            if next_sibling:
                combined_data.append((heading.text, next_sibling.text))

    return combined_data
    # paragraphs = [paragraph.text for paragraph in soup.find_all('p')]
    
  return 'NO DATA'
#pjdj100001_APIWebScrapingTop5ITStockMarket Scope of Django project Get from from web page investing five stock values, and publish it into a table. 

#Architecture 
Operating system: Windows 10 Pro
Virtual environments: venv module python version = 3.8.1
Packages: Django, requests, BeautifulSoup, pandas, matplotlib

#Technical function:
1. Connect to investing web page (requests.get)
2. Get all DOM span elements and find stock name and value (BeautifulSoup)
3. Build a dataframe with all values scraping (pd.DataFrame)
4. And display them into a matplotlib bar (plt.Figure())
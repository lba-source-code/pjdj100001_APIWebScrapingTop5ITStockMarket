#Presentation
Thanks to be here, I would like to share a hands-on experience about a Django application. I am using some steps of DevOps methodology, like control version with git, share development in remote repository like github, and doing integrations more than one by day.

#pjdj100001_APIWebScrapingTop5ITStockMarket 
The scope of this Django project is Get from web page investing, five stock values, and publish them into a dataframe table on html template. 

#Architecture 
Operating system: Windows 10 Pro
Virtual environments: venv module with runtime python version = 3.8.1
Packages: Django, requests, BeautifulSoup, pandas, matplotlib

#The control flow coding into application is:
1. Connect to investing web page (requests.get)
2. Get all DOM <span> elements and find stock name and value (BeautifulSoup)
3. Build a dataframe with all values scraping (pd.DataFrame)
4. And display them into a matplotlib bar in a html template (plt.Figure())

Additional support

Tag
#freelancercolaboration #remotework

I am always open to join or colaborate in development web app, mobile app and api. 

Thanks for your time
Luis :)
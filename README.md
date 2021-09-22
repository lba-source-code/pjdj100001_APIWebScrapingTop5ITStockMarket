# Presentation
Thanks to be here, I would like to share a hands-on experience about a process automation with Django application. I am using some steps of DevOps methodology, like control version with git, share development in remote repository like github, and doing integrations more than one by day.

# Scope
The scope of this project of process automation is to get from web page investing, five stock values, and publish them into a dataframe table on html template. 

# Architecture 
Operating system: Windows 10 Pro
Virtual environments: venv module with runtime python version = 3.8.1
Packages: Django, requests, BeautifulSoup, pandas, matplotlib

# Unit test
Into the project I have included some examples of unit test. 
1. test_check_request_status_ok
2. test_check_request_status_ko
3. test_check_content_have_stockname
4. test_check_content_have_stockvalue

# The control flow structure of application is:
1. Connect to investing web page (requests.get)
2. Get all DOM <span> elements and find stock name and value (BeautifulSoup)
3. Build a dataframe with all values scraping (pd.DataFrame)
4. And display them into a matplotlib bar in a html template (plt.Figure())

## Additional support

1. Requests is a simple, yet elegant, HTTP library <https://pypi.org/project/requests/>.
2. Beautiful Soup is a library that makes it easy to scrape information from web pages. It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree <https://pypi.org/project/beautifulsoup4/>
3. Pandas is a Python package that provides fast, flexible, and expressive data structures designed to make working with "relational" or "labeled" data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, real world data analysis in Python. Additionally, it has the broader goal of becoming the most powerful and flexible open source data analysis / manipulation tool available in any language. It is already well on its way towards this goal <https://pypi.org/project/pandas/>.
4. Matplotlib produces publication-quality figures in a variety of hardcopy formats and interactive environments across platforms. Matplotlib can be used in Python scripts, the Python and IPython shell, web application servers, and various graphical user interface toolkits <https://pypi.org/project/matplotlib/>. 


## Tag
#djangodeveloper #pythondeveloper #freelancercolaboration #remotework

## Open to colaborate

I am always open to join or colaborate in development web app, mobile app, api and rpa services. 

**Thanks for your time**
**Luis** :smiley:
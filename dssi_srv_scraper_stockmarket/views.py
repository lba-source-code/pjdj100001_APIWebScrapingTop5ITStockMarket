"""DSSi comment: standar package """
from django.shortcuts import render
from django.http import HttpResponse
from matplotlib.figure import Figure
import requests #https://pypi.org/project/requests/
from bs4 import BeautifulSoup #https://pypi.org/project/beautifulsoup4/
import numpy as np
import pandas as pd #https://pypi.org/project/pandas/
import matplotlib.pyplot as plt #https://pypi.org/project/matplotlib/
import base64
from io import BytesIO

"""DSSi comment: class message log"""
class Cl_message:
    def mt_message_log(self,message='message',description='initialization'):
        print(f'\nDSSi log {message}: {description}\n')
    def mt_message_log_error(self,message='message',description='initialization\n'):
        print(f'\nDSSi log ERROR {message}: {description}')
    def mt_message_out(self,message='message',description='initialization'):
        vr_msgout = f'<div class="my-3">DSSi msg OUT {message}: {description}</div>'
        return vr_msgout
    def mt_message_out_error(self,message='message',description='initialization'):
        vr_msgout = f'<div class="my-3">DSSi msg OUT ERROR {message}: {description} </div>'
        return vr_msgout

"""DSSi define views """

def srv_scraper_stockmarket(request):
    vr_message = Cl_message()
    vr_message.mt_message_log('srv_scraper_stockmarket','initialization')
    vr_message_out = 'No message :)'

    try:
  
        vr_web_urls_source = ['https://www.investing.com/equities/microsoft-corp',
                              'https://www.investing.com/equities/google-inc',
                              'https://www.investing.com/equities/sap-ag',
                              'https://www.investing.com/equities/apple-computer-inc',
                              'https://www.investing.com/equities/uipath']
        vr_soupb = []
        vr_stockvaluelist   = []
        vr_stocknamelist    = []
        df_stockmarkettop5  = pd.DataFrame()
        df_stockmarkettop5_ind_html  = pd.DataFrame()

        for vr_web_url in vr_web_urls_source:

            #requests get content
            vr_requests = requests.get(vr_web_url)
            
            if vr_requests.status_code == 200:

                #extract data
                vr_soupb = BeautifulSoup(vr_requests.text, 'html.parser')
                vr_listoftargetvalues = f'{vr_soupb.find_all("span")}'
            
                for span_tag_attr in vr_soupb.find_all("h1"):
                    if 'instrument-header_title__GTWDv' in str(span_tag_attr.get("class")):
                        vr_message.mt_message_log('span_tag_attr type',f'{type(span_tag_attr)}')
                        vr_message.mt_message_log('span_tag_attr get("class"',f'{span_tag_attr.get("class")}')
                        vr_message.mt_message_log('span_tag_attr string',f'{span_tag_attr.string}')
                        vr_stocknamelist.append(f'{span_tag_attr.string}')
                        break
                for span_tag_attr in vr_soupb.find_all("span"):
                    if 'instrument-price_last__KQzyA' in str(span_tag_attr.get("class")):
                        vr_message.mt_message_log('span_tag_attr type',f'{type(span_tag_attr)}')
                        vr_message.mt_message_log('span_tag_attr get("class"',f'{span_tag_attr.get("class")}')
                        vr_message.mt_message_log('span_tag_attr string',f'{span_tag_attr.string}')
                        vr_stockvaluelist.append(f'{span_tag_attr.string}')
                        break
            else:
                vr_message_out = vr_message.mt_message_out_error('srv_scraper_stockmarket <strong>requests.get</strong> url source', f'{vr_web_url}')
                vr_message_out += vr_message.mt_message_out_error('srv_scraper_stockmarket <strong>requests.get</strong> status_code', f'{vr_requests.status_code}')

        #build a dataframe with the name and value of the stock
        vr_stockvaluelist = list(map(lambda elem: elem.replace(',', ''), vr_stockvaluelist))
        vr_stockvaluelist = list(map(float, vr_stockvaluelist))
        vr_message.mt_message_log('srv_scraper_stockmarket vr_stockvaluelist',vr_stockvaluelist)
        vr_dict_of_lists = {'Stock':vr_stocknamelist, 'Value':vr_stockvaluelist}
        df_stockmarkettop5 = pd.DataFrame(vr_dict_of_lists)
        df_stockmarkettop5_ind = df_stockmarkettop5.set_index("Stock")
        vr_message.mt_message_log('srv_scraper_stockmarket df_stockmarkettop5_ind',df_stockmarkettop5_ind)
        df_stockmarkettop5_ind_html = df_stockmarkettop5_ind.to_html()

        #build a plt bar to corparer of each other
        fig = plt.Figure()    
        ax = fig.subplots()
        ax.bar(df_stockmarkettop5_ind.index, df_stockmarkettop5_ind["Value"])
        ax.set_xticklabels(df_stockmarkettop5_ind.index, rotation=45)
        buf = BytesIO()
        fig.set_size_inches(8, 4)
        fig.savefig(buf, format="png")
        vr_stockmarket_graph = base64.b64encode(buf.getbuffer()).decode("ascii")

    except Exception as msg_error:
        vr_message.mt_message_log_error('srv_scraper_stockmarket',f'{msg_error}')
        vr_message_out = vr_message.mt_message_out_error('srv_scraper_stockmarket',f'{msg_error}...')

    context = {
        'title':'<span class="btn dssi-style">DSSi App</span> - Stock Market Top 5 Scraper',
        'vr_message_out':vr_message_out,
        'vr_web_urls_source':vr_web_urls_source,
        'vr_soupb':f'DSSi msg vr_soupb span_tag_attr string {vr_listoftargetvalues[:450]}...',
        'vr_stocknamelist':vr_stocknamelist,
        'vr_stockvaluelist':vr_stockvaluelist,
        'df_stockmarkettop5':df_stockmarkettop5_ind_html,    
        'vr_stockmarket_graph':vr_stockmarket_graph
    }

    return render(request,'srv_scraper_stockmarket/srv_scraper_stockmarket.html', context)



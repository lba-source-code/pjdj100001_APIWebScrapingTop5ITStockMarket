"""DSSi comment: standar package """
from django.shortcuts import render
import requests #https://pypi.org/project/requests/
from bs4 import BeautifulSoup #https://pypi.org/project/beautifulsoup4/
import numpy as np
import pandas as pd

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
    vr_message_out = vr_message.mt_message_out('srv_scraper_stockmarket','initialization')

    try:
  
        vr_web_urls_source = ['https://www.investing.com/equities/microsoft-corp','https://www.investing.com/equities/google-inc','https://www.investing.com/equities/sap-ag']
        vr_stockvaluelist = []
        vr_stocknamelist = []

        for vr_web_url in vr_web_urls_source:

            vr_requests = requests.get(vr_web_url)
            vr_message_out += vr_message.mt_message_out('srv_scraper_stockmarket <strong>requests.get</strong> url source', f'<a href="{vr_web_url}" target="_blank">{vr_web_url}</a>')
            vr_message_out += vr_message.mt_message_out('srv_scraper_stockmarket <strong>requests.get</strong> status_code', f'{vr_requests.status_code}')
            vr_message_out += vr_message.mt_message_out('srv_scraper_stockmarket <strong>requests.get</strong> headers', f'{vr_requests.headers}')
            vr_soupb = BeautifulSoup(vr_requests.text, 'html.parser')
            vr_listoftargetvalues = f'{vr_soupb.find_all("span")}'
            
            for span_tag_attr in vr_soupb.find_all("h1"):
                if 'instrument-header_title__GTWDv' in str(span_tag_attr.get("class")):
                    vr_message.mt_message_log('span_tag_attr type',f'{type(span_tag_attr)}')
                    vr_message.mt_message_log('span_tag_attr get("class"',f'{span_tag_attr.get("class")}')
                    vr_message.mt_message_log('span_tag_attr string',f'{span_tag_attr.string}')
                    vr_stocknamelist.append(f'{span_tag_attr.string}')
            for span_tag_attr in vr_soupb.find_all("span"):
                if 'instrument-price_last__KQzyA' in str(span_tag_attr.get("class")):
                    vr_message.mt_message_log('span_tag_attr type',f'{type(span_tag_attr)}')
                    vr_message.mt_message_log('span_tag_attr get("class"',f'{span_tag_attr.get("class")}')
                    vr_message.mt_message_log('span_tag_attr string',f'{span_tag_attr.string}')
                    vr_stockvaluelist.append(f'{span_tag_attr.string}')

        df_stockmarkettop5 = pd.DataFrame(list(zip(vr_stocknamelist,vr_stockvaluelist)),columns =['Name', 'val'])
        vr_message.mt_message_log('srv_scraper_stockmarket df_stockmarkettop5',df_stockmarkettop5)

    except Exception as msg_error:
        vr_listoftargetvalues = None
        vr_message.mt_message_log_error('srv_scraper_stockmarket',f'{msg_error}')
        vr_message_out += vr_message.mt_message_out_error('srv_scraper_stockmarket',f'{msg_error}...')

    context = {
        'title':'Stock Market Top 5 Scraper',
        'vr_message_out':vr_message_out,
        'vr_soupb':f'DSSi msg vr_soupb span_tag_attr string {vr_listoftargetvalues[:450]}...',
        'vr_stocknamelist':vr_stocknamelist,
        'vr_stockvaluelist':vr_stockvaluelist,
    }

    return render(request,'srv_scraper_stockmarket/srv_scraper_stockmarket.html', context)



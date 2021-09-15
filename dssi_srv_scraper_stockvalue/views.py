"""DSSi comment: standar package """
from django.shortcuts import render
import requests #https://pypi.org/project/requests/

"""DSSi comment: class message log"""
class Cl_message:
    def mt_message_log(self,message='message',description='initialization'):
        print(f'\nDSSi log {message}: {description}\n')
    def mt_message_log_error(self,message='message',description='initialization\n'):
        print(f'\nDSSi log ERROR {message}: {description}')
    def mt_message_out(self,message='message',description='initialization'):
        vr_msgout = f'DSSi OUT {message}: {description}<br><br>'
        return vr_msgout
    def mt_message_out_error(self,message='message',description='initialization<br><br>'):
        vr_msgout = f'DSSi OUT ERROR {message}: {description}'
        return vr_msgout

"""DSSi define views """

def srv_scraper_stockvalue(request):
    vr_message = Cl_message()
    vr_message.mt_message_log('srv_scraper_stockvalue','initialization')
    vr_message_out = vr_message.mt_message_out('srv_scraper_stockvalue','initialization')

    try:
        vr_message.mt_message_log('srv_scraper_stockvalue','try')
        vr_message_out += vr_message.mt_message_out('srv_scraper_stockvalue','try')

        vr_requests = requests.get('https://www.investing.com/equities/google-inc')

        vr_message_out += vr_message.mt_message_out('srv_scraper_stockvalue status_code', f'{vr_requests.status_code}')

        vr_message_out += vr_message.mt_message_out('srv_scraper_stockvalue headers', f'{vr_requests.headers}')

        #vr_message_out += vr_message.mt_message_out('srv_scraper_stockvalue text', f'{vr_requests.text}')

    except Exception as msg_error:
        vr_message.mt_message_log('srv_scraper_stockvalue',f'{msg_error}')
        vr_message_out += vr_message.mt_message_out('srv_scraper_stockvalue',f'{msg_error}')

    context = {
        'title':'Stock Market Top 5 Scraper',
        'vr_message_out':vr_message_out,
        'vr_requests_content':vr_requests.text,
    }

    return render(request,'srv_scraper_stockvalue/srv_scraper_stockvalue.html', context)



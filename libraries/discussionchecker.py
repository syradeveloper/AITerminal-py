import requests
from bs4 import BeautifulSoup

class DiscussionChecker:
    def get_info(id, amountposts):
        data = requests.get(f'https://forum.wayzer.ru/api/discussions/{id}').json()
        title = data['data']['attributes']['title']
        link = f"https://forum.wayzer.ru/d/{data['data']['attributes']['slug']}"
        if amountposts == 9999: 
            amountposts = data['data']['attributes']['commentCount']
        formated_text = ""
        for i in range(amountposts):
            posts = data['included'][i]
            userid = posts['relationships']['user']['data']['id']
            user = requests.get(f'https://forum.wayzer.ru/api/users/{userid}').json()['data']['attributes']['displayName']
            if posts['attributes']['contentHtml']:
                html_content = posts['attributes']['contentHtml']
                soup = BeautifulSoup(html_content, 'html.parser')
                text = soup.get_text()
                formated_text += f"\n>  post from {user}:\n{text}\n"

        return f"""
    Title :: {title}
    Link :: {link}
    Amount of posts :: {amountposts}
{formated_text}
"""
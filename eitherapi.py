import requests
from bs4 import BeautifulSoup

class Eitherio:

  def __init__(self):
    res = requests.get('https://either.io').content.decode()
    html = BeautifulSoup(res, 'html.parser')
    self.title = html.find('h2', {'id':'question-title'}).getText()
    self.author = html.find('span', {'id':'question-author'}).getText()[9:]
    self.link = html.find('input', {'type':'hidden'})['value']
    self.tags = [tag.getText().replace('\n','') for tag in html.find_all('ul', {'class':'tags'})]
    self.comments = int(html.find('span', {'class':'comment-number'}).getText().replace(',',''))
    self.choices = html.find_all('span', {'class':'option-text'})
    self.percentages = html.find_all('div', {'class':'percentage'})
    self.votes = html.find_all('span', {'class':'count'})

  def get_question(self):
    '''
    Fetch various data for a random question, returns dict.
    '''
    return {
      'title': self.title,
      'author': self.author,
      'link': self.link,
      'tags': self.tags,
      'comments': self.comments,
      'choice_1': {
        'text': self.choices[0].getText(),
        'percentage': self.percentages[0].getText(),
        'votes': int(self.votes[0].getText().replace(',',''))
      },
      'choice_2': {
        'text': self.choices[1].getText(),
        'percentage': self.percentages[1].getText(),
        'votes': int(self.votes[1].getText().replace(',',''))
      }
    }

import requests
from bs4 import BeautifulSoup

class eitherio:

  def __init__(self):
    res = requests.get('https://either.io').content.decode()
    self.html = BeautifulSoup(res, 'html.parser')

  def get_question(self):
    '''
    Fetch various data for a random question, returns dict.
    '''
    title = self.html.find('h2', {'id':'question-title'}).getText()
    author = self.html.find('span', {'id':'question-author'}).getText()[9:]
    link = self.html.find('input', {'type':'hidden'})['value']
    tags = [tag.getText().replace('\n','') for tag in self.html.find_all('ul', {'class':'tags'})]
    comments = int(self.html.find('span', {'class':'comment-number'}).getText().replace(',',''))
    choices = self.html.find_all('span', {'class':'option-text'})
    percentages = self.html.find_all('div', {'class':'percentage'})
    votes = self.html.find_all('span', {'class':'count'})
    return {
      'title': title,
      'author': author,
      'link': link,
      'tags': tags,
      'comments': comments,
      'choice_1': {
        'text': choices[0].getText(),
        'percentage': percentages[0].getText(),
        'votes': int(votes[0].getText().replace(',',''))
      },
      'choice_2': {
        'text': choices[1].getText(),
        'percentage': percentages[1].getText(),
        'votes': int(votes[1].getText().replace(',',''))
      }
    }
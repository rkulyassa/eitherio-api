# eitherio-api
Simple python module and web api for https://either.io

## Installation
Clone this repository into your current working directory, run `pip install -r requirements.txt` to install all deps then import wherever you want.

## Module
### Usage
```py
from eitherapi import Eitherio

q = Eitherio().get_question()
print(q)
```
#### Sample output:
```py
{
    'title': 'Exotic Homes',
    'author': 'Zach Dunn',
    'link': 'http://either.io/101/exotic-homes',
    'tags': ['Life'],
    'comments': 811,
    'choice_1': {
        'text': 'Live in a treehouse',
        'percentage': '59%',
        'votes': 966920
    },
    'choice_2': {
        'text': 'Live in a floating boathouse',
        'percentage': '41%',
        'votes': 685263
    }
}
```

## api

### Usage
install all deps: `pip install -r requirements.txt`

start the server: `python3 api.py`

send GET requests to `/api/question`

#### Sample output:

```sh
❯ curl http://127.0.0.1:5000/api/question
{
  "author": "Zach Dunn",
  "choice_1": {
    "percentage": "29%",
    "text": "Only listen to bagpipe music",
    "votes": 443785
  },
  "choice_2": {
    "percentage": "71%",
    "text": "Only listen to banjo music",
    "votes": 1112244
  },
  "comments": 654,
  "link": "http://either.io/228/country-bagpipes",
  "tags": [
    "Life"
  ],
  "title": "Country Bagpipes"
}
``` 

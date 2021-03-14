# eitherio-api
Simple python web api for https://either.io

## Installation
Clone `eitherapi.py` into cwd, then import wherever you want.

## Usage
```py
from eitherapi import eitherio

q = eitherio().get_question()
print(q)
```
### Sample output:
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

import json
import openai
import logging
import configparser
import os

config = configparser.ConfigParser()
config.read(f'{os.getcwd()}/conf.ini')

openai.api_key= config['SERVER']['open-api-key']

logger=logging.getLogger(__name__)
MODEL = 'gpt-3.5-turbo'
place = 'Ann Arbor'
num_birds = 5
season = 'fall'


def chatgpt_query(place: str = place, num_birds: int = num_birds, season: str = season):
    logging.debug('IN @ chatgptquery')
    try:
        reponse = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "user",
                 "content": f"give me {num_birds} birds with scientific name that I can photograph \
                              in {place} during {season} in JSON array. Just provide the JSON"}
            ],
            temperature=0,)
        data = reponse['choices'][0]['message']['content']
        logging.debug(data)
        return json.loads(data)
    except Exception as e:
        logging.error(f'ERR @ chatgptquery: {e}')
        return None

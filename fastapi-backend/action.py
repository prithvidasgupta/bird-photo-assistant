import json
import openai
import logging
import configparser
import os

# read config
config = configparser.ConfigParser()
config.read(f'{os.getcwd()}/conf.ini')

# openai library set with api key 
openai.api_key= config['SERVER']['open-api-key']

# setting module level variables
logger=logging.getLogger(__name__)
MODEL = 'gpt-3.5-turbo'
place = 'Ann Arbor'
num_birds = 5
season = 'fall'

# @app.get_bird_names("/place/{place}/season/{season}/birds/{num_birds}")
def chatgpt_query(place: str = place, num_birds: int = num_birds, season: str = season):
    '''
    This function is the function responsible for creating and fetching the respone of the ChatGPT
    API. There is no input sanitization needed for this function as the expectation is that ChatGPT is
    'clever' enough to handle bad input

    Parameters:
        place: str -> Requested place of interest
        season: str -> Relevant season. Can only have Fall,Winter, Spring and Summer values
        num_birds: int -> Requested number of birds
    Returns:
        dict -> A dict with all the birding data returned by the ChatGPT API
        or
        None -> An error will trigger a None return
    '''
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

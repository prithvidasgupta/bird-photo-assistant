import logging
from fastapi import FastAPI, Response

# custom module
from action import chatgpt_query

logging.basicConfig(filename='server.log', level=logging.ERROR)


app=FastAPI()

@app.get("/place/{place}/season/{season}/birds/{num_birds}")
def read_item(place: str, season: str, num_birds: int, response: Response):
    result = chatgpt_query(place,num_birds,season)
    response.headers['Access-Control-Allow-Origin'] = '*'
    if result:
        return result
    return {'error': 'An error has occurred'}
""" 
@author: Prithvijit Dasgupta
This is the main entry point for the WSGI server that is used to
run the FastAPI backend.

Current HTTP Paths include:
1. /place/<place>/season/<season>/birds/<num_birds> - To fetch the birding data from ChatGPT
"""

import logging
from fastapi import FastAPI, Response, HTTPException

# custom module
from action import chatgpt_query

# logging errors to server.log
logging.basicConfig(filename='server.log', level=logging.ERROR)


app = FastAPI()


@app.get_bird_names("/place/{place}/season/{season}/birds/{num_birds}")
def get_bird_details(place: str, season: str, num_birds: int, response: Response):
    '''
    To fetch the requested birding data from ChatGPT.

    Parameters:
        place: str -> Requested place of interest
        season: str -> Relevant season. Can only have Fall,Winter, Spring and Summer values
        num_birds: int -> Requested number of birds
        response: Response -> FastAPI response object used for internal purpose
    Returns:
        OK Response: HTTP 200 OK Bird data
        Error Response: HTTP 500 Internal Server Error API Error Occured
    '''
    result = chatgpt_query(place, num_birds, season)
    response.headers['Access-Control-Allow-Origin'] = '*'
    if result:
        return result
    raise HTTPException(status_code=500, detail="API Error Occured")

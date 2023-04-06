# Bird Photo Assistant

Birding a very exciting hobby for millions around the globe. People spend a lot of effort, time and patience in order to get a sight of unique birds around them. For the most part, birding is an inexpensive hobby that?s easy to pick up and encourages getting outside and decreasing screen time. However, for bird photographers like myself, it becomes almost an obsession on how to get the most crisp and clear shots of birds. It usually involves a lot of sunk monetary cost (getting equipment, cameras and lenses) and a lot of patience (birds are fickle creatures) to even get a good (or okayish) shots. For this niche hobby, one would say you have to be lucky to be the best photographer.

This tool is a project (with assistance from OpenAI) that would enable bird photographers to estimate what birds might be available around a location given a place and date. This would bring value to birders understanding what they might be able to photograph on that
specific date.

This project has only been tested locally and is prone to bugs. It is not meant for production use and is only for demonstration purpose.

#### YouTube Video 

[![Bird Photo Assistant](https://img.youtube.com/vi/j11LiaW59Nc/0.jpg)](https://youtu.be/j11LiaW59Nc)

## The Backend

Requirements: **Python 3.11** (and free TCP port 8000)

### How to run the backend?

1. Navigate to `fastapi-backend`
2. Run `pip install -r requirements.txt`
3. Change the OpenAI API Key in `conf.ini` to your own API Key
4. Run `uvicorn main:app`

## The Frontend

Requirements: **NodeJS 16** (and free TCP port 5173)

### How to run the frontend?

1. Navigate to `svelte-frontend`
2. Run `npm install`
3. Run `npm run dev --open`
4. A browser window should open up

## How does the project leverage ChatGPT (GPT3.5)?

This project utilizes the innovative ChatGPT model to create the required data to show on the webpage. While this data can be obtained from structured databases, their APIs are not trivial and to get generic seasonal information would require a lot of filtering. ChatGPT allows an easy solution where it can (or atleast attempt to) provide a structured response to a semi-structured query about birds and seasons (and the relevant number of birds).

Example ChatGPT Query:

```
give me 2 birds with scientific name that I can photograph in Delhi during summer in JSON array. Just provide the JSON.
```
will generate a JSON response (in most cases)

```
{
  "birds": [
    {
      "common_name": "House Sparrow",
      "scientific_name": "Passer domesticus"
    },
    {
      "common_name": "House Sparrow",
      "scientific_name": "Passer domesticus"
    }
  ]
}

```

### Hallunication Issues

ChatGPT is known to 'hallucinate' fake information especially when it cannot find any data. In my observations, it has been known to hallucinate the structure of the response. The response structure is not set in stone and ChatGPT could send back a response which this project is incapable of handling. It is a major bug in this project which i was not able to address due to time constraints.

# Acknowledgements

I would like the thank the instruction team of SI 568 (Neha Bhomia, Michael Hess, Naren Doraiswamy and Ishank Juneja) for their support all through Winter 2023 @ University of Michigan, Ann Arbor.
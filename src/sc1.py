""" Get the Jobs from Reed using the Reed API """
import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

base_url = "https://www.reed.co.uk/api/1.0/search"
api_key = os.getenv("API_KEY")
auth = (api_key, "")
params = {"keywords": "Rust", "resultsToTake": 2, "resultsToSkip": 10}


def get_jobs(base_url: str, auth: tuple, params: dict) -> str:
    """
    :param base_url: this is the REED API url
    :param auth: this is a tuple with the API KEY
    :returns: The Dictionary of the result
    """
    resp = requests.get(url=base_url, auth=auth, params=params)
    result = json.loads(resp.content)
    return result["results"]


def generator_jobs():
    """
    Returns a generator of jobs ready to print
    """
    res = get_jobs(base_url, auth, params)
    for i in res:
        yield (i["jobTitle"])


print(*generator_jobs(), sep="\n")

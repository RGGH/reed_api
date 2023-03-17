import os

from dotenv import load_dotenv
from src.sc1 import generator_jobs

load_dotenv()

base_url = "https://www.reed.co.uk/api/1.0/search"
api_key = os.getenv("API_KEY")
auth = (api_key, "")

def test_generator_jobs():
    """
    Test the print from generator comprehension
    """
    assert generator_jobs() !=0

    

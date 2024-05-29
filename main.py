from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")

app = FastAPI()


@app.get("/")
def read_root():
    return {"LANGCHAIN_API_KEY": LANGCHAIN_API_KEY, "asda": LANGCHAIN_TRACING_V2}


# make a dummy post request to the server
@app.get("/dummy")
def dummy_post():
    return {"message": "dummy post request"}

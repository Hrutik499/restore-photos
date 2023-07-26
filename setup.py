import os
import streamlit as st
import pandas as pd
import openai
from pandasai import PandasAI
import json
import seaborn as sns
import matplotlib.pyplot as plt
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
openai.api_key = os.getenv("OPENAI_API_KEY")
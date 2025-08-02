#!D:\Documents\Python\NII_PROJECT\bankstress\Scripts\python.exe

from datetime import datetime, timedelta
from pathlib import Path
import os
import sys

import pandas as pd
import requests
from fredapi import Fred
from dotenv import load_dotenv
from cachetools import TTLCache
print(os.getcwd())
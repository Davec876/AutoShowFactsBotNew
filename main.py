import gspread
from twitter import *
# from dotenv import load_dotenv
# load_dotenv()
import os
import json
import qrng
import threading

# def get_keys(path):
#     with open(path) as f:
#         return json.load(f)
#
# keys = get_keys(".secret/package.json")

gc = gspread.service_account("credentials.json")

# ALTERNATE METHOD TO GET API ACCESS FOR TWITTER
token = os.environ.get('TOKEN')
token_secret = os.environ.get('TOKEN_SECRET')
consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')

# opening the spreadsheet
sheet = gc.open_by_key('1p04UtmPblK9JsXSWAbTwhr7ukMw1i8BA3NyAtRKEGc4')
worksheet = sheet.sheet1

# token = keys['TOKEN']
# token_secret = keys['TOKEN_SECRET']
# consumer_key = keys['CONSUMER_KEY']
# consumer_secret = keys['CONSUMER_SECRET']

t = Twitter(
    auth=OAuth(token, token_secret, consumer_key, consumer_secret))

qrng.set_provider_as_IBMQ('') # empty string denotes local backend which can only use 'qasm_simulator'
qrng.set_backend() # no args defaults to `qasm_simulator`

# random cell position
factRef = int(qrng.get_random_double(2, len(worksheet.col_values(1))))

beginning = "Did you know? "
tweet = worksheet.cell(factRef, 1).value
show = worksheet.cell(factRef, 2).value
hashtag = " #"

# TIMED TWEET
threading.Timer(28800.0, t.statuses.update(
    status=beginning+tweet+hashtag+show))

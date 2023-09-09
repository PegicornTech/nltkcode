#!/usr/bin/python
import os
import openai
import argparse

argParser = argparse.ArgumentParser()
argParser.add_argument("-s", "--string", help="Hash you are trying to identify")

args = argParser.parse_args()
thehash = args.string

apikey = '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'

openai.api_key = os.getenv(apikey)

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=thehash,
  temperature=0,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0.2,
  presence_penalty=0
)

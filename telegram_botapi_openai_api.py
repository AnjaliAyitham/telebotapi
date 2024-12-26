# -*- coding: utf-8 -*-
"""Telegram - BOTAPI OPENAI API.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/199DQUNFRSFR_vh7w3eDeUQkfI18Emed5
"""

#AIMER Society - Indian Servers
!pip install pyTelegramBotAPI
!pip install openai
!pip install google-generativeai #For Google Gemini #AIMERS
!pip install anthropic
TelegramBOT_TOKEN = '7096176919:AAHRThrKHqMo3wW1xJBayQlsGLNg0pu9nFk'

#general

#Latest version #Gemini API #AIMER Society #IndianServers
import telebot
import os


"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os

import google.generativeai as genai

genai.configure(api_key="AIzaSyB56p_5paUJyFyPvHdwXTlqFEEcoJpg0oA")

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)


bot = telebot.TeleBot(TelegramBOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Indian Servers AI Powerful BOT, Ask your questions related to UPSC.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
 try :
  print(message)
  response=chat_session.send_message(message.text)
  bot.reply_to(message, response.text)

 except Exception as e:
        print(f"An error occurred: {e}")
        bot.reply_to(message, "Sorry, I couldn't process your request.")

bot.polling()

#Latest version
import telebot
import os
import openai
from openai import OpenAI


OPENAI_API_KEY = "sk-proj-bKcwWzKAPvMr8fnkj90tT3BlbkFJaViNbMV9mKNhG8pWUIYF"
client = OpenAI(api_key=OPENAI_API_KEY)


bot = telebot.TeleBot(TelegramBOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! The MOST POWERFUL AI BOT from IndianServers")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
 try :
  print(message)
  completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": message.text},
  ]
    )
  bot.reply_to(message, completion.choices[0].message.content)
 except Exception as e:
        print(f"An error occurred: {e}")
        bot.reply_to(message, "Sorry, I couldn't process your request.")

bot.polling()

import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="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",
)

bot = telebot.TeleBot(TelegramBOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! The MOST POWERFUL AI BOT from IndianServers")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try :
        print(message)
        message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        temperature=0,
        messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": message.text
                }
            ]
        }
        ]
        )
        bot.reply_to(message, message.content)
    except Exception as e:
        print(f"An error occurred: {e}")
        bot.reply_to(message, "Sorry, I couldn't process your request.")

bot.polling()
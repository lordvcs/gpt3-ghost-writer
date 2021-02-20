# GPT3 spooky story writer

A python flask app that generates a spooky story using openai's gpt-3

## Setup

1. Rename `.env.example` to `.env` and set `OPENAI_KEY` to your openapi api key.
2. Run the command `poetry install` to install the dependecies.
3. Run the flask app
4. POST: `http://127.0.0.1:5000/bot` to get the next part of the spooky story as response
5. POST: `http://127.0.0.1:5000/bot?Body=the end` to end the story.

The story is written based on the initial `session_prompt` text in `story.py` file. If you need a new starting story text, use a different text there.

## Credits

Based on this article: [Twilio article](https://www.twilio.com/blog/ghost-writer-spooky-openai-gpt3-python-whatsapp)

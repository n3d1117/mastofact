import os
import time

from mastodon import Mastodon
import openai
import logging
from dotenv import load_dotenv


def main():
    # Read .env file
    load_dotenv()

    # Setup logging
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    # Check if the required environment variables are set
    required_values = ['MASTODON_INSTANCE', 'MASTODON_BOT_TOKEN', 'OPENAI_API_KEY']
    missing_values = [value for value in required_values if os.environ.get(value) is None]
    if len(missing_values) > 0:
        logging.error(f'The following environment values are missing in your .env: {", ".join(missing_values)}')
        exit(1)

    # Setup Mastodon
    mastodon = Mastodon(
        access_token=os.environ['MASTODON_BOT_TOKEN'],
        api_base_url=os.environ['MASTODON_INSTANCE']
    )

    # Setup OpenAI
    openai.api_key = os.environ['OPENAI_API_KEY']
    prompt = "Tell me a random fact, be it fun, lesser-known or just interesting. Before answering, always " \
             "check your previous answers to make sure you haven't answered with the same fact before, " \
             "even in different form."
    history = [{
        "role": "system",
        "content": "You are a helpful assistant. When asked about a random fun, lesser-known or interesting fact, "
                   "you only reply with the fact and nothing else."
    }]

    # Post status every POST_INTERVAL_SECONDS
    while True:
        try:
            history.append({"role": "user", "content": prompt})

            # Only keep the last 10 messages to avoid excessive token usage
            if len(history) > 10:
                history = history[-10:]

            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=history,
                temperature=1.3,
            )

            answer = response.choices[0]['message']['content']\
                .strip()\
                .encode('utf-8')\
                .decode('utf-8')

            mastodon.status_post(status=answer)

            logging.info(f'Posted status: "{answer}", usage: {response.usage.total_tokens} tokens')

        except Exception as e:
            logging.error(e)

        time.sleep(float(os.environ.get('POST_INTERVAL_SECONDS', 3600)))


if __name__ == '__main__':
    main()

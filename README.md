<img src="https://user-images.githubusercontent.com/11541888/225115015-ce860820-9470-406b-bf24-a70b110ec67b.png" width="150" height="150">

# Mastofact
![python-version](https://img.shields.io/badge/python-3.10-blue.svg)
[![openai-version](https://img.shields.io/badge/openai-0.27.0-green.svg)](https://openai.com/)
[![mastodon.py-version](https://img.shields.io/badge/mastodon.py-1.8.0-red.svg)](https://openai.com/)
[![license](https://img.shields.io/badge/License-MIT-brightgreen.svg)](LICENSE)

A silly ChatGPT-powered Mastodon bot that toots a random fact every hour. Running at [@mastofact](https://mastodon.social/@mastofact)

## Prerequisites
- Python 3.10+ and [Pipenv](https://pipenv.readthedocs.io/en/latest/)
- A Mastodon access token (create one under `Development` > `Your applications` > `New application` > `Your access token`)
- An [OpenAI](https://openai.com) account (see [configuration](#configuration) section)

## Getting started

### Configuration
Customize the configuration by copying `.env.example` and renaming it to `.env`, then editing the parameters as desired:
```bash
MASTODON_INSTANCE="YOUR_MASTODON_INSTANCE" # e.g. https://mastodon.social/
MASTODON_BOT_TOKEN="YOUR_MASTODON_BOT_TOKEN"
OPENAI_API_KEY="YOUR_OPENAI_API_KEY"

# Optional parameters
POST_INTERVAL_SECONDS=3600 # Defaults to 3600 (1h)
```

### Installing
1. Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/n3d1117/mastofact.git
cd mastofact
```

#### From Source
2. Create a new virtual environment with Pipenv and install the required dependencies:
```
pipenv install
```

3. Activate the virtual environment:
```
pipenv shell
```

4. Use the following command to start the bot:
```
python main.py
```

#### Using Docker Compose

2. Run the following command to build and run the Docker image:
```bash
docker-compose up
```

## Credits
- [ChatGPT](https://chat.openai.com/chat) from [OpenAI](https://openai.com)
- [Mastodon.py](https://github.com/halcy/Mastodon.py)

## Disclaimer
This is a personal project and is not affiliated with OpenAI in any way.

## License
MIT license. For more information, see the [LICENSE](LICENSE) file included in the repository.

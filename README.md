# tempofy_bot

## Description

Returns Spotify track features by track URI. Bot in Telegram: https://t.me/tempofy_bot

## Install

Clone the repo and change directory to the cloned repo:

```bash
git clone https://github.com/hardkoro/tempofy_bot.git
```

```bash
cd tempofy_bot
```

Create and activate virtual environment:

```bash
python -m venv venv
```

```bash
source venv/source/activate
```

Install requirements from file requirements.txt:

```bash
pip install -r requirements.txt
```

Run project:

```bash
python tempofy_bot.py
```

## Example

Link: https://open.spotify.com/track/5J9lPVAyScSLtJ0XqJUBm6?si=a2c7c9347bbb4c6e

Bot response:
```
Самшит — Зима (2020)
  Tempo:    140.005 BPM
  Key:      C# Major
  Loudness: -7.821 dB

  Danceability:     80 %
  Energy:           67 %
  Speechiness:      29 %
  Acousticness:      3 %
  Instrumentalness:  0 %
  Liveness:         10 %
  Valence:          73 %
```

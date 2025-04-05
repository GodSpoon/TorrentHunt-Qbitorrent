# TorrentHunt with qBittorrent Integration

This is a modified version of [TorrentHunt](https://github.com/hemantapkh/TorrentHunt) that adds direct downloading to a qBittorrent instance.

## Features

- All features of the original TorrentHunt bot
- Direct downloading to qBittorrent with a single click
- Docker/Portainer ready for easy deployment

## Setup

1. Clone this repository
2. Copy `.env.example` to `.env` and update the values
3. Deploy using Docker or Portainer

## Configuration

Required environment variables:

- `BOT_TOKEN`: Your Telegram Bot token
- `API_ID`: Your Telegram API ID
- `API_HASH`: Your Telegram API Hash
- `TORRENTHUNT_API_KEY`: RapidAPI key for TorrentHunt
- `QBITTORRENT_HOST`: URL to your qBittorrent WebUI (e.g., http://qbittorrent:8080)
- `QBITTORRENT_USERNAME`: qBittorrent WebUI username
- `QBITTORRENT_PASSWORD`: qBittorrent WebUI password

## Docker Deployment

```bash
docker-compose up -d

## Portainer Deployment

Add the git repository to Portainer
Deploy the stack using the docker-compose.yml file
Configure environment variables in Portainer UI

## License
This project is licensed under the MIT License - see the LICENSE file for details.

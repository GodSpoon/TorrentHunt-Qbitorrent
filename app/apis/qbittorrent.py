"""Connecting with qBittorrent API"""

from os import environ
import logging
import aiohttp

class QBittorrent:
    def __init__(self):
        self.host = environ.get("QBITTORRENT_HOST", "http://localhost:8080")
        self.username = environ.get("QBITTORRENT_USERNAME", "admin")
        self.password = environ.get("QBITTORRENT_PASSWORD", "adminadmin")
        self.session = None
        self.logger = logging.getLogger(__name__)
    
    async def _get_session(self):
        """Get authenticated session"""
        if not self.session:
            self.session = aiohttp.ClientSession()
            try:
                login_url = f"{self.host}/api/v2/auth/login"
                data = {'username': self.username, 'password': self.password}
                async with self.session.post(login_url, data=data) as resp:
                    if resp.status != 200:
                        self.logger.error(f"Failed to log in to qBittorrent: {await resp.text()}")
                        await self.session.close()
                        self.session = None
                        return None
            except Exception as e:
                self.logger.error(f"Error connecting to qBittorrent: {e}")
                if self.session:
                    await self.session.close()
                self.session = None
                return None
        return self.session
    
    async def add_torrent(self, magnet_link, category="TorrentHunt"):
        """Add torrent to qBittorrent"""
        session = await self._get_session()
        if not session:
            return False, "Failed to connect to qBittorrent"
        
        try:
            add_url = f"{self.host}/api/v2/torrents/add"
            data = {
                'urls': magnet_link,
                'category': category
            }
            
            async with session.post(add_url, data=data) as resp:
                if resp.status == 200:
                    text = await resp.text()
                    if text == "Ok.":
                        return True, "Torrent added successfully"
                    else:
                        return False, f"Failed to add torrent: {text}"
                else:
                    return False, f"Failed to add torrent: HTTP {resp.status}"
                
        except Exception as e:
            return False, f"Error adding torrent: {e}"

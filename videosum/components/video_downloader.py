import os
import sys
import requests
import yt_dlp

from videosum.exception import CustomException
from videosum.logger import logger


class VideoDownloader:
    def __init__(self, url: str, save_path: str):
        self.url = url
        self.save_path = save_path

    def download(self) -> str | None:
        """
        It downloads a video from a given url, and returns the path to the downloaded video
        
        Returns:
          The return value is a string or None.
        """
        try:
            if 'youtu' in self.url:
                return self._download_youtube()
            else:
                return self._download_other()
        except Exception as e:
            raise CustomException(e, sys)

    def _download_youtube(self) -> str:
        """
        It downloads a youtube video from a given url and saves it to a given path

        Returns:
          The path to the downloaded video
        """
        try:
            ydl_opts = {
                'format': 'best',
                'outtmpl': os.path.join(self.save_path, '%(title)s.%(ext)s'),
                'quiet': True,
                'no_warnings': True,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(self.url, download=True)
                filename = ydl.prepare_filename(info)

            logger.info(f"Youtube Video downloaded to {filename}")
            return filename
        except Exception as e:
            raise CustomException(e, sys)

    def _download_other(self) -> str:
        """
        It downloads the video from the url and saves it to the save_path
        
        Returns:
          The path to the downloaded file.
        """
        try:
            response = requests.get(self.url, stream=True)
            filename = self.url.split("/")[-1]
            with open(os.path.join(self.save_path, f"{filename}"), "wb") as f:
                for chunk in response.iter_content(chunk_size=4096):
                    f.write(chunk)
            logger.info(f"Video downloaded to {os.path.join(self.save_path, filename)}")
            return os.path.join(self.save_path, filename)
        except Exception as e:
            raise CustomException(e, sys)

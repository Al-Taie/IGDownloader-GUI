from os import path, mkdir, makedirs

import requests

from utils.configurations import PATH_IG_DOWNLOAD


class Downloader:
    @staticmethod
    def folder(category, user, short_code):
        root = f'{PATH_IG_DOWNLOAD}/{category}'
        post_path = f'{root}/{user}/{short_code}'
        makedirs(post_path, exist_ok=True)
        return post_path

    @staticmethod
    def save_file(file_path, content):
        with open(file_path, 'w+') as wf:
            wf.write(content)

    def download_prepare(self, on_progress, *args, **kwargs):
        (items, username, short_code, is_video, current_post, caption) = kwargs.values()

        if is_video:
            url = items.get('video_url')
            save_path = self.folder('Videos', username, short_code)
            filename = f'{save_path}/{current_post}.mp4'
        else:
            url = items.get('display_url')
            save_path = self.folder('Images', username, short_code)
            filename = f'{save_path}/{current_post}.jpg'
            self.save_file(file_path=f'{save_path}/title.txt', content=caption)
        self.download(url, filename, on_progress)

    @staticmethod
    def download(url, filename, on_progress, headers=None, *args, **kwargs):
        if headers is None:
            headers = {}

        with requests.get(url, headers=headers, stream=True) as resp:
            try:
                total_size = int(resp.headers.get('content-length'))
            except TypeError:
                content_length = resp.headers.get('Content-Range')
                if content_length:
                    content_length = content_length.split('/')[-1]
                    total_size = int(content_length)
                else:
                    return

            current_size = 0

            with open(filename, 'wb') as f:
                for chunk in resp.iter_content(chunk_size=total_size // 100):
                    current_size += len(chunk)
                    try:
                        on_progress(total_size, current_size)
                    except RuntimeError:
                        return
                    f.write(chunk) if chunk else None

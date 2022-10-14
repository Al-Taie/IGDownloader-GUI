from os import makedirs

import requests

from data.models.media import Media
from data.models.post import Post
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
        with open(file_path, 'w+', encoding='utf-8') as wf:
            wf.write(content)

    def download_prepare(self, on_progress, media_item: Media, post: Post, index=1, *args, **kwargs):
        if media_item.is_video:
            save_path = self.folder('Videos', post.username, post.short_code)
            filename = f'{save_path}/{index}.mp4'
            if post.caption:
                self.save_file(file_path=f'{save_path}/title.txt', content=post.caption)
        else:
            save_path = self.folder('Images', post.username, post.short_code)
            filename = f'{save_path}/{index}.jpg'
            if post.caption:
                self.save_file(file_path=f'{save_path}/title.txt', content=post.caption)
        self.download(media_item.url, filename, on_progress)

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

from typing import Dict, List

import requests

from data.models.media import Media
from data.models.media_type import MediaType
from data.models.post import Post


class ApiService:
    def __init__(self, cookie=None):
        self.cookie = cookie

    def get_post(self, url: str, headers: Dict[str, str]) -> Post:
        if self.cookie:
            return self.__get_post_login(url=url, headers=headers)
        else:
            return self.__get_post_no_login(url=url, headers=headers)

    def __get_post_login(self, url: str, headers: Dict[str, str]) -> Post:

        with requests.get(url, headers=headers, cookies=self.cookie) as resp:
            response = resp.json().get('items')[0]
            media_type = response.get('media_type')
            is_video = media_type == MediaType.VIDEO.value
            is_slide = media_type == MediaType.MIXED.value

            try:
                caption: str = (
                    response
                    .get('edge_media_to_caption')
                    .get('edges')[0]
                    .get('node')
                    .get('text')
                ).split('\n')[0]
            except (IndexError, AttributeError):
                caption: str = ''

            short_code = response["code"]
            username = response['user']['username']

        media_items = []

        if is_slide:
            post_list: list = response.get('carousel_media')
            media_items: List[Media] = list(map(
                lambda item: self.__get_media_item_login(json=item),
                post_list
            ))

        media_item = None

        if not is_slide:
            media_item = self.__get_media_item_login(response)

        return Post(
            username=username,
            caption=caption,
            is_video=is_video,
            is_slide=is_slide,
            item=media_item,
            short_code=short_code,
            items=media_items,
        )

    def __get_post_no_login(self, url: str, headers: Dict[str, str]) -> Post:
        with requests.get(url, headers=headers) as resp:
            resp_json = resp.json()
            response = resp_json.get('graphql').get('shortcode_media')
            is_video = response.get('is_video')
            is_slide = response.get('edge_sidecar_to_children')

            try:
                caption: str = (
                    response
                    .get('edge_media_to_caption')
                    .get('edges')[0]
                    .get('node')
                    .get('text')
                ).split('\n')[0]
            except (IndexError, AttributeError):
                caption: str = ''

            short_code = response["shortcode"]
            username = response['owner']['username']

        media_item = None

        if not is_slide:
            media_item = self.__get_media_item_no_login(response)

        media_items = []

        if is_slide:
            post_list: list = response.get('edge_sidecar_to_children').get('edges')

            media_items: List[Media] = list(map(
                lambda item: self.__get_media_item_no_login(json=item),
                post_list
            ))

        return Post(
            username=username,
            caption=caption,
            is_video=is_video,
            is_slide=is_slide,
            item=media_item,
            short_code=short_code,
            items=media_items,
        )

    @staticmethod
    def __get_media_item_no_login(json) -> Media:
        json = json.get('node')
        is_video = json.get('is_video')

        if is_video:
            video = json.get('video_url')
            return Media(url=video, is_video=True)
        else:
            image = json.get('display_url')
            return Media(url=image, is_video=False)

    @staticmethod
    def __get_media_item_login(json) -> Media:
        is_video = json.get('media_type') == MediaType.VIDEO.value

        if is_video:
            video = json.get('video_versions')[0]
            return Media(url=video.get('url'), is_video=True)
        else:
            image = json.get('image_versions2').get('candidates')[0]
            return Media(url=image.get('url'), is_video=False)

from os import getlogin


headers = {'authority': 'www.instagram.com',
           'method': 'GET',
           'scheme': 'https',
           'accept': ('text/html,application/xhtml+xml,application/xml;q=0.9,'
                      'image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'),
           'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'ar,en;q=0.9',
           'cache-control': 'max-age=0',
           'sec-fetch-dest': 'document',
           'sec-fetch-mode': 'navigate',
           'sec-fetch-site': 'none',
           'sec-fetch-user': '?1',
           'upgrade-insecure-requests': '1',
           'user-agent': ('Mozilla/5.0 (Windows NT 11.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63')}
app_name = 'IG Downloader'
developer = 'Ahmed Al-Taie'
version = '2.1'

PC_USER = getlogin()
PATH_DOWNLOADS = f'C:/Users/{PC_USER}/Downloads/'
PATH_IG_DOWNLOAD = PATH_DOWNLOADS + app_name


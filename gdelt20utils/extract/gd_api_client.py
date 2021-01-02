from gdelt20utils.common import constants_api
from gdelt20utils.common import utils_request


class Gdelt20ApiClietnt():
    def __init__(self):
        self.rate_limiter = utils_request.ThreadRateLimiter(constants_api.API_RATE_LIMIT)

    def save_file_list(self, language, save_path):
        url = constants_api.API_MASTER_FILE_LIST_URL[language]
        next(self.rate_limiter)

        return utils_request.download_url(url, save_path)

    def save_file(self, language, ts, obj_type, save_path):
        url = constants_api.API_FILE_LIST_URL[language][obj_type].format(ts, obj_type)

        next(self.rate_limiter)
        return utils_request.download_url(url, save_path), url


gd_api_client = Gdelt20ApiClietnt()

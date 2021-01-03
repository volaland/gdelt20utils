import json

from gdelt20utils.common import gd_path_gen
from gdelt20utils.common.gd_logger import logger_obj
from gdelt20utils.extract.check_point import Gdelt20CheckPoint
from gdelt20utils.extract.extraction_worker import FileExtractWorker
from gdelt20utils.extract.gd_api_client import gd_api_client


class Gdelt20Extractor():
    def __init__(self, config_obj, base_path, start_date, finish_date, languages, object_types):
        self.config_obj = config_obj
        self.base_path = base_path
        self.start_date = start_date
        self.finish_date = finish_date

        self.languages = languages
        self.object_types = object_types

        self.path_gen = gd_path_gen.Gdelt20PathGen(base_path, start_date, finish_date)
        self.gd_api_client = gd_api_client
        self.check_point = Gdelt20CheckPoint(base_path, start_date, finish_date)

        self.logger = logger_obj.logger

    def __call__(self, *args, **kwargs):
        for language in self.languages:

            self.check_point.set_language(language)

            with open(self.path_gen.get_list_timestamps_file_name(language), "r") as tof:
                ts_list = json.load(tof)
                ts_list_len = len(ts_list)
                if self.check_point.get_cnt() == ts_list_len:
                    self.logger.info(f"Skip processing {language}, downloaded {ts_list_len}, job complete")
                    continue

                self.logger.info("Downloading {}, count {} from {}".format(
                    language, len(ts_list), self.path_gen.get_list_timestamps_file_name(language)))

                FileExtractWorker(
                    language,
                    ts_list,
                    self.path_gen,
                    self.check_point,
                    self.gd_api_client,
                    self.object_types
                ).run()

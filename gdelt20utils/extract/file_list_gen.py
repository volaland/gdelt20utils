import json
import os

from gdelt20utils.common import gd_path_gen
from gdelt20utils.common.gd_logger import logger_obj
from gdelt20utils.extract.gd_api_client import gd_api_client


class Gdelt20FileListGen():
    def __init__(self, config_obj, base_path, start_date, finish_date, languages, object_types):
        self.config_obj = config_obj

        self.languages = languages
        self.object_types = object_types

        self.path_gen = gd_path_gen.Gdelt20PathGen(base_path, start_date, finish_date)
        self.start_date_int = int(self.path_gen.start_date_str)
        self.finish_date_int = int(self.path_gen.finish_date_str)

        self.gd_api_client = gd_api_client

        self.logger = logger_obj.logger

    def save_masterfile(self, language, list_file_name):
        if not os.path.exists(list_file_name):
            self.gd_api_client.save_file_list(language, list_file_name)

        self.logger.info(f"{language} masterfile is loaded {list_file_name}")

    def get_timestamp_from_masterline(self, line):
        timestamp_str = line.split("/")[-1].split(".")[0]
        return int(timestamp_str)

    def save_timestamps(self, list_file_name, list_timestamps_file_name):
        if not os.path.exists(list_timestamps_file_name):
            with open(list_file_name, "r") as mfo:
                with open(list_timestamps_file_name, "w") as tfo:
                    ts_set = set(
                        (self.get_timestamp_from_masterline(line) for line in mfo if not line.startswith("http")))
                    ts_list = sorted(filter(lambda ts: self.start_date_int <= ts <= self.finish_date_int, ts_set))
                    json.dump(ts_list, tfo)
        self.logger.info(f"{list_file_name} master file is transformed {list_timestamps_file_name}")

    def __call__(self, *args, **kwargs):
        for language in self.languages:
            list_file_name = self.path_gen.get_list_file_full_name(language)
            self.save_masterfile(language, list_file_name)

            list_timestamps_file_name = self.path_gen.get_list_timestamps_file_name(language)
            self.save_timestamps(list_file_name, list_timestamps_file_name)

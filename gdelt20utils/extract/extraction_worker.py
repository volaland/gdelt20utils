import os
import requests
from gdelt20utils.common import utils_worker
from gdelt20utils.common.gd_logger import logger_obj

HEARTBEAT_LOG_NUM = 10
WORKER_ERROR_MAX = 100

class ExtractorError(Exception):
    pass

class FileExtractWorker():

    def __init__(
            self,
            language,
            timestamps=None,
            path_gen=None,
            check_point=None,
            api_client=None,
            obj_types=None):

        self.language = language
        self.obj_types = obj_types

        self.api_client = api_client

        self.path_gen = path_gen

        self.check_point = check_point

        self.jobq = utils_worker.JobQueue()

        skip_processed = check_point.get_cnt()
        for ts in timestamps[skip_processed:]:
            self.jobq.put(ts)

        self.api_request_cnt = 0

        self.logger = logger_obj.logger

    def extract_data_worker(self, queue=None, worker_num=None):
        heartbeat_cnt = 0
        worker_error = 0
        self.logger.info(f"Worker {worker_num} started")
        while True:
            ts = queue.get()

            for obj_type in self.obj_types:
                save_path = self.path_gen.get_data_file_path(
                    self.language, obj_type, ts)
                try:
                    if not os.path.exists(save_path):
                        res_code, url = self.api_client.save_file(self.language, ts, obj_type, save_path)
                        if res_code != requests.codes.ok:
                            if res_code == requests.codes.not_found:
                                self.logger.warning(f"Worker {worker_num}: requests error - {url} code 404")
                            else:
                                raise ExtractorError(
                                    f"Worker {worker_num}: requests error - url {url}, code {res_code}")
                    else:
                        self.logger.info(f"Worker {worker_num}: {save_path} exists, skip")
                except Exception as exp:
                    self.logger.error(f"Worker {worker_num} error: {exp}")
                    worker_error += 1
            queue.task_done()

            self.check_point.update_checkpoint(ts)

            if worker_error >= WORKER_ERROR_MAX:
                self.logger.info(f"Worker {worker_num}: max error acceded {worker_error}")
                queue.lock_flush()

            heartbeat_cnt += 1
            if not heartbeat_cnt % HEARTBEAT_LOG_NUM:
                self.logger.info(f"Worker {worker_num}: heartbeat {heartbeat_cnt}, last ts {ts}")

    def run(self):
        self.logger.info(f"Start extraction, concurrency {utils_worker.CONCURENCY_NUM}, stats {self.check_point}")

        self.jobq.start(
            concurrency=utils_worker.CONCURENCY_NUM,
            worker=self.extract_data_worker
        )

        self.logger.info(f"Finish extraction, stats {self.check_point}")

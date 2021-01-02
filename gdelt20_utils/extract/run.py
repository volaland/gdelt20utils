from gdelt20_utils.common.gd_logger import logger_obj

from gdelt20_utils.common.gd_path_gen import Gdelt20PathGen
from gdelt20_utils.extract.extractor import Gdelt20Extractor
from gdelt20_utils.extract.file_list_gen import Gdelt20FileListGen
from gdelt20_utils.extract.gd_dir_tree import create_path_tree


def check_params(start_date, finish_date):
    assert start_date <= finish_date, f"{start_date} gt {finish_date}"


def run_extract(config_obj, base_path, start_date, finish_date, languages, obj_types):
    check_params(start_date, finish_date)

    create_path_tree(base_path, start_date, finish_date, languages, obj_types)
    logger_obj.init_loger(filename=Gdelt20PathGen(base_path, start_date, finish_date).get_log_file_name())
    logger = logger_obj.logger
    logger.info("Creating path tree")

    logger.info("Creating file lists")
    Gdelt20FileListGen(
        config_obj,
        base_path,
        start_date,
        finish_date,
        languages,
        obj_types
    )()

    logger.info("Extracting files")
    Gdelt20Extractor(
        config_obj,
        base_path,
        start_date,
        finish_date,
        languages,
        obj_types
    )()

    logger.info("Gdelt data extraction is finished")

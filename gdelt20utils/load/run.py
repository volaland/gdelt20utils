from gdelt20utils.common.gd_logger import logger_obj

from gdelt20utils.common.gd_path_gen import Gdelt20PathGen


def check_params(start_date, finish_date):
    assert start_date <= finish_date, f"{start_date} gt {finish_date}"


def run_load(config_obj, base_path, target_service, start_date, finish_date, languages, obj_types):
    check_params(start_date, finish_date)

    logger_obj.init_loger(filename=Gdelt20PathGen(base_path, start_date, finish_date).get_log_file_name())
    logger = logger_obj.logger

    if target_service == "s3":
        logger.info("Load target AWS S3 bucket")
    elif target_service == "cs":
        logger.info("Load target GCP Cloud Storage bucket")
    elif target_service == "es":
        logger.info("Load target ElasticSearch")
    elif target_service == "db":
        logger.info("Load target data base")
    elif target_service == "avro":
        logger.info("Load target avro files")
    else:
        raise NotImplementedError(f"Target {target_service} is not implemented")

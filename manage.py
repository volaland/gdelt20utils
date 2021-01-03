import click

from gdelt20utils.common import constants
from gdelt20utils.common.gd_config import config
from gdelt20utils.extract.run import run_extract
from gdelt20utils.load.run import run_load


@click.group(help="Extract")
@click.pass_context
def cli(ctx):
    ctx.obj.update(config)


@cli.command("extract", help="Extract gdelt20 data")
@click.option("--base_path", "-b",
              type=click.Path(),
              required=True,
              default=constants.DEFAULT_DATA_PATH,
              help="gdelt20 data target path")
@click.option("--start_date", "-d",
              type=click.DateTime(),
              required=True,
              help="gdelt20 data set start day")
@click.option("--finish_date", "-n",
              type=click.DateTime(),
              required=True,
              help="gdelt20 data set finish date")
@click.option("--languages", "-l",
              type=click.Choice(constants.GDELT_LANGUAGE, case_sensitive=True),
              required=True,
              default=constants.GDELT_LANGUAGE,
              multiple=True,
              help="gdelt20 data set language corpus")
@click.option("--object_types", "-o",
              type=click.Choice(constants.GDELT_OBJ_TYPE, case_sensitive=True),
              required=True,
              default=constants.GDELT_OBJ_TYPE,
              multiple=True,
              help="gdelt20 data set object type to load")
@click.pass_obj
def extract(config_obj, base_path, start_date, finish_date, languages, object_types):
    run_extract(
        config_obj,
        base_path,
        start_date,
        finish_date,
        languages,
        object_types
    )

@cli.command("load", help="load gdelt20 data")
@click.option("--base_path", "-b",
              type=click.Path(),
              required=True,
              default=constants.DEFAULT_DATA_PATH,
              help="gdelt20 data source path")
@click.option("--target_service", "-s",
              required=True,
              default=constants.TARGET_SERVISES[0],
              help="gdelt20 data source path")
@click.option("--start_date", "-d",
              type=click.DateTime(),
              required=True,
              help="gdelt20 data set start day")
@click.option("--finish_date", "-n",
              type=click.DateTime(),
              required=True,
              help="gdelt20 data set finish date")
@click.option("--languages", "-l",
              type=click.Choice(constants.GDELT_LANGUAGE, case_sensitive=True),
              required=True,
              default=constants.GDELT_LANGUAGE,
              multiple=True,
              help="gdelt20 data set language corpus")
@click.option("--object_types", "-o",
              type=click.Choice(constants.GDELT_OBJ_TYPE, case_sensitive=True),
              required=True,
              default=constants.GDELT_OBJ_TYPE,
              multiple=True,
              help="gdelt20 data set object type to load")
@click.pass_obj
def extract(config_obj, base_path, target_service, start_date, finish_date, languages, object_types):
    # TODO: implement extraction into targets directly from api
    run_load(
        config_obj,
        base_path,
        target_service,
        start_date,
        finish_date,
        languages,
        object_types
    )


if __name__ == "__main__":
    cli(obj={})

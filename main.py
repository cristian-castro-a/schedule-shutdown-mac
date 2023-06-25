import yaml
from pathlib import Path
from typing import Dict
from yaml.loader import BaseLoader
import os

CONFIG_FILE = 'config.yaml'


def load_yaml(config_file: Path) -> Dict:
    with open(config_file, 'r') as stream:
        try:
            dict = yaml.load(stream=stream, Loader=BaseLoader)
            return dict
        except FileNotFoundError as e:
            print('Config.yaml not found')


def run(config_file: Path) -> None:
    config = load_yaml(config_file=config_file)
    days_of_the_week = ''.join([config['Nomenclature'].get(i) for i in config['Days']])
    time_of_the_day = f"{config['Time'][0]}:00"

    os.system(f"sudo pmset repeat shutdown {days_of_the_week} {time_of_the_day}")
    os.system("pmset -g sched")


if __name__ == '__main__':
    """
    Sets a schedule for your Mac computer to shutdown
    
    inputs:
        - config.yaml: States the days and time at which you want to shutdown your Mac
    """
    config_file = Path.cwd() / CONFIG_FILE
    run(config_file=config_file)
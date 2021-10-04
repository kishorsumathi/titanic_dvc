import os
import pandas as pd
import argparse
import numpy as np
from src.utils.all_utils import read_yaml

def get_data(config_path):
     config= read_yaml(config_path)
     remote_data=config["data_path"]
     df= pd.read_csv(remote_data,sep=";")
     df.head()













if __name__=="__main__":
      args=argparse.ArgumentParser()
      args.add_argument("--config","-c",default="config/config.yaml")
      parsed_args= args.parse_args()
      get_data(config_path=parsed_args.config)

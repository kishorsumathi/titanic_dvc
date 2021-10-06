import os
import pandas as pd
import argparse
import numpy as np
from src.utils.all_utils import create_directory, read_yaml 
def get_data(config_path):
     config= read_yaml(config_path)
     remote_data=config["data_source"]
     df= pd.read_csv(remote_data)
     artifacts_dir1=config["artifacts"]["artifacts_dir"]
     local_data_path=config["artifacts"]["raw_local_dir"]
     data_path=config["artifacts"]["raw_local_file"]
     raw_local_dir_path=os.path.join(artifacts_dir1,local_data_path)
     create_directory(dirs=[raw_local_dir_path])
     raw_local_file_path=os.path.join(raw_local_dir_path,data_path)
     df.to_csv(raw_local_file_path,sep=",",index=False)














if __name__=="__main__":
      args=argparse.ArgumentParser()
      args.add_argument("--config","-c",default="config/config.yaml")
      parsed_args= args.parse_args()
      get_data(config_path=parsed_args.config)

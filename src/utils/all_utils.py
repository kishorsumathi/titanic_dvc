import yaml
import os
import pickle
import json
import datawig

def read_yaml(path_to_yaml:str):
    with open(path_to_yaml) as yaml_file:
        content= yaml.safe_load(yaml_file)
    
    return content
def create_directory(dirs: list):
    for dir_path in dirs:
          os.makedirs(dir_path,exist_ok=True)
          print(f"directory is created at {dir_path}")

def save_local_df(df,path,index_status=False):
    df.to_csv(path,index=index_status)
    print(f"data is saved at {path}")


def save_model(model,model_path):
    with open(model_path, 'wb') as files:
        pickle.dump(model, files)
        print(f"model is stored at {model_path}")



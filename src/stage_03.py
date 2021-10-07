from src.utils.all_utils import create_directory, read_yaml, save_local_df, save_model
import pandas as pd
import numpy as np
import argparse
from sklearn.ensemble import RandomForestClassifier
import os
 

def train(config_path,params_path):
    config=read_yaml(config_path)
    params=read_yaml(params_path)
    artifact_dir=config["artifacts"]["artifacts_dir"]
    split_data=config["artifacts"]["split_data_dir"]
    train_path=config["artifacts"]["train"]
    test_path=config["artifacts"]["test"]
    n_tree=params["model_params"]["random_forest"]["n_estimators"]
    criteria=params["model_params"]["random_forest"]["criterion"]
    depth=params["model_params"]["random_forest"]["max_depth"]
    score=params["model_params"]["random_forest"]["oob_score"]
    model_dir=config["artifacts"]["model_dir"]
    model_path=config["artifacts"]["model_path"]
    path_to_load=os.path.join(artifact_dir,split_data,train_path)
    model_path1=os.path.join(artifact_dir,model_dir)
    create_directory([model_path1])
    saved_model=os.path.join(model_path1,model_path)
    df=pd.read_csv(path_to_load)
    x_train=df.drop(["Survived"],axis=1)
    y_train=df["Survived"]
    model=RandomForestClassifier(n_estimators=n_tree,criterion=criteria,max_depth=depth,oob_score=score)
    model.fit(x_train,y_train)
    save_model(model,saved_model)  




if __name__ == "__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config","-c",default="config/config.yaml")
    args.add_argument("--params","-p",default="params.yaml")
      
    parsed_args= args.parse_args()
    train(config_path=parsed_args.config,params_path=parsed_args.params)
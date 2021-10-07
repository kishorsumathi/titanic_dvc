from src.utils.all_utils import create_directory, read_yaml, save_local_df,save_model,load_model,save_reports
from sklearn.metrics import confusion_matrix, precision_score,recall_score,f1_score,accuracy_score
import argparse
import pandas as pd
import numpy as np
import os

def evaluate(config_path):
    config=read_yaml(config_path)
    artifact_dir=config["artifacts"]["artifacts_dir"]
    split_data=config["artifacts"]["split_data_dir"]
    test_path=config["artifacts"]["test"]
    model_dir=config["artifacts"]["model_dir"]
    model_path=config["artifacts"]["model_path"]
    metric_dir=config["artifacts"]["report_dir"]
    metric_path=config["artifacts"]["report"]
    path_to_load=os.path.join(artifact_dir,split_data,test_path)
    model_path1=os.path.join(artifact_dir,model_dir)
    metric_path_dir=os.path.join(artifact_dir,metric_dir)
    load_model_path=os.path.join(model_path1,model_path)
    df=pd.read_csv(path_to_load)
    model=load_model(load_model_path)
    x_test=df.drop(["Survived"],axis=1)
    y_test=df["Survived"]
    y_pred=model.predict(x_test)
    confusion_matrix1=confusion_matrix(y_test,y_pred)
    matrix=confusion_matrix1.tolist()
    evaluation_metric={
        "confusion_matrix":matrix,
        "accuracy"  :   accuracy_score(y_test,y_pred),
        "precision" :   precision_score(y_test,y_pred),
        "reecall"   :   recall_score(y_test,y_pred),
        "f1_score"  :   f1_score(y_test,y_pred),
        "oob_score" :   model.oob_score_,
    }
    create_directory([metric_path_dir])
    metric_path_json=os.path.join(metric_path_dir,metric_path)
    save_reports(evaluation_metric,metric_path_json)





if __name__ == "__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config","-c",default="config/config.yaml")
      
    parsed_args= args.parse_args()
    evaluate(config_path=parsed_args.config)
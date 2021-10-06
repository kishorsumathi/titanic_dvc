from os import read
import pandas as pd
import numpy as np
import os
import argparse
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from src.utils.all_utils import create_directory, read_yaml, save_local_df


def preprocess_data(config_path):
    config=read_yaml(config_path)
    artifact_dir=config["artifacts"]["artifacts_dir"]
    local_data_dir=config["artifacts"]["raw_local_dir"]
    data_file=config["artifacts"]["raw_local_file"]
    split_data=config["artifacts"]["split_data_dir"]
    train_path=config["artifacts"]["train"]
    test_path=config["artifacts"]["test"]
    path_to_load=os.path.join(artifact_dir,local_data_dir,data_file)
    df=pd.read_csv(path_to_load)
    print(df["Embarked"].value_counts())
    df.drop(["Name","Ticket","PassengerId","Cabin"],axis=1,inplace=True)
    df["Age"].fillna(df.Age.mean(),inplace=True)
    print(df["Embarked"].fillna(df["Embarked"].value_counts().index[0],inplace=True))
    df["Sex"]=np.where(df["Sex"]=="male",1,0)
    le = preprocessing.LabelEncoder()
    df["Embarked"]=df["Embarked"].astype("str")
    df["Embarked"]=le.fit_transform(df["Embarked"])
    print(df.info())
    x_train,y_test=train_test_split(df,test_size=0.25,random_state=0)
    raw_local_dir_path=os.path.join(artifact_dir,split_data)
    create_directory([raw_local_dir_path])
    raw_local_train_path=os.path.join(raw_local_dir_path,train_path)
    raw_local_test_path=os.path.join(raw_local_dir_path,test_path)
    save_local_df(x_train,raw_local_train_path)
    save_local_df(y_test,raw_local_test_path)




if __name__=="__main__":
      args=argparse.ArgumentParser()
      args.add_argument("--config","-c",default="config/config.yaml")
      parsed_args= args.parse_args()
      preprocess_data(config_path=parsed_args.config)
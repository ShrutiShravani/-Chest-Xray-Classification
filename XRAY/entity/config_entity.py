import os
from dataclasses import dataclass
from XRAY.constant.training_pipeline import *

from torch import device


@dataclass
class DataIngestionconfig:
    def __init__(self):
        self.s3_data_folder:str= S3_DATA_FOLDER
        self.bucket_name:str= BUCKET_NAME
        self.artifact_dir:str= os.path.join(ARTIFACT_DIR,TIMESTAMP)

        self.data_path:str=os.path.join(self.artifact_dir,self.s3_data_folder)
        self.train_data_path=os.path.join(self.data_path,"train")
        self.test_data_path:str=os.path.join(self.data_path,"test")



        

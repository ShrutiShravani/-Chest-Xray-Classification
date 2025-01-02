from datetime import datetime
from typing import List


TIMESTAMP:datetime= datetime.now().strftime("%m_%d_%H_%M_%S")

#Data Ingestion Constants
BUCKET_NAME:str="chestxrayclassification"
ARTIFACT_DIR:str="artifacts"
S3_DATA_FOLDER: str= "data"
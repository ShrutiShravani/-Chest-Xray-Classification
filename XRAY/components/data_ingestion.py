from XRAY.exception import XrayException
from XRAY.logger import logging
import os,sys
from XRAY.entity.artifact_entity import DataIngestionArtifact
from XRAY.entity.config_entity import DataIngestionconfig

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionconfig):
        self.data_ingestion_config= data_ingestion_config

        #GET DATA FROM S3 BUCKET
    
    
    
    def get_data_from_s3(self)->None:
        try:
            pass
        except XrayException as e:
            raise XrayException(e,sys)
    

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            pass
    
        except XrayException as e:
            raise XrayException(e,sys)
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

def setup_aws_glue_job(job_name):
    """
    Sets up the AWS Glue job environment.
    """
    glue_context = GlueContext(SparkContext.getOrCreate())
    spark = glue_context.spark_session
    job = Job(glue_context)
    job.init(job_name, getResolvedOptions(sys.argv, ['JOB_NAME']))
    return glue_context, spark, job

def setup_logger():
    """
    Sets up the logger for the Glue job.
    """
    import logging
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    return logger


def source_s3_data(glue_context,source_bucket):
    # Read data from the source S3 bucket
    source_df = glue_context.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [source_bucket]},
    format="csv" )
    
    return source_df

def writing_data_to_s3(glue_context,source_df,destination_bucket):
    glue_context.write_dynamic_frame.from_options(
    frame=source_df,
    connection_type="s3",
    connection_options={"path": destination_bucket},
    format="csv" )
    print("Data copied successfully from source to destination S3 bucket")
    


def main():
    # Define source and destination S3 paths
    source_bucket = "s3://testinp/"
    destination_bucket = "s3://oupbuck/"
    glue_context, spark, job = setup_aws_glue_job(job_name="Data_Cpy_AWS_Glue")
    logger = setup_logger()
    
    logger.info("Starting the AWS Glue job.")
    
    # Read data from the source S3 bucket
    logger.info(f"Reading data from source bucket: {source_bucket}")
    source_df = source_s3_data(glue_context, source_bucket)
    logger.info("Data read successfully from source bucket.")
    
    # Write data to the destination S3 bucket
    logger.info(f"Writing data to destination bucket: {destination_bucket}")
    writing_data_to_s3(glue_context, source_df, destination_bucket)
    logger.info("Data written successfully to destination bucket.")
    
    logger.info("Committing the job.")
    job.commit()
    logger.info("Job committed successfully.")
    
    logger.info("Stopping the Spark context.")
    spark.stop()
    logger.info("Spark context stopped. Job completed successfully.")

if __name__ == "__main__":
    main()
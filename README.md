# AWS Glue Data Copy 🛠️

![AWS Glue](https://img.shields.io/badge/AWS%20Glue-Data%20Copy-blue?style=flat&logo=amazonaws)

Welcome to the **AWS Glue Data Copy** repository! This project provides a robust function for copying data such as CSV, Parquet, Avro, and more from a source S3 bucket to a destination S3 bucket using AWS Glue. This repository includes the necessary setup for the Glue job, logging, and efficient data handling.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Configuration](#configuration)
- [Logging](#logging)
- [Contributing](#contributing)
- [License](#license)
- [Releases](#releases)

## Features ✨

- **Data Formats**: Supports various data formats including CSV, Parquet, and Avro.
- **AWS Glue Integration**: Seamlessly integrates with AWS Glue for data processing.
- **S3 Buckets**: Easily read from and write to S3 buckets.
- **Logging**: Built-in logging for monitoring job execution.
- **Efficient Data Handling**: Optimized for performance and reliability.

## Getting Started 🚀

To get started with the AWS Glue Data Copy function, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/muhd-minhaz/AWS-Glue--Data-Copy.git
   cd AWS-Glue--Data-Copy
   ```

2. **Install Dependencies**:
   Make sure you have the necessary dependencies installed. You can install them using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure AWS Credentials**:
   Ensure your AWS credentials are configured. You can set them up in the `~/.aws/credentials` file or use environment variables.

## Usage 📖

To use the AWS Glue Data Copy function, you need to create a Glue job in the AWS Management Console. Here’s how to do it:

1. **Create a Glue Job**:
   - Navigate to the AWS Glue Console.
   - Click on "Jobs" and then "Add job".
   - Set the job name and choose the IAM role.
   - In the script path, point to your Glue script in the repository.

2. **Run the Job**:
   - Start the job from the AWS Glue Console.
   - Monitor the job execution in the console.

3. **Check Logs**:
   - View logs in CloudWatch to troubleshoot any issues.

## Configuration ⚙️

You can customize the Glue job by modifying the parameters in the script. Here are some key parameters:

- **Source Bucket**: Specify the S3 bucket where the source data resides.
- **Destination Bucket**: Specify the S3 bucket where the copied data will be stored.
- **Data Format**: Choose the format of the data you are copying (CSV, Parquet, etc.).

## Logging 📜

The AWS Glue Data Copy function includes logging capabilities to help you monitor job execution. The logs are sent to Amazon CloudWatch. You can view the logs to troubleshoot issues or verify that the job ran successfully.

### Example Log Messages:

- **Job Started**: Indicates when the job begins execution.
- **Data Read**: Confirms data has been read from the source bucket.
- **Data Written**: Confirms data has been written to the destination bucket.
- **Job Completed**: Indicates successful completion of the job.

## Contributing 🤝

We welcome contributions to the AWS Glue Data Copy project. If you would like to contribute, please follow these steps:

1. **Fork the Repository**: Click the "Fork" button on the top right of the page.
2. **Create a New Branch**: 
   ```bash
   git checkout -b feature/YourFeature
   ```
3. **Make Your Changes**: Implement your feature or fix.
4. **Commit Your Changes**:
   ```bash
   git commit -m "Add Your Feature"
   ```
5. **Push to Your Branch**:
   ```bash
   git push origin feature/YourFeature
   ```
6. **Create a Pull Request**: Go to the original repository and create a pull request.

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Releases 📦

To download the latest release or previous versions, visit the [Releases](https://github.com/muhd-minhaz/AWS-Glue--Data-Copy/releases) section. Here, you can find the necessary files to be downloaded and executed.

If you need to check for updates or previous versions, you can also refer to the [Releases](https://github.com/muhd-minhaz/AWS-Glue--Data-Copy/releases) section.

---

Thank you for checking out the AWS Glue Data Copy repository! We hope you find it useful for your data processing needs. If you have any questions or feedback, feel free to reach out. Happy coding!
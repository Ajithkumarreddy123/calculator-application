# 🔋 Power Calculator using Python on AWS

This project provides a simple and efficient Power Calculator built using Python, deployed and run on AWS services. It allows users to calculate the result of raising a number (base) to the power of another (exponent), supporting both positive and negative exponents, including decimals.

---

## 🚀 Overview

The Power Calculator is designed as a beginner-friendly project that demonstrates clean code structure, modularity, and testability in Python. It supports both command-line interaction and an optional graphical user interface (GUI), and it is deployed on AWS for scalability and ease of use.

---

## 🧰 Technologies Used

- **Python** – Core language for implementation  
- **AWS Lambda** – For serverless compute tasks  
- **AWS API Gateway** – For exposing the power calculator as a web service  
- **AWS S3** – For storing input data or results (optional)   

---

## 🔧 Setup and Usage

### 1. Prerequisites

- AWS account with access to Lambda, API Gateway, and CloudWatch
- Python 3.x installed on your local system
- AWS CLI installed and configured with your credentials  
- `pip` for installing packages (if needed)  


### 2. Deployment on AWS

1. **Deploy Lambda function:**
    - Create a new Lambda function in AWS Management Console.
    - Upload the Python script for the power calculator.
    - Set the Lambda function's execution role permissions.

2. **Set up API Gateway:**
    - Create a new API in AWS API Gateway.
    - Configure an endpoint for invoking the Lambda function.
    - Enable CORS for web access if necessary.
      
3. **Static website Hosting:**
    - Deploy the html file in s3 bucket
    - Then go to the properties -> static website hosting-> enable it
    - enter the html file name in that
    - click save
    - then click the website link
4. **Testing**
   - enter tha values of base and exponenets
   - click on the result you can see the result
-------

## 📊 Example Inputs & Outputs

| Base | Exponent | Result |
|------|----------|--------|
| 2    | 3        | 8      |
| 5    | 0        | 1      |
| 2    | -2       | 0.25   |
| 9    | 0.5      | 3.0    |

------
### 🌟 Features
-Accepts both integers and floats

-Handles negative exponents and zero values

-Clean and modular code structure

-Optional GUI for better user interaction

-Includes test cases for robustness

-Serverless AWS deployment with Lambda and API Gateway

------------

### 🤝 Contributing
Contributions are welcome! Feel free to fork the repo, make changes, and submit a pull request.

📩 For feedback or questions, reach out to: ajithbhumireddy30@gmail.com

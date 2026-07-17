# 🚀 Daily DSA Challenge Agent

> An AI-powered serverless agent built using AWS that automatically sends a random Data Structures & Algorithms (DSA) challenge to your email every morning at 6:00 AM.

![AWS](https://img.shields.io/badge/AWS-Lambda-orange)
![Python](https://img.shields.io/badge/Python-3.13-blue)
![EventBridge](https://img.shields.io/badge/AWS-EventBridge-red)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📌 Overview

The **Daily DSA Challenge Agent** is a fully automated cloud application designed to help developers improve their coding skills consistently.

Instead of manually searching for coding problems every day, this agent automatically sends a random Data Structures & Algorithms challenge directly to your inbox every morning at **6:00 AM**.

The project is built entirely on a **serverless architecture**, requiring no servers to manage. Once deployed, the system runs automatically without any manual intervention.

---

# ✨ Features

- ✅ Fully Automated Daily Execution
- ✅ Runs Every Day at 6:00 AM
- ✅ Built on AWS Serverless Architecture
- ✅ Random DSA Challenge Generator
- ✅ Sends Email Automatically
- ✅ Secure Environment Variables
- ✅ Easy to Deploy
- ✅ Zero Manual Interaction

---

# 🏗️ Architecture

```
Amazon EventBridge Scheduler
            │
            ▼
      AWS Lambda Function
            │
            ▼
 Generate Random DSA Question
            │
            ▼
     Format Email Content
            │
            ▼
       Gmail SMTP Server
            │
            ▼
        User's Inbox
```

> *(Replace this section with your architecture diagram image after uploading it.)*

```markdown
![Architecture](architecture/architecture-diagram.png)
```

---

# ⚙️ Technologies Used

| Technology | Purpose |
|------------|---------|
| AWS Lambda | Serverless Compute |
| Amazon EventBridge Scheduler | Daily Automation |
| Python 3.13 | Application Logic |
| Gmail SMTP | Email Delivery |
| IAM Role | Permissions |

---

# 📂 Project Structure

```
Daily-DSA-Challenge-Agent/
│
├── lambda_function.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── architecture/
│   └── architecture-diagram.png
│
├── screenshots/
│   ├── lambda.png
│   ├── scheduler.png
│   └── email-output.png
│
└── docs/
    └── workflow.md
```

---

# 🚀 How It Works

1. Amazon EventBridge Scheduler triggers every day at **6:00 AM**.
2. The scheduler invokes the AWS Lambda function.
3. Lambda randomly selects one DSA question.
4. The question is formatted into an email.
5. Gmail SMTP securely sends the email.
6. The user receives a new coding challenge every morning.

The entire process is fully automatic.

---

# 🔧 Deployment Steps

## Step 1

Create an AWS Lambda Function.

---

## Step 2

Create an IAM Role with the required permissions.

---

## Step 3

Add the following Environment Variables.

```
SENDER_EMAIL
RECEIVER_EMAIL
GMAIL_APP_PASSWORD
```

---

## Step 4

Deploy the Lambda Function.

---

## Step 5

Create an Amazon EventBridge Scheduler.

Schedule:

```
Every Day
6:00 AM
```

Target:

```
AWS Lambda Function
```

---

## Step 6

Test the Lambda Function.

The email should arrive in your inbox successfully.

---

# 📸 Screenshots

## AWS Lambda

*(Add Screenshot Here)*

```
screenshots/lambda.png
```

---

## EventBridge Scheduler

*(Add Screenshot Here)*

```
screenshots/scheduler.png
```

---

## Email Output

*(Add Screenshot Here)*

```
screenshots/email-output.png
```

---

# 🔒 Environment Variables

The project securely stores credentials using Lambda Environment Variables.

```
SENDER_EMAIL
RECEIVER_EMAIL
GMAIL_APP_PASSWORD
```

Sensitive credentials are **never hardcoded** inside the source code.

---

# 📈 Future Improvements

- AI-generated DSA explanations
- Difficulty Levels (Easy, Medium, Hard)
- Daily Coding Streak Tracker
- Telegram Notifications
- Slack Integration
- Weekly Coding Report
- LeetCode API Integration
- Progress Dashboard

---

# 📚 Learning Outcomes

Through this project I learned:

- AWS Lambda
- Amazon EventBridge Scheduler
- Serverless Computing
- IAM Roles and Permissions
- Environment Variables
- Gmail SMTP Integration
- Cloud Automation
- Event-Driven Architecture
- Python Automation

---

# 🌟 Why This Project?

Practicing one coding problem every day is one of the best ways to improve problem-solving skills.

This project automates that habit by ensuring a fresh DSA challenge arrives in the inbox every morning without requiring any manual effort.

It demonstrates how AWS serverless services can be combined to build lightweight, event-driven automation that is practical, scalable, and easy to maintain.

---

# 👨‍💻 Author

**Siva Selvakumar**

🎓 Final Year Electronics and Communication Engineering Student

🔗 GitHub:
https://github.com/siva8115

🔗 LinkedIn:
https://www.linkedin.com/in/siva-selvakumar/

---

# 📄 License

This project is licensed under the MIT License.

Feel free to fork, modify, and use it for learning purposes.

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!

# Daily DSA Agent

## Overview

Daily DSA Agent is an Always-On Agent built for the AWS Builder Weekend Challenge.

Every day at 6:00 AM, Amazon EventBridge Scheduler automatically triggers an AWS Lambda function.

The Lambda function selects a random Data Structures and Algorithms (DSA) challenge and sends it to my email using Gmail SMTP.

No manual intervention is required after deployment.

---

## Features

- Runs automatically every day at 6:00 AM
- Sends one random DSA question
- Email delivered using Gmail SMTP
- Fully serverless
- Easy to customize

---

## AWS Services Used

- AWS Lambda
- Amazon EventBridge Scheduler

---

## Architecture

EventBridge Scheduler
        ↓
AWS Lambda
        ↓
Random DSA Challenge
        ↓
Gmail SMTP
        ↓
Inbox

---

## Author

Siva

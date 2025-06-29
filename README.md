# 💸 AWS Cost Optimizer Bot

This project automates AWS cost tracking and idle resource detection. It runs daily, checks for unused EC2/EBS, pulls cost data from Cost Explorer, and sends a detailed email report using Amazon SNS.

---

## ✅ Features

- Detects **unattached EBS volumes**
- Flags **stopped EC2 instances**
- Pulls **daily AWS cost** (Cost Explorer)
- Sends **email reports** via SNS
- **Automated daily execution** with EventBridge

---

## 📌 Architecture

![ChatGPT Image Jun 29, 2025, 11_57_02 AM](https://github.com/user-attachments/assets/f7ef023c-3e29-45c3-91dc-17f391c6ec8b)

---

## 🛠️ Technologies Used

- AWS Lambda
- AWS Cost Explorer (ce:GetCostAndUsage)
- Amazon EC2 & EBS
- Amazon SNS (Email Alerts)
- Amazon EventBridge (Scheduled Runs)
- IAM Role with fine-grained permissions

---

## 🚀 How It Works

1. Lambda script checks:
   - Any unattached EBS volumes
   - Any stopped EC2 instances
   - Yesterday’s AWS cost
2. It compiles a message
3. Sends it as an **email report** via SNS
4. Runs daily at **9:00 AM IST** via EventBridge schedule

---

## 📂 Project Structure

```bash
.
├── lambda_function.py       # Core logic
├── IAMPolicy.json           # Permissions for Lambda execution
└── README.md

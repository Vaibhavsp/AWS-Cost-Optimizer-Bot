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

![ChatGPT Image Jun 29, 2025, 11_57_02 AM](https://github.com/user-attachments/assets/cce1b666-b98f-4b44-a7bf-df5d456dd0cc)

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

## 🧪 Test it Yourself

1. **Create Lambda Function**

2. Assign IAM role with:

   * `ec2:Describe*`
   * `ce:GetCostAndUsage`
   * `sns:Publish`

3. Create **SNS Topic**, subscribe your email

4. Connect SNS ARN in the code

5. Use **EventBridge** to schedule daily runs

---

## 📌 Why this project?

Recruiters love:

* Cost awareness 💰
* Automation mindset 🤖
* Hands-on AWS work 💻

Perfect to showcase on LinkedIn, GitHub, or resume.

---

## ✍️ Author

Built by \Vaibhav Parekh

---

## 📄 License

This project is licensed under the MIT License.

````

---

## 🔗 LinkedIn Post (Short + Punchy)

```markdown
🚀 Just built an **AWS Cost Optimizer Bot**!

This project:
✅ Identifies unused EC2 & EBS volumes  
✅ Tracks daily AWS cost via Cost Explorer  
✅ Sends email reports via SNS  
✅ Runs automatically every morning with EventBridge

No more logging into the console manually 👀  
Just wake up to an optimized AWS account 🔁💡

It’s clean, useful, and resume-worthy.

#AWS #Lambda #CostExplorer #DevOps #Projects #CloudComputing #Automation #EventBridge #Python
````


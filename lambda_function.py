import boto3
import datetime

ec2 = boto3.client('ec2')
ce = boto3.client('ce')
sns = boto3.client('sns')

SNS_TOPIC_ARN = 'arn:aws:sns:<region>:<account-id>:<your-topic-name>'  # Replace with yours

def lambda_handler(event, context):
    report = []

    # 1. Unattached EBS volumes
    volumes = ec2.describe_volumes(
        Filters=[{'Name': 'status', 'Values': ['available']}]
    )['Volumes']
    if volumes:
        report.append("🧊 Unattached EBS Volumes:")
        for vol in volumes:
            report.append(f" - Volume ID: {vol['VolumeId']}, Size: {vol['Size']}GiB")

    # 2. Stopped EC2 Instances
    instances = ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}]
    )
    stopped = []
    for res in instances['Reservations']:
        for inst in res['Instances']:
            stopped.append(inst['InstanceId'])

    if stopped:
        report.append("\n🛑 Stopped EC2 Instances:")
        for inst_id in stopped:
            report.append(f" - Instance ID: {inst_id}")

    # 3. Estimated Cost (Last 1 day)
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    cost = ce.get_cost_and_usage(
        TimePeriod={
            'Start': str(yesterday),
            'End': str(today)
        },
        Granularity='DAILY',
        Metrics=['UnblendedCost']
    )
    amount = cost['ResultsByTime'][0]['Total']['UnblendedCost']['Amount']
    currency = cost['ResultsByTime'][0]['Total']['UnblendedCost']['Unit']
    report.append(f"\n💸 Estimated Cost (yesterday): {amount} {currency}")

    # 4. Send Report via SNS
    message = "\n".join(report) if report else "✅ No idle resources or waste detected today."
    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject="AWS Cost Optimizer Report",
        Message=message
    )

    return {"status": "done", "message": message}

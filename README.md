# tealeaf
A Modular CloudWatch Python Feeder



#IAM Profile

    {
    "Statement": [
    {
    "Action": [
    "cloudwatch:ListMetrics",
    "cloudwatch:GetMetricStatistics",
    "cloudwatch:PutMetricData",
    "autoscaling:DescribeAutoScalingInstances"
    ],
    "Effect": "Allow",
    "Resource": "*"
    }
    ]
    }


#Build

    virtualenv venv -p /usr/local/Cellar/python/2.7.10_2/
    source venv/bin/activate
    pip install -r requirements.txt
    

#Tested Systems

- Mac to a certian extent for testing only
- AWS Linux
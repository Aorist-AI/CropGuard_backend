import boto3
from botocore.exceptions import ClientError
from email_work.email_templates import send_verification_template
from aws_config import aws_config


def send(email, code):
    key = aws_config.config()
    # Replace sender@example.com with your "From" address.
    # This address must be verified with Amazon SES.
    sender = key['sender']

    # Replace recipient@example.com with a "To" address. If your account
    # is still in the sandbox, this address must be verified.
    recipient = email

    # Specify a configuration set. If you do not want to use a configuration
    # set, comment the following variable, and the
    # ConfigurationSetName=CONFIGURATION_SET argument below.
    # CONFIGURATION_SET = "ConfigSet"

    # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
    aws_region = "us-east-1"

    # The subject line for the email.
    subject = "Tamu Verification"

    # The email body for recipients with non-HTML email clients.
    body_text = f"Welcome to Tamu, your verification code is {code}"

    # The HTML body of the email.
    body_html = send_verification_template.html(code)

    # The character encoding for the email.
    charset = "UTF-8"

    # Create a new SES resource and specify a region.

    client = boto3.client('ses', aws_access_key_id=key['aws_access_key_id'],
                          aws_secret_access_key=key['aws_secret_access_key'],
                          region_name=aws_region)

    # Try to send the email.
    try:
        # Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    recipient,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': charset,
                        'Data': body_html,
                    },
                    'Text': {
                        'Charset': charset,
                        'Data': body_text,
                    },
                },
                'Subject': {
                    'Charset': charset,
                    'Data': subject,
                },
            },
            Source=sender,
            # If you are not using a configuration set, comment or delete the
            # following line
            # ConfigurationSetName=CONFIGURATION_SET,
        )
    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {'Message': 'Email not sent, kindly contact support.', "statusCode": 500}
    else:
        # print("Email sent! Message ID:"),
        # print(response['MessageId'])
        return {'Message': 'Email has been sent, use the code in the email as verification', "statusCode": 200}


# print(send('hassan.k.athumani@gmail.com','1234'))

FROM public.ecr.aws/lambda/python:3.12

# Install required Python libraries
RUN pip install langchain langchain_community boto3

# Copy your lambda function
COPY lambda_function.py .

# Set the CMD to your handler
CMD ["lambda_function.lambda_handler"]

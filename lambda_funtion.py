import json
import boto3


client=boto3.client(service_name='bedrock-runtime',
    region_name="us-east-1")

from langchain.prompts import ChatPromptTemplate
prompt=ChatPromptTemplate.from_messages([
    ("system","Based on the topic given by the user generate a 200 word blog"),
    ("user","{topic}")
])

from langchain.llms.bedrock import Bedrock
llm=Bedrock(model_id="meta.llama3-8b-instruct-v1:0",client=client)

blog_chain=prompt|llm

def blog_gen(topic:str):
  response=blog_chain.invoke({
      "topic":topic
  })

  return response


def lambda_handler(event,context):
  event=json.loads(event['body'])
  topic=event['input']

  blog=blog_gen(topic)

  return{
      "statusCode":200,
      "Blog":json.dumps(blog)
  }

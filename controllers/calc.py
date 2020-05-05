import json


def estimate_pi(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    print(event)

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

"""
import random
import math

def calc_pi(n):
  in_circle = 0
  total = 0

  for i in range(n):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)

    dist = math.sqrt((x**2) + (y**2))

    if (dist <= 1):
      in_circle += 1

    total += 1

  return 4 * in_circle/total

iterations = int(input("Cuantas veces quieres iterar? "))
print(calc_pi(iterations))
"""
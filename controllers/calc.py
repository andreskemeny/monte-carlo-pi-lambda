import json
import random


def estimate_pi(event, context):
  iterations = json.loads(event["body"])["iterations"]

  x_in_circle = []
  y_in_circle = []
  x_outside_circle = []
  y_outside_circle = []

  for i in range(iterations):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)

    dist = (x**2) + (y**2)

    if (dist <= 1):
      x_in_circle.append(x)
      y_in_circle.append(y)
    else:
      x_outside_circle.append(x)
      y_outside_circle.append(y)

  pi = 4 * len(x_in_circle)/((len(x_in_circle)) + len(x_outside_circle))

  body = {
    "x_in_circle": x_in_circle,
    "y_in_circle": y_in_circle,
    "x_outside_circle": x_outside_circle,
    "y_outside_circle": y_outside_circle,
    "pi": pi
  }

  response = {
    "statusCode": 200,
    "body": json.dumps(body)
  }

  return response


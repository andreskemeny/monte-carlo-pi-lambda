import json
import random
import sys


def estimate_pi(event, context):
  iterations = json.loads(event["body"])["iterations"]
  
  in_circle = 0
  total = 0
  coords_x_in_circle = []
  coords_y_in_circle = []
  coords_x_outside_circle = []
  coords_y_outside_circle = []

  for i in range(iterations):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)

    dist = (x**2) + (y**2)

    total_coords = len(coords_x_in_circle) + len(coords_x_outside_circle)

    if (dist <= 1):
      in_circle += 1
      if (total_coords < 10000):
        coords_x_in_circle.append(x)
        coords_y_in_circle.append(y)
    else:
      if (total_coords < 10000):
        coords_x_outside_circle.append(x)
        coords_y_outside_circle.append(y)
    
    total += 1

  pi = 4 * in_circle/total

  print(sys.getsizeof(coords_x_in_circle))
  print(sys.getsizeof(coords_y_in_circle))
  print(sys.getsizeof(coords_x_outside_circle))
  print(sys.getsizeof(coords_y_outside_circle))
  print(sys.getsizeof(pi))

  body = {
    "coords_x_in_circle": coords_x_in_circle,
    "coords_y_in_circle": coords_y_in_circle,
    "coords_x_outside_circle": coords_x_outside_circle,
    "coords_y_outside_circle": coords_y_outside_circle,
    "in_circle": in_circle,
    "pi": pi
  }

  response = {
    "statusCode": 200,
    "body": json.dumps(body),
    "headers": {
			"Content-Type": "application/json",
			"Access-Control-Allow-Origin": "*",
			"Access-Control-Allow-Credentials": True
		},
  }

  return response
  


from flask import Flask

app = Flask(__name__)


@app.route("/")
def health_check():
  return {
      "status": "healthy",
      "message": "Local K8s Microservice Pipeline is running smoothly!",
  }


@app.route("/api/v1/data")
def get_data():
  return {"data": [10, 20, 30, 40, 50], "environment": "local-sandbox"}


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)

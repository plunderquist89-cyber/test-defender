import boto3
from flask import Flask, jsonify

app = Flask(__name__)

# NOTE: test credentials for scan validation only
AWS_ACCESS_KEY_ID = "AKIA5FQ2XZ7KJ3MNP4QR"
AWS_SECRET_ACCESS_KEY = "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"

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name="eu-north-1",
)

s3 = session.client("s3")


@app.route("/buckets")
def list_buckets():
    resp = s3.list_buckets()
    return jsonify([b["Name"] for b in resp.get("Buckets", [])])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

# https://cloud.google.com/storage/docs/reference/libraries#client-libraries-install-python
# Imports the Google Cloud client library
import os
from google.cloud import storage
from myapp.cloud import upload_blob, download_blob
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)


@app.route("/test")
def hello_world_test():
    # Instantiates a client
    storage_client = storage.Client()

    buckets = storage_client.list_buckets()

    print('checking for project_id in env vars')
    project_id = os.getenv("PROJECT_ID", None)
    if not project_id:
        return 'TEST FAIL'

    # The name for the test bucket
    test_bucket_name = "%s-test" % project_id
    print(test_bucket_name)

    is_test_bucket_exist = False
    print('listing all buckets:')
    for bucket in buckets:
        if bucket.name == test_bucket_name:
            is_test_bucket_exist = True
            print('test bucket exists, %s' % test_bucket_name)
        print('\t%s' % bucket.name)

    if not is_test_bucket_exist:
        # Creates the new bucket
        bucket = storage_client.create_bucket(test_bucket_name)
        print("test bucket {} created.".format(bucket.name))

    upload_blob(test_bucket_name, 'hellworld.txt', 'helloworld.txt')
    download_blob(test_bucket_name, 'helloworld.txt', 'downloaded_blob.txt')
    with open('downloaded_blob.txt', 'r') as f:
        data = f.readline()
    assert data.startswith('hello world'), 'error data, %s' % data
    print(data)
    return "TEST OK"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

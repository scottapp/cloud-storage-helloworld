from google.cloud import storage
import os


def test_storage_client():
    storage_client = storage.Client()
    assert storage_client


def test_storage_bucket():
    storage_client = storage.Client()
    assert storage_client

    project_id = os.getenv("PROJECT_ID", None)
    print(project_id)
    assert project_id, 'error project id'

    test_bucket_name = "%s-test" % project_id

    try:
        bucket = storage_client.create_bucket(test_bucket_name)
    except Exception as e:
        print(e)

    bucket = storage_client.bucket(test_bucket_name)
    print('bucket name: %s' % bucket)
    assert bucket

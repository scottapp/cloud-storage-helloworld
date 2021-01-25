# cloud-storage-helloworld

## Stacks

- google cloud run
- google cloud storage
- python
- flask
- docker
- make tool

You need to setup a Google Cloud Run project and export the environment variables in order to run the code

```
export PROJECT_ID=YOUR_PROJECT_ID
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/credential
make build
make run 
```

Open a browser and go to 127.0.0.1:8080/test, a message should be displayed

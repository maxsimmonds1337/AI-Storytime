# AI-Storytime


# How to build

Code runs on GCP cloud run. Build and push the docker file, tagging it with your id etc

* docker build -t gcr.io/ai-storytime-387614/prompt-engine:v1.0.0 .

* docker push gcr.io/ai-storytime-387614/prompt-engine:v1.0.0

* gcloud run deploy prompt-engine --image gcr.io/ai-storytime-387614/prompt-engine:v1.0.0 --platform managed --region europe-west1

The above wasn't working but there was a lot of other errors, so it might work now. However, in the end I used a single command - gcloud run deploy --source .

Also, I had to use a specific version of python (3.10.10) the same as my local version. Remember to python freeze > requirements.txt!

## todo
[] user profile, so don't have to ask about the child each time
[] use the user profile to make images of the same person for each image, maybe seed the image to help
[] host on gcp some how
[] allow people to slightly edit the same story, this would mean having to pass the same story back I guess
[] be able to send different temps, so that the "imagination" can be adjusted
[] there's another prompt I can use (prompt chat) this will allow some more interacaction rather that sending back the old story for updates

docker run -it \
  -e PLUGIN_APP=hello-estabilis \
  -v ${PWD}:/usr/app \
  -w /usr/app \
  fbcbarbosa/heroku:latest

#!/bin/sh
cat >~/.netrc <<EOF
machine git.heroku.com
  login ${PLUGIN_LOGIN}
  password ${PLUGIN_TOKEN}
EOF
git push -f https://git.heroku.com/${PLUGIN_APP}.git master

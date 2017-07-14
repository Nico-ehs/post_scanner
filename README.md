# Post Scanner

This rails app that creates and charts metadata on blog comments. This is a early stage work in progress and I'm still testing out some basic features. The app is being run at:

- https://post-scanner-243653.herokuapp.com/. 

I'm using a few posts from:

- https://twigserial.wordpress.com/ 

For the chart display it uses the chartkick gem and Highcharts. For web-scraping it uses separate python code in the "Post Scanner" folder.

## Setup CMD Line

```
gem install rails
bundle install
sudo service postgresql start
psql -c "create user username with password 'password' SUPERUSER"
psql -c "create database myapp_development"
rake db:migrate
rake db:seed
rails server -b $IP -p $PORT
```
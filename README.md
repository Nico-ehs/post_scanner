# Post Scanner

This rails app that creates and charts metadata on blog comments. This is a early stage work in progress and I'm still testing out some basic features. The app is being run at:

- https://post-scanner-243653.herokuapp.com/.

I'm using a few posts from the blogs:

- [Twig](https://twigserial.wordpress.com/)
- [Armed and Dangerous](http://esr.ibiblio.org/)

For the chart display it uses the chartkick gem and Highcharts. For web-scraping it uses separate python code in the "Post Scanner" folder.

## Some of what it tracks:

Tracks *reader enthusiasm*, by calculating the comment rate of posts within the first 10 days, broken down by blog:

![Post-Scanner-Comment-Rate](https://raw.githubusercontent.com/Nico-ehs/post_scanner/master/img/Post-Scanner-Comment-Rate.PNG)

Looks at reader engagement vs. popularity, by measuring the ratio of post-lengths to comments

![Post-Scanner-Ratio](https://raw.githubusercontent.com/Nico-ehs/post_scanner/master/img/Post-Scanner-Ratio.PNG)

Identifies what content is being engaged with, and by whom, by tracking comment volume for individual posts, and individual users:

![Post-Scanner-Individual-Posts](https://raw.githubusercontent.com/Nico-ehs/post_scanner/master/img/Post-Scanner-Individual-Posts.PNG)


![Post-Scanner-10-comments](https://raw.githubusercontent.com/Nico-ehs/post_scanner/master/img/Post-Scanner-10-comments.PNG)




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

# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ name: 'Chicago' }, { name: 'Copenhagen' }])
#   Mayor.create(name: 'Emanuel', city: cities.first)
# Site.create(url: "twig test", time: Time.now)
data=eval(File.read("post_test1.html"))
data.each do |el|
    Post.create(html_id: el[0], title: el[1], author: el[2], time: el[3], text: el[4])
end

print "test1"
data=eval(File.read("comment_test1.html"))
data.each do |el|
    Comment.create(html_id: el[0], author: el[1], time: DateTime.parse(el[2]), depth: el[3], text: el[4], post_id: 1)
end


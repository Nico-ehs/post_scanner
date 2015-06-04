class WebscannerController < ApplicationController
    
    
    def run_scan(scan_input)
        File.write("scan_input.txt", scan_input)
        system("python webscanner.py")
    end
    
    def load_data
        posts=eval(File.read("post_test.html"))
        posts.each do |el|
            Post.create(html_id: el[0], title: el[1], author: el[2], time: el[3], text: el[4])
        end
        comments=eval(File.read("comments_test.html"))
        comments.each do |el|
            Comment.create(html_id: el[0], author: el[1], time: el[2], depth: el[3], text: el[4])
        end
    end
end

class WebscannerController < ApplicationController
    
    
    def show
        @sites=Site.all.size
        @posts=Post.all.size
        @comments=Comment.all.count
        @authors=Author.all.count
    end
    
    def scan_test
        run_scan
        redirect_to "/webscanner"
    end
    
    def load_test
        load_data
        redirect_to "/webscanner"
    end
    
    def run_scan
        # Dir.chdir("Post Scanner") do
        #     system('python3 "post scanner.py"')
        #     system('python3 "parser.py"') 
        # end
        # File.write("scan_input.txt", scan_input)
        # system("python webscanner.py")
    end
    
    def load_data
        sitelist=eval(File.read("Post Scanner//sitelist.txt"))
        sitelist.each do |site|
            if Site.find_by_sitename(site)==nil
                Site.create(sitename: site)
            end
	        posts=eval(File.read("Post Scanner//site data//#{site}//posts.txt"))
	        posts.each do |el|
	            unless el[2]==""
	    	        Post.create(site_id: Site.find_by_sitename(el[0]).id, html_id: el[1], title: el[2], post_author_name: el[3],
	    	        post_time: el[4], text: el[5], post_size: el[5].size)
	    	    end
	        end
	        comments=eval(File.read("Post Scanner//site data//#{site}//comments.txt"))
	        comments.each do |el|
	            comment_post_id=Post.where("site_id = #{Site.find_by_sitename(el[0]).id} AND title = '#{el[1]}'")[0].id
		        Comment.create(post_id: comment_post_id, html_id: el[2], comment_author_name: el[3][0..-3], comment_time: el[4],
		        depth: el[5], text: el[6].each_char.select{|c| c.bytes.count < 4 }.join(''), comment_size: el[6].size)
            end
        end
        MetadataCreationController.generate_authors
        # posts=eval(File.read("post_test.html"))
        # posts.each do |el|
        #     Post.create(html_id: el[0], title: el[1], author: el[2], time: el[3], text: el[4])
        # end
        # comments=eval(File.read("comments_test.html"))
        # comments.each do |el|
        #     Comment.create(html_id: el[2], author: el[3], time: el[4], depth: el[5], text: el[6])
        # end
    end
end

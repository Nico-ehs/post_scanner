class PostsController < ApplicationController
    impressionist
    
    def show
        @post=Post.find(params[:id]).sort_by(&:title)  
    end
    
    def index
        @posts=Post.all
    end
    
    
    # def date_filter
    #   Post.where(:post_time => date_start.beginning_of_day..date_end.end_of_day) 
    # end
    
    
end


# <h2>Individual Posts</h2>
#   <% @site.posts.each do |el| %>
#       <h3>
#       <%= link_to "#{el.title}", post_url(el) %>
#       <%= " Comments: #{el.comments.count}  " %>
      
#       </h3>
#   <% end %>
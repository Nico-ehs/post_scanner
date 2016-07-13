class PostsController < ApplicationController
    impressionist
    
    def show
        @post=Post.find(params[:id])
    end
    
    def index
        @posts=Post.all
    end
    
    
    # def date_filter
    #   Post.where(:post_time => date_start.beginning_of_day..date_end.end_of_day) 
    # end
    
    
end

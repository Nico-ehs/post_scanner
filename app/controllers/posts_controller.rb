class PostsController < ApplicationController
    impressionist
    
    def show
        @post=Post.find(params[:id]).sort_by(&:title)  
    end
    
    def index
        @posts=Post.all
    end
end


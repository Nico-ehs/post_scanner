class VeiwsController < ApplicationController
    
    def show
        @sites=Site.all
        @posts=Post.all
    end
end

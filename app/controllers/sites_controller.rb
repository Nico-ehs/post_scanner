class SitesController < ApplicationController
    impressionist
    
    def show
        @site=Site.find(params[:id])
        @posts=@site.posts
    end
    
    def index
        @sites=Site.all
    end
end

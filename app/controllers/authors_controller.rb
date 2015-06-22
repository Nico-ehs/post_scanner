class AuthorsController < ApplicationController
    def show
        @author=Author.find(params[:id])
        @comments=@author.comments
        
    end
    
    def index
        @authors=Author.all
    end
end

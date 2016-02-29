class CommentsController < ApplicationController
    impressionist
    
    def show
        @comment=Comment.find(params[:id])
    end
end

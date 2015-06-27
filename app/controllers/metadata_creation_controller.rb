class MetadataCreationController < ApplicationController
    
    def self.generate_authors
        Post.all.each do |el|
            if Author.find_by_name(el.post_author_name)==nil
                Author.create(name: el.post_author_name)
            end
        end
        Comment.all.each do |el|
            if Author.find_by_name(el.comment_author_name)==nil
                Author.create(name: el.comment_author_name)
            end
        end
        get_author_ids
    end
    
    def self.get_author_ids
        Post.all.each do |el|
            if Author.find_by_name(el.post_author_name)!=nil
                el.author_id=Author.find_by_name(el.post_author_name).id
            end
        end
        Comment.all.each do |el|
            if Author.find_by_name(el.comment_author_name)!=nil
                el.author_id=Author.find_by_name(el.comment_author_name).id
            end
        end
    end
    
    
end

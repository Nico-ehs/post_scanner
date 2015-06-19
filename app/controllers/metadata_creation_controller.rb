class MetadataCreationController < ApplicationController
    
    def self.generate_authors
        Post.all.each do |el|
            if Author.find_by_name(el.author)==nil
                Author.create(name: el.author)
            end
        end
        Comment.all.each do |el|
            if Author.find_by_name(el.author)==nil
                Author.create(name: el.author)
            end
        end
        get_author_ids
    end
    
    def self.get_author_ids
        Post.all.each do |el|
            if Author.find_by_name(el.author)!=nil
                el.author_id=Author.find_by_name(el.author).id
            end
        end
        Comment.all.each do |el|
            if Author.find_by_name(el.author)!=nil
                el.author_id=Author.find_by_name(el.author).id
            end
        end
    end
    
    
end

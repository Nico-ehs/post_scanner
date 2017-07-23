class MetadataCreationController < ApplicationController
    
    def self.generate_authors
        # Creates Authors from the author names of posts and comments.
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
        # Adds an author_id for author lookup to posts and comments.
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
    
    def self.get_days_after
        # Adds a days_after element to comments mesuring how long after the post the comment was made.
        Comment.all.each do |el|
             el.days_after=((el.comment_time.to_date)-(el.post.post_time.to_date)).to_i
             el.save
        end
        5
    end
    
end

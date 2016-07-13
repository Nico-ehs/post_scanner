class Post < ActiveRecord::Base
    is_impressionable
    belongs_to :site
    has_many :comments
    
    def test1
        comments.size
    end
    
    def comment_rate1
       comments.group_by_day(:comment_time).count.map {|k, v| [((k.to_datetime().to_date)-post_time.to_date).to_i, v] }
    end

end

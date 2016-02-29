class Post < ActiveRecord::Base
    is_impressionable
    belongs_to :site
    has_many :comments
    

end

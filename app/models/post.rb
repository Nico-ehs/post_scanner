class Post < ActiveRecord::Base
    # belongs_to :site
    has_many :comments
end

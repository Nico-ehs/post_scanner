class Site < ActiveRecord::Base
    is_impressionable
    has_many :posts
    has_many :comments, through: :posts
    
    def name
        self.sitename
    end
end

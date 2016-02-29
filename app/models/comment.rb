class Comment < ActiveRecord::Base
    is_impressionable
    belongs_to :post
    belongs_to :author
    # belongs_to :site, through: :post
end

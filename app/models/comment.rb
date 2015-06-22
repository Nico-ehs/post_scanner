class Comment < ActiveRecord::Base
    belongs_to :post
    belongs_to :author
    # belongs_to :site, through: :post
end

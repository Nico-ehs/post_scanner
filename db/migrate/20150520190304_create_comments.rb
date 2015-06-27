class CreateComments < ActiveRecord::Migration
  def change
    create_table :comments do |t|
      t.integer :post_id
      t.text :text
      t.string :comment_author_name
      t.integer :author_id
      t.datetime :comment_time
      t.integer :html_id
      t.string :depth
      t.integer :comment_size
      
      
      t.timestamps
    end
  end
end

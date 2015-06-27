class CreatePosts < ActiveRecord::Migration
  def change
    create_table :posts do |t|
      t.integer :site_id
      t.integer :html_id
      t.string :title
      t.string :post_author_name
      t.integer :author_id
      t.datetime :post_time
      t.text :text
      t.integer :post_size


      t.timestamps
    end
  end
end

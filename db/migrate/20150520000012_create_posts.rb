class CreatePosts < ActiveRecord::Migration
  def change
    create_table :posts do |t|
      t.integer :site_id
      t.integer :html_id
      t.string :title
      t.string :author_name
      t.integer :author_id
      t.time :time
      t.text :text


      t.timestamps
    end
  end
end

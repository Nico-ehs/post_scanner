class CreatePosts < ActiveRecord::Migration
  def change
    create_table :posts do |t|
      t.integer :html_id
      t.string :title
      t.string :author
      t.time :time
      t.text :text


      t.timestamps
    end
  end
end

class CreateComments < ActiveRecord::Migration
  def change
    create_table :comments do |t|
      t.integer :post_id
      t.string :text
      t.string :author
      t.datetime :time
      t.integer :html_id
      t.string :depth

      t.timestamps
    end
  end
end

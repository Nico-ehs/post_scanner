# encoding: UTF-8
# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20150520190330) do

  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "authors", force: true do |t|
    t.string   "name"
    t.integer  "site_id"
    t.datetime "created_at"
    t.datetime "updated_at"
  end

  create_table "comments", force: true do |t|
    t.integer  "post_id"
    t.text     "text"
    t.string   "comment_author_name"
    t.integer  "author_id"
    t.datetime "comment_time"
    t.integer  "html_id"
    t.string   "depth"
    t.integer  "comment_size"
    t.datetime "created_at"
    t.datetime "updated_at"
  end

  create_table "posts", force: true do |t|
    t.integer  "site_id"
    t.integer  "html_id"
    t.string   "title"
    t.string   "post_author_name"
    t.integer  "author_id"
    t.datetime "post_time"
    t.text     "text"
    t.integer  "post_size"
    t.datetime "created_at"
    t.datetime "updated_at"
  end

  create_table "sites", force: true do |t|
    t.string   "sitename"
    t.datetime "created_at"
    t.datetime "updated_at"
  end

end

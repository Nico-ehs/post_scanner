class ApplicationController < ActionController::Base
  # Prevent CSRF attacks by raising an exception.
  # For APIs, you may want to use :null_session instead.
  # protect_from_forgery with: :exception
  
  def remove_empty(table)
    # removes entries in table with a 0 value
    table.select {|k,v| v!=0 }
  end
  helper_method :remove_empty
  
end

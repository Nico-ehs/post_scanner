class ApplicationController < ActionController::Base
  # Prevent CSRF attacks by raising an exception.
  # For APIs, you may want to use :null_session instead.
  # protect_from_forgery with: :exception
  
  # def key_map(hash)
    
  # end
  
  def remove_empty(table)
    table.select {|k,v| v!=0 }
  end
  helper_method :remove_empty
  
  
  def format_name(table)
    true
  end
  helper_method :format_name
  
  def format_day(table)
    r={}
    table.each_key do |k|
      puts "test"
      r["#{k}"[0..5]]=table[k]
    end
    remove_empty(r)
  end
  helper_method :format_day
  
  def format_month(date)
    r={}
    table.each_key do |k|
      puts "test"
      r["#{k}"[0..5]]=table[k]
    end
    remove_empty(r)
  end
  helper_method :format_month
end




sitelist=eval(File.read(""))
sitelist.each do |site|
	posts=eval(File.read(""))
	posts.each do |post|
		Post.create()
	end
	comments=eval(File.read(""))
	comments.each do |comment|
		Comment.create()
	end
end






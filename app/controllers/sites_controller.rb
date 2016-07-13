class SitesController < ApplicationController
    impressionist
    
    def show
        @site=Site.find(params[:id])
        @posts=@site.posts
    end
    
    def index
        @sites=Site.all
        site_rate=Hash.new(0)
            (0..9).each {|n| site_rate[n]=0 }
        @chart1=@sites.map { |site| {name: site.sitename, data: first_10_days(site.comments.group("days_after").count)}}
        # @test=Post.all.map { |el| {name: el.title, data: Comment.group("author_id").where("post_id = #{1}").count}}
        # @test=Comment.first.days_after.class
        @test=@chart1
        @ratios=@sites.map { |site| [site.sitename, char_ratio(site)]}
        # @comment_rate=[]
        # @sites.each do |site|
        #     site_rate=Hash.new(0)
        #     (0..9).each {|n| site_rate[n]=0 }
        #     site.posts.each do |el|
        #         post_rate=el.comment_rate1
        #         post_rate.each {|key, count| site_rate[key] += count}
        #     end
        #     @comment_rate+=[site_rate]
        # end
    end
    
    def first_10_days(data)
        site_rate=Hash.new(0)
        (0..9).each {|n| site_rate[n]=0 }
        site_rate.each {|key, count| (site_rate[key] += data[key]) if data.has_key?(key)}
        site_rate.each {|key, value| site_rate[key]=value.to_i}
        site_rate
    end
    
    def char_ratio(site)
        site.comments.sum('comment_size')/(1.0*site.posts.sum('post_size'))
    end
    
end

# Comment.where("post_id = #{el.id}").group(:days_after).count

# Comment.group("days_after").where("post_id = #{1}").count.to_s[0..200]
# Comment.group("post_id").count.to_s[0..200]
# Comment.where("day_after < ? AND day > ?").group("days_after").count.to_s[0..200]
# Comment.where("days_after = 1").to_s[0..200]
# a.comments.group("post_id").count.to_s[0..600]
# Comment.group("days_after").count.to_s[0..200]

# (site_rate.each {|key, count| site_rate[key] +=Comment.group("days_after").count[key]}).to_s
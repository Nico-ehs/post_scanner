class SitesController < ApplicationController
    impressionist
    
    def show
        @site=Site.find(params[:id])
        @posts=@site.posts.sort_by(&:title)
    end
    
    def index
        @sites=Site.all
        @chart1=@sites.map { |site| {name: site.sitename, data: first_10_days(site.comments.group("days_after").count)}}
        @ratios=@sites.map { |site| [site.sitename, char_ratio(site)]}
    end
    
    def first_10_days(data)
        # 
        site_rate=Hash.new(0)
        (0..9).each {|n| site_rate[n]=0 }
        site_rate.each {|key, count| (site_rate[key] += data[key]) if data.has_key?(key)}
        site_rate.each {|key, value| site_rate[key]=value.to_i}
        site_rate
    end
    
    def char_ratio(site)
        # Returns the comparative ratio of the length of text of all the comment to the lenge of the posts.
        site.comments.sum('comment_size')/(1.0*site.posts.sum('post_size'))
    end
    
end

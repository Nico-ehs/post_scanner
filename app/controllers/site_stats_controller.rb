class SiteStatsController < ApplicationController
    def overview
        @sites=Site.all
    end
end

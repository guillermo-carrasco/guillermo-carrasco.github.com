require 'html/proofer'

task :test do
  sh "bundle exec jekyll build"
  HTML::Proofer.new("./_site", {
		:href_ignore => [
			"#",
            "\Ahttp://t.co",
            # Linkedin is bloking travis-ci
            "*linkedin*"
        ],
        # Ignore Survey URL
        :url_ignore => ["https://t.co/tTz4qaCSwQ"]
    }).run
end

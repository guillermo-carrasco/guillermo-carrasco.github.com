require 'html/proofer'

task :test do
  sh "bundle exec jekyll build"
  HTML::Proofer.new("./_site", {
		:href_ignore => [
			"#"
        ],
        # Ignore Survey and linkedin URLs
        :url_ignore => [
            "https://t.co/tTz4qaCSwQ",
            "https://www.linkedin.com/in/guillermocarrasco"
        ]
    }).run
end

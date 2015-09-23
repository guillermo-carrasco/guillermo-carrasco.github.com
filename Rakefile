require 'html/proofer'

task :test do
  sh "bundle exec jekyll build"
  HTML::Proofer.new("./_site", {
		:href_ignore => [
			"#"
        ],
        :url_ignore => [
            "\Ahttps\?://t.co"
        ]
        }).run
end

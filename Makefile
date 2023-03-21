clean:
	rm -rf Gemfile.lock _site .jekyll-metadata

install-local:
	bundle install

run-local: install
	bundle exec jekyll serve --host 0.0.0.0 --drafts --incremental --config _config.yml,_config_devel.yml

run-docker:
	docker run --rm \
	-p 4000:4000 \
	-v $(CURDIR):/srv/jekyll \
	-it \
	jekyll/jekyll:pages \
	bundle exec jekyll serve --host 0.0.0.0 --drafts --incremental --config _config.yml,_config_devel.yml

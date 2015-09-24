# Mussol blog

[![Build Status](https://travis-ci.org/guillermo-carrasco/guillermo-carrasco.github.com.svg?branch=master)](https://travis-ci.org/guillermo-carrasco/guillermo-carrasco.github.com)

This repository contains the whole source code for my blog, including images,
code and more.

Go to www.mussol.org to visit it!

To run it locally, you'll need to:

1. Clone the repository: `git clone https://github.com/guillermo-carrasco/guillermo-carrasco.github.com.git`
2. Install dependencies with `bundle exec jekyll build`
3. Run the project using the development configuration (just for the base url to work:)
`jekyll serve --config _config.yml,_config_devel.yml --drafts`

## Structure
The project follows the standard Jekyll structure. I also added a directory called
`assets` that contains images and other media data.

## Writing a blog post
Just use as a template any of the existing ones. The important thing to know is
that the filename will be used to construct the final URL, i.e if the blog post is
named `2015-10-16-my-awesome-post.md`, the final url for the blog post will be
`<base_url>/2015/10/16/my-awesome-post`. It's a nice way of having organized URLs.

### Writing drafts
Any blog post in the `_drafts` directory will not be published in the built web site,
so if desired, you can work on your blog posts there

### Theme
The theme used for this blog is a slight modification of [jekyll-qck-theme][https://github.com/qckanemoto/jekyll-qck-theme].

All attributions on style to qckanemoto, I just added some bits here and there. 

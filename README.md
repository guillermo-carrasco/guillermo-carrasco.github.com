# Mussol blog
This repository contains the whole source code for my blog, including images,
code and more.

To run it locally, you'll need to:

1. Clone the repository: `git clone https://github.com/guillermo-carrasco/guillermo-carrasco.github.com.git`
2. [Install Jekyll][install-jekyll]
3. Run the project using the development configuration (just for the base url to work:)
`jekyll serve --config _config.yml,_config_devel.yml`

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

[install-jekyll]: https://help.github.com/articles/using-jekyll-with-pages/

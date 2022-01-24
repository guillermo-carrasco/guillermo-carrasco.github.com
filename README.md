# Guillermo Carrasco - Personal blog


This repository contains the whole source code for my blog, including images,
code and more.

Go to www.guillermoch.com to visit it!

To run it locally, you'll need to:

1. Clone the repository: `git clone https://github.com/guillermo-carrasco/guillermo-carrasco.github.com.git`
2. Run `make run-blog`

_(docker is required)_

## Structure
The project follows the standard Jekyll structure. I also added a directory called
`assets` that contains images and other media data.

## Writing a blog post
Just use as a template any of the existing ones. The important thing to know is
that the filename will be used to construct the final URL, i.e if the blog post is
named `2015-10-16-my-new-post.md`, the final url for the blog post will be
`<base_url>/2015/10/16/my-new-post`. It's a nice way of having organized URLs.

### Writing drafts
Any blog post in the `_drafts` directory will not be published in the built website,
so if desired, you can work on your blog posts there, commit them and they will _not_ be visible.

### Theme
The theme used for this blog is a slight modification of [accent](https://github.com/bk2dcradle/accent).

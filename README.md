# Commonplace journal

## Motivation

Learn! This site is my playground and where I gather ideas.

## Log

### 22-10-2024

What it entails

- Auto-generation of the RSS feed upon pushing to main
  - I tried using the [PyRSS2Gen](https://pypi.org/project/PyRSS2Gen/) library first, but I wasn't familiar enough with its underlying code to extend it just yet, so I ended up building an XML tree element by element, using Python's built-in [ElementTree API](https://docs.python.org/3/library/xml.etree.elementtree.html)
- Added meta tags to <head> of my posts
  - I read about various protocols for metadata design (so intriguing) and picked [OpenGraph](https://ogp.me/) for storing information on article published and updated dates
- Included `pubDate`, `lastBuildDate` and `guid` that's automatically generated using each post's filepath
  - They follow RSS 2.0's specification based on the [RSS Advisory Board](https://www.rssboard.org/rss-specification) (love that site design, so ancient)

Up next

- The RSS feed gets updated with every push to main now, so I feel more confident in continuing writing posts now; it also looks so good on certain RSS feed readers, I'm happy
- Clean up my Python code and the site layout (e.g. replace "Return to home" <a> links in each post with a navigation bar, include post publication and update dates in my webpages and index)
- Look into why the tags and posts don't work on mobile

### 14-10-2024

What it entails

- Cleaned up home page, posts and tags
- Replaced "Show all posts" button with the ability to deselect tags and unfilter posts

Resources

- [search.gov](https://search.gov/indexing/metadata.html#tags--keywords) introduced me to standard, OpenGraph and DublinCore fields for metadata design; I'm intrigued

### 06-10-2024

What it entails

- Tag-navigation using JavaScript and buttons :) my first time properly learning JS syntax + async/await 
- GitHub workflows set up to run a Python file that generates metadata of my posts, upon pushing to main

Resources

- [javascript.info](https://javascript.info) for JS fundamentals and data types
- [Claude](https://claude.ai) - great for troubleshooting my yaml files

Up next

- Auto-generation of the RSS feed upon pushing to main
- Ability to deselect buttons and unfilter posts
- Ensuring the tags and posts work on mobile

### 28-09-2024

What it entails

- Vanilla HTML hosted on Cloudflare Pages
- A styles sheet where I had fun changing link colours when I hover above them + learning about flex containers and viewports
- RSS feed, currently manually written

Resources

- [Flexbox Froggy](https://flexboxfroggy.com) for learning flex containers

Up next

- Tag-navigation system, because I don't want to cram all my writing into select few pages
- Auto-generation of post metadata and the RSS feed upon pushing to main

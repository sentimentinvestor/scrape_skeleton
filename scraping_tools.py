def scrape(target):
    posts = []

    # do some scraping with the target

    # the fields below are required, but feel free to add any additional fields
    post = {
        "id": "ensure this is unique across the website",
        "timestamp": "the upload time in time since epoch of the content",
        "content": "the actual content"
    }

    posts.append(post)

    return posts
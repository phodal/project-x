from xunta.articles import models
from xunta.utils import slugify


class Article():
    def __init__(self, title=None, description=None, tag=None, content=None, author=None, slug=None):
        self.slug = slug
        self.author = author
        self.content = content
        self.tag = tag
        self.title = title
        self.description = description
        self.id = None

    def save(self):
        slug = self.slug
        if not self.slug:
            print "no function", self.title
            slug = slugify(self.title)

        articles = models.Article(title=self.title, description=self.description,
                                  content=self.content, tag=self.tag, author=self.author, slug=slug)
        articles.save()
        print "new articles id = %s " % articles.id
        self.id = articles.id
        return self.id


    def get_all_articles(self):
        results = models.Article.objects()
        print results
        return results


    def get_article_by_slug(self, slug):
        results = models.Article.objects.get(slug=slug)
        print results
        return results
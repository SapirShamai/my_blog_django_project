
class BlogMethods:
    @staticmethod
    def list_blog_posts_html(posts):
        """adding html to the posts list"""

        posts_titles = f"""
        <h1>TITLES:</h1>
        <ul>
        {''.join(["<li>" + post.title + "</li>" for post in posts])}
        </ul>
        """
        return posts_titles

    @staticmethod
    def get_post_from_user():
        """gets all the post info from the user"""

        title = input('choose your title: ')
        content = input('enter post content: ')
        response = {'title': title, 'content': content}
        return response

    @staticmethod
    def get_title():
        """gets a new title from the user"""

        new_title = input('Please enter the new title: ')
        return new_title

    @staticmethod
    def get_content():
        """gets a new content from the user"""

        new_content = input("Please enter the new content: ")
        return new_content



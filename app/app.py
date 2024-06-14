from fastapi import FastAPI, HTTPException, Request
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.future import select
from database import get_session, engine, Base
import logging
from pydantic import BaseModel

logging.basicConfig(filename='app.log', level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()

blog_posts = []

class BlogPost(BaseModel):
    id: int
    title: str
    content: str

@app.post('/blog')
async def create_blog_post(post: BlogPost):
    try:
        blog_posts.append(post)
        logging.warning(f"new post created: {post}")
        return {'status': 'success'}
    except Exception as e:
        logging.error(f"error creating post: {str(e)}")
        raise HTTPException(status_code=500, detail="internal server error")

@app.get('/blog')
async def get_blog_posts():
    return {'posts': [blog.dict() for blog in blog_posts]}

@app.get('/blog/{id}')
async def get_blog_post(id: int):
    for post in blog_posts:
        if post.id == id:
            return {'post': post}
    logging.warning(f"post with {id} not found")
    raise HTTPException(status_code=404, detail="post not found")

@app.delete('/blog/{id}')
async def delete_blog_post(id: int):
    for post in blog_posts:
        if post.id == id:
            blog_posts.remove(post)
            logging.warning(f"post with {id} deleted")
            return {'status': 'success'}
    logging.warning(f"post with {id} not found")
    raise HTTPException(status_code=404, detail="post not found")

@app.put('/blog/{id}')
async def update_blog_post(id: int, post: BlogPost):
    try:
        for existing_post in blog_posts:
            if existing_post.id == id:
                existing_post.title = post.title
                existing_post.content = post.content
                logging.warning(f"post with {id} updated")
                return {'status': 'success'}
        logging.warning(f"post with {id} not found")
        raise HTTPException(status_code=404, detail="post not found")
    except Exception as e:
        logging.error(f"error updating post with {id}: {str(e)}")
        raise HTTPException(status_code=500, detail="internal server error")

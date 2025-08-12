# Blog Post Management

## Features
- List all posts (`/posts/`)
- View single post (`/posts/<id>/`)
- Create new post (`/posts/new/`) — authenticated users only
- Edit post (`/posts/<id>/edit/`) — author only
- Delete post (`/posts/<id>/delete/`) — author only

## Permissions
- Anyone can view posts.
- Only logged-in users can create.
- Only the post’s author can update or delete.

## Files Updated
- `blog/models.py`
- `blog/forms.py`
- `blog/views.py`
- `blog/urls.py`
- Templates in `blog/templates/blog/`

# blog/views.py
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Post, Tag
from .forms import PostForm
from urllib.parse import urlparse, parse_qs
from django.urls import reverse_lazy

# 게시글 목록
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-id'] # 최신순

    # 목록에 유튜브 썸네일을 출력하는 함수
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = context['posts']

        # 각 post에 youtube_thumbnail_url 추가
        for post in posts:
            post.youtube_thumbnail_url = self.get_thumbnail_url(post.link)

        return context

    def get_thumbnail_url(self, link):
        try:
            parsed_url = urlparse(link)
            query = parse_qs(parsed_url.query)
            video_id = query.get('v', [None])[0]
            if video_id:
                return f"https://img.youtube.com/vi/{video_id}/0.jpg"
            return None
        except Exception:
            return None

# 게시글 글 내용
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    # 복잡한 유튜브 링크를 iframe에 가지고 오는 것은 불가능.
    # 사용자가 입력한 유튜브 링크 뒤의 id를 가져와 iframe에 적용
    # 복잡한 유튜브 링크에서 id를 추출하는 함수
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        video_id = self.extract_video_id(post.link)
        context['youtube_embed_url'] = f"https://www.youtube.com/embed/{video_id}" if video_id else None
        return context

# 추출한 아이디를 iframe 코드에 넣는 함수
    def extract_video_id(self, link):
        try:
            parsed_url = urlparse(link)
            query = parse_qs(parsed_url.query)
            video_id = query.get('v', [None])[0]
            return video_id
        except Exception:
            return None

# 게시글 수정
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_update.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        tags = form.cleaned_data['tag_input']
        self.object.tags.clear()
        for tag_name in tags:
            tag_obj, created = Tag.objects.get_or_create(name=tag_name.lstrip('#'))
            self.object.tags.add(tag_obj)
        return response

    def get_success_url(self):
        return self.object.get_absolute_url()

# 게시글 삭제
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView,View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostCreateForm,PostUpdateForm
from django.contrib import messages
from django.urls import reverse_lazy
from accounts.models import CustomUser
from .forms import ProfileForm 


class PostCreateView(LoginRequiredMixin, CreateView): #モデルオブジェクト作成クラス
    template_name = 'post/create.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('post:mypost')
    
    def form_valid(self, form):
        # request.userが一つのセットでAuthenticationMiddlewareでセットされている。
        form.instance.owner_id = self.request.user.id
        messages.success(self.request, '投稿が完了しました')
        return super(PostCreateView, self).form_valid(form)
        
    def form_invalid(self, form):
        messages.warning(self.request, '投稿が失敗しました')
        return redirect('post:create')

class PostListView(LoginRequiredMixin,ListView):# #モデルオブジェクトの一覧を表示する
    template_name ='post/postlist.html'
    model = Post
    # paginate_by =5 様子見 テンプレート側を消すのをわすれないで

    def get_queryset(self):
        return Post.objects.all()


class PostUpdateView(LoginRequiredMixin, UpdateView): 
    model = Post
    form_class = PostUpdateForm
    template_name = 'post/update.html'
    success_url = reverse_lazy('post:mypost')


    def form_valid(self, form):
        messages.success(self.request, '更新が完了しました')
        return super(PostUpdateView, self).form_valid(form)
        
    def get_success_url(self):
        return reverse_lazy('post:update', kwargs={'pk': self.object.id})  
        
    def form_invalid(self, form):
        messages.warning(self.request, '更新が失敗しました')
        return reverse_lazy('post:update', kwargs={'pk': self.object.id})
#見直し

class PostDeleteView(LoginRequiredMixin,DeleteView):# #モデルオブジェクトの削除を表示する
    model = Post
    template_name = 'post/delete.html'
    success_url =reverse_lazy('post:mypost')
    success_message ="投稿は削除しました。"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PostDeleteView, self).delete(request, *args, **kwargs)


class MyPostsView(LoginRequiredMixin, ListView): # 自分の投稿を見れるようにする
    
    template_name = 'post/mypost.html'
    model = Post

    # Postsテーブルのowner_idが自分自身の全データを取得するメソッド定義
    def get_queryset(self):  # 自分の投稿オブジェクトを返す。
        return Post.objects.filter(owner_id=self.request.user)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Postsテーブルの自分の投稿数をmy_posts_countへ格納
        context['my_posts_count'] = Post.objects.filter(owner_id=self.request.user).count()
        context['data']=CustomUser.objects.filter(email=self.request.user)
        return context







class ProfileEditView(LoginRequiredMixin, UpdateView): # ユーザー情報の編集
    template_name = 'post/edit_profile.html'
    model = CustomUser
    form_class = ProfileForm
    success_url = '/post/mypost/'
    
    def get_object(self):
        return self.request.user







class UserListView(LoginRequiredMixin, ListView): 
    template_name = 'post/userlist.html'
    model =CustomUser
    
    def get_queryset(self):
        
        return CustomUser.objects.all()        




def profile(request):
    data = CustomUser.objects.filter(email=request.user)
    params = {
        'title':'自己紹介',
        'data': data,
    }
    return render(request, 'post/profile.html',params)




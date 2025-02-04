class TimelineApp {
    constructor() {
        this.commentsModal = new bootstrap.Modal(document.getElementById('commentsModal'));
        this.postsContainer = document.getElementById('posts-container');
        this.users = [];
        if (!this.postsContainer) {
            console.error('Sem Posts!');
            return;
        }
        this.init();
    }

    async init() {
        try {
            await this.usuario();
            await this.posts();
        } catch (error) {
            console.error('Erro ao iniciar:', error);
        }
    }

    async usuario() {
        try {
            const response = await fetch('https://jsonplaceholder.typicode.com/users');
            this.users = await response.json();
        } catch (error) {
            this.users = [];
        }
    }

    async posts() {
        try {
            const response = await fetch('https://jsonplaceholder.typicode.com/posts');
            const posts = await response.json();
            
            if (Array.isArray(posts)) {
                for (const post of posts) {
                    const author = this.users.find(user => user.id === post.userId) || 
                                 await this.author(post.userId);
                    this.createPostElement(post, author);
                }
            } else {
                console.error('Isso não é um post', posts);
            }
        } catch (error) {
            console.error('Erro ao carregar posts:', error);
        }

    }

    async author(userId) {
        try {
            const response = await fetch(`https://jsonplaceholder.typicode.com/users/${userId}`);
            const author = await response.json();
            return author;
        } catch (error) {
            return null;
        }
    }

    async comments(postId) {
        try {
            const response = await fetch(`https://jsonplaceholder.typicode.com/posts/${postId}/comments`);
            return await response.json();
        } catch (error) {
            return [];
        }
    }

    createPostElement(post, author) {
        if (!this.postsContainer || !post || !author) {
            return;
        }

        const article = document.createElement('article');
        article.className = 'post';
        
        article.innerHTML = `
            <div class="author-info">
                <strong>${author.name}</strong>
                <span>(${author.email})</span>
            </div>
            <h2>${post.title}</h2>
            <p>${post.body}</p>
            <button class="btn btn-link comments-toggle" data-post-id="${post.id}">
                Ver comentários
            </button>
            <div id="comments-${post.id}" class="comments-section">
                <div class="spinner-border text-primary" role="status">
                    <span class="visually-hidden">Carregando...</span>
                </div>
            </div>
        `;

        const commentsButton = article.querySelector('.comments-toggle');
        commentsButton.addEventListener('click', () => this.toggleComments(post.id, commentsButton));
        
        this.postsContainer.appendChild(article);
    }

    async toggleComments(postId, button) {
        const commentsSection = document.getElementById(`comments-${postId}`);
        
        if (!commentsSection) {
            return;
        }

        if (commentsSection.style.display === 'block') {
            commentsSection.style.display = 'none';
            button.textContent = 'Ver comentários';
            return;
        }
        
        commentsSection.style.display = 'block';
        button.textContent = 'Ocultar comentários';
        
        if (!commentsSection.hasAttribute('data-loaded')) {
            const comments = await this.comments(postId);
            
            let commentsHTML = '<h3>Comentários</h3>';
            comments.forEach(comment => {
                commentsHTML += `
                    <div class="comment mb-3">
                        <strong>${comment.name}</strong>
                        <p class="mb-1"><em>${comment.email}</em></p>
                        <p>${comment.body}</p>
                    </div>
                `;
            });
            
            commentsSection.innerHTML = commentsHTML;
            commentsSection.setAttribute('data-loaded', 'true');
        }
    }

    async showComments(postId) {
        const comments = await this.comments(postId);
        const commentsContent = document.getElementById('commentsContent');
        
        commentsContent.innerHTML = comments.map(comment => `
            <div class="comment">
                <div class="comment-email">${comment.email}</div>
                <strong>${comment.name}</strong>
                <p>${comment.body}</p>
            </div>
        `).join('');

        this.commentsModal.show();
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const app = new TimelineApp();
    app.init();
}); 

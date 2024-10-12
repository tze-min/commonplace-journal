let POSTS_LIST = [];
let TAGS_MAP = new Map();
const FILEPATH = 'pages.json';

async function getPosts() {
// fetch all posts from pages.json
    try {
        const response = await fetch(FILEPATH);
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        pagesJson = await response.json();
        
        // display a unique set of tags
        pagesJson.forEach(page => {
            buildPostsList(page.title, page.url);
            page.tags.forEach(tag => { 
                buildTagsMap(tag, page.title, page.url);
            })
        })

        // listen for click of "show all" button
        const showAllButton = document.getElementById('showAll');
        showAllButton.addEventListener('click', () => showPosts());
    } catch (error) {
        console.error(error.message);
    }

    showTags();
    showPosts();
}

function buildPostsList(title, url) {
    POSTS_LIST.push([title, url]);
}

function buildTagsMap(tag, title, url) {
    if (TAGS_MAP.has(tag)) {
        let posts = TAGS_MAP.get(tag);
        posts.push([title, url]);
        TAGS_MAP.set(tag, posts);
    } else {
        TAGS_MAP.set(tag, [[title, url]]);
    }
}

function showTags() {
// display a unique list of tags
    const tagList = document.getElementById('tagList');
    TAGS_MAP.keys().forEach(tag => {
        const tagButton = document.createElement('button');
        tagButton.innerHTML = tag;
        tagButton.className = 'tagContainer';
        tagButton.addEventListener('click', () => filterPosts(tag));

        tagList.appendChild(tagButton);
    })
}

function filterPosts(selectedTag) {
// select posts given a tag
    const tagButtons = document.querySelectorAll('.tagContainer');
    
    // check if user's deselecting any tag buttons
    let isDeselecting = false;
    tagButtons.forEach(button => {
        if (button.innerHTML === selectedTag && button.classList.contains('selected')) {
            isDeselecting = true;
        }
    })

    if (isDeselecting) {
        // if user's deselecting a tag, show all posts
        showPosts();
        tagButtons.forEach(button => button.classList.remove('selected'));
    } else {
        // else, show only the filtered posts and add the selected class to the tag button element
        const filteredPosts = TAGS_MAP.get(selectedTag);
        tagButtons.forEach(button => {
            button.innerHTML === selectedTag ? button.classList.add('selected') : button.classList.remove('selected');
        })
        showPosts(filteredPosts);
    }
}

function clearPosts() {
    const postList = document.getElementById('postList');
    postList.innerHTML = '';
}

function showPosts(filteredPosts = POSTS_LIST) {
// display a unique list of posts, filtered if a tag's been selected
    clearPosts();

    const postList = document.getElementById('postList');
    filteredPosts.forEach(post => {
        const [title, url] = [post[0], post[1]];
        const postContainer = document.createElement('div');
        postContainer.className = 'postContainer';

        postElement = document.createElement('a');
        postElement.innerHTML = title;
        postElement.href = url;

        postContainer.appendChild(postElement);
        postList.appendChild(postContainer);
    })
}

getPosts();
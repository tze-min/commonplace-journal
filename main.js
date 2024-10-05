let POSTS_SET = new Set();
let TAGS_SET = new Set();
const FILEPATH = 'pages.json';

async function getPosts() {
// fetch all posts from pages.json
    try {
        const response = await fetch(FILEPATH);
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        const postsList = await response.json();
        console.log('postsList after fetching json', postsList);
        
        // display a unique set of tags
        postsList.forEach(page => {
            page.tags.forEach(tag => {
                TAGS_SET.add(tag);
            })
            const content = [page.url, page.title];
            POSTS_SET.add(content);
        })
    } catch (error) {
        console.error(error.message);
    }

    showTags();
    showPosts();
}

function showTags() {
// display a unique list of tags
    const tagList = document.getElementById('tagList');
    TAGS_SET.forEach(tag => {
        const tagButton = document.createElement('button');
        tagButton.innerHTML = tag;
        tagButton.className = 'tagContainer';
        // tagButton.addEventListener('click', filterPosts(tag));

        tagList.appendChild(tagButton);
    })
}

// function filterPosts(selectedTag) {
//     // filter posts given a tag
//         console.log('im getting run');
//         const filteredPosts = POSTS_SET.filter(post => post.tags.includes(selectedTag));
//         console.log(filteredPosts);
//         showPosts(filteredPosts);
//     }

function showPosts(filteredPosts = POSTS_SET) {
// display a unique list of posts, filtered if a tag's been selected
    const postList = document.getElementById('postList');
    filteredPosts.forEach(post => {
        console.log('looping through', post);
        const [url, title] = [post[0], post[1]];
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
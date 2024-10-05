let tags_list = new Set();

async function get_posts() {
    const filepath = 'pages.json';

    try {
        const response = await fetch(filepath);
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        const json = await response.json();
        json.forEach(page => {
            page.tags.forEach(tag => tags_list.add(tag));
        });
        console.log(json);
    } catch (error) {
        console.error(error.message);
    }

    show_tags();
}

function show_tags() {
    console.log(tags_list);
    const tagList = document.getElementById('tagList');
    tags_list.forEach(tag => {
        const tag_element = document.createElement('span');
        tag_element.innerHTML = tag;
        tag_element.className = 'tag';
        tagList.appendChild(tag_element);
    })
}

get_posts();
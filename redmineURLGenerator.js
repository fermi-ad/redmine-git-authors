function genRMURL(url){
    projectName = url.match(/projects\/([^/]+)/)[1];
    isNotMainRepo = url.match(/repository\/([^/]+)/);
    repoName = projectName;

    if (isNotMainRepo) repoName += `-${isNotMainRepo[1]}`;

    return repoName;
}

const sidebar = document.querySelector("#sidebar > p");

if (sidebar) {
    console.log(Array.from(sidebar.querySelectorAll("a"))
        .map(node => genRMURL(node.getAttribute('href'))).join('\n'));
} else {
    console.log(genRMURL(location.pathname));
}

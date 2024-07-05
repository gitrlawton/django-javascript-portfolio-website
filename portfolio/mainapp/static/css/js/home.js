
// Wait until all of the DOM content has been loaded to execute this code.
document.addEventListener("DOMContentLoaded", function () {
    const nameSearch = document.getElementById("name-search")
    const tags = document.querySelectorAll(".tag")
    const projects = document.querySelectorAll(".project")

    // Function to filter the projects.
    function filterProjects() {
        // Get the value of the name-search field and convert it to lowercase.
        const nameQuery = nameSearch.value.toLowerCase();

        // Loop through all the projects we have and see if the proj name we're
        // searching for matches the current project's name.
        projects.forEach((project) => {
            const name = project.getAttribute('data-name')
            const nameMatches = name.includes(nameQuery)

            // If it does match, set the display property to nothing.
            if (nameMatches) {
                project.style.display = "";
            }
            // If it doesn't match, set the display property to hide the project.
            else {
                project.style.display = "none";
            }
        })
    }

    // Loop through all the tags we have associated with a project...
    tags.forEarch((tag) => {
        // ...add an event listening to it...
        tag.addEventListener("click", function () {
            // When it is clicked, get it's name...
            const selectedTag = this.getAttribute("data-tag")

            // ...and for each of the projects, see if that project is
            // associated with the selected tag.
            projects.forEach((project) => {
                const projectTags = project.getAttribute("data_tags")

                // If the project is associated with the selected tag,
                // set the display property to nothing.
                if (projectTags.includes(selectedTag)) {
                    project.style.display = ""
                }
                // Otherwise, hide the project from being displayed.
                else {
                    project.style.display = "none"
                }
            })
        })
    })

    // Event listener which calls the filterProjects function after each
    // key release.
    nameSearch.addEventListener("keyup", filterProjects)


})
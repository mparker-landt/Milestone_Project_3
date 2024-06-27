/** 
 * When page fully loaded create the table needed for the page. 
 */
$(document).ready( function () {
    console.log("Table Loaded");
    $('#dataTable').DataTable();
});

/**
 * 
 */
$('#projectChoose').change(function() {
    var selectedProjectId = $(this).val();
    console.log('User selected project with id: ' + selectedProjectId);
    // You can send 'selectedProjectId' to the server here
    $.ajax({
        url: '/primary_reqs',  // replace with your endpoint
        method: 'POST',
        data: {'project_id': selectedProjectId},
        success: function(response) {
            // This will run after the server responds successfully.
            // 'response' will contain whatever the server sent back.
            console.log("AJAX sent...");
            console.log(response);

            var primarys = response.primarys;
            // Now you can use 'primarys' to update your page
            // For example, if you have a list element for primarys:
            var primarysList = $('#primarys-list');
            primarysList.empty();  // clear the list
            primarys.forEach(function(primary) {
                primarysList.append('<li>' + primary.title + '</li>');  // assuming 'title' is a field
            });
        }
    });
});

/**
 * [bar description]
 * @param  {[type]} foo [description]
 * @return {[type]}     [description]
 */
function bar (foo) {
    return foo + foo;
}

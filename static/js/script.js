
var projectTitle = $("<h3/>").addClass("dashboard-item-header");
var projectBody = $("<p/>").addClass("dashboard-item-body");

var newDiv = $("<div/>")   // creates a div element
                .addClass("dashboard-item")   // add a class
                .html(projectTitle.add(projectBody));

$(function() {
    $(".AddTable").click(function() {
        $(this).parents('table').find("tr:last").before('<tr><td>&nbsp;</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>');
    });
});

$(function() {
    $("#AddGrid").click(function() {
        var count = $("#dashboard-grid").children().length;
        console.log(count);

        let cardId = "card" + count;
        console.log(cardId);

        $(newDiv.clone()).attr('id',cardId).insertBefore('#AddGrid');
    });
});
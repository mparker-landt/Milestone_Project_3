
$(document).ready( function () {
    $('#dataTable').DataTable();
} );

var cardTitle = $("<h3/>").addClass("dashboard-item-header");
var cardBody = $("<p/>").addClass("dashboard-item-body");
var card = $("<div/>").addClass("dashboard-item").html(cardTitle.add(cardBody));

var test = $("<div/>").addClass("dashboard-item dashboard-item-new")

$(function() {
    $(".AddTable").click(function() {
        $(this).parents('table')
                .find("tr:last")
                .before('<tr><td>&nbsp;</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>');
    });
});

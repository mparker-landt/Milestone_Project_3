
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

// $(function() {
//     $("#AddGrid").click(function() {
//         var gridCount = $("#dashboard-grid").children().length;
//         console.log(gridCount);

//         let cardId = "card" + gridCount;
//         console.log(cardId);

//         $(card.clone()).attr('id',cardId).insertBefore('#AddGrid');
//     });
// });

$(function() {
    $("#AddTest").click(function() {
        $(test.clone()).insertBefore('#AddTest');
    });
});

$(document).ready(function() {
    $('.modal').modal();
});


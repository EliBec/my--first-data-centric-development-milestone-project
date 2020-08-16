/* Search and Clear buttons will change colors upon clicking any of the search or 'select' fields */
$(document).ready(function(){
    $("#categorysearch").click(function(){
    $("#search-btn").removeClass("btn btn-secondary").addClass("btn btn-info" );
    $("#clearsearch-btn").removeClass("btn btn-secondary").addClass("btn btn-warning" );
    });

    $("#date-search").click(function(){
    $("#search-btn").removeClass("btn btn-secondary").addClass("btn btn-info" );
    $("#clearsearch-btn").removeClass("btn btn-secondary").addClass("btn btn-warning" );
    });

    $("#cityorzipsearch").click(function(){
    $("#search-btn").removeClass("btn btn-secondary").addClass("btn btn-info" );
    $("#clearsearch-btn").removeClass("btn btn-secondary").addClass("btn btn-warning" );
    });

    $("#itemsearch").click(function(){
    $("#search-btn").removeClass("btn btn-secondary").addClass("btn btn-info" );
    $("#clearsearch-btn").removeClass("btn btn-secondary").addClass("btn btn-warning" );
    });

    /* Click the 'Clear button will reset fields and buttons */
    $("#clearsearch-btn").click(function(){
    $("#search-btn").removeClass("btn btn-info").addClass("btn btn-secondary" );
    $("#clearsearch-btn").removeClass("btn btn-warning").addClass("btn btn-secondary");
    $('#search-form input[type="search"]').val('');
    $('#search-form #date-search').val('');
    });
});
